import streamlit as st
import os
import google.generativeai as genai
from config import Config

def apply\_css(dark\_mode):
css = Config.DARK\_MODE\_CSS if dark\_mode else Config.LIGHT\_MODE\_CSS
st.markdown(css, unsafe\_allow\_html=True)

def initialize\_session():
if 'dark\_mode' not in st.session\_state:
st.session\_state\['dark\_mode'] = False

def get\_model\_name(model\_choice):
if model\_choice == "Gemini 1.5 Flash":
return "gemini-1.5-flash-latest"
elif model\_choice == "Gemini 1.5 Pro":
return "gemini-1.5-pro-latest"
else:
return "gemini-1.0-pro"

def create\_chat\_session(api\_key, model\_name, temperature, top\_p, top\_k, max\_output\_tokens):
os.environ\["GEMINI\_API\_KEY"] = api\_key
genai.configure(api\_key=api\_key)

```
generation_config = {
    "temperature": temperature,
    "top_p": top_p,
    "top_k": top_k,
    "max_output_tokens": max_output_tokens,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name=model_name,
    safety_settings=Config.SAFETY_SETTINGS,
    generation_config=generation_config,
)

return model.start_chat(history=[])
```
