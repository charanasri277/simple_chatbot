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
        safety_settings=[
            {"category": "harm_category_derogatory", "threshold": 2},
            {"category": "harm_category_violence", "threshold": 2},
            {"category": "harm_category_sexual", "threshold": 2},
            {"category": "harm_category_medical", "threshold": 2},
            {"category": "harm_category_dangerous", "threshold": 2}
        ]
    )

    return model.start_chat()
