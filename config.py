class Config:
    GEMINI_API_KEY = "AIzaSyCSyFw6GbmO724yym-plLlCLu_1pVsiJKc"

    LIGHT_MODE_CSS = """
    <style>
        .chat-message.user { background-color: #e0f7fa; padding: 10px; border-radius: 10px; margin-bottom: 5px; }
        .chat-message.ai { background-color: #f1f8e9; padding: 10px; border-radius: 10px; margin-bottom: 5px; }
    </style>
    """

    DARK_MODE_CSS = """
    <style>
        .chat-message.user { background-color: #263238; color: white; padding: 10px; border-radius: 10px; margin-bottom: 5px; }
        .chat-message.ai { background-color: #37474f; color: white; padding: 10px; border-radius: 10px; margin-bottom: 5px; }
    </style>
    """

    SAFETY_SETTINGS = [
        {"category": "HARM_CATEGORY_DEROGATORY", "threshold": 3},
        {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 3},
        {"category": "HARM_CATEGORY_SEXUAL", "threshold": 3},
        {"category": "HARM_CATEGORY_MEDICAL", "threshold": 3},
        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 3},
    ]

