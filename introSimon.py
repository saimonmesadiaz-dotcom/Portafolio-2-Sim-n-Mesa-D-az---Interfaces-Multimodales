import base64
import html
import mimetypes
import re
from pathlib import Path
from urllib.parse import urlparse

import streamlit as st
import streamlit.components.v1 as components

# ==========================================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================================
st.set_page_config(
    page_title="Portafolio II | Interfaces Multimodales",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# DIRECTORIO Y CONFIGURACIÓN DE ARCHIVOS
# ==========================================================
CARPETA = Path(__file__).resolve().parent
FOTO = "Simon.jpeg"


# ==========================================================
# FUNCIONES AUXILIARES (BÚSQUEDA INTELIGENTE DE IMÁGENES)
# ==========================================================

def esc(texto):
    """Evita que los textos introducidos rompan el HTML."""
    return html.escape(str(texto), quote=True)


def buscar_imagen(nombre):
    """Busca de forma flexible la imagen en el directorio del proyecto."""
    archivos = list(CARPETA.glob("*"))

    for f in archivos:
        if f.name.lower() == nombre.lower():
            return f

    base = Path(nombre).stem.lower()

    for f in archivos:
        if f.stem.lower() == base:
            return f

    return None


def incrustar_imagenes(html_content):
    """Reemplaza dinámicamente las rutas de imágenes locales por Base64."""
    def reemplazo(m):
        f = buscar_imagen(m.group(1))

        if f is None:
            return m.group(0)

        mime = mimetypes.guess_type(f.name)[0] or "image/jpeg"
        b64 = base64.b64encode(f.read_bytes()).decode()

        return f'src="data:{mime};base64,{b64}"'

    return re.sub(
        r'src="([^"/:]+\.(?:jpe?g|png|webp|gif))"',
        reemplazo,
        html_content,
        flags=re.I
    )


def cargar_foto_portada():
    """Carga la foto principal de la portada."""
    ruta = buscar_imagen(FOTO)

    if ruta and ruta.is_file():
        mime = mimetypes.guess_type(ruta.name)[0] or "image/jpeg"
        datos = base64.b64encode(ruta.read_bytes()).decode("utf-8")
        return f"data:{mime};base64,{datos}"
    return ""


def crear_enlace(url, texto):
    """Crea un enlace únicamente si se ha configurado una URL válida."""
    url = str(url).strip()
    partes = urlparse(url)

    if partes.scheme in ("https", "http") and partes.netloc:
        return (
            f'<a class="btn-vintage btn-link" href="{esc(url)}" '
            f'target="_blank" rel="noopener noreferrer">'
            f'↗ {esc(texto)}</a>'
        )

    return '<span class="text-xs font-mono text-[#84664a] bg-[#f2e3ce] px-3 py-1 rounded-full border border-dashed border-[#b89570]">↗ Enlace pendiente</span>'


# ==========================================================
# ESTILOS CSS GENERALES Y DE LA BARRA LATERAL
# ==========================================================
st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;700&family=Playfair+Display:wght@400;700&display=swap');

      header, footer, #MainMenu {visibility:hidden;}

      .stApp, [data-testid="stAppViewContainer"],
      [data-testid="stMain"] {
        background:#e4ceb0 !important;
      }

      section[data-testid="stSidebar"] {
        background:linear-gradient(170deg,#493025,#302019) !important;
        border-right:1px solid rgba(101,68,47,.35);
      }

      section[data-testid="stSidebar"] * {
        color: #f8e9d2 !important;
      }

      .pf-side {
        font-family:'DM Sans',sans-serif;
        color:#f8e9d2;
        padding:0 .4rem 1rem;
      }

      .pf-star {
        font-size:30px;
        line-height:1;
        color:#e8c27a;
        text-align:center;
        margin:1.1rem 0 .9rem;
      }

      .pf-title {
        font-family:'Playfair Display',serif;
        font-size:1.7rem;
        font-weight:700;
        color:#f8e9d2;
        line-height:1.15;
        margin:.3rem 0;
      }

      .pf-sub {
        font-family:'DM Mono',monospace;
        font-size:.72rem;
        letter-spacing:.14em;
        text-transform:uppercase;
        color:#d5bea0;
        margin-bottom:1.2rem;
      }

      .pf-desc {
        font-size:.88rem;
        line-height:1.65;
        color:#dfc8ae;
        margin-bottom:1rem;
      }

      .pf-div {
        height:1px;
        margin:1.2rem 0;
        background:linear-gradient(
          90deg,transparent,#98704e 20%,#e0c49e 50%,
          #98704e 80%,transparent
        );
      }

      .pf-h {
        font-family:'Playfair Display',serif;
        font-size:1.2rem;
        color:#f8e9d2;
        margin-bottom:.7rem;
      }

      .nav-item {
        display:flex;
        align-items:center;
        gap:.6rem;
        padding:.35rem 0;
        cursor:pointer;
        font-size:.9rem;
        color:#e8d5bf;
        text-decoration:none;
        transition:transform .25s ease,color .25s ease;
      }

      .nav-item span {
        display:inline-block;
        color:#c7a47e;
        transition:transform .4s ease,color .3s;
      }

      .nav-item:hover {
        transform:translateX(7px);
        color:#fff;
      }

      .nav-item:hover span {
        transform:rotate(180deg) scale(1.35);
        color:#e8c27a;
      }

      .pf-foot {
        margin-top:1.6rem;
        padding-top:1rem;
        border-top:1px solid rgba(101,68,47,.5);
        font-family:'DM Mono',monospace;
        font-size:.72rem;
        color:#b89c7d;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# CONTENIDO DE LA BARRA LATERAL (SIDEBAR)
# ==========================================================
SIDEBAR_HTML = """
<div class="pf-side">
    <div class="pf-star">✦</div>
    <div class="pf-title">Archivo Creativo</div>
    <div class="pf-sub">Portafolio · Segunda etapa</div>

    <div class="pf-desc">
        Una colección de experimentos donde la voz, el gesto, el tacto
        y la imagen se combinan para crear formas más naturales de
        dialogar con la tecnología.
    </div>

    <div class="pf-div"></div>
    <div class="pf-h">Dentro del cuaderno</div>

    <a href="#card-1" class="nav-item"><span>✎</span> Dibujo y reconocimiento</a>
    <a href="#card-2" class="nav-item"><span>◉</span> Sensores y simulación</a>
    <a href="#card-5" class="nav-item"><span>⌘</span> Herramientas tecnológicas</a>
    <a href="#card-6" class="nav-item"><span>↗</span> Repositorios y proyectos</a>
    <a href="#reflexiones" class="nav-item"><span>✧</span> Reflexiones</a>

    <div class="pf-foot">Voz · Gesto · Tacto · Imagen · Sonido</div>
</div>
"""
st.sidebar.markdown(SIDEBAR_HTML, unsafe_allow_html=True)


# ==========================================================
# DATOS DE LAS ACTIVIDADES PRÁCTICAS
# ==========================================================
actividades = [
    {
        "id": 1,
        "titulo": "Actividad 01: Detección de Números a través de dibujos",
        "categoria": "Práctica · 01",
        "resumen": "Una red neuronal entrenada con MNIST que reconoce los dígitos que dibujo sobre un lienzo.",
        "descripcion": "MNIST es una base de datos compuesta por 70,000 imágenes de dígitos escritos a mano. Desplegué la aplicación del repositorio y escribí diferentes números; el modelo reconoce lo escrito después de revisar el Google Colab.",
        "aprendizaje": "Aprendí cómo las redes convolucionales aprenden bordes, formas y texturas, y que el trazo debe prepararse para que el modelo lo interprete bien.",
        "url": "https://mnistpredsimon-5vckfxydhqvco4snzsuo8s.streamlit.app/",
        "botonTexto": "Abrir recurso"
    },
    {
        "id": 2,
        "titulo": "Actividad 02: Tablero Personalizado",
        "categoria": "Edición · 02",
        "resumen": "Un tablero de dibujo cuyas propiedades puedo configurar a mi gusto.",
        "descripcion": "Edité el ejemplo inicial de la primera actividad para que las propiedades del tablero se configuren desde la interfaz.",
        "aprendizaje": "Personalizar la herramienta es parte de diseñar la interacción; se practica cómo exponer parámetros con los controles de Streamlit.",
        "url": "https://repositorio-2-simon-eg936rwzmxxzqdssn5lhlk.streamlit.app/",
        "botonTexto": "Abrir recurso"
    },
    {
        "id": 3,
        "titulo": "Actividad 03: Tablero Reconocimiento",
        "categoria": "Interfaz · 03",
        "resumen": "Un tablero que reconoce lo que dibujo usando modelos de visión.",
        "descripcion": "Combiné el tablero con un modelo de visión que identifica bocetos.",
        "aprendizaje": "Aprendí la diferencia entre un clasificador de una sola tarea (MNIST) y un modelo de visión más general, y cómo dibujo e imagen funcionan como un canal multimodal de reconocimiento.",
        "url": "https://drawrecogsimon-mrzchike38innmhbruk49k.streamlit.app/",
        "botonTexto": "Abrir recurso"
    },
    {
        "id": 4,
        "titulo": "Actividad 04: Tablero Cuenta Historias",
        "categoria": "Simulación · 04",
        "resumen": "Un tablero digital que convierte mis dibujos en historias.",
        "descripcion": "Fui más allá de reconocer una figura para crear narrativamente una historia con contexto.",
        "aprendizaje": "Aprendí a pensar el reconocimiento como el inicio de una experiencia y a encadenar una entrada visual con una salida de texto.",
        "url": "https://simonhistoriadibujo-cbtrgvlhhqu3aht43y8tlo.streamlit.app/",
        "botonTexto": "Abrir recurso"
    },
    {
        "id": 5,
        "titulo": "Actividad 05: Recepción de Datos MQTT",
        "categoria": "Tecnología · 05",
        "resumen": "Monitoreo en tiempo real de telemetría desde un sensor analógico simulado en Wokwi hacia la app en Streamlit.",
        "descripcion": "Se organizó bajo la arquitectura cliente-broker. Un circuito en Wokwi actúa como cliente publicador, enviando lecturas de un sensor analógico a un broker MQTT en un tópico específico. La app en Streamlit opera como cliente suscriptor, conectándose al broker y escuchando ese tópico para visualizar los datos en vivo.",
        "aprendizaje": "Entendí el patrón Publish/Subscribe, cómo el broker gestiona los mensajes y cómo recibir flujo continuo de telemetría en un cliente web.",
        "url": "https://recepmqtt-c632mej72ce2uypzr9henl.streamlit.app/",
        "botonTexto": "Abrir recurso"
    },
    {
        "id": 6,
        "titulo": "Actividad 06: Publicación y Telecontrol MQTT",
        "categoria": "Aprendizaje · 06",
        "resumen": "Telecontrol bidireccional desde la interfaz web para activar LEDs en el simulador Wokwi.",
        "descripcion": "Se invirtió el flujo de control: la app en Streamlit funciona como cliente publicador, enviando comandos de encendido/apagado de luces y ángulo del servomotor a un tópico del broker MQTT. En Wokwi, el microcontrolador actúa como cliente suscriptor, escuchando el tópico para ejecutar las acciones en el hardware simulado.",
        "aprendizaje": "Aprendí a estructurar comandos de control desde un cliente web hacia actuadores remotos usando tópicos de instrucción en el broker MQTT.",
        "url": "https://sendcmqttsimon-5e3raacaadr2kz3jago5z9.streamlit.app/",
        "botonTexto": "Abrir recurso"
    },
    {
        "id": 7,
        "titulo": "Actividad 07: Control Multimodal por Voz",
        "categoria": "Hardware · 07",
        "resumen": "Control de luces y puertas mediante comandos vocales procesados en la web y transmitidos al simulador.",
        "descripcion": "Se estructuró capturando la voz del usuario en un cliente web (Streamlit), traduciendo frases habladas en variables lógicas. Estas se publican hacia el broker MQTT dentro del tópico correspondiente, donde el microcontrolador en Wokwi (cliente suscriptor) recibe la orden y mueve el servomotor o altera los LEDs.",
        "aprendizaje": "Aprendí a integrar la voz como canal de entrada multimodal y a mapear eventos de audio con comandos enviados a través de un broker MQTT.",
        "url": "https://ctrlvoicesimon-skzxvxkj3e8l323ky3i5bp.streamlit.app/",
        "botonTexto": "Abrir recurso"
    }
]


# ==========================================================
# CONSTRUCCIÓN DE LAS TARJETAS HTML (DISEÑO AISLADO PARA EVITAR QUE AFECTE A LAS VECINAS)
# ==========================================================
foto_b64 = cargar_foto_portada()

if foto_b64:
    img_portada_html = f'<img src="{foto_b64}" alt="Fotografía de portada" class="w-full h-full object-cover">'
else:
    img_portada_html = """
    <div class='img-fallback'>
        <span class='text-2xl'>✦</span>
        <strong class='text-xs mt-1'>Fotografía de prueba</strong>
        <small class='text-[10px]'>Simon.jpeg</small>
    </div>
    """

cards_html_string = ""
for act in actividades:
    url_btn = crear_enlace(act["url"], act["botonTexto"])
    cards_html_string += f"""
    <article id="card-{act['id']}" class="polaroid-card flex flex-col justify-between">
        <div>
            <div class="polaroid-img-wrapper mb-4">
                <img src="Blanco.jpeg" alt="{esc(act['titulo'])}" class="polaroid-img"
                     onerror="this.onerror=null;this.parentElement.innerHTML='<div class=\\'img-fallback\\'><span>✦</span><strong class=\\'text-xs\\'>Blanco.jpeg</strong></div>';">
            </div>

            <div class="flex justify-between items-center mb-2 font-mono-custom text-xs text-[#987554] uppercase tracking-wider">
                <span>{esc(act['categoria'])}</span>
                <span class="num-badge border border-[#d5b995] bg-[#f6e7d1] rounded-full w-7 h-7 flex items-center justify-center font-semibold text-[#65442f]">
                    {act['id']:02d}
                </span>
            </div>

            <h3 class="font-serif-custom text-xl font-bold mb-2 text-[#38251d]">
                {esc(act['titulo'])}
            </h3>

            <p class="text-sm text-[#796451] leading-relaxed">
                {esc(act['resumen'])}
            </p>
        </div>

        <div class="mt-4 pt-3 border-t border-[#e0ccb0]">
            <button onclick="toggleCard({act['id']})" id="btn-toggle-{act['id']}" class="btn-vintage btn-read-more mb-3">
                Leer más información ＋
            </button>

            <div id="details-{act['id']}" class="expandable-content space-y-3">
                <p class="text-sm text-[#6f5845] leading-relaxed">
                    {esc(act['descripcion'])}
                </p>
                <p class="text-sm text-[#6f5845] leading-relaxed">
                    <strong class="text-[#4a3021]">Lo que me llevo:</strong> 
                    {esc(act['aprendizaje'])}
                </p>
                <div class="pt-2">
                    {url_btn}
                </div>
            </div>
        </div>
    </article>
    """


# ==========================================================
# ESTRUCTURA HTML PRINCIPAL CON CSS AISLADO PARA LAS TARJETAS
# ==========================================================
HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Portafolio II | Interfaces Multimodales</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;700&family=Playfair+Display:wght@400;700;800&display=swap" rel="stylesheet">

<script src="https://cdn.tailwindcss.com"></script>

<style>
:root {{
    --dark-coffee:#38251d;
    --coffee:#65442f;
    --brown-accent:#916a49;
    --beige-dark:#d5bea0;
    --beige-light:#ead7bb;
    --cream-bg:#fff8ec;
    --cream-card:#fffaf0;
    --ink-text:#402d21;
    --terracotta:#a8583b;
}}

body {{
    margin:0;
    background:
        radial-gradient(ellipse at 10% 10%,#fff9e9,transparent 40%),
        linear-gradient(135deg,#e4ceb0,#f6ead7 50%,#dfc4a0);
    font-family:'DM Sans',sans-serif;
    color:var(--ink-text);
    padding: 1.5rem 1rem;
}}

h1,h2,h3,.font-serif-custom {{
    font-family:'Playfair Display',serif;
    color:var(--dark-coffee);
}}

.font-mono-custom {{font-family:'DM Mono',monospace;}}

.vintage-divider {{
    border:0;
    height:1px;
    background:linear-gradient(
        90deg,transparent,#98704e 20%,#e0c49e 50%,
        #98704e 80%,transparent
    );
    margin:2.5rem 0;
}}

.hero-box {{
    background:linear-gradient(125deg,#fff9ed,#ead6b8);
    border:1px solid #d2b99a;
    box-shadow:0 18px 42px rgba(87,58,38,.12);
}}

.portrait-frame {{
    position:relative;
    background:#fffaf0;
    box-shadow:8px 12px 0 rgba(105,72,43,.12),
               0 15px 30px rgba(64,41,25,.15);
    transform:rotate(-2.5deg);
    transition:transform .4s ease;
}}

.portrait-frame:hover {{transform:rotate(0) scale(1.02);}}

/* GRILLA DE 2 COLUMNAS PERFECTA Y ESTABLE */
.gallery-grid {{
    display:grid;
    grid-template-columns:repeat(2,minmax(0,1fr));
    gap:2.5rem 2rem;
    align-items:start;
}}

/* CADA TARJETA ES INDEPENDIENTE EN SU ALTO Y ANIMACIÓN */
.polaroid-card {{
    position:relative;
    isolation:isolate;
    padding:18px 18px 22px;
    border:2px solid #dcd0be;
    border-radius:16px;
    background:linear-gradient(145deg,#fffaf0,#f2e4cf);
    box-shadow:0 10px 22px rgba(56,37,29,.1);
    transition:transform .3s ease, border-color .3s ease, box-shadow .3s ease, background-color .3s ease;
    height: auto;
}}

.polaroid-card:hover {{
    transform:translateY(-5px);
    border-color:#65442f;
    background:#fff;
    box-shadow:0 20px 35px rgba(56,37,29,0.18);
    z-index: 10;
}}

.polaroid-img-wrapper {{
    width:100%;
    height:210px;
    overflow:hidden;
    border-radius:10px;
    border:1px solid rgba(101,68,47,.15);
    background:#e8d7c1;
    position:relative;
}}

.polaroid-img {{
    width:100%;
    height:100%;
    object-fit:cover;
    filter:sepia(.9) saturate(.85) contrast(.95) brightness(.98);
    transition:filter .5s ease,transform .4s ease;
}}

.polaroid-card:hover .polaroid-img {{
    filter:sepia(0) saturate(1) contrast(1) brightness(1);
    transform:scale(1.03);
}}

/* BOTONES VINTAGE */
.btn-vintage {{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    padding:8px 16px;
    border-radius:20px;
    font-size:.82rem;
    font-weight:600;
    text-decoration:none;
    transition:all .25s ease;
    cursor:pointer;
    user-select:none;
    white-space:nowrap;
}}

.btn-read-more {{
    background:#ebd8bf;
    color:#523724;
    border:1px solid #c5aa8a;
    width: 100%;
}}

.btn-read-more:hover {{
    background:#dfc3a1;
    color:#38251d;
}}

.btn-link {{
    background:#65442f;
    color:#fff8ec;
    border:1px solid #4a3121;
    display: inline-block;
    margin-top: 4px;
}}

.btn-link:hover {{
    background:#38251d;
    color:#fff;
    box-shadow:0 4px 10px rgba(56,37,29,.25);
}}

/* CONTENIDO DESPLEGABLE CON JS PURO (SOLO SE EXTIENDE LA CARD ACTIVA) */
.expandable-content {{
    max-height: 0;
    overflow: hidden;
    opacity: 0;
    transition: max-height 0.4s ease-out, opacity 0.3s ease-out;
}}

.expandable-content.open {{
    max-height: 500px;
    opacity: 1;
}}

.img-fallback {{
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    width:100%;
    height:100%;
    min-height:180px;
    background:repeating-linear-gradient(
        45deg,#f2e2cb,#f2e2cb 10px,#ead7bb 10px,#ead7bb 12px
    );
    color:#725942;
    text-align:center;
}}

.modal-note {{
    background:linear-gradient(135deg,#fffaf0,#f2e4cf);
    border:1px solid #d2b895;
    border-radius:16px;
    box-shadow:0 10px 24px rgba(56,37,29,.1);
}}

.channel-chip {{
    display:inline-flex;
    align-items:center;
    gap:.4rem;
    padding:.35rem .8rem;
    border-radius:999px;
    background:#fff9ef;
    border:1px solid #cdb393;
    color:#694a32;
    font-family:'DM Mono',monospace;
    font-size:.75rem;
}}

@media (max-width:900px) {{
    .gallery-grid {{grid-template-columns:1fr;}}
}}
</style>
</head>

<body>

<main class="max-w-[1450px] mx-auto w-full">

    <!-- PORTADA -->
    <section class="hero-box rounded-2xl p-6 md:p-8 relative mb-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            <div class="lg:col-span-4 flex justify-center lg:justify-start">
                <div class="portrait-frame p-3 pb-4 max-w-[280px] w-full rounded-sm">
                    <div class="w-full h-48 md:h-52 bg-[#e2d1b8] rounded overflow-hidden">
                        {img_portada_html}
                    </div>
                    <div class="text-center mt-3 font-mono-custom text-xs text-[#79583e] tracking-wider uppercase font-semibold">
                        SIMÓN MESA DÍAZ · PORTAFOLIO II
                    </div>
                </div>
            </div>

            <div class="lg:col-span-8 space-y-4">
                <div class="font-mono-custom text-xs tracking-widest text-[#8d5b3d] uppercase">
                    Cuaderno digital · Semestre 2026-02 · Edición 02
                </div>

                <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold leading-tight">
                    ✦ Interfaces<br>
                    <span class="italic text-[#9a714d]">multimodales.</span> ✦
                </h1>

                <div class="text-base md:text-lg text-[#65442f] leading-relaxed max-w-3xl">
                    Hola, soy <strong>Simón Mesa Díaz</strong> y me encuentro
                    cursando el sexto semestre del pregrado de Diseño Interactivo
                    en la Universidad EAFIT. Este espacio reúne mis experiencias,
                    experimentos y aprendizajes de la segunda parte de las clases
                    de "Creación de Interfaces Multimodales" del semestre.
                    <br><br>
                    Aprender haciendo, experimentar sin miedo y transformar
                    códigos e ideas en experiencias interactivas con intención
                    y temáticas aplicables de forma multimodal.
                </div>

                <div class="flex flex-wrap gap-2 pt-2">
                    <span class="px-3 py-1 bg-[#fff9ef] border border-[#cdb393] rounded-full text-xs font-mono-custom text-[#694a32]">✳ Diseño interactivo</span>
                    <span class="px-3 py-1 bg-[#fff9ef] border border-[#cdb393] rounded-full text-xs font-mono-custom text-[#694a32]">⌘ Experimentación</span>
                    <span class="px-3 py-1 bg-[#fff9ef] border border-[#cdb393] rounded-full text-xs font-mono-custom text-[#694a32]">↗ Aprender haciendo</span>
                </div>
            </div>
        </div>
    </section>

    <hr class="vintage-divider">

    <section class="mb-8">
        <div class="font-mono-custom text-xs tracking-widest text-[#8d5b3d] uppercase mb-1">
            Galería de procesos · 01—07
        </div>
        <h2 class="text-3xl md:text-4xl font-bold text-[#38251d]">
            Actividades prácticas realizadas
        </h2>
        <p class="text-sm text-[#725942] mt-2">
            Pasa el cursor sobre las tarjetas y despliega la información detallada de cada práctica de manera independiente.
        </p>
    </section>

    <!-- GALERÍA DE CARDS -->
    <div class="gallery-grid">
        {cards_html_string}
    </div>

    <!-- REFLEXIÓN FINAL -->
    <section id="reflexiones" class="modal-note mt-12 p-6 md:p-8 text-center">
        <div class="font-mono-custom text-xs tracking-widest text-[#8d5b3d] uppercase mb-2">
            Reflexión · Multimodalidad
        </div>

        <h3 class="font-serif-custom text-2xl md:text-3xl font-bold mb-3">
            Hablar con la tecnología con todos los sentidos
        </h3>

        <p class="text-[#65442f] leading-relaxed max-w-3xl mx-auto mb-5">
            Una interfaz multimodal no depende de un solo canal: permite tocar,
            hablar, señalar, mirar o escuchar, y elegir en cada momento la forma
            más natural de comunicarse. Diseñar así es pensar en las personas,
            en sus contextos y en sus capacidades, para que la tecnología se
            adapte a ellas y no al revés.
        </p>

        <div class="flex flex-wrap justify-center gap-2">
            <span class="channel-chip">✋ Tacto</span>
            <span class="channel-chip">🎙 Voz</span>
            <span class="channel-chip">👁 Visión</span>
            <span class="channel-chip">☝ Gesto</span>
            <span class="channel-chip">🔊 Sonido</span>
        </div>
    </section>

    <footer class="mt-8 mb-2 text-center text-xs font-mono-custom text-[#80654d] tracking-widest uppercase">
        Fin de la página, no del proceso · Diseñado con curiosidad
    </footer>
</main>

<script>
// Función para expandir y contraer de forma totalmente independiente cada tarjeta
function toggleCard(id) {{
    const content = document.getElementById('details-' + id);
    const btn = document.getElementById('btn-toggle-' + id);
    
    if (content.classList.contains('open')) {{
        content.classList.remove('open');
        btn.innerHTML = 'Leer más información ＋';
    }} else {{
        content.classList.add('open');
        btn.innerHTML = 'Leer menos información －';
    }}
}}
</script>

</body>
</html>
"""

# Renderizamos todo el diseño integrado con el sistema incrustador de imágenes
components.html(incrustar_imagenes(HTML_CONTENT), height=2400, scrolling=True)
