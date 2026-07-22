import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="RAG Chatbot")
st.title("Conversational RAG System")

@st.cache_resource
def load_vector_db():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local("vector_db", embeddings, allow_dangerous_deserialization=True)

db = load_vector_db()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask something about your documents..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Combine current prompt with previous user question for follow-up context
    search_query = prompt
    user_msgs = [m["content"] for m in st.session_state.messages if m["role"] == "user"]
    if len(user_msgs) > 1:
        search_query = f"{user_msgs[-2]} {prompt}"

    with st.chat_message("assistant"):
        with st.spinner("Searching documents..."):
            docs = db.similarity_search(search_query, k=1)
            if docs:
                answer = docs[0].page_content
            else:
                answer = "No relevant context found in your documents."
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})