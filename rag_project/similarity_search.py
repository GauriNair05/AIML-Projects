from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def perform_search(query: str, k: int = 2):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vector_db", embeddings, allow_dangerous_deserialization=True)
    
    docs = db.similarity_search(query, k=k)
    return docs

query = "What is FAISS?"
results = perform_search(query)

print(f"Query: '{query}'\n")
print(f"Retrieved {len(results)} relevant chunks:\n")

for i, doc in enumerate(results, 1):
    print(f"--- Result {i} ---")
    print(doc.page_content)
    print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")