import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold

class Config:
    # ✅ API key is securely loaded from environment variables (Streamlit secrets)
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # ✅ Light theme CSS for user and AI message bubbles
    LIGHT_MODE_CSS = """
    <style>
        .chat-message.user {
            background-color: #e0f7fa;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
        }
        .chat-message.ai {
            background-color: #f1f8e9;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
        }
    </style>
    """

    # ✅ Dark theme CSS for user and AI message bubbles
    DARK_MODE_CSS = """
    <style>
        .chat-message.user {
            background-color: #263238;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
        }
        .chat-message.ai {
            background-color: #37474f;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
        }
    </style>
    """

    # ✅ Recommended safety settings (BLOCK_MEDIUM)
    SAFETY_SETTINGS = [
        {"category": HarmCategory.HARM_CATEGORY_DEROGATORY, "threshold": HarmBlockThreshold.BLOCK_MEDIUM},
        {"category": HarmCategory.HARM_CATEGORY_VIOLENCE, "threshold": HarmBlockThreshold.BLOCK_MEDIUM},
        {"category": HarmCategory.HARM_CATEGORY_SEXUAL, "threshold": HarmBlockThreshold.BLOCK_MEDIUM},
        {"category": HarmCategory.HARM_CATEGORY_MEDICAL, "threshold": HarmBlockThreshold.BLOCK_MEDIUM},
        {"category": HarmCategory.HARM_CATEGORY_DANGEROUS, "threshold": HarmBlockThreshold.BLOCK_MEDIUM},
    ]
