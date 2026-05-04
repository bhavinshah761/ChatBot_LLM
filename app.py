import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="RAG Chatbot")
st.title("My First RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask a question about your text document")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post(
                API_URL,
                json={"question": question}
            )
            data = response.json()
            answer = data["answer"]

            st.write(answer)

            with st.expander("Sources"):
                st.write(data["sources"])

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })