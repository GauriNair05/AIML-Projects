from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

def setup_rag_chain():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vector_db", embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={"k": 2})

    hf_pipe = pipeline("text-generation", model="gpt2", max_new_tokens=100, pad_token_id=50256)
    llm = HuggingFacePipeline(pipeline=hf_pipe)

    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question.\n\nContext:\n{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain

rag_chain = setup_rag_chain()
query = "What is Retrieval-Augmented Generation?"
response = rag_chain.invoke({"input": query})

print(f"Question: {query}\n")
print(f"Answer: {response['answer']}")