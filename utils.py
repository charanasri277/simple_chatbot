import google.generativeai as genai

def create_chat_session(api_key, model_name, temperature, top_p, top_k, max_output_tokens):
    genai.configure(api_key=api_key)

    safety_settings = [
        {"category": "HARM_CATEGORY_DEROGATORY", "threshold": 2},
        {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 2},
        {"category": "HARM_CATEGORY_SEXUAL", "threshold": 2},
        {"category": "HARM_CATEGORY_MEDICAL", "threshold": 2},
        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 2}
    ]

    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config={
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "max_output_tokens": max_output_tokens
        },
        safety_settings=safety_settings
    )

    return model.start_chat()

