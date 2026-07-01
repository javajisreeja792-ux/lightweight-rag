import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(question, context):
    prompt = f"""
You are a helpful AI assistant.

Answer the question using ONLY the context below.
If the answer is not found in the context, say:
"I couldn't find the answer in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)
    return response.text
