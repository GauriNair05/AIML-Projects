from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

def setup_custom_rag():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vector_db", embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={"k": 2})

    hf_pipe = pipeline("text-generation", model="gpt2", max_new_tokens=100, pad_token_id=50256)
    llm = HuggingFacePipeline(pipeline=hf_pipe)

    custom_system_prompt = (
        "You are a helpful assistant. Use ONLY the context below to answer "
        "the question. If the answer is not mentioned in the context, reply "
        "with 'I cannot find that in the provided documents.'\n\n"
        "Context:\n{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", custom_system_prompt),
        ("human", "{input}"),
    ])

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, question_answer_chain)

rag_chain = setup_custom_rag()

query1 = "What is Chunking?"
res1 = rag_chain.invoke({"input": query1})
print(f"Q1: {query1}")
print(f"A1: {res1['answer']}\n")

query2 = "What is the capital of France?"
res2 = rag_chain.invoke({"input": query2})
print(f"Q2: {query2}")
print(f"A2: {res2['answer']}")