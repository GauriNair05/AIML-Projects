from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

def setup_conversational_rag():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vector_db", embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={"k": 2})

    hf_pipe = pipeline("text-generation", model="gpt2", max_new_tokens=100, pad_token_id=50256)
    llm = HuggingFacePipeline(pipeline=hf_pipe)

    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question, formulate a standalone question."
    )
    contextualize_q_prompt = ChatPromptTemplate.from_messages([
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])

    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )

    qa_system_prompt = "Use the retrieved context to answer the question:\n\n{context}"
    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])

    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    return create_retrieval_chain(history_aware_retriever, question_answer_chain)

rag_chain = setup_conversational_rag()
chat_history = []

q1 = "What is FAISS?"
res1 = rag_chain.invoke({"input": q1, "chat_history": chat_history})
print(f"User: {q1}")
print(f"Bot: {res1['answer']}\n")

chat_history.append(HumanMessage(content=q1))
chat_history.append(AIMessage(content=res1["answer"]))

q2 = "Who developed it?"
res2 = rag_chain.invoke({"input": q2, "chat_history": chat_history})
print(f"User: {q2}")
print(f"Bot: {res2['answer']}")