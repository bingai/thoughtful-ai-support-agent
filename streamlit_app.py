import streamlit as st
import requests

st.title("Thoughtful AI Chat")

user_question = st.text_input("Ask a question:")

if st.button("Send"):
    response = requests.post("http://127.0.0.1:5000/ask", json={"question": user_question})
    answer = response.json().get("answer")
    st.write(f"Answer: {answer}")