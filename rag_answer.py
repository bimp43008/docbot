from langchain_community.vectorstores import FAISS
from e5_embeddings import E5Embeddings
from llm import client

emb = E5Embeddings()
vs = FAISS.load_local("index_faiss", emb, allow_dangerous_deserialization=True)
retriever = vs.as_retriever(search_kwargs={"k": 3})

def rag_answer(question: str) -> str:
    chunks = retriever.invoke(question)

    context = "\n\n".join(
        f"[{c.metadata['source']}] {c.page_content}" for c in chunks
    )

    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": (
                "Ты — эксперт по документам. "
                "Твоя задача — отвечать на вопросы, используя только предоставленные документы. "
                "Если ответа нет в документах, скажи «Извините, я не знаю ответа на этот вопрос». "
                "Не придумывай информацию и не используй внешние источники."
            )},
            {"role": "user", "content": f"КОНТЕКСТ:\n{context}\n\nВОПРОС: {question}"}
        ],
        temperature=0,
    )

    return resp.choices[0].message.content

for q in ["Кто продал автомобиль и почём?", "Сколько стоит Москва?"]:
    print(f"\n=== {q} ===\n{rag_answer(q)}")