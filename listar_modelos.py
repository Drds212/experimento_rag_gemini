import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.environ.get('GEMINI_KEY'),
    http_options={'api_version': 'v1beta'}
)

print(f"{'NOMBRE DEL MODELO':<40} | {'HABILIDADES'}")
print("-" * 70)

for model in client.models.list():
    print(f"{model.name:<40}")