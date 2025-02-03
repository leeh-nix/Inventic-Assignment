import google.generativeai as genai
import streamlit as st


# Initialize the Gemini API
@st.cache_data
def initialize_gemini(api_key):
    genai.configure(api_key=api_key)


# Generate a response from Gemini
def geminiai(paragraph, model_name="gemini-1.5-flash"):
    """
    Generate a response from Gemini given a paragraph of text.

    Args:
        paragraph (str): The paragraph of text to generate a response from.
        model_name (str, optional): The name of the model to use. Defaults to "gemini-1.5-flash".

    Returns:
        str: The generated response from Gemini.
    """
    model = genai.GenerativeModel(
        model_name,
        safety_settings=None,
        system_instruction=f"Role: You are an AI summarizer, your role is to summarize the given paragraphs. You must also guess which book does it belongs and summarize it.",
    )
    prompt = f"User input: {paragraph}, \n Book Name: \n Author:  === \n Summary \n"
    response = model.generate_content(prompt)
    return response.text
