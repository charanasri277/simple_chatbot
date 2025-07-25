import streamlit as st
import google.generativeai as genai
from config import Config

def apply_css(dark_mode):
    css = Config.DARK_MODE_CSS if dark_mode else Config.LIGHT_MODE_CSS
    st.markdown(css, unsafe_allow_html=True)

def initialize_session():
    if 'dark_mode' not in st.session_state:
        st.session_state['dark_mode'] = False

def get_model_name(choice):
    mapping = {
        "Gemini 1.5 Flash": "models/gemini-1.5-flash",
        "Gemini 1.5 Pro": "models/gemini-1.5-pro",
        "Gemini 1.0 Pro": "models/gemini-pro"
    }
    return mapping.get(choice, "models/gemini-1.5-flash")

def create_chat_session(api_key, model_name, temperature, top_p, top_k, max_output_tokens):
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config={
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "max_output_tokens": max_output_tokens
        },
        safety_settings=Config.SAFETY_SETTINGS
    )

    return model.start_chat()

