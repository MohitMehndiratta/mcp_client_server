import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()
groq_api_key=os.getenv('GROQ_API_KEY')


st.set_page_config(page_title="Multi Client App")
st.title("Welcome to the Utility Portal!")

# Take user input
user_input = st.chat_input("Tell me.. what do you want to do today?")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # LLM call
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=groq_api_key,
        temperature=0.7
    )

    # CORRECT: dictionary, not set
    response = llm.invoke(user_input)

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response.content)
