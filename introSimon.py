import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Portafolio II | Interfaces Multimodales", layout="wide")

# Quita márgenes y cabecera de Streamlit para que se vea como la página original
st.markdown(
    """
    <style>
      header, footer, #MainMenu {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

base = Path(__file__).parent
html = (base / "index.html").read_text(encoding="utf-8")

# Incrusta blanco.jpeg como base64 (dentro del iframe de Streamlit las rutas relativas no cargan).
# Si el archivo no existe, la página muestra automáticamente el recuadro de respaldo.
img = base / "blanco.jpeg"
if img.exists():
    b64 = base64.b64encode(img.read_bytes()).decode()
    html = html.replace('src="blanco.jpeg"', f'src="data:image/jpeg;base64,{b64}"')

components.html(html, height=3000, scrolling=True)
