
import base64
import html
import mimetypes
from pathlib import Path
from urllib.parse import urlparse

import streamlit as st


# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

st.set_page_config(
    page_title="Mi portafolio | Interfaces multimodales",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).parent


# =========================================================
# FUNCIONES AUXILIARES
# Cada imagen tiene su propia ruta y se carga por separado.
# =========================================================

def cargar_foto(ruta_imagen, texto_alternativo="Fotografía"):
    ruta = BASE_DIR / ruta_imagen

    if ruta.is_file():
        mime_type = mimetypes.guess_type(ruta.name)[0] or "image/jpeg"

        with open(ruta, "rb") as archivo:
            contenido = base64.b64encode(archivo.read()).decode("utf-8")

        return (
            f'<img class="foto-polaroid" '
            f'src="data:{mime_type};base64,{contenido}" '
            f'alt="{html.escape(texto_alternativo)}">'
        )

    # Si todavía no has agregado la imagen, muestra un espacio
    # reservado con el nombre del archivo que debes colocar.
    return f"""
    <div class="foto-pendiente">
        <span class="camara">✳</span>
        <span>Coloca aquí</span>
        <strong>Blanco.jpg</strong>
    </div>
    """


def validar_url(url):
    """Permite enlaces web válidos y evita enlaces vacíos."""
    if not url:
        return None

    url = url.strip()
    partes = urlparse(url)

    if partes.scheme in ("http", "https") and partes.netloc:
        return url

    return None


def crear_tarjeta(actividad, numero):
    # Cada tarjeta llama su propia ruta de imagen.
    # No se comparte una variable de imagen entre tarjetas.
    imagen_html = cargar_foto(
        actividad["imagen"],
        actividad["titulo"],
    )

    titulo = html.escape(actividad["titulo"])
    descripcion = html.escape(actividad["descripcion"])
    categoria = html.escape(actividad["categoria"])

    url = validar_url(actividad["url"])

    if url:
        boton_enlace = f"""
        <a class="boton boton-enlace"
           href="{html.escape(url, quote=True)}"
           target="_blank"
           rel="noopener noreferrer">
            Enlace <span>↗</span>
        </a>
        """
    else:
        # Si todavía no has agregado la URL, se usa una
        # dirección de ejemplo que puedes reemplazar.
        boton_enlace = """
        <a class="boton boton-enlace"
           href="https://www.google.com/"
           target="_blank"
           rel="noopener noreferrer">
            Enlace <span>↗</span>
        </a>
        """

    return f"""
    <article class="tarjeta" style="--retraso: {numero * 0.08}s;">
        <div class="marco-foto">
            {imagen_html}
            <span class="numero-foto">{numero:02d}</span>
        </div>

        <div class="contenido-tarjeta">
            <p class="categoria">{categoria}</p>
            <h3>{titulo}</h3>

            <div class="botones">
                <details class="detalle">
                    <summary class="boton boton-leer">
                        Leer más <span class="flecha">⌄</span>
                    </summary>

                    <div class="descripcion">
                        <p>{descripcion}</p>
                    </div>
                </details>

                {boton_enlace}
            </div>
        </div>
    </article>
    """


# =========================================================
# INFORMACIÓN EDITABLE DEL PORTAFOLIO
# =========================================================

nombre = "Tu nombre aquí"
subtitulo = "Creación de Interfaces Multimodales"
presentacion = (
    "Este portafolio reúne mis actividades, aprendizajes y "
    "experiencias durante el curso. Aquí podrás explorar "
    "cada proyecto, conocer su propósito y visitar el enlace "
    "correspondiente. Este texto es de ejemplo y puedes "
    "reemplazarlo por tu presentación personal."
)

# Cada imagen usa una ruta distinta, aunque todos los archivos
# se llamen Blanco.jpg.
actividades = [
    {
        "titulo": "Actividad 01",
        "categoria": "Exploración",
        "descripcion": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing "
            "elit. Esta actividad permitió explorar conceptos "
            "iniciales del curso, reconocer referentes y comprender "
            "los fundamentos necesarios para desarrollar una "
            "interfaz multimodal. Aquí podrás escribir la descripción "
            "real de tu actividad."
        ),
        "imagen": "imagenes/actividad01/Blanco.jpg",
        "url": "https://www.google.com/",
    },
    {
        "titulo": "Actividad 02",
        "categoria": "Investigación",
        "descripcion": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing "
            "elit. En esta actividad se recopilaron ideas, se "
            "analizaron referentes y se organizaron los hallazgos "
            "más importantes. Reemplaza este contenido con la "
            "información de tu trabajo."
        ),
        "imagen": "imagenes/actividad02/Blanco.jpg",
        "url": "https://www.google.com/",
    },
    {
        "titulo": "Actividad 03",
        "categoria": "Diseño",
        "descripcion": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing "
            "elit. Esta propuesta se centra en la construcción "
            "visual de una experiencia, la elección de recursos "
            "gráficos y la organización de los contenidos."
        ),
        "imagen": "imagenes/actividad03/Blanco.jpg",
        "url": "https://www.google.com/",
    },
    {
        "titulo": "Actividad 04",
        "categoria": "Prototipado",
        "descripcion": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing "
            "elit. En este ejercicio se desarrolla una propuesta "
            "de interacción y se exploran distintas posibilidades "
            "para mejorar la experiencia de las personas usuarias."
        ),
        "imagen": "imagenes/actividad04/Blanco.jpg",
        "url": "https://www.google.com/",
    },
    {
        "titulo": "Actividad 05",
        "categoria": "Experimentación",
        "descripcion": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing "
            "elit. Este espacio está destinado a documentar "
            "pruebas, decisiones de diseño, observaciones y "
            "resultados obtenidos durante el proceso creativo."
        ),
        "imagen": "imagenes/actividad05/Blanco.jpg",
        "url": "https://www.google.com/",
    },
    {
        "titulo": "Actividad 06",
        "categoria": "Proyecto final",
        "descripcion": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing "
            "elit. Aquí puedes presentar el resultado final, "
            "explicar sus características principales y compartir "
            "una reflexión sobre lo aprendido durante el curso."
        ),
        "imagen": "imagenes/actividad06/Blanco.jpg",
        "url": "https://www.google.com/",
    },
]


# =========================================================
# ESTILOS VISUALES
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap');

    :root {
        --crema: #f7f0e5;
        --papel: #fffaf1;
        --beige: #e5d3b8;
        --cafe: #77543b;
        --cafe-oscuro: #3f2c20;
        --tinta: #38291f;
        --dorado: #c19a60;
        --borde: #dfcbb0;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 10% 5%,
                rgba(193,154,96,.12), transparent 35%),
            var(--crema);
        color: var(--tinta);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stSidebar"] {
        background: #e9dcc8;
        border-right: 1px solid #d4bea0;
    }

    [data-testid="stSidebar"] * {
        color: var(--cafe-oscuro);
    }

    .bloque-sidebar {
        padding: 16px 5px;
    }

    .sello {
        display: inline-block;
        border: 1px solid var(--cafe);
        border-radius: 50%;
        width: 66px;
        height: 66px;
        line-height: 64px;
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        transform: rotate(-9deg);
        margin-bottom: 18px;
        background: rgba(255,250,241,.45);
    }

    .sidebar-titulo {
        font-family: 'Playfair Display', serif;
        font-size: 25px;
        font-weight: 600;
        line-height: 1.2;
        margin-bottom: 8px;
    }

    .sidebar-texto {
        font-size: 13px;
        line-height: 1.7;
        opacity: .8;
    }

    .sidebar-linea {
        height: 1px;
        background: #cbb494;
        margin: 22px 0;
    }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 45px 40px;
        border-radius: 7px;
        border: 1px solid var(--borde);
        background:
            linear-gradient(125deg,
                rgba(255,250,241,.97),
                rgba(235,219,195,.88));
        box-shadow: 0 12px 32px rgba(73,49,29,.08);
        margin-bottom: 35px;
    }

    .hero::before {
        content: "✳";
        position: absolute;
        right: 32px;
        top: 8px;
        font-size: 110px;
        color: rgba(151,111,65,.14);
        transform: rotate(15deg);
        pointer-events: none;
    }

    .eyebrow {
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 11px;
        font-weight: 700;
        color: var(--cafe);
        margin-bottom: 14px;
    }

    .hero h1 {
        font-family: 'Playfair Display', serif;
        font-weight: 500;
        font-size: clamp(36px, 5vw, 65px);
        line-height: 1.06;
        color: var(--cafe-oscuro);
        margin: 0 0 18px;
        max-width: 720px;
    }

    .hero p {
        font-size: 15px;
        line-height: 1.9;
        max-width: 650px;
        color: #6d5540;
    }

    .hero-pie {
        margin-top: 25px;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }

    .etiqueta {
        display: inline-block;
        border: 1px solid #cbb494;
        padding: 7px 12px;
        border-radius: 30px;
        font-size: 11px;
        letter-spacing: .5px;
        color: #6b4c32;
        background: rgba(255,250,241,.65);
    }

    .presentacion {
        background: var(--papel);
        border: 1px solid var(--borde);
        padding: 20px;
        border-radius: 6px;
        box-shadow: 5px 6px 0 rgba(119,84,59,.10);
        transform: rotate(1deg);
        margin-bottom: 28px;
    }

    .presentacion img,
    .presentacion .foto-pendiente {
        width: 100%;
        aspect-ratio: 4 / 5;
        object-fit: cover;
        display: block;
    }

    .presentacion-pie {
        font-family: 'Playfair Display', serif;
        text-align: center;
        font-size: 19px;
        padding-top: 15px;
        color: var(--cafe-oscuro);
    }

    .seccion-kicker {
        text-transform: uppercase;
        letter-spacing: 3px;
        color: var(--cafe);
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .seccion-titulo {
        font-family: 'Playfair Display', serif;
        color: var(--cafe-oscuro);
        font-size: clamp(29px, 4vw, 42px);
        font-weight: 500;
        line-height: 1.15;
        margin: 0 0 12px;
    }

    .seccion-descripcion {
        color: #78624d;
        font-size: 14px;
        line-height: 1.8;
        margin-bottom: 26px;
    }

    .tarjeta {
        background: var(--papel);
        border: 1px solid #e4d4bf;
        padding: 12px 12px 16px;
        border-radius: 4px;
        box-shadow: 0 5px 12px rgba(62,42,25,.08),
                    0 16px 28px rgba(62,42,25,.04);
        height: 100%;
        position: relative;
        transition: transform .28s ease,
                    box-shadow .28s ease,
                    border-color .28s ease;
        animation: aparecer .6s ease both;
        animation-delay: var(--retraso, 0s);
    }

    .tarjeta::after {
        content: "✦";
        position: absolute;
        top: -11px;
        right: 8px;
        font-size: 22px;
        color: var(--dorado);
        opacity: 0;
        transition: opacity .25s ease, transform .25s ease;
        pointer-events: none;
    }

    .tarjeta:hover {
        transform: translateY(-7px) rotate(-1deg) scale(1.015);
        border-color: #c19a60;
        box-shadow: 0 0 0 1px rgba(193,154,96,.24),
                    0 12px 30px rgba(62,42,25,.14),
                    0 0 22px rgba(193,154,96,.12);
    }

    .tarjeta:hover::after {
        opacity: 1;
        transform: rotate(20deg);
    }

    .marco-foto {
        position: relative;
        background: #e7d9c5;
        overflow: hidden;
    }

    .foto-polaroid {
        display: block;
        width: 100%;
        aspect-ratio: 4 / 3;
        object-fit: cover;
        filter: sepia(.12) saturate(.85);
        transition: transform .45s ease, filter .45s ease;
    }

    .tarjeta:hover .foto-polaroid {
        transform: scale(1.035);
        filter: sepia(0) saturate(1);
    }

    .foto-pendiente {
        width: 100%;
        aspect-ratio: 4 / 3;
        background:
            repeating-linear-gradient(
                135deg,
                #efe4d3,
                #efe4d3 12px,
                #e8d8c2 12px,
                #e8d8c2 24px
            );
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 7px;
        color: #80654a;
        font-size: 12px;
        text-align: center;
    }

    .foto-pendiente strong {
        font-family: 'DM Mono', monospace;
        font-size: 12px;
    }

    .camara {
        font-size: 30px;
        color: #a1825d;
    }

    .numero-foto {
        position: absolute;
        right: 8px;
        top: 8px;
        background: rgba(255,250,241,.91);
        border: 1px solid #ddc8aa;
        padding: 4px 7px;
        font-family: 'DM Mono', monospace;
        font-size: 10px;
        color: var(--cafe);
    }

    .contenido-tarjeta {
        padding: 16px 5px 0;
    }

    .categoria {
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #9a7954;
        font-weight: 700;
        margin: 0 0 7px;
    }

    .contenido-tarjeta h3 {
        font-family: 'Playfair Display', serif;
        font-size: 23px;
        font-weight: 500;
        line-height: 1.25;
        color: var(--cafe-oscuro);
        margin: 0 0 16px;
        overflow-wrap: anywhere;
    }

    .botones {
        display: grid;
        grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
        gap: 8px;
        align-items: start;
    }

    .boton {
        box-sizing: border-box;
        width: 100%;
        min-height: 39px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 7px;
        padding: 10px 7px;
        border-radius: 3px;
        font-family: 'DM Sans', sans-serif;
        font-size: 12px;
        font-weight: 600;
        text-align: center;
        text-decoration: none !important;
        cursor: pointer;
        transition: background .2s ease, color .2s ease;
    }

    .boton-leer {
        list-style: none;
        background: #745238;
        color: #fff8ed !important;
        border: 1px solid #745238;
    }

    .boton-leer::-webkit-details-marker {
        display: none;
    }

    .boton-leer:hover {
        background: #513823;
    }

    .flecha {
        transition: transform .2s ease;
    }

    .detalle[open] .flecha {
        transform: rotate(180deg);
    }

    .boton-enlace {
        background: #eee1cd;
        border: 1px solid #d6c1a2;
        color: #5d422b !important;
    }

    .boton-enlace:hover {
        background: #dfc8a8;
    }

    .descripcion {
        grid-column: 1 / -1;
        padding: 13px 2px 3px;
        animation: aparecer .25s ease;
    }

    .descripcion p {
        color: #715a43;
        font-size: 12px;
        line-height: 1.85;
        margin: 0;
        overflow-wrap: anywhere;
    }

    .detalle {
        min-width: 0;
    }

    .detalle[open] {
        grid-column: 1 / -1;
    }

    .detalle[open] .descripcion {
        padding: 12px 10px 13px;
        background: #f3e8d7;
        border-left: 2px solid #b89568;
        margin-top: 8px;
    }

    .detalle[open] ~ .boton-enlace {
        grid-column: 1 / -1;
    }

    .pie {
        text-align: center;
        border-top: 1px solid #d9c6aa;
        padding: 25px 10px 8px;
        margin-top: 45px;
        color: #896e50;
        font-size: 11px;
        letter-spacing: 1px;
    }

    @keyframes aparecer {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @media (max-width: 700px) {
        .hero {
            padding: 30px 23px;
        }

        .hero::before {
            right: 8px;
            font-size: 75px;
        }

        .contenido-tarjeta h3 {
            font-size: 20px;
        }
    }

    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            animation-duration: .01ms !important;
            transition-duration: .01ms !important;
            scroll-behavior: auto !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# BARRA LATERAL
# =========================================================

with st.sidebar:
    st.markdown(
        f"""
        <div class="bloque-sidebar">
            <div class="sello">MM</div>
            <div class="sidebar-titulo">Mi cuaderno<br>creativo</div>
            <p class="sidebar-texto">
                Un archivo visual de ideas, experimentos
                y aprendizajes.
            </p>
            <div class="sidebar-linea"></div>
            <p class="eyebrow">Índice del portafolio</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    seccion = st.radio(
        "Navegación",
        ["Portada", "Mis actividades", "Sobre mí"],
        label_visibility="collapsed",
    )

    st.markdown(
        """
        <div class="sidebar-linea"></div>
        <p class="sidebar-texto">
            CREACIÓN DE INTERFACES MULTIMODALES<br><br>
            Edición de portafolio · 2026
        </p>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# PORTADA
# =========================================================

if seccion == "Portada":
    st.markdown(
        f"""
        <section class="hero">
            <div class="eyebrow">Portafolio académico · 2026</div>
            <h1>Ideas que toman<br>forma y color.</h1>
            <p>{html.escape(presentacion)}</p>
            <div class="hero-pie">
                <span class="etiqueta">Diseño</span>
                <span class="etiqueta">Exploración</span>
                <span class="etiqueta">Interfaces multimodales</span>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    col_foto, col_texto = st.columns([1, 2], gap="large")

    with col_foto:
        foto_presentacion = cargar_foto(
            "imagenes/perfil/Blanco.jpg",
            "Fotografía de presentación",
        )

        st.markdown(
            f"""
            <div class="presentacion">
                {foto_presentacion}
                <div class="presentacion-pie">
                    {html.escape(nombre)}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_texto:
        st.markdown(
            """
            <div style="padding: 12px 5px;">
                <div class="seccion-kicker">Un poco sobre mí</div>
                <h2 class="seccion-titulo">
                    Mi proceso, mis ideas y mi aprendizaje.
                </h2>
                <p class="seccion-descripcion">
                    Lorem ipsum dolor sit amet, consectetur
                    adipiscing elit. Sed do eiusmod tempor
                    incididunt ut labore et dolore magna aliqua.
                    Este espacio está pensado para que presentes
                    quién eres, qué te inspira y qué esperas
                    aprender durante el curso.
                </p>
                <p class="seccion-descripcion">
                    Puedes cambiar este texto cuando tengas
                    lista tu presentación personal. La fotografía
                    también es un espacio reservado: agrega tu
                    archivo Blanco.jpg a la carpeta de perfil.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="seccion-kicker">Una colección en construcción</div>
        <h2 class="seccion-titulo">Pequeñas piezas de mi proceso</h2>
        <p class="seccion-descripcion">
            Explora algunas tarjetas de ejemplo. Cada una tiene
            su propia imagen, descripción y enlace.
        </p>
        """,
        unsafe_allow_html=True,
    )

    tarjetas_html = "".join(
        crear_tarjeta(actividad, i)
        for i, actividad in enumerate(actividades[:3], start=1)
    )

    st.markdown(
        f'<div class="grid-tarjetas">{tarjetas_html}</div>',
        unsafe_allow_html=True,
    )

    if st.button("Explorar todas las actividades →", type="primary"):
        st.session_state["ir_a_actividades"] = True
        st.rerun()


# =========================================================
# GALERÍA DE ACTIVIDADES
# =========================================================

elif seccion == "Mis actividades" or st.session_state.get(
    "ir_a_actividades", False
):
    st.session_state["ir_a_actividades"] = False

    st.markdown(
        """
        <div class="seccion-kicker">Archivo de proyectos</div>
        <h1 class="seccion-titulo">Mis actividades</h1>
        <p class="seccion-descripcion">
            Cada tarjeta contiene una fotografía, el título
            de la actividad y dos botones. Pulsa «Leer más»
            para desplegar la descripción o «Enlace» para
            abrir la dirección correspondiente.
        </p>
        """,
        unsafe_allow_html=True,
    )

    tarjetas_html = "".join(
        crear_tarjeta(actividad, i)
        for i, actividad in enumerate(actividades, start=1)
    )

    st.markdown(
        f"""
        <div class="grid-tarjetas">
            {tarjetas_html}
        </div>
        <div class="pie">
            HECHO CON CURIOSIDAD · DISEÑADO CON INTENCIÓN
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# SOBRE MÍ
# =========================================================

elif seccion == "Sobre mí":
    st.markdown(
        """
        <div class="seccion-kicker">Detrás del portafolio</div>
        <h1 class="seccion-titulo">Sobre mí</h1>
        <p class="seccion-descripcion">
            Un espacio para contar tu historia.
        </p>
        """,
        unsafe_allow_html=True,
    )

    col_foto, col_texto = st.columns([1, 2], gap="large")

    with col_foto:
        foto_sobre_mi = cargar_foto(
            "imagenes/perfil/Blanco.jpeg",
            "Fotografía personal",
        )

        st.markdown(
            f'<div class="presentacion">{foto_sobre_mi}'
            f'<div class="presentacion-pie">'
            f'{html.escape(nombre)}</div></div>',
            unsafe_allow_html=True,
        )

    with col_texto:
        st.markdown(
            """
            <h2 class="seccion-titulo">Mi historia creativa</h2>
            <p class="seccion-descripcion">
                Lorem ipsum dolor sit amet, consectetur adipiscing
                elit. Aquí puedes escribir una breve biografía,
                hablar de tus intereses y explicar qué significa
                para ti el diseño de interfaces multimodales.
            </p>
            <p class="seccion-descripcion">
                Este texto es provisional. Puedes reemplazarlo
                por tu historia, tus objetivos y tus reflexiones
                personales.
            </p>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="pie">MI PORTAFOLIO CREATIVO · 2026</div>',
        unsafe_allow_html=True,
    )
