import streamlit as st
from ecocoach import analizar_alimentos

st.set_page_config(
    page_title="EcoCoach",
    page_icon="🌱",
    layout="wide"
)

# ---------------- ESTILOS ----------------

st.markdown("""
<style>

.block-container{
    max-width:900px;
    padding-top:2rem;
}

h1{
    text-align:center;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:25px;
}

.card{
    padding:18px;
    border-radius:15px;
    border:1px solid #2E7D32;
    margin-bottom:15px;
}

.example{
    background:#E8F5E9;
    color:#1B5E20;
    padding:8px;
    border-radius:8px;
    margin:5px 0;
}

.stChatMessage{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🌱 EcoCoach")

    st.write("")

    st.info(
        """
**Asistente inteligente para reducir el desperdicio de alimentos.**

✔ Sugiere recetas.

✔ Prioriza alimentos próximos a vencer.

✔ Calcula ahorro económico.

✔ Recomienda conservación.
"""
    )

    st.write("---")

    st.success("ODS 12\n\nProducción y consumo responsables")

    st.write("---")

    if st.button("🗑 Nueva conversación", use_container_width=True):

        st.session_state.messages=[]

        st.rerun()

# ---------------- TITULO ----------------

st.title("🌱 EcoCoach")

st.markdown(
'<p class="subtitle">Aprovecha tus alimentos antes de que se desperdicien.</p>',
unsafe_allow_html=True
)

# ---------------- TARJETA ----------------

if "messages" not in st.session_state:

    st.markdown("""
<div class="card">

### 👋 Bienvenido

Escribe los alimentos que tienes en casa y EcoCoach hará todo el análisis automáticamente.

<b>Ejemplos:</b>

<div class="example">
Tengo pollo, arroz y zanahorias.
</div>

<div class="example">
Se me vence un yogur mañana.
</div>

<div class="example">
Tengo tomate, queso y pan.
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- HISTORIAL ----------------

if "messages" not in st.session_state:

    st.session_state.messages=[]

for mensaje in st.session_state.messages:

    avatar="👤"

    if mensaje["role"]=="assistant":
        avatar="🌱"

    with st.chat_message(mensaje["role"], avatar=avatar):

        st.markdown(mensaje["content"])

# ---------------- INPUT ----------------

prompt=st.chat_input("Escribe los alimentos que tienes en casa...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user", avatar="👤"):

        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🌱"):

        with st.spinner("🌱 EcoCoach está analizando tus alimentos..."):

            try:

                respuesta=analizar_alimentos(prompt)

            except Exception as e:

                respuesta=f"❌ {e}"

        st.markdown(respuesta)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":respuesta
        }
    )