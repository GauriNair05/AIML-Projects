from langchain_text_splitters import RecursiveCharacterTextSplitter
from load_docs import load_documents

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    return text_splitter.split_documents(documents)

raw_docs = load_documents("./data")
chunks = split_documents(raw_docs)

print(f"Total raw documents: {len(raw_docs)}")
print(f"Total document chunks created: {len(chunks)}")
print("\n--- First Chunk Preview ---")
print(chunks[0].page_content)