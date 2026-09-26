import ollama
import streamlit as st 
st.title("Welcome!  to my chatbot app!!!")
with st.sidebar:
    uploaded_file =st.file_uploader("upload a text file...")
    if uploaded_file is not None:
        st.write("uploaded file:",uploaded_file.name)
        context=uploaded_file.read().decode("utf-8")
        st.text(context)
if "messages" not in st.session_state:
    st.session_state.messages =[ ]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
question = st.chat_input("Type your message...")
if question:
    st.session_state.messages.append({
        "role":"user",
        "content":question
    })
    with st.chat_message("user"):
        st.write(question)
with st.spinner("loading"):
        response =ollama.chat(
            model = "llama3.2:3b",
            messages =st.session_state.messages
        )

        answer = response["message"]["content"]

        st.session_state.messages.append({
            "role":"assistant",
            "content":answer
        })

        with st.chat_message("assistant"):
            st.write(answer) 

uploaded_file =st.file_uploader("upload a text file...")

