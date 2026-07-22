import os
from langchain_community.document_loaders import TextLoader, PyPDFDirectoryLoader, DirectoryLoader

def load_documents(data_directory: str):
    documents = []
    
    if os.path.exists(data_directory):
        txt_loader = DirectoryLoader(data_directory, glob="./*.txt", loader_cls=TextLoader)
        documents.extend(txt_loader.load())
        
        pdf_loader = DirectoryLoader(data_directory, glob="./*.pdf", loader_cls=PyPDFDirectoryLoader)
        documents.extend(pdf_loader.load())
        
    return documents

raw_docs = load_documents("./data")
print(f"Loaded {len(raw_docs)} documents successfully.")