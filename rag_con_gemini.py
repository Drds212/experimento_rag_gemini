import os
from google import genai
from cliente_supabase import supabase
from dotenv import load_dotenv


load_dotenv()
GEMINI_KEY = os.environ.get('GEMINI_KEY')
client = genai.Client(
    api_key=GEMINI_KEY
)



def alimentar_cerebro(texto):
    print(f"Procesando fragmento...")
    

    res = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texto,
    )
    
 
    vector = res.embeddings[0].values

    supabase.table("documentos").insert({
        "contenido": texto,
        "embedding": vector
    }).execute()
    print("✅ Guardado exitosamente.")





def preguntar(duda_usuario):

    res_query = client.models.embed_content(
        model="gemini-embedding-001",
        contents=duda_usuario,
    )
    query_vector = res_query.embeddings[0].values

    # Búsqueda en Supabase
    rpc_res = supabase.rpc("buscar_documentos", {
        "query_embedding": query_vector,
        "match_threshold": 0.4,
        "match_count": 2
    }).execute()

    contexto = "\n".join([item['contenido'] for item in rpc_res.data])
    

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=f"Contexto: {contexto}\n\nPregunta: {duda_usuario}"
    )
    
    return response.text