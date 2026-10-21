
import base64
import html
import mimetypes
from pathlib import Path
from urllib.parse import urlparse

import streamlit as st

# ======================================================
# PORTAFOLIO II — CUADERNO DE EXPERIMENTOS
# SIMÓN MESA DÍAZ | INTERFACES MULTIMODALES
# ======================================================

st.set_page_config(
    page_title="Cuaderno de Experimentos | Portafolio II",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).parent


# ======================================================
# FUNCIONES AUXILIARES
# ======================================================

def imagen_uri(nombre):
    """Lee una imagen local y la convierte en una URL incrustada."""
    ruta = BASE_DIR / nombre

    if not ruta.is_file():
        return ""

    mime = mimetypes.guess_type(ruta.name)[0] or "image/png"
    contenido = base64.b64encode(ruta.read_bytes()).decode("utf-8")

    return f"data:{mime};base64,{contenido}"


def escapar(texto):
    return html.escape(str(texto), quote=True)


def imagen_html(nombre, alt, clase="polaroid-photo"):
    uri = imagen_uri(nombre)

    if uri:
        return (
            f'<img class="{clase}" src="{uri}" '
            f'alt="{escapar(alt)}" loading="lazy">'
        )

    return f"""
    <div class="photo-placeholder">
        <span>✦</span>
        <strong>{escapar(alt)}</strong>
        <small>Agrega: {escapar(nombre)}</small>
    </div>
    """


def enlace_html(url, etiqueta):
    """Solo habilita enlaces web HTTP o HTTPS."""
    url = str(url).strip()

    if urlparse(url).scheme in ("https", "http") and urlparse(url).netloc:
        return (
            f'<a class="action-link primary" href="{escapar(url)}" '
            'target="_blank" rel="noopener noreferrer">'
            f'↗ {escapar(etiqueta)}</a>'
        )

    return (
        '<span class="action-link unavailable">'
        '↗ Enlace pendiente</span>'
    )


# ======================================================
# ESTÉTICA VINTAGE — CSS
# ======================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700;800&display=swap');

:root {
    --espresso: #38251d;
    --coffee: #5c3d2e;
    --cocoa: #805b40;
    --caramel: #b58b63;
    --paper: #f0e1ca;
    --cream: #fff8ec;
    --ink: #3d2b21;
    --muted: #806b58;
    --border: #d2b99a;
}

.stApp {
    background:
        radial-gradient(ellipse at 12% 10%,
            rgba(255,250,235,.95), transparent 34%),
        radial-gradient(ellipse at 88% 34%,
            rgba(177,130,85,.20), transparent 35%),
        linear-gradient(135deg, #e8d6bb, #f4e9d6 48%, #dfc5a3);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

#MainMenu, footer {
    visibility: hidden;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: var(--espresso) !important;
}

p {
    color: var(--muted);
    line-height: 1.8;
}

hr {
    border: none;
    height: 1px;
    background: linear-gradient(
        90deg, transparent, #9c7755, #d9bd96, #9c7755, transparent
    );
    margin: 2rem 0;
}

/* BARRA LATERAL */

section[data-testid="stSidebar"] {
    background: linear-gradient(165deg, #493025, #35231b 80%);
    border-right: 1px solid rgba(255,244,223,.2);
}

section[data-testid="stSidebar"] * {
    color: #f7e8d2 !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    font-family: 'Playfair Display', serif !important;
}

section[data-testid="stSidebar"] p {
    font-size: .92rem;
}

/* PORTADA */

.hero {
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(95,65,43,.24);
    border-radius: 28px;
    padding: clamp(1.5rem, 4vw, 3.6rem);
    background: linear-gradient(
        125deg, rgba(255,249,237,.96), rgba(231,211,183,.91)
    );
    box-shadow: 0 18px 45px rgba(73,48,30,.13);
}

.hero-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.7fr) minmax(190px, .7fr);
    gap: 2.4rem;
    align-items: center;
}

.eyebrow {
    font: 500 .72rem 'DM Mono', monospace;
    letter-spacing: .2em;
    text-transform: uppercase;
    color: #916d4d;
    margin-bottom: .8rem;
}

.hero h1 {
    font-size: clamp(2.8rem, 5.7vw, 5.4rem);
    line-height: .98;
    letter-spacing: -.045em;
    margin: .2rem 0 1.3rem;
}

.hero h1 em {
    color: #986f4c;
    font-weight: 500;
}

.hero-copy {
    max-width: 760px;
    color: #715a46;
    font-size: 1rem;
    line-height: 1.9;
}

.hero-tags {
    display: flex;
    flex-wrap: wrap;
    gap: .55rem;
    margin-top: 1.4rem;
}

.hero-tag {
    padding: .45rem .75rem;
    border-radius: 999px;
    border: 1px solid #ceb494;
    background: rgba(255,250,240,.8);
    color: #694b36;
    font: .7rem 'DM Mono', monospace;
}

.portrait-frame {
    padding: 11px 11px 32px;
    background: #fffaf0;
    border: 1px solid #d6c2a5;
    box-shadow: 8px 12px 0 rgba(92,61,40,.12),
                0 14px 35px rgba(62,39,24,.16);
    transform: rotate(3deg);
    animation: floatPhoto 5s ease-in-out infinite;
    max-width: 280px;
    margin: auto;
}

.portrait-photo {
    display: block;
    width: 100%;
    height: 280px;
    object-fit: cover;
    background: #e6d2b5;
    filter: sepia(.15) saturate(.85);
}

.portrait-caption {
    margin-top: 12px;
    text-align: center;
    color: #79583e;
    font: .68rem 'DM Mono', monospace;
    letter-spacing: .1em;
}

@keyframes floatPhoto {
    0%, 100% { transform: translateY(0) rotate(3deg); }
    50% { transform: translateY(-7px) rotate(1deg); }
}

.hero-sparkles {
    position: absolute;
    right: 4%;
    top: 6%;
    color: rgba(128,93,69,.28);
    font-size: 3rem;
    letter-spacing: .3em;
    pointer-events: none;
}

/* ENCABEZADO DE GALERÍA */

.section-heading {
    margin: 3rem 0 1.2rem;
}

.section-heading h2 {
    font-size: clamp(2.1rem, 4vw, 3.3rem);
    margin: .1rem 0 .5rem;
}

.section-heading p {
    max-width: 760px;
}

/* GALERÍA DE POLAROIDS */

.activity-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1.65rem;
    align-items: stretch;
    padding: 1rem .25rem 2rem;
}

.activity-card {
    --tilt: 0deg;
    position: relative;
    isolation: isolate;
    min-width: 0;
    padding: 13px 13px 18px;
    border: 1px solid #d4bea0;
    border-radius: 16px;
    background: linear-gradient(145deg, #fffaf0, #f3e5d0);
    box-shadow: 0 10px 22px rgba(65,43,27,.14),
                inset 0 1px 0 #fff;
    transform: rotate(var(--tilt));
    transition:
        transform .38s cubic-bezier(.2,.8,.2,1),
        box-shadow .38s ease,
        background .38s ease,
        border-color .38s ease,
        filter .38s ease;
    animation: cardEntrance .7s both;
}

.activity-card:nth-child(3n+1) { --tilt: -.55deg; }
.activity-card:nth-child(3n+2) { --tilt: .5deg; }
.activity-card:nth-child(3n) { --tilt: -.25deg; }

.activity-card::before {
    content: "";
    position: absolute;
    z-index: -1;
    inset: -5px;
    border-radius: 20px;
    background: conic-gradient(
        from 0deg,
        transparent 0 15%,
        #d5a46b 20%,
        transparent 27% 49%,
        #b58b63 54%,
        transparent 61% 78%,
        #e7c68d 84%,
        transparent 91%
    );
    opacity: 0;
    filter: blur(8px);
    transition: opacity .35s ease;
}

.activity-card::after {
    content: "✦  ·  ✧  ·  ✦";
    position: absolute;
    top: -15px;
    right: 12px;
    color: #a97542;
    font-size: 15px;
    letter-spacing: 7px;
    opacity: 0;
    transform: translateY(7px) scale(.7);
    transition: all .35s ease;
    pointer-events: none;
}

.activity-card:hover,
.activity-card:focus-within {
    z-index: 5;
    transform: translateY(-8px) scale(1.035) rotate(0deg);
    background: linear-gradient(145deg, #fffdf7, #f8ead5);
    border-color: #8d6444;
    box-shadow: 0 24px 42px rgba(54,34,21,.25),
                0 0 0 2px rgba(155,111,72,.18);
}

.activity-card:hover::before,
.activity-card:focus-within::before {
    opacity: .65;
    animation: sparkleSpin 5s linear infinite;
}

.activity-card:hover::after,
.activity-card:focus-within::after {
    opacity: 1;
    transform: translateY(0) scale(1);
}

.activity-grid:has(.activity-card:hover) .activity-card:not(:hover) {
    filter: brightness(.88) saturate(.82);
    transform: scale(.985) rotate(var(--tilt));
}

@keyframes sparkleSpin {
    to { transform: rotate(360deg); }
}

@keyframes cardEntrance {
    from { opacity: 0; translate: 0 15px; }
    to { opacity: 1; translate: 0 0; }
}

.polaroid-photo,
.photo-placeholder {
    display: block;
    width: 100%;
    height: 205px;
    object-fit: cover;
    border-radius: 8px;
    background: #e6d3b6;
    border: 1px solid rgba(79,52,34,.13);
    transition: filter .35s ease, transform .35s ease;
}

.polaroid-photo {
    filter: sepia(.14) saturate(.88);
}

.activity-card:hover .polaroid-photo {
    filter: sepia(0) saturate(1.05);
    transform: scale(.99);
}

.photo-placeholder {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: .5rem;
    border: 1px dashed #b89a78;
    color: #805d45;
    background: repeating-linear-gradient(
        45deg, #f2e2cb, #f2e2cb 10px, #ead7bb 10px, #ead7bb 11px
    );
    text-align: center;
    padding: 1rem;
}

.photo-placeholder span { font-size: 2.7rem; }
.photo-placeholder strong { font-size: .8rem; }
.photo-placeholder small { font: .63rem 'DM Mono', monospace; }

.card-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: .5rem;
    margin: 15px 2px 9px;
    font: .64rem 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: .08em;
    color: #967452;
}

.card-index {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 29px;
    height: 29px;
    border-radius: 50%;
    border: 1px solid #d5b995;
    color: #6e4a30;
    background: #f6e7d1;
    flex-shrink: 0;
}

.activity-card h3 {
    font: 600 1.28rem/1.25 'Playfair Display', serif !important;
    color: #402b20 !important;
    text-align: left !important;
    min-height: 3.15rem;
    margin: 0 2px .65rem !important;
}

.card-short {
    color: #796451;
    font-size: .85rem;
    line-height: 1.7;
    margin: 0 2px 1rem;
    min-height: 4.3rem;
}

/* DETALLES DESPLEGABLES */

.activity-card details {
    border-top: 1px solid #e0ccb0;
    margin-top: .7rem;
    padding-top: .8rem;
}

.activity-card summary {
    list-style: none;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    color: #70472e;
    font: 600 .8rem 'DM Sans', sans-serif;
    padding: .6rem .85rem;
    border: 1px solid #c8a985;
    border-radius: 999px;
    background: #f5e5cf;
    transition: all .2s ease;
}

.activity-card summary::-webkit-details-marker {
    display: none;
}

.activity-card summary::after {
    content: "＋";
    font-size: 1rem;
}

.activity-card details[open] summary::after {
    content: "−";
}

.activity-card summary:hover {
    background: #e7d0b1;
    transform: translateY(-1px);
}

.card-details {
    color: #6f5845;
    font-size: .85rem;
    line-height: 1.75;
    padding: .8rem .1rem .25rem;
}

.card-details p {
    color: #6f5845;
    font-size: .85rem;
}

.card-details strong {
    color: #4a3021;
}

.card-actions {
    display: flex;
    flex-wrap: wrap;
    gap: .55rem;
    margin-top: .85rem;
}

.action-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: .35rem;
    padding: .62rem .85rem;
    border-radius: 999px;
    text-decoration: none !important;
    font: 600 .76rem 'DM Sans', sans-serif;
}

.action-link.primary {
    color: #fff6e9 !important;
    background: #65442f;
    border: 1px solid #65442f;
    transition: transform .2s, background .2s;
}

.action-link.primary:hover {
    background: #3f2a1e;
    transform: translateY(-2px);
}

.action-link.unavailable {
    color: #84664a !important;
    background: #f2e3ce;
    border: 1px dashed #b89570;
    font-size: .73rem;
}

.note-bar {
    border: 1px solid #d2b895;
    border-radius: 16px;
    padding: 1rem 1.2rem;
    background: rgba(255,249,238,.65);
    color: #765a43;
    font-size: .84rem;
}

.note-bar strong { color: #4a3021; }

.footer-note {
    text-align: center;
    color: #80654d;
    padding: 2rem 0 .5rem;
    font: .68rem 'DM Mono', monospace;
    letter-spacing: .12em;
}

/* RESPONSIVE */

@media (max-width: 1000px) {
    .activity-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .hero-grid {
        grid-template-columns: minmax(0, 1fr) 220px;
    }
}

@media (max-width: 650px) {
    .activity-grid {
        grid-template-columns: 1fr;
    }

    .hero-grid {
        grid-template-columns: 1fr;
    }

    .portrait-frame { max-width: 220px; }
    .portrait-photo { height: 220px; }

    .activity-card:hover {
        transform: translateY(-4px) scale(1.01);
    }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        transition-duration: .01ms !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ======================================================
# PORTADA
# ======================================================

foto = imagen_html(
    "SimonImagen.png",
    "Retrato de Simón Mesa Díaz",
    "portrait-photo"
)

st.markdown(f"""
<section class="hero">
    <div class="hero-sparkles">✧ ✦ ✧</div>

    <div class="hero-grid">
        <div>
            <div class="eyebrow">
                Cuaderno digital · Semestre II · Edición 02
            </div>

            <h1>
                Interfaces<br>
                <em>multimodales.</em>
            </h1>

            <div class="hero-copy">
                Soy <strong>Simón Mesa Díaz</strong>, y este espacio
                reúne una nueva etapa de exploración, práctica y creatividad.
                Aquí conviven las actividades realizadas en clase, los recursos
                temáticos y los experimentos con dibujo, reconocimiento,
                sensores, simulación y herramientas digitales.

                Cada actividad es una pequeña evidencia de lo aprendido
                y de las ganas de seguir diseñando experiencias interactivas
                con intención, curiosidad y pasión.
            </div>

            <div class="hero-tags">
                <span class="hero-tag">✳ Diseño interactivo</span>
                <span class="hero-tag">⌘ Experimentación</span>
                <span class="hero-tag">↗ Aprender haciendo</span>
                <span class="hero-tag">☕ Edición vintage</span>
            </div>
        </div>

        <div class="portrait-frame">
            {foto}
            <div class="portrait-caption">
                SIMÓN MESA DÍAZ · PORTAFOLIO II
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# ======================================================
# BARRA LATERAL
# ======================================================

with st.sidebar:
    st.markdown("# ✦ Archivo creativo")
    st.markdown("**PORTAFOLIO · SEGUNDA ETAPA**")

    st.write(
        "Un recorrido por los aprendizajes, ejercicios y experimentos "
        "de Creación de Interfaces Multimodales."
    )

    st.markdown("---")
    st.markdown("### Dentro de este cuaderno")
    st.markdown("""
    - ✎ Dibujo y reconocimiento
    - ◉ Sensores y simulación
    - ⌘ Herramientas tecnológicas
    - ↗ Repositorios y proyectos
    - ✧ Reflexiones de aprendizaje
    """)

    st.markdown("---")
    st.markdown("### Mi filosofía")
    st.write(
        "Explorar, probar, equivocarse, aprender y volver a crear. "
        "Porque cada intento también hace parte del diseño."
    )

    st.markdown("---")
    st.caption("Hecho con curiosidad, café y ganas de crear. ☕")


# ======================================================
# TÍTULO DE LA GALERÍA
# ======================================================

st.markdown("""
<div class="section-heading">
    <div class="eyebrow">Galería de procesos · 01—∞</div>
    <h2>Mis actividades prácticas</h2>
    <p>
        Cada Polaroid guarda una experiencia. Explora las tarjetas,
        descubre lo aprendido y visita los recursos relacionados.
        Pasa el cursor sobre las fotografías para revelar sus destellos.
    </p>
</div>
""", unsafe_allow_html=True)


# ======================================================
# ACTIVIDADES
#
# Cambia las imágenes, descripciones y URL por las reales.
# Usa url="" si todavía no tienes el enlace.
# ======================================================

actividades = [
    {
        "titulo": "Tablero de dibujo y reconocimiento numérico",
        "imagen": "tablero_dibujo.png",
        "categoria": "Dibujo · Reconocimiento",
        "resumen": (
            "Una experiencia donde los trazos se convierten en información "
            "que una máquina puede interpretar."
        ),
        "descripcion": (
            "Se exploró el uso de un tablero de dibujo para representar "
            "caracteres numéricos y observar cómo una interfaz recibe "
            "trazos como entrada. La actividad relaciona la interacción "
            "directa del usuario con procesos de reconocimiento y clasificación."
        ),
        "aprendizaje": (
            "Comprender la relación entre entrada visual, representación "
            "de datos y reconocimiento automático."
        ),
        "url": "",
        "boton": "Ver actividad",
    },
    {
        "titulo": "Simuladores físicos y sensores",
        "imagen": "sensores.png",
        "categoria": "Simulación · Hardware",
        "resumen": (
            "Exploración de componentes y sensores para comprender cómo "
            "el entorno físico puede activar una interfaz."
        ),
        "descripcion": (
            "Se realizaron pruebas con simuladores de sistemas físicos "
            "y sensores para observar sus respuestas. La práctica permitió "
            "relacionar variables del entorno con comportamientos digitales "
            "y comprender la lógica de los sistemas interactivos."
        ),
        "aprendizaje": (
            "Reconocer el papel de los sensores, las señales de entrada "
            "y las respuestas de un sistema."
        ),
        "url": "",
        "boton": "Ver simulación",
    },
    {
        "titulo": "Exploración de herramientas Huawei",
        "imagen": "huawei.png",
        "categoria": "Tecnología · Recursos",
        "resumen": (
            "Acercamiento a herramientas y recursos tecnológicos para "
            "experimentar con nuevas posibilidades digitales."
        ),
        "descripcion": (
            "Se exploraron recursos tecnológicos y entornos de aprendizaje "
            "asociados con las herramientas utilizadas durante el curso. "
            "La actividad se enfocó en investigar sus posibilidades, "
            "comprender sus funciones y relacionarlas con los conceptos vistos."
        ),
        "aprendizaje": (
            "Investigar plataformas tecnológicas y reconocer sus aplicaciones "
            "en experiencias interactivas."
        ),
        "url": "",
        "boton": "Ir al recurso",
    },
    {
        "titulo": "Prácticas con Simbly",
        "imagen": "simbly.png",
        "categoria": "Práctica · Simulación",
        "resumen": (
            "Experimentación con recursos interactivos para llevar "
            "los conceptos de clase a pruebas concretas."
        ),
        "descripcion": (
            "Se utilizó el entorno de práctica para explorar configuraciones, "
            "observar resultados y ajustar los elementos de la actividad. "
            "El proceso permitió aprender mediante la experimentación "
            "y la comparación de diferentes respuestas."
        ),
        "aprendizaje": (
            "Aplicar conceptos vistos en clase y documentar los resultados "
            "de la experimentación."
        ),
        "url": "",
        "boton": "Abrir recurso",
    },
    {
        "titulo": "GitHub: repositorio y documentación",
        "imagen": "github.png",
        "categoria": "Código · Versionamiento",
        "resumen": (
            "Organización de archivos y proyectos para documentar "
            "el proceso y compartir los resultados."
        ),
        "descripcion": (
            "Se exploró GitHub como plataforma para crear repositorios, "
            "organizar archivos y presentar proyectos. Esta práctica permite "
            "comprender la importancia de documentar el trabajo y mantener "
            "un espacio donde se pueda consultar su evolución."
        ),
        "aprendizaje": (
            "Comprender la estructura de un repositorio, la documentación "
            "y los fundamentos del control de versiones."
        ),
        "url": "https://github.com/",
        "boton": "Ir a GitHub",
    },
    {
        "titulo": "Bitácora de aprendizajes",
        "imagen": "bitacora.png",
        "categoria": "Reflexión · Proceso",
        "resumen": (
            "Un registro de los ejercicios, los retos y los descubrimientos "
            "realizados durante esta etapa del semestre."
        ),
        "descripcion": (
            "Esta sección reúne reflexiones sobre las actividades "
            "desarrolladas y los recursos utilizados. La bitácora permite "
            "reconocer la evolución del proceso, identificar dificultades "
            "y conectar los ejercicios con los objetivos de la asignatura."
        ),
        "aprendizaje": (
            "Comunicar el proceso, evaluar los resultados y reconocer "
            "oportunidades de mejora."
        ),
        "url": "",
        "boton": "Ver bitácora",
    },
]


# ======================================================
# GENERADOR DE TARJETAS
# ======================================================

def crear_tarjeta(actividad, numero):
    foto_html = imagen_html(
        actividad["imagen"],
        actividad["titulo"]
    )

    titulo = escapar(actividad["titulo"])
    categoria = escapar(actividad["categoria"])
    resumen = escapar(actividad["resumen"])
    descripcion = escapar(actividad["descripcion"])
    aprendizaje = escapar(actividad["aprendizaje"])

    boton_html = enlace_html(
        actividad["url"],
        actividad["boton"]
    )

    return f"""
    <article class="activity-card">
        {foto_html}

        <div class="card-meta">
            <span>{categoria}</span>
            <span class="card-index">{numero:02d}</span>
        </div>

        <h3>{titulo}</h3>

        <div class="card-short">
            {resumen}
        </div>

        <details>
            <summary>Leer más información</summary>

            <div class="card-details">
                <p>{descripcion}</p>

                <p>
                    <strong>Lo que me llevo:</strong>
                    {aprendizaje}
                </p>

                <div class="card-actions">
                    {boton_html}
                </div>
            </div>
        </details>
    </article>
    """


tarjetas_html = "".join(
    crear_tarjeta(actividad, i)
    for i, actividad in enumerate(actividades, start=1)
)

st.markdown(
    f'<div class="activity-grid">{tarjetas_html}</div>',
    unsafe_allow_html=True
)


# ======================================================
# CIERRE
# ======================================================

st.markdown("""
<div class="note-bar">
    ✦ <strong>Nota del creador:</strong>
    Este portafolio está en constante evolución.
    Cada actividad representa una oportunidad para explorar,
    aprender y diseñar algo nuevo.
</div>

<div class="footer-note">
    FIN DE LA PÁGINA, NO DEL PROCESO · DISEÑADO CON CURIOSIDAD ☕
</div>
""", unsafe_allow_html=True)
