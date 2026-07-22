from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from load_docs import load_documents
from split_docs import split_documents

def build_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("vector_db")
    return db

raw_docs = load_documents("./data")
chunks = split_documents(raw_docs)

print("Generating embeddings and creating FAISS index...")
db = build_vector_store(chunks)
print("FAISS vector database saved locally to 'vector_db/' directory!")