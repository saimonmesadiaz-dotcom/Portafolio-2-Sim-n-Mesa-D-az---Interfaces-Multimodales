import base64
import html
import mimetypes
from pathlib import Path
from urllib.parse import urlparse

import streamlit as st

# ==========================================================
# PORTAFOLIO II — INTERFACES MULTIMODALES
# ==========================================================

st.set_page_config(
    page_title="Portafolio II | Interfaces Multimodales",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

CARPETA = Path(__file__).resolve().parent
FOTO = "Blanco.jpg"


# ==========================================================
# FUNCIONES AUXILIARES
# ==========================================================

def esc(texto):
    """Evita que los textos introducidos rompan el HTML."""
    return html.escape(str(texto), quote=True)


def cargar_foto(nombre, clase):
    """
    Carga una imagen local y la convierte en una imagen integrada.
    Si no existe, muestra un espacio provisional.
    """
    ruta = CARPETA / nombre

    if ruta.is_file():
        mime = mimetypes.guess_type(ruta.name)[0] or "image/jpeg"
        datos = base64.b64encode(ruta.read_bytes()).decode("utf-8")

        return (
            f'<img class="{clase}" '
            f'src="data:{mime};base64,{datos}" '
            f'alt="Fotografía de prueba">'
        )

    return """
    <div class="placeholder">
        <span>✦</span>
        <strong>Fotografía de prueba</strong>
        <small>Agrega el archivo Blanco.jpg</small>
    </div>
    """


def crear_enlace(url, texto):
    """Crea un enlace únicamente si se ha configurado una URL válida."""
    url = str(url).strip()
    partes = urlparse(url)

    if partes.scheme in ("https", "http") and partes.netloc:
        return (
            f'<a class="link-button" href="{esc(url)}" '
            f'target="_blank" rel="noopener noreferrer">'
            f'↗ {esc(texto)}</a>'
        )

    return '<span class="pending">↗ Enlace pendiente</span>'


# ==========================================================
# ESTILOS CSS — ESTÉTICA VINTAGE CREMA Y CAFÉ
# ==========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono&family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap');

:root {
    --dark: #38251d;
    --coffee: #65442f;
    --brown: #916a49;
    --beige: #ead7bb;
    --cream: #fff8ec;
    --ink: #402d21;
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 10%, #fff8e9, transparent 38%),
        linear-gradient(135deg, #e4ceb0, #f6ead7 50%, #dfc4a0);
    font-family: 'DM Sans', sans-serif;
    color: var(--ink);
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

#MainMenu, footer {
    visibility: hidden;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: var(--dark) !important;
}

p {
    line-height: 1.8;
    color: #79634f;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(170deg, #493025, #302019);
}

section[data-testid="stSidebar"] * {
    color: #f8e9d2 !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    font-family: 'Playfair Display', serif !important;
}

hr {
    border: none;
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        #98704e,
        #e0c49e,
        #98704e,
        transparent
    );
    margin: 2.5rem 0;
}

/* ==================================================
   PORTADA (POLAROID IZQUIERDA / TEXTO DERECHA)
================================================== */

.hero {
    padding: clamp(2rem, 4vw, 3.5rem);
    border: 1px solid #d2b99a;
    border-radius: 26px;
    background: linear-gradient(125deg, #fff9ed, #ead6b8);
    box-shadow: 0 18px 42px #573a261f;
    margin-bottom: 2rem;
}

.hero-grid {
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 3rem;
    align-items: center;
}

.eyebrow {
    font: .72rem 'DM Mono', monospace;
    letter-spacing: .17em;
    text-transform: uppercase;
    color: #946d4b;
    margin-bottom: 0.5rem;
}

.hero h1 {
    font-size: clamp(2.5rem, 4.5vw, 4.2rem);
    line-height: 1.1;
    margin: 0.5rem 0 1rem 0;
}

.hero h1 em {
    color: #9a714d;
}

.hero-copy {
    line-height: 1.8;
    color: #725942;
    margin-bottom: 1.5rem;
}

.tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.tag {
    padding: 6px 12px;
    border: 1px solid #cdb393;
    border-radius: 30px;
    background: #fff9ef;
    color: #694a32;
    font: .7rem 'DM Mono', monospace;
}

.portrait-frame {
    padding: 12px 12px 28px;
    background: #fffaf0;
    box-shadow: 8px 12px 0 #69482b20, 0 15px 30px #40291924;
    transform: rotate(-2deg);
    width: 100%;
}

.portrait {
    display: block;
    width: 100%;
    height: 240px;
    object-fit: cover;
    filter: grayscale(1) contrast(.95);
    background: #e2d1b8;
    border-radius: 4px;
}

.caption {
    text-align: center;
    margin-top: 12px;
    font: .68rem 'DM Mono', monospace;
    color: #79583e;
}

/* ==================================================
   GALERÍA DE 2 COLUMNAS
================================================== */

.section-title {
    margin: 3rem 0 1.5rem;
}

.section-title h2 {
    font-size: clamp(2rem, 3.5vw, 2.8rem);
    margin: .3rem 0;
}

.gallery {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 28px;
    padding: 10px 0 30px;
    align-items: start;
}

/* TARJETAS POLAROID */

.card {
    position: relative;
    isolation: isolate;
    padding: 16px;
    border: 1px solid #d5bea0;
    border-radius: 18px;
    background: linear-gradient(145deg, #fffaf0, #f0dfc7);
    box-shadow: 0 10px 22px #432d1f20;
    transition: transform .3s ease, box-shadow .3s ease, border-color .3s ease;
}

/* EFECTO HOVER: SE AGRANDA Y BORDE CAFÉ */

.card:hover {
    transform: translateY(-6px) scale(1.02);
    border-color: #65442f;
    box-shadow: 0 20px 35px #39251d35, 0 0 0 2px #65442f40;
    background: #fffdf7;
    z-index: 5;
}

.polaroid {
    display: block;
    width: 100%;
    height: 210px;
    object-fit: cover;
    border-radius: 6px;
    border: 1px solid #6c4a301c;
    filter: grayscale(1) contrast(.95);
    background: #e6d3b6;
    transition: filter .3s;
}

.card:hover .polaroid {
    filter: grayscale(.2);
}

.meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 14px 2px 8px;
    font: .65rem 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: .06em;
    color: #987554;
}

.number {
    border: 1px solid #d5b995;
    background: #f6e7d1;
    border-radius: 50%;
    padding: 4px 8px;
    text-align: center;
}

.card h3 {
    font: 600 1.25rem/1.2 'Playfair Display', serif !important;
    margin: 0 2px .5rem !important;
    color: var(--dark) !important;
}

.summary {
    font-size: .88rem;
    line-height: 1.6;
    color: #796451;
    margin-bottom: 1rem;
    min-height: 2.8rem;
}

/* DESPLEGABLE LEER MÁS */

.card details {
    border-top: 1px solid #e0ccb0;
    padding-top: .8rem;
    margin-top: .8rem;
}

.card summary {
    display: inline-block;
    list-style: none;
    cursor: pointer;
    padding: 8px 14px;
    border: 1px solid #c8a985;
    border-radius: 30px;
    background: #f5e5cf;
    color: #70472e;
    font-size: .78rem;
    font-weight: 600;
    transition: background .2s;
}

.card summary::-webkit-details-marker {
    display: none;
}

.card summary::after {
    content: " ＋";
}

.card details[open] summary::after {
    content: " −";
}

.card summary:hover {
    background: #e7d0b1;
}

.details-text {
    color: #6f5845;
    font-size: .85rem;
    line-height: 1.7;
    padding-top: .8rem;
}

.details-text strong {
    color: #4a3021;
}

/* BOTONES DE ENLACE */

.link-button, .pending {
    display: inline-block;
    margin-top: 10px;
    padding: 8px 14px;
    border-radius: 30px;
    font-size: .76rem;
    font-weight: 600;
    text-decoration: none !important;
}

.link-button {
    color: #fff6e9 !important;
    background: #65442f;
}

.link-button:hover {
    background: #3f2a1e;
}

.pending {
    border: 1px dashed #b89570;
    color: #84664a;
    background: #f2e3ce;
}

/* RESPONSIVO */

@media (max-width: 900px) {
    .hero-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
    .portrait-frame {
        max-width: 260px;
        margin: 0 auto;
    }
    .gallery {
        grid-template-columns: 1fr;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================================
# PORTADA PRINCIPAL (FOTO IZQUIERDA / TEXTO DERECHA)
# ==========================================================

foto_portada = cargar_foto(FOTO, "portrait")

st.markdown(f"""
<section class="hero">
    <div class="hero-grid">
        <div class="portrait-frame">
            {foto_portada}
            <div class="caption">TU NOMBRE · PORTAFOLIO II</div>
        </div>
        <div>
            <div class="eyebrow">Cuaderno digital · Semestre II · Edición 02</div>
            <h1>Interfaces<br><em>multimodales.</em></h1>
            <div class="hero-copy">
                Hola, soy <strong>Tu nombre aquí</strong>. Este espacio reúne mis experiencias, 
                experimentos y aprendizajes de la segunda parte del semestre. Aprender haciendo, 
                experimentar sin miedo y transformar ideas en experiencias interactivas.
            </div>
            <div class="tags">
                <span class="tag">✳ Diseño interactivo</span>
                <span class="tag">⌘ Experimentación</span>
                <span class="tag">↗ Aprender haciendo</span>
                <span class="tag">☕ Edición vintage</span>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# ==========================================================
# BARRA LATERAL
# ==========================================================

with st.sidebar:
    st.markdown("# Archivo creativo")
    st.markdown("**PORTAFOLIO · SEGUNDA ETAPA**")
    st.write("Una colección de actividades, recursos y pruebas de clase.")
    st.markdown("---")
    st.markdown("### Dentro del cuaderno")
    st.markdown("""
    - ✎ Dibujo y reconocimiento
    - ◉ Sensores y simulación
    - ⌘ Herramientas tecnológicas
    - ↗ Repositorios y proyectos
    - ✧ Reflexiones
    """)
    st.markdown("---")
    st.caption("Plantilla para GitHub · Hecha con café y código.")


# ==========================================================
# LÍNEA DIVISORIA ESTÉTICA
# ==========================================================

st.markdown("<hr>", unsafe_allow_html=True)


# ==========================================================
# TÍTULO DE LA GALERÍA
# ==========================================================

st.markdown("""
<div class="section-title">
    <div class="eyebrow">Galería de procesos · 01—08</div>
    <h2>Actividades prácticas realizadas</h2>
    <p>Pasa el cursor sobre las Polaroids para ver el efecto y despliega los detalles de cada práctica.</p>
</div>
""", unsafe_allow_html=True)


# ==========================================================
# DATOS DE LAS 8 ACTIVIDADES
# ==========================================================

texto_lorem = "Descripción detallada provisional de la actividad práctica desarrollada en clase."
aprendizaje_lorem = "Concepto clave, habilidad o reflexión obtenida en este ejercicio."

actividades = [
    {"titulo": "Actividad práctica uno", "categoria": "Práctica · 01", "resumen": "Primer acercamiento a interfaces y prototipado multimodal.", "descripcion": texto_lorem, "aprendizaje": aprendizaje_lorem, "url": "", "boton": "Abrir recurso"},
    {"titulo": "Actividad práctica dos", "categoria": "Experimentación · 02", "resumen": "Pruebas de interacción con sensores y estímulos visuales.", "descripcion": texto_lorem, "aprendizaje": aprendizaje_lorem, "url": "", "boton": "Abrir recurso"},
    {"titulo": "Actividad práctica tres", "categoria": "Interfaz · 03", "resumen": "Diseño de flujos de navegación orientados al usuario.", "descripcion": texto_lorem, "aprendizaje": aprendizaje_lorem, "url": "", "boton": "Abrir recurso"},
    {"titulo": "Actividad práctica cuatro", "categoria": "Simulación · 04", "resumen": "Simulación de escenarios interactivos en entornos virtuales.", "descripcion": texto_lorem, "aprendizaje": aprendizaje_lorem, "url": "", "boton": "Abrir recurso"},
    {"titulo": "Actividad práctica cinco", "categoria": "Tecnología · 05", "resumen": "Implementación de herramientas tecnológicas avanzadas.", "descripcion": texto_lorem, "aprendizaje": aprendizaje_lorem, "url": "", "boton": "Abrir recurso"},
    {"titulo": "Actividad práctica seis", "categoria": "Desarrollo · 06", "resumen": "Construcción de componentes dinámicos y adaptativos.", "descripcion": texto_lorem, "aprendizaje": aprendizaje_lorem, "url": "", "boton": "Abrir recurso"},
    {"titulo": "Actividad práctica siete", "categoria": "Evaluación · 07", "resumen": "Pruebas de usabilidad y análisis de retroalimentación.", "descripcion": texto_lorem, "aprendizaje": aprendizaje_lorem, "url": "", "boton": "Abrir recurso"},
    {"titulo": "Actividad práctica ocho", "categoria": "Proyecto Final · 08", "resumen": "Consolidación de aprendizajes del portafolio multimodal.", "descripcion": texto_lorem, "aprendizaje": aprendizaje_lorem, "url": "", "boton": "Abrir recurso"},
]


# ==========================================================
# FUNCIÓN PARA CREAR CADA TARJETA
# ==========================================================

def tarjeta(actividad, numero):
    foto = cargar_foto(FOTO, "polaroid")
    boton = crear_enlace(actividad["url"], actividad["boton"])

    return f"""
    <article class="card">
        {foto}
        <div class="meta">
            <span>{esc(actividad["categoria"])}</span>
            <span class="number">{numero:02d}</span>
        </div>
        <h3>{esc(actividad["titulo"])}</h3>
        <div class="summary">
            {esc(actividad["resumen"])}
        </div>
        <details>
            <summary>Leer más información</summary>
            <div class="details-text">
                <p>{esc(actividad["descripcion"])}</p>
                <p>
                    <strong>Lo que me llevo:</strong>
                    {esc(actividad["aprendizaje"])}
                </p>
                {boton}
            </div>
        </details>
    </article>
    """


# ==========================================================
# CONSTRUIR Y MOSTRAR LA GALERÍA (2 COLUMNAS)
# ==========================================================

galeria = "".join(
    tarjeta(actividad, numero)
    for numero, actividad in enumerate(actividades, start=1)
)

st.markdown(f'<div class="gallery">{galeria}</div>', unsafe_allow_html=True)


# ==========================================================
# PIE DE PÁGINA
# ==========================================================

st.markdown("""
<hr>
<div style="padding: 16px; border: 1px solid #d2b895; border-radius: 14px; background: #fff9eea8; color: #765a43; text-align: center; font-size: 0.9rem;">
    ✦ <strong>Modo demostración:</strong> Sube tu imagen como <code>Blanco.jpg</code> en el repositorio de GitHub junto a este archivo <code>app.py</code>.
</div>
""", unsafe_allow_html=True)
