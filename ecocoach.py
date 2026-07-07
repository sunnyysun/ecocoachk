from google import genai
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Crear cliente
client = genai.Client(api_key=API_KEY)


def analizar_alimentos(mensaje_usuario):

    prompt = f"""
Eres EcoCoach, un asistente inteligente especializado en reducir el desperdicio de alimentos en los hogares.

Tu objetivo es ayudar al usuario utilizando únicamente los alimentos que él indique.

Mensaje del usuario:

{mensaje_usuario}

Realiza estas tareas:

1. Identifica todos los alimentos mencionados.
2. Prioriza los que puedan vencer primero.
3. Sugiere entre 2 y 4 recetas.
4. Si falta algún ingrediente secundario, indícalo.
5. Explica por qué elegiste esas recetas.
6. Da consejos de conservación.
7. Calcula aproximadamente cuánto dinero podría ahorrar el usuario (en soles peruanos).
8. Explica el impacto ambiental positivo.

Responde SIEMPRE usando Markdown.

Organiza la respuesta con títulos grandes.

Utiliza emojis.

El formato debe ser:

# 🍽 Recetas recomendadas

...

# 🥕 Ingredientes prioritarios

...

# 🧊 Conservación

...

# 💰 Ahorro económico

...

# 🌎 Impacto ambiental

...

Las recetas deben estar numeradas.

El ahorro debe mostrarse en soles peruanos.

No escribas párrafos demasiado largos.

Utiliza listas cuando sea posible.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text