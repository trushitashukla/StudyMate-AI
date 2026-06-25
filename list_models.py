import google.generativeai as genai

API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=API_KEY)

print("Available Models:\n")

for model in genai.list_models():
    print(model.name)