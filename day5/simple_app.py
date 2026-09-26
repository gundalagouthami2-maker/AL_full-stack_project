import streamlit as st
import ollama
st.title("my first streamlit app!!!")
st.write("welcome to my ai application!")
name=st.text_input("enter your name;")
if st.button("submit"):
    st.write("hello ,name")
