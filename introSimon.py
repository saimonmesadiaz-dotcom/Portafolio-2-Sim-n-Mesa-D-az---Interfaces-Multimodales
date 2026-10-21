
import base64
import html
from pathlib import Path
from urllib.parse import urlparse

import streamlit as st

# ==================================================
# PORTAFOLIO II - PLANTILLA VINTAGE
# ==================================================

st.set_page_config(
    page_title="Portafolio II | Interfaces Multimodales",
    page_icon="☕",
    layout="wide",
)

CARPETA = Path(__file__).resolve().parent
FOTO = "blanco negro.jpg"


# ---------------- FUNCIONES ----------------

def esc(texto):
    return html.escape(str(texto), quote=True)


def cargar_foto(nombre, clase):
    ruta = CARPETA / nombre

    if ruta.is_file():
        import mimetypes
        mime = mimetypes.guess_type(ruta.name)[0] or "image/jpeg"
        datos = base64.b64encode(ruta.read_bytes()).decode("utf-8")
        return (
            f'<img class="{clase}" '
            f'src="data:{mime};base64,{datos}" '
            f'alt="Fotografía de prueba en blanco y negro">'
        )

    return """
    <div class="placeholder">
        <span>✦</span>
        <strong>Fotografía de prueba</strong>
        <small>Sube blanco negro.jpg</small>
    </div>
    """


def crear_enlace(url, texto):
    url = str(url).strip()
    partes = urlparse(url)

    if partes.scheme in ("https", "http") and partes.netloc:
        return (
            f'<a class="link-button" href="{esc(url)}" '
            f'target="_blank" rel="noopener noreferrer">'
            f'↗ {esc(texto)}</a>'
        )

    return '<span class="pending">↗ Enlace pendiente</span>'


# ---------------- DISEÑO CSS ----------------

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

[data-testid="stHeader"] { background: transparent; }
.block-container { max-width: 1450px; padding-top: 2rem; }
#MainMenu, footer { visibility: hidden; }

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: var(--dark) !important;
}

p { line-height: 1.8; color: #79634f; }

section[data-testid="stSidebar"] {
    background: linear-gradient(170deg, #493025, #302019);
}

section[data-testid="stSidebar"] * { color: #f8e9d2 !important; }

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    font-family: 'Playfair Display', serif !important;
}

hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #98704e, #e0c49e, #98704e, transparent);
    margin: 2rem 0;
}

/* PORTADA */

.hero {
    padding: clamp(1.5rem, 4vw, 3.5rem);
    border: 1px solid #d2b99a;
    border-radius: 26px;
    background: linear-gradient(125deg, #fff9ed, #ead6b8);
    box-shadow: 0 18px 42px #573a261f;
    overflow: hidden;
    position: relative;
}

.hero-grid {
    display: grid;
    grid-template-columns: 1.6fr .7fr;
    gap: 2rem;
    align-items: center;
}

.eyebrow {
    font: .72rem 'DM Mono', monospace;
    letter-spacing: .17em;
    text-transform: uppercase;
    color: #946d4b;
}

.hero h1 {
    font-size: clamp(2.7rem, 5.5vw, 5rem);
    line-height: 1;
    margin: 1rem 0;
}

.hero h1 em { color: #9a714d; }

.hero-copy {
    line-height: 1.9;
    color: #725942;
}

.tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 20px; }

.tag {
    padding: 7px 11px;
    border: 1px solid #cdb393;
    border-radius: 30px;
    background: #fff9ef;
    color: #694a32;
    font: .7rem 'DM Mono', monospace;
}

.portrait-frame {
    padding: 10px 10px 28px;
    background: #fffaf0;
    box-shadow: 8px 12px 0 #69482b20, 0 15px 30px #40291924;
    transform: rotate(3deg);
    animation: float 5s ease-in-out infinite;
    max-width: 270px;
    margin: auto;
}

.portrait {
    display: block;
    width: 100%;
    height: 260px;
    object-fit: cover;
    filter: grayscale(1) contrast(.95);
    background: #e2d1b8;
}

.caption {
    text-align: center;
    margin-top: 12px;
    font: .68rem 'DM Mono', monospace;
    color: #79583e;
}

@keyframes float {
    0%, 100% { transform: translateY(0) rotate(3deg); }
    50% { transform: translateY(-7px) rotate(1deg); }
}

/* GALERÍA */

.section-title { margin: 3rem 0 1rem; }
.section-title h2 { font-size: clamp(2rem, 4vw, 3.1rem); margin: .5rem 0; }

.gallery {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 24px;
    padding: 12px 4px 30px;
    align-items: start;
}

.card {
    --tilt: 0deg;
    position: relative;
    isolation: isolate;
    min-width: 0;
    padding: 12px 12px 18px;
    border: 1px solid #d5bea0;
    border-radius: 15px;
    background: linear-gradient(145deg, #fffaf0, #f0dfc7);
    box-shadow: 0 10px 22px #432d1f20;
    transform: rotate(var(--tilt));
    transition: transform .35s ease, box-shadow .35s ease,
                filter .35s ease, background .35s ease;
    animation: appear .65s both;
}

.card:nth-child(3n+1) { --tilt: -.6deg; }
.card:nth-child(3n+2) { --tilt: .5deg; }
.card:nth-child(3n) { --tilt: -.25deg; }

.card::before {
    content: "";
    position: absolute;
    z-index: -1;
    inset: -5px;
    border-radius: 19px;
    background: conic-gradient(
        transparent, #d4a56f, transparent 25%,
        #b68a5f, transparent 60%, #edcb91, transparent
    );
    opacity: 0;
    filter: blur(8px);
    transition: opacity .3s;
}

.card::after {
    content: "✦  ✧  ✦";
    position: absolute;
    right: 12px;
    top: -17px;
    color: #a87543;
    letter-spacing: 5px;
    opacity: 0;
    transform: translateY(5px);
    transition: all .3s;
    pointer-events: none;
}

.card:hover, .card:focus-within {
    z-index: 5;
    transform: translateY(-8px) scale(1.035) rotate(0);
    background: #fffdf7;
    box-shadow: 0 24px 40px #39251d40, 0 0 0 2px #9b6f4830;
}

.card:hover::before, .card:focus-within::before {
    opacity: .8;
    animation: spin 6s linear infinite;
}

.card:hover::after, .card:focus-within::after {
    opacity: 1;
    transform: translateY(0);
}

.gallery:has(.card:hover) .card:not(:hover) {
    filter: brightness(.88) saturate(.8);
    transform: scale(.985) rotate(var(--tilt));
}

@keyframes spin { to { transform: rotate(360deg); } }
@keyframes appear {
    from { opacity: 0; translate: 0 15px; }
    to { opacity: 1; translate: 0 0; }
}

.polaroid, .placeholder {
    display: block;
    box-sizing: border-box;
    width: 100%;
    height: 205px;
    object-fit: cover;
    border-radius: 7px;
    border: 1px solid #6c4a301c;
    background: #e6d3b6;
}

.polaroid {
    filter: grayscale(1) contrast(.95);
    transition: filter .3s, transform .3s;
}

.card:hover .polaroid {
    filter: grayscale(.3);
    transform: scale(.99);
}

.placeholder {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
    border: 1px dashed #b89a78;
    color: #805d45;
    text-align: center;
    padding: 10px;
    background: repeating-linear-gradient(45deg, #f2e2cb, #f2e2cb 10px, #ead7bb 10px, #ead7bb 11px);
}

.placeholder span { font-size: 2.5rem; }
.placeholder strong { font-size: .8rem; }
.placeholder small { font: .62rem 'DM Mono', monospace; }

.meta {
    display: flex;
    justify-content: space-between;
    gap: 8px;
    align-items: center;
    margin: 15px 2px 9px;
    font: .64rem 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: .06em;
    color: #987554;
}

.number {
    border: 1px solid #d5b995;
    background: #f6e7d1;
    border-radius: 50%;
    padding: 7px;
    min-width: 15px;
    text-align: center;
}

.card h3 {
    font: 600 1.3rem/1.25 'Playfair Display', serif !important;
    text-align: left !important;
    min-height: 3rem;
    margin: 0 2px .6rem !important;
}

.summary {
    min-height: 4.2rem;
    font-size: .85rem;
    line-height: 1.7;
    color: #796451;
    margin-bottom: 1rem;
}

.card details {
    border-top: 1px solid #e0ccb0;
    padding-top: .8rem;
    margin-top: .5rem;
}

.card summary {
    display: inline-block;
    list-style: none;
    cursor: pointer;
    padding: 9px 13px;
    border: 1px solid #c8a985;
    border-radius: 30px;
    background: #f5e5cf;
    color: #70472e;
    font-size: .8rem;
    font-weight: 600;
    transition: background .2s;
}

.card summary::-webkit-details-marker { display: none; }
.card summary::after { content: "  ＋"; }
.card details[open] summary::after { content: "  −"; }
.card summary:hover { background: #e7d0b1; }

.details-text {
    color: #6f5845;
    font-size: .85rem;
    line-height: 1.75;
    padding-top: .7rem;
}

.details-text strong { color: #4a3021; }

.link-button, .pending {
    display: inline-block;
    margin-top: 8px;
    padding: 10px 13px;
    border-radius: 30px;
    font-size: .76rem;
    font-weight: 600;
    text-decoration: none !important;
}

.link-button {
    color: #fff6e9 !important;
    background: #65442f;
}

.link-button:hover { background: #3f2a1e; }

.pending {
    border: 1px dashed #b89570;
    color: #84664a;
    background: #f2e3ce;
}

.notice {
    padding: 16px;
    border: 1px solid #d2b895;
    border-radius: 14px;
    background: #fff9eea8;
    color: #765a43;
}

.footer {
    text-align: center;
    padding: 30px 0 10px;
    color: #80654d;
    font: .68rem 'DM Mono', monospace;
    letter-spacing: .1em;
}

@media (max-width: 950px) {
    .gallery { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .hero-grid { grid-template-columns: 1fr 210px; }
}

@media (max-width: 620px) {
    .gallery, .hero-grid { grid-template-columns: 1fr; }
    .portrait-frame { max-width: 220px; }
    .portrait { height: 220px; }
    .card:hover { transform: translateY(-4px) scale(1.01); }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        transition-duration: .01ms !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------------- PORTADA ----------------

foto_portada = cargar_foto(FOTO, "portrait")

st.markdown(f"""
<section class="hero">
    <div class="hero-grid">
        <div>
            <div class="eyebrow">Cuaderno digital · Semestre II · Edición 02</div>
            <h1>Interfaces<br><em>multimodales.</em></h1>

            <div class="hero-copy">
                Hola, soy <strong>Tu nombre aquí</strong>. Este espacio reúne
                mis experiencias, experimentos y aprendizajes de la segunda
                parte del semestre.
                <br><br>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Aprender haciendo, experimentar sin miedo y transformar ideas
                en experiencias interactivas.
            </div>

            <div class="tags">
                <span class="tag">✳ Diseño interactivo</span>
                <span class="tag">⌘ Experimentación</span>
                <span class="tag">↗ Aprender haciendo</span>
                <span class="tag">☕ Edición vintage</span>
            </div>
        </div>

        <div class="portrait-frame">
            {foto_portada}
            <div class="caption">TU NOMBRE · PORTAFOLIO II</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# ---------------- BARRA LATERAL ----------------

with st.sidebar:
    st.markdown("# ✦ Archivo creativo")
    st.markdown("**PORTAFOLIO · SEGUNDA ETAPA**")
    st.write(
        "Una colección de actividades, recursos y pruebas de clase. "
        "Esta versión usa contenido provisional para probar el diseño."
    )
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
    st.caption("Plantilla de prueba · Hecha con curiosidad y café. ☕")


# ---------------- DATOS DE PRUEBA ----------------

texto_lorem = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Integer vitae sem sed justo malesuada finibus. Este texto es "
    "provisional y luego podrás sustituirlo por la descripción real "
    "de la actividad desarrollada en clase."
)

aprendizaje_lorem = (
    "Lorem ipsum dolor sit amet. Escribe aquí el concepto, la habilidad "
    "o la reflexión que te dejó esta actividad."
)

actividades = [
    {
        "titulo": "Actividad de ejemplo uno",
        "categoria": "Práctica · 01",
        "resumen": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "descripcion": texto_lorem,
        "aprendizaje": aprendizaje_lorem,
        "url": "",
        "boton": "Ir a la actividad",
    },
    {
        "titulo": "Actividad de ejemplo dos",
        "categoria": "Experimentación · 02",
        "resumen": "Sed do eiusmod tempor incididunt ut labore et dolore.",
        "descripcion": texto_lorem,
        "aprendizaje": aprendizaje_lorem,
        "url": "",
        "boton": "Abrir recurso",
    },
    {
        "titulo": "Actividad de ejemplo tres",
        "categoria": "Interfaz · 03",
        "resumen": "Ut enim ad minim veniam, quis nostrud exercitation.",
        "descripcion": texto_lorem,
        "aprendizaje": aprendizaje_lorem,
        "url": "",
        "boton": "Ver proyecto",
    },
    {
        "titulo": "Actividad de ejemplo cuatro",
        "categoria": "Simulación · 04",
        "resumen": "Duis aute irure dolor in reprehenderit in voluptate.",
        "descripcion": texto_lorem,
        "aprendizaje": aprendizaje_lorem,
        "url": "",
        "boton": "Explorar",
    },
    {
        "titulo": "Actividad de ejemplo cinco",
        "categoria": "Tecnología · 05",
        "resumen": "Excepteur sint occaecat cupidatat non proident.",
        "descripcion": texto_lorem,
        "aprendizaje": aprendizaje_lorem,
        "url": "",
        "boton": "Ir al recurso",
    },
    {
        "titulo": "Actividad de ejemplo seis",
        "categoria": "Aprendizaje · 06",
        "resumen": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "descripcion": texto_lorem,
        "aprendizaje": aprendizaje_lorem,
        "url": "",
        "boton": "Conocer más",
    },
]


# ---------------- GALERÍA ----------------

st.markdown("""
<div class="section-title">
    <div class="eyebrow">Galería de procesos · 01—∞</div>
    <h2>Mis actividades prácticas</h2>
    <p>
        Pasa el cursor sobre las Polaroids para descubrir sus efectos.
        Pulsa «Leer más información» para abrir los detalles.
    </p>
</div>
""", unsafe_allow_html=True)


def tarjeta(actividad, numero):
    foto = cargar_foto(FOTO, "polaroid")
    boton = crear_enlace(actividad["url"], actividad["boton"])

    titulo = esc(actividad["titulo"])
    categoria = esc(actividad["categoria"])
    resumen = esc(actividad["resumen"])
    descripcion = esc(actividad["descripcion"])
    aprendizaje = esc(actividad["aprendizaje"])

    return f"""
    <article class="card">
        {foto}
        <div class="meta">
            <span>{categoria}</span>
            <span class="number">{numero:02d}</span>
        </div>

        <h3>{titulo}</h3>
        <div class="summary">{resumen}</div>

        <details>
            <summary>Leer más información</summary>
            <div class="details-text">
                <p>{descripcion}</p>
                <p><strong>Lo que me llevo:</strong> {aprendizaje}</p>
                {boton}
            </div>
        </details>
    </article>
    """


galeria = "".join(
    tarjeta(actividad, numero)
    for numero, actividad in enumerate(actividades, start=1)
)

st.markdown(
    f'<div class="gallery">{galeria}</div>',
    unsafe_allow_html=True,
)

st.markdown("""
<div class="notice">
    ✦ <strong>Modo demostración:</strong>
    los textos son provisionales. Todas las tarjetas y la portada usan
    el mismo archivo de imagen. Los enlaces se pueden completar después.
</div>

<div class="footer">
    FIN DE LA PÁGINA, NO DEL PROCESO · DISEÑADO CON CURIOSIDAD ☕
</div>
""", unsafe_allow_html=True)
</div>
""", unsafe_allow_html=True)
