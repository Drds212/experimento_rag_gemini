import os
from google import genai
from dotenv import load_dotenv
#Este script lista los modelos disponibles en la api de gemini para ayudar e solucionar errores
#en las funciones que consultan a dichos modelos 
load_dotenv()

client = genai.Client(
    api_key=os.environ.get('GEMINI_KEY'),
    http_options={'api_version': 'v1beta'}
)

print(f"{'NOMBRE DEL MODELO':<40}")
print("-" * 70)

for model in client.models.list():
    print(f"{model.name:<40}")