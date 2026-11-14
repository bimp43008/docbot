from langchain_community.vectorstores import FAISS
from e5_embeddings import E5Embeddings

emb = E5Embeddings()
vectorstore = FAISS.load_local("index_faiss", emb, allow_dangerous_deserialization=True)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
for q in ["Кто продал автомобиль и почём?", "Сколько стоит Москва?"]:
    print("\n=== ВОПРОС:", q, "===")
    for d in retriever.invoke(q):
        print(f"[{d.metadata['source']}] {d.page_content[:120]}")