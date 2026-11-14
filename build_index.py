from pathlib import Path
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from e5_embeddings import E5Embeddings

docs = DirectoryLoader(
    str(Path("docs")),
    glob="*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"},
).load()
print(f"loaded {len(docs)} documents")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""],
)
chunks = splitter.split_documents(docs)
print(f"split into {len(chunks)} chunks")

emb = E5Embeddings()

FAISS.from_documents(chunks, emb).save_local("index_faiss")
print("index saved")