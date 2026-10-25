import base64
import mimetypes
import re
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Portafolio II | Interfaces Multimodales",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# ESTILOS DE STREAMLIT Y BARRA LATERAL
# ============================================================
st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;700&family=Playfair+Display:wght@400;700&display=swap');

      header, footer, #MainMenu {visibility:hidden;}

      .block-container, [data-testid="stMainBlockContainer"] {
        padding:0 !important;
        max-width:100% !important;
        min-height:0 !important;
      }

      [data-testid="stMain"] [data-testid="stVerticalBlock"] {
        gap:0 !important;
      }

      [data-testid="stMain"] {padding-bottom:0 !important;}
      [data-testid="stBottom"], [data-testid="stBottomBlockContainer"] {
        display:none !important;
      }

      iframe {display:block;}

      .stApp, [data-testid="stAppViewContainer"],
      [data-testid="stMain"] {
        background:#e4ceb0 !important;
      }

      [data-testid="stSidebarCollapsedControl"],
      [data-testid="stSidebarCollapsedControl"] *,
      [data-testid="stExpandSidebarButton"],
      [data-testid="stExpandSidebarButton"] * {
        visibility:visible !important;
      }

      [data-testid="stSidebarCollapsedControl"] button,
      [data-testid="stExpandSidebarButton"] {
        color:#65442f !important;
        background:#f6e7d1 !important;
        border:1px solid #c5aa8a !important;
        border-radius:999px !important;
      }

      [data-testid="stSidebarCollapseButton"] button,
      [data-testid="stSidebarCollapseButton"] svg,
      [data-testid="stSidebarHeader"] button {
        color:#e8d5bf !important;
      }

      section[data-testid="stSidebar"] {
        background:linear-gradient(170deg,#493025,#302019) !important;
        border-right:1px solid rgba(101,68,47,.35);
      }

      section[data-testid="stSidebar"][aria-expanded="true"] {
        min-width:290px !important;
        max-width:290px !important;
        width:290px !important;
      }

      [data-testid="stSidebarHeader"] {padding-bottom:0 !important;}

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

      .pf-about-title {
        font-family:'Playfair Display',serif;
        font-size:1.05rem;
        font-weight:700;
        color:#f8e9d2;
        line-height:1.3;
        margin-bottom:.6rem;
      }

      .pf-about {
        font-size:.84rem;
        line-height:1.65;
        color:#dfc8ae;
      }

      .nav-item {
        display:flex;
        align-items:center;
        gap:.6rem;
        padding:.35rem 0;
        cursor:pointer;
        font-size:.9rem;
        color:#e8d5bf;
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
    <div class="pf-about-title">
        Aplicaciones e Interfaces Multimodales y de Inteligencia Artificial
    </div>
    <div class="pf-about">
        Este portafolio reúne las actividades desarrolladas durante la
        primera mitad del curso de Creación de Interfaces Multimodales,
        donde estamos explorando diferentes herramientas y tecnologías
        de inteligencia artificial aplicadas a la interacción digital.
        A través de ejercicios de procesamiento de texto, audio e imágenes,
        reconocimiento de voz, visión artificial y aprendizaje automático,
        experimenté con distintas formas de crear interfaces más interactivas,
        accesibles y dinámicas.
    </div>

    <div class="pf-div"></div>
    <div class="pf-h">Dentro del cuaderno</div>

    <div class="nav-item" data-target="parte-1"><span>❖</span> Parte 1 · Primeras actividades</div>
    <div class="nav-item" data-target="parte-2"><span>✦</span> Parte 2 · Portafolio del semestre</div>
    <div class="nav-item" data-target="card-1"><span>✎</span> Dibujo y reconocimiento</div>
    <div class="nav-item" data-target="card-2"><span>◉</span> Sensores y simulación</div>
    <div class="nav-item" data-target="card-5"><span>⌘</span> Herramientas tecnológicas</div>
    <div class="nav-item" data-target="card-7"><span>↗</span> Repositorios y proyectos</div>
    <div class="nav-item" data-target="reflexiones"><span>✧</span> Reflexiones</div>

    <div class="pf-foot">Voz · Gesto · Tacto · Imagen · Sonido</div>
</div>
"""

# Markdown interpreta las líneas con 4+ espacios de sangría (después de una
# línea en blanco) como bloque de código y rompe el HTML. Se compacta el HTML
# en una sola línea, quitando sangrías y uniendo con un espacio para que las
# palabras no queden pegadas.
SIDEBAR_HTML = " ".join(
    linea.strip() for linea in SIDEBAR_HTML.splitlines() if linea.strip()
)

st.sidebar.markdown(SIDEBAR_HTML, unsafe_allow_html=True)


# ============================================================
# HTML PRINCIPAL
# ============================================================
HTML = r"""<!DOCTYPE html>
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
:root {
    --dark-coffee:#38251d;
    --coffee:#65442f;
    --brown-accent:#916a49;
    --beige-dark:#d5bea0;
    --beige-light:#ead7bb;
    --cream-bg:#fff8ec;
    --cream-card:#fffaf0;
    --ink-text:#402d21;
    --terracotta:#a8583b;
}

* {box-sizing:border-box;}

html {
    scroll-behavior:smooth;
    overflow-y:hidden;
    background:#e4ceb0;
}

body {
    margin:0;
    background:
        radial-gradient(ellipse at 10% 10%,#fff9e9,transparent 40%),
        linear-gradient(135deg,#e4ceb0,#f6ead7 50%,#dfc4a0);
    font-family:'DM Sans',sans-serif;
    color:var(--ink-text);
}

h1,h2,h3,.font-serif-custom {
    font-family:'Playfair Display',serif;
    color:var(--dark-coffee);
}

.font-mono-custom {font-family:'DM Mono',monospace;}

.vintage-divider {
    border:0;
    height:1px;
    background:linear-gradient(
        90deg,transparent,#98704e 20%,#e0c49e 50%,
        #98704e 80%,transparent
    );
    margin:2.5rem 0;
}

.hero-box {
    background:linear-gradient(125deg,#fff9ed,#ead6b8);
    border:1px solid #d2b99a;
    box-shadow:0 18px 42px rgba(87,58,38,.12);
}

/* CORRECCIÓN: la card de portada es un poco más alta/larga */
@media (min-width:768px) {
    .hero-box {
        padding-top:3.5rem !important;
        padding-bottom:3.5rem !important;
        min-height:480px;
        display:flex;
        align-items:center;
    }

    .hero-box > .grid {
        width:100%;
    }
}

.portrait-frame {
    position:relative;
    background:#fffaf0;
    box-shadow:8px 12px 0 rgba(105,72,43,.12),
               0 15px 30px rgba(64,41,25,.15);
    transform:rotate(-2.5deg);
    transition:transform .4s ease;
}

.portrait-frame:hover {transform:rotate(0) scale(1.02);}

.gallery-grid {
    display:grid;
    grid-template-columns:repeat(3,minmax(0,1fr));
    gap:2.2rem 1.8rem;
    align-items:stretch;
}

/* CORRECCIÓN: mientras haya una card abierta, las demás no se estiran */
.gallery-grid.has-open {
    align-items:start;
}

.polaroid-card {
    min-width:0;
    position:relative;
    isolation:isolate;
    padding:16px 16px 20px;
    border:2px solid #dcd0be;
    border-radius:14px;
    background:linear-gradient(145deg,#fffaf0,#f2e4cf);
    box-shadow:0 10px 22px rgba(56,37,29,.1);
    transition:transform .35s cubic-bezier(.2,.8,.2,1),
               border-color .35s ease,
               box-shadow .35s ease,
               background-color .35s ease;
}

.polaroid-card:nth-child(2n+1) {transform:rotate(-.5deg);}
.polaroid-card:nth-child(2n) {transform:rotate(.5deg);}

.polaroid-card:hover,
.polaroid-card:focus-within {
    z-index:20;
    transform:translateY(-6px) rotate(0) !important;
    border-color:#65442f !important;
    background:#fff;
    box-shadow:0 24px 40px rgba(56,37,29,.22),
               0 0 0 3px rgba(101,68,47,.25),
               0 0 34px rgba(217,164,65,.3);
}

/* IMÁGENES DE LAS TARJETAS NORMALES */
.polaroid-img-wrapper {
    width:100%;
    height:200px;
    overflow:hidden;
    border-radius:8px;
    border:1px solid rgba(101,68,47,.15);
    background:#e8d7c1;
    position:relative;
}

.polaroid-img {
    width:100%;
    height:100%;
    object-fit:cover;
    filter:sepia(.9) saturate(.85) contrast(.95) brightness(.98);
    transition:filter .5s ease,transform .4s ease;
}

.polaroid-card:hover .polaroid-img {
    filter:sepia(0) saturate(1) contrast(1) brightness(1);
    transform:scale(1.03);
}

.polaroid-img-wrapper::after {
    content:'';
    position:absolute;
    inset:0;
    pointer-events:none;
    background:linear-gradient(
        115deg,transparent 35%,rgba(255,248,230,.6) 50%,transparent 65%
    );
    transform:translateX(-130%);
    transition:transform .9s ease;
}

.polaroid-card:hover .polaroid-img-wrapper::after {
    transform:translateX(130%);
}

.polaroid-card h3 {
    width:fit-content;
    max-width:100%;
    padding-bottom:2px;
    background:linear-gradient(var(--terracotta),var(--terracotta))
               0 100% / 0% 2px no-repeat;
    transition:background-size .5s ease;
}

.polaroid-card:hover h3 {background-size:100% 2px;}

.num-badge {
    flex-shrink:0;
    transition:transform .6s cubic-bezier(.2,.8,.2,1),
               background-color .3s,color .3s;
}

.polaroid-card:hover .num-badge {
    transform:rotate(360deg) scale(1.1);
    background:#a8583b !important;
    color:#fff8ec !important;
    border-color:#a8583b !important;
}

/* BOTONES */
.btn-vintage {
    display:inline-flex;
    align-items:center;
    justify-content:center;
    padding:8px 18px;
    border-radius:20px;
    font-size:.82rem;
    font-weight:600;
    text-decoration:none;
    transition:all .25s ease;
    cursor:pointer;
    user-select:none;
    white-space:nowrap;
}

.btn-read-more {
    background:#ebd8bf;
    color:#523724;
    border:1px solid #c5aa8a;
}

.btn-read-more:hover {
    background:#dfc3a1;
    color:#38251d;
}

.btn-link {
    background:#65442f;
    color:#fff8ec;
    border:1px solid #4a3121;
}

.btn-link:hover {
    background:#38251d;
    color:#fff;
    box-shadow:0 4px 10px rgba(56,37,29,.25);
}

/* CONTENIDO DESPLEGABLE */
.expandable-content {
    max-height:0;
    overflow:hidden;
    opacity:0;
    margin-top:0;
    transition:max-height .45s ease,opacity .3s ease,margin-top .3s ease;
}

.expandable-content.open {
    max-height:700px;
    opacity:1;
    margin-top:14px;
}

/* TARJETA ESPECIAL DE LA ACTIVIDAD 7 */
.polaroid-card-wide {
    grid-column:1 / -1;
    justify-self:center;
    width:100%;
    max-width:1000px;
    display:grid;
    grid-template-columns:minmax(250px,.85fr) minmax(0,1.4fr);
    grid-template-rows:auto auto;
    column-gap:28px;
    row-gap:14px;
    align-items:center;
    padding:26px;
    transform:none !important;
}

.polaroid-card-wide:hover,
.polaroid-card-wide:focus-within {
    transform:translateY(-6px) !important;
}

/* La imagen queda a la izquierda y ocupa las dos filas */
.polaroid-card-wide .wide-image {
    grid-column:1;
    grid-row:1 / 3;
    min-width:0;
}

.polaroid-card-wide .polaroid-img-wrapper {
    height:100%;
    min-height:300px;
    margin-bottom:0;
}

.polaroid-card-wide .wide-content {
    grid-column:2;
    grid-row:1;
    min-width:0;
    align-self:end;
}

.polaroid-card-wide .wide-actions {
    grid-column:2;
    grid-row:2;
    align-self:start;
    display:flex;
    flex-wrap:wrap;
    justify-content:flex-start;
    align-items:center;
    gap:10px;
    margin-top:0;
    padding-top:14px;
    border-top:1px solid rgba(213,190,160,.7);
}

/* DIVISOR ENTRE PARTE 1 Y PARTE 2 */
.part-divider {
    display:flex;
    align-items:center;
    gap:1.2rem;
    margin:4rem 0 2.5rem;
}

.part-divider .line {
    flex:1;
    height:1px;
    background:linear-gradient(
        90deg,transparent,#98704e 30%,#e0c49e 50%,
        #98704e 70%,transparent
    );
}

.part-divider .label {
    font-family:'DM Mono',monospace;
    font-size:.78rem;
    letter-spacing:.2em;
    text-transform:uppercase;
    color:#8d5b3d;
    padding:.5rem 1.2rem;
    border:1px solid #cdb393;
    border-radius:999px;
    background:#fff9ef;
    white-space:nowrap;
}

@media (max-width:640px) {
    .part-divider .label {
        white-space:normal;
        text-align:center;
        letter-spacing:.12em;
    }
}

/* TARJETA DE RESPALDO DE IMAGEN */
.img-fallback {
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
}

/* REFLEXIÓN */
.modal-note {
    background:linear-gradient(135deg,#fffaf0,#f2e4cf);
    border:1px solid #d2b895;
    border-radius:16px;
    box-shadow:0 10px 24px rgba(56,37,29,.1);
}

.channel-chip {
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
    transition:transform .25s ease,background-color .25s ease,color .25s ease;
}

.channel-chip:hover {
    transform:translateY(-3px) rotate(-2deg);
    background:#65442f;
    color:#fff8ec;
}

.tag-chip {
    cursor:default;
    transition:transform .25s ease,background-color .25s ease,color .25s ease;
}

.tag-chip:hover {
    transform:translateY(-3px) rotate(-2deg);
    background:#65442f !important;
    color:#fff8ec !important;
}

.float-star {
    position:absolute;
    pointer-events:none;
    color:#c99a5b;
    opacity:.75;
    animation:floaty 7s ease-in-out infinite;
}

@keyframes floaty {
    0%,100% {transform:translateY(0) rotate(0) scale(1);opacity:.45;}
    50% {transform:translateY(-14px) rotate(25deg) scale(1.2);opacity:.95;}
}

.title-star {
    display:inline-block;
    color:#65442f;
    font-size:.42em;
    vertical-align:middle;
    margin:0 .5em 0 0;
    animation:twinkle 3.2s ease-in-out infinite;
}

.title-star.end {
    margin:0 0 0 .35em;
    animation-delay:-1.6s;
}

@keyframes twinkle {
    0%,100% {transform:scale(1) rotate(0);opacity:.95;}
    50% {transform:scale(1.4) rotate(90deg);opacity:.55;}
}

.shimmer-text {
    display:inline-block;
    padding:0 .1em .12em 0;
    background:linear-gradient(
        100deg,#8d5b3d 20%,#d9a441 45%,#a8583b 55%,#8d5b3d 80%
    );
    background-size:200% auto;
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
    color:transparent;
    animation:shimmer 5s linear infinite;
}

@keyframes shimmer {
    to {background-position:-200% center;}
}

.sparkle {
    position:absolute;
    pointer-events:none;
    z-index:40;
    line-height:1;
    text-shadow:0 0 6px rgba(232,194,122,.9);
    animation:sparkle .95s ease-out forwards;
}

@keyframes sparkle {
    0% {opacity:0;transform:translate(-50%,-50%) scale(.2) rotate(0);}
    25% {opacity:1;}
    100% {
        opacity:0;
        transform:translate(calc(-50% + var(--dx)),calc(-50% + var(--dy)))
                   scale(1.1) rotate(200deg);
    }
}

.reveal:not(.in) {opacity:0;}
.reveal.in {animation:reveal .8s cubic-bezier(.2,.8,.2,1) backwards;}

@keyframes reveal {
    from {opacity:0;translate:0 25px;}
}

body::after {
    content:"";
    position:fixed;
    inset:0;
    pointer-events:none;
    z-index:90;
    opacity:.10;
    mix-blend-mode:multiply;
    background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)' opacity='.3'/></svg>");
}

@media (max-width:1100px) {
    .gallery-grid {grid-template-columns:repeat(2,minmax(0,1fr));}

    .polaroid-card-wide {
        max-width:900px;
        grid-template-columns:minmax(210px,.8fr) minmax(0,1.2fr);
        column-gap:20px;
    }

    .polaroid-card-wide .polaroid-img-wrapper {min-height:260px;}
}

@media (max-width:640px) {
    .gallery-grid {
        grid-template-columns:1fr;
        gap:1.8rem;
    }

    .polaroid-card-wide {
        grid-column:1;
        grid-template-columns:minmax(0,1fr);
        grid-template-rows:auto auto auto;
        padding:16px;
        gap:14px;
    }

    .polaroid-card-wide .wide-image {
        grid-column:1;
        grid-row:1;
    }

    .polaroid-card-wide .polaroid-img-wrapper {
        height:230px;
        min-height:0;
    }

    .polaroid-card-wide .wide-content {
        grid-column:1;
        grid-row:2;
    }

    .polaroid-card-wide .wide-actions {
        grid-column:1;
        grid-row:3;
    }

    .btn-vintage {padding:8px 13px;}
}

@media (prefers-reduced-motion:reduce) {
    *,*::before,*::after {
        animation:none !important;
        transition:none !important;
    }
    .reveal:not(.in) {opacity:1;}
}
</style>
</head>

<body class="flex flex-col md:flex-row">

<main class="flex-1 p-4 md:p-10 max-w-[1600px] mx-auto w-full"
      style="padding-bottom:.75rem">

    <!-- PORTADA -->
    <section class="hero-box rounded-2xl p-6 md:p-8 relative mb-8">
        <span class="float-star" style="top:10px;right:28px;font-size:28px">✦</span>
        <span class="float-star" style="bottom:18px;right:46%;font-size:18px;animation-delay:-2s">✧</span>
        <span class="float-star" style="top:46%;left:-12px;font-size:22px;animation-delay:-4s">✦</span>
        <span class="float-star" style="bottom:10px;right:20px;font-size:24px;animation-delay:-1s">✶</span>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            <div class="lg:col-span-4 flex justify-center lg:justify-start">
                <div class="portrait-frame p-3 pb-4 max-w-[320px] w-full rounded-sm">
                    <div class="w-full h-64 md:h-80 bg-[#e2d1b8] rounded overflow-hidden">
                        <img id="foto-portada" src="Simon.jpeg"
                             alt="Fotografía de portada"
                             class="w-full h-full object-cover"
                             onerror="this.onerror=null;this.parentElement.innerHTML='<div class=\'img-fallback\'><span class=\'text-2xl\'>✦</span><strong class=\'text-xs mt-1\'>Fotografía de prueba</strong><small class=\'text-[10px]\'>Simon.jpeg</small></div>';">
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
                    <span class="title-star">✦</span>Interfaces<br>
                    <span class="italic shimmer-text">multimodales.</span><span class="title-star end">✦</span>
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
                    <span class="tag-chip px-3 py-1 bg-[#fff9ef] border border-[#cdb393] rounded-full text-xs font-mono-custom text-[#694a32]">✳ Diseño interactivo</span>
                    <span class="tag-chip px-3 py-1 bg-[#fff9ef] border border-[#cdb393] rounded-full text-xs font-mono-custom text-[#694a32]">⌘ Experimentación</span>
                    <span class="tag-chip px-3 py-1 bg-[#fff9ef] border border-[#cdb393] rounded-full text-xs font-mono-custom text-[#694a32]">↗ Aprender haciendo</span>
                </div>
            </div>
        </div>
    </section>

    <hr class="vintage-divider">

    <!-- PARTE 1 -->
    <section id="parte-1" class="mb-8">
        <div class="font-mono-custom text-xs tracking-widest text-[#8d5b3d] uppercase mb-1">
            Parte 1 · Primera sesión del semestre 2026-2 · 01—10
        </div>
        <h2 class="text-3xl md:text-4xl font-bold text-[#38251d]">
            Primeras actividades realizadas en clase
        </h2>
        <p class="text-sm text-[#725942] mt-2">
            Los primeros experimentos del semestre: texto, voz, imagen y visión
            artificial aplicados a interfaces web interactivas.
        </p>
    </section>

    <div class="gallery-grid" id="cardsContainerP1"></div>

    <!-- DIVISOR PARTE 2 -->
    <div id="parte-2" class="part-divider">
        <span class="line"></span>
        <span class="label">✦ Parte 2 · Portafolio del semestre ✦</span>
        <span class="line"></span>
    </div>

    <!-- PARTE 2 -->
    <section class="mb-8">
        <div class="font-mono-custom text-xs tracking-widest text-[#8d5b3d] uppercase mb-1">
            Parte 2 · Galería de procesos · 01—07
        </div>
        <h2 class="text-3xl md:text-4xl font-bold text-[#38251d]">
            Actividades prácticas realizadas
        </h2>
        <p class="text-sm text-[#725942] mt-2">
            Cada tarjeta es un experimento: una manera distinta de combinar
            sentidos y canales para que las personas interactúen con la tecnología.
        </p>
    </section>

    <div class="gallery-grid" id="cardsContainer"></div>

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
// ============================================================
// CONTENIDO DE LAS ACTIVIDADES
// Para editar el portafolio, modifica estos datos.
// La variable aprendizaje se conserva (solo en la Parte 2).
// ============================================================

// ============================================================
// PARTE 1: PRIMERA SESIÓN DEL SEMESTRE 2026-2
// Sin apartado "Lo que aprendí". Las URLs no se modifican.
// La imagen se busca junto a app.py (campo "imagen").
// ============================================================

const actividadesParte1 = [
    {
        id:101,
        titulo:"Mi primer repositorio - Intro GitHub",
        categoria:"GitHub · 01",
        resumen:"Mi primer repositorio en GitHub, usado para publicar y modificar una interfaz web.",
        descripcion:"Exploración inicial de GitHub como herramienta para el desarrollo y publicación de interfaces. Se experimentó con modificaciones visuales y transformaciones básicas de imágenes dentro de una interfaz de formato web, como primer paso para trabajar con repositorios.",
        imagen:"SnoopyP.jpg",
        archivo:"SnoopyP.jpg",
        enlaces:[
            {texto:"Intro Repositorio Snoopy", url:"https://el-primer-repo-de-saimon-fnendgpad7jxzqwkawtxsa.streamlit.app/"}
        ]
    },
    {
        id:102,
        titulo:"Conversión de texto a audio",
        categoria:"Texto a voz · 02",
        resumen:"Una interfaz que lee en voz alta el texto que escribo.",
        descripcion:"Desarrollo de una interfaz para convertir texto escrito en audio, explorando herramientas de voz que facilitan la interacción con contenidos escritos. Se publicaron dos versiones: una con fábulas como contenido de ejemplo y otra de texto a voz de uso general.",
        imagen:"LECTURA.png",
        archivo:"LECTURA.png",
        enlaces:[
            {texto:"Fábulas: Texto a Voz", url:"https://gaticorat-cxqqen2bqdsebk6fnnoapf.streamlit.app/"},
            {texto:"Texto a Voz", url:"https://gaticorat-v3kscp9uekqdd9qqfauysz.streamlit.app/"}
        ]
    },
    {
        id:103,
        titulo:"Voz a texto multilingüe",
        categoria:"Voz a texto · 03",
        resumen:"Convierte lo que digo en texto, en seis idiomas distintos.",
        descripcion:"Creación de una interfaz capaz de transformar audio de voz en texto en diferentes idiomas, incluyendo español, inglés, francés, italiano, alemán y mandarín. Muestra cómo la voz puede ser un canal de entrada más natural que el teclado.",
        imagen:"Traduccion.avif",
        archivo:"Traduccion.avif",
        enlaces:[
            {texto:"Traductor", url:"https://traductorsimon-5msaydpezd7zgwclllbkmy.streamlit.app/"}
        ]
    },
    {
        id:104,
        titulo:"Interfaz OCR Audio y análisis estadístico",
        categoria:"OCR · 04",
        resumen:"Extrae el texto de una imagen y analiza sus vocales, con temática de playa.",
        descripcion:"Interfaz de conversión de imagen a texto, complementada con un análisis estadístico de las vocales identificadas en el contenido extraído. La propuesta de diseño incorporó una temática playera para integrar una visual personalizada.",
        imagen:"Playa.jpg",
        archivo:"Playa.jpg",
        enlaces:[
            {texto:"OCR Audio Temático", url:"https://ocr-audiosimon-awv2toavjnd8nxdt7uuqvh.streamlit.app/"}
        ]
    },
    {
        id:105,
        titulo:"WordCloud - Nube de palabras",
        categoria:"Lenguaje · 05",
        resumen:"Nubes de palabras que muestran los términos más relevantes de un texto.",
        descripcion:"Creación de nubes de palabras a partir de fragmentos de texto para representar visualmente los términos más relevantes. Se exploró el uso de TextBlob y técnicas de procesamiento de lenguaje natural.",
        imagen:"WORDCLOUD.png",
        archivo:"WORDCLOUD.png",
        enlaces:[
            {texto:"WordCloud", url:"https://wordcloudsimon-5ftjecuahge5koe5fvwyka.streamlit.app/"}
        ]
    },
    {
        id:106,
        titulo:"Análisis sentimientos - Emociones",
        categoria:"Emociones · 06",
        resumen:"Detecta las emociones de un texto y responde con animaciones y videos.",
        descripcion:"Interfaz que identifica sentimientos y emociones presentes en un texto de entrada. Los resultados se complementaron con animaciones de Lottie y videos asociados a las emociones detectadas.",
        imagen:"EMOCIONES.png",
        archivo:"EMOCIONES.png",
        enlaces:[
            {texto:"Análisis de sentimientos", url:"https://sentimentasimon-kxq5k5hfxwdmkofrfih48x.streamlit.app/"}
        ]
    },
    {
        id:107,
        titulo:"Evaluación automática - TF-IDF",
        categoria:"TF-IDF · 07",
        resumen:"Genera preguntas y respuestas automáticas a partir de textos.",
        descripcion:"Creación de una interfaz para generar preguntas y respuestas automáticas a partir de textos mediante procesamiento de lenguaje natural. Se utilizó TF-IDF para identificar términos relevantes dentro de conjuntos de documentos.",
        imagen:"PREGUNTAS.png",
        archivo:"PREGUNTAS.png",
        enlaces:[
            {texto:"TF-IDF", url:"https://tdfespsimon-5bvcznbfcefdobupqjkmqe.streamlit.app/"}
        ]
    },
    {
        id:108,
        titulo:"YOLO - Detección de objetos",
        categoria:"Visión · 08",
        resumen:"Un modelo que detecta y reconoce objetos dentro de imágenes.",
        descripcion:"Exploración del modelo YOLO (You Only Look Once) para el reconocimiento y detección de objetos en imágenes. La actividad permitió comprender cómo la inteligencia artificial puede interpretar información visual.",
        imagen:"CAPTCHA.png",
        archivo:"CAPTCHA.png",
        enlaces:[
            {texto:"YOLO", url:"https://yolov5simon-hzxwgknlx5tajlvax74gns.streamlit.app/"}
        ]
    },
    {
        id:109,
        titulo:"Teachable Machine - Reconocer objetos",
        categoria:"Aprendizaje · 09",
        resumen:"Un modelo entrenado por mí que reconoce personas en tiempo real.",
        descripcion:"Experimentación con Teachable Machine de Google para entrenar modelos personalizados de aprendizaje automático. Se realizaron pruebas de reconocimiento de personas en tiempo real.",
        imagen:"FACEID.png",
        archivo:"FACEID.png",
        enlaces:[
            {texto:"Teachable Machine", url:"https://t8pwvf7om2y4dwtcjzvsyu.streamlit.app/"}
        ]
    },
    {
        id:110,
        ancha:true,
        titulo:"Imagen a texto - Reconocimiento Óptico de Caracteres OCR",
        categoria:"OCR · 10",
        resumen:"Extrae texto editable a partir de imágenes usando OCR.",
        descripcion:"Implementación de OCR para extraer texto a partir de imágenes. La actividad permitió explorar cómo una imagen con información escrita puede ser procesada y convertida en texto editable. Se publicaron dos interfaces: la versión de reconocimiento óptico de caracteres y una versión de OCR sin intervención.",
        imagen:"ocr.png",
        archivo:"ocr.png",
        enlaces:[
            {texto:"Reconocimiento óptico de caracteres", url:"https://ocrsimonclase7-7mfw3mnqwhzk63smvxw2sv.streamlit.app/"},
            {texto:"Interfaz OCR sin intervención", url:"https://ocr-audiosimon-abfnnjajxn75g8upksqeq6.streamlit.app/"}
        ]
    }
];


// ============================================================
// PARTE 2: ACTIVIDADES DEL PORTAFOLIO DEL SEMESTRE
// ============================================================

const actividadesParte2 = [
    {
        id:1,
        titulo:"Actividad 01: Detección de Números a través de dibujos",
        categoria:"Práctica · 01",
        resumen:"Una red neuronal entrenada con MNIST que reconoce los dígitos que dibujo sobre un lienzo.",
        descripcion:"MNIST es una base de datos compuesta por 70,000 imágenes de dígitos escritos a mano. Desplegué la aplicación del repositorio y escribí diferentes números; el modelo reconoce lo escrito después de revisar el Google Colab.",
        aprendizaje:"Aprendí cómo las redes convolucionales aprenden bordes, formas y texturas, y que el trazo debe prepararse para que el modelo lo interprete bien.",
        url:"https://mnistpredsimon-5vckfxydhqvco4snzsuo8s.streamlit.app/",
        botonTexto:"Abrir recurso"
    },
    {
        id:2,
        titulo:"Actividad 02 (Editada) - Tablero Personalizado",
        categoria:"Edición · 02",
        resumen:"Un tablero de dibujo cuyas propiedades puedo configurar a mi gusto.",
        descripcion:"Edité el ejemplo inicial de la primera actividad para que las propiedades del tablero se configuren desde la interfaz.",
        aprendizaje:"Personalizar la herramienta es parte de diseñar la interacción; se practica cómo exponer parámetros con los controles de Streamlit.",
        url:"https://repositorio-2-simon-eg936rwzmxxzqdssn5lhlk.streamlit.app/",
        botonTexto:"Abrir recurso"
    },
    {
        id:3,
        titulo:"Actividad 03: Tablero Reconocimiento",
        categoria:"Interfaz · 03",
        resumen:"Un tablero que reconoce lo que dibujo usando modelos de visión.",
        descripcion:"Combiné el tablero con un modelo de visión que identifica bocetos.",
        aprendizaje:"Aprendí la diferencia entre un clasificador de una sola tarea (MNIST) y un modelo de visión más general, y cómo dibujo e imagen funcionan como un canal multimodal de reconocimiento.",
        url:"https://drawrecogsimon-mrzchike38innmhbruk49k.streamlit.app/",
        botonTexto:"Abrir recurso"
    },
    {
        id:4,
        titulo:"Actividad 04: Tablero Personalizado Cuenta Historias",
        categoria:"Simulación · 04",
        resumen:"Un tablero digital que convierte mis dibujos en historias.",
        descripcion:"Fui más allá de reconocer una figura para crear narrativamente una historia con contexto.",
        aprendizaje:"Aprendí a pensar el reconocimiento como el inicio de una experiencia y a encadenar una entrada visual con una salida de texto.",
        url:"https://simonhistoriadibujo-cbtrgvlhhqu3aht43y8tlo.streamlit.app/",
        botonTexto:"Abrir recurso"
    },
    {
        id:5,
        titulo:"Actividad 05: Recepción de Datos MQTT (Recep_mqtt)",
        categoria:"Tecnología · 05",
        resumen:"Monitoreo en tiempo real de telemetría desde un sensor analógico simulado en Wokwi hacia la app en Streamlit.",
        descripcion:"Se organizó bajo la arquitectura cliente-broker. Un circuito en Wokwi actúa como cliente publicador, enviando lecturas de un sensor analógico a un broker MQTT en un tópico específico. La app en Streamlit opera como cliente suscriptor, conectándose al broker y escuchando ese tópico para visualizar los datos en vivo.",
        aprendizaje:"Entendí el patrón Publish/Subscribe, cómo el broker gestiona los mensajes y cómo recibir flujo continuo de telemetría en un cliente web.",
        url:"https://recepmqtt-c632mej72ce2uypzr9henl.streamlit.app/",
        botonTexto:"Abrir recurso"
    },
    {
        id:6,
        titulo:"Actividad 06: Publicación y Telecontrol MQTT",
        categoria:"Aprendizaje · 06",
        resumen:"Telecontrol bidireccional desde la interfaz web para activar LEDs en el simulador Wokwi.",
        descripcion:"Se invirtió el flujo de control: la app en Streamlit funciona como cliente publicador, enviando comandos de encendido/apagado de luces y ángulo del servomotor a un tópico del broker MQTT. En Wokwi, el microcontrolador actúa como cliente suscriptor, escuchando el tópico para ejecutar las acciones en el hardware simulado.",
        aprendizaje:"Aprendí a estructurar comandos de control desde un cliente web hacia actuadores remotos usando tópicos de instrucción en el broker MQTT.",
        url:"https://sendcmqttsimon-5e3raacaadr2kz3jago5z9.streamlit.app/",
        botonTexto:"Abrir recurso"
    },
    {
        id:7,
        ancha:true,
        titulo:"Actividad 07: Control Multimodal por Voz (Ctrl_Voice)",
        categoria:"Hardware · 07",
        resumen:"Control de luces y puertas mediante comandos vocales procesados en la web y transmitidos al simulador.",
        descripcion:"Se estructuró capturando la voz del usuario en un cliente web (Streamlit), traduciendo frases habladas en variables lógicas. Estas se publican hacia el broker MQTT dentro del tópico correspondiente, donde el microcontrolador en Wokwi (cliente suscriptor) recibe la orden y mueve el servomotor o altera los LEDs.",
        aprendizaje:"Aprendí a integrar la voz como canal de entrada multimodal y a mapear eventos de audio con comandos enviados a través de un broker MQTT.",
        url:"https://github.com",
        botonTexto:"Abrir recurso"
    }
];

const reduceMotion = window.matchMedia(
    '(prefers-reduced-motion: reduce)'
).matches;


// ============================================================
// EFECTOS DE CHISPITAS
// ============================================================

function attachSparkles(el) {
    const glyphs = ['✦','✧','✶','✦','·'];
    const colors = ['#d9a441','#a8583b','#916a49','#e8c27a','#c99a5b'];
    let timer = null;

    function spawn() {
        const s = document.createElement('span');
        s.className = 'sparkle';
        s.textContent = glyphs[Math.floor(Math.random()*glyphs.length)];

        const side = Math.floor(Math.random()*4);
        const t = Math.random()*100;
        const far = 18+Math.random()*28;
        const drift = (Math.random()-.5)*34;
        let x,y,dx,dy;

        if (side===0) {
            x=t; y=0; dx=drift; dy=-far;
        } else if (side===1) {
            x=100; y=t; dx=far; dy=drift;
        } else if (side===2) {
            x=t; y=100; dx=drift; dy=far;
        } else {
            x=0; y=t; dx=-far; dy=drift;
        }

        s.style.left=x+'%';
        s.style.top=y+'%';
        s.style.setProperty('--dx',dx+'px');
        s.style.setProperty('--dy',dy+'px');
        s.style.fontSize=(10+Math.random()*14)+'px';
        s.style.color=colors[Math.floor(Math.random()*colors.length)];
        s.addEventListener('animationend',()=>s.remove());
        el.appendChild(s);
    }

    el.addEventListener('mouseenter',()=>{
        if (reduceMotion) return;
        for (let i=0;i<7;i++) setTimeout(spawn,i*40);
        timer=setInterval(spawn,110);
    });

    el.addEventListener('mouseleave',()=>{
        clearInterval(timer);
        timer=null;
    });
}


// ============================================================
// ANIMACIÓN DE APARICIÓN
// ============================================================

const revealObserver = new IntersectionObserver(entries=>{
    entries.forEach(e=>{
        if (e.isIntersecting) {
            e.target.classList.add('in');
            revealObserver.unobserve(e.target);
        }
    });
},{threshold:.12});


// ============================================================
// ALTURA DEL IFRAME
// ============================================================

function fitFrame() {
    try {
        if (window.frameElement) {
            const alto=Math.ceil(document.body.getBoundingClientRect().height);
            window.frameElement.style.height=alto+'px';
            window.frameElement.setAttribute('height',alto);
        }
    } catch(e) {}
}


// ============================================================
// COMUNICACIÓN CON LA PÁGINA PADRE DE STREAMLIT
// ============================================================

function conectarConPaginaPadre() {
    let P,pdoc;

    try {
        P=window.parent;
        pdoc=P.document;
        void pdoc.body;
    } catch(e) {
        return;
    }

    if (!P || P===window || !window.frameElement) return;

    try {
        if (P.__pfCleanup) P.__pfCleanup();
    } catch(e) {}

    function findScroller() {
        let el=window.frameElement.parentElement;

        while (el && el!==pdoc.body && el!==pdoc.documentElement) {
            const oy=P.getComputedStyle(el).overflowY;
            if (
                (oy==='auto'||oy==='scroll') &&
                el.scrollHeight>el.clientHeight+1
            ) return el;

            el=el.parentElement;
        }

        return pdoc.scrollingElement||pdoc.documentElement;
    }

    const bar=pdoc.createElement('div');
    bar.id='pf-progress';

    bar.style.cssText=
        'position:fixed;top:0;left:0;height:5px;width:0;z-index:2147483000;pointer-events:none;'+
        'background:linear-gradient(90deg,#a8583b,#d9a441,#e8c27a);'+
        'box-shadow:0 0 10px rgba(217,164,65,.7);transition:width .08s linear;';

    pdoc.body.appendChild(bar);

    function actualizar() {
        const sc=findScroller();
        const max=sc.scrollHeight-sc.clientHeight;
        bar.style.width=(
            max>0?Math.min(100,(sc.scrollTop/max)*100):0
        )+'%';
    }

    const onScroll=()=>actualizar();

    pdoc.addEventListener('scroll',onScroll,true);
    P.addEventListener('resize',onScroll);

    const onClick=e=>{
        const item=e.target?.closest?.('.nav-item');
        if (!item) return;

        const destino=document.getElementById(
            item.getAttribute('data-target')
        );

        if (!destino) return;

        const sc=findScroller();
        const topFrame=window.frameElement.getBoundingClientRect().top;
        const topDestino=destino.getBoundingClientRect().top;
        const topScroller=(
            sc===pdoc.scrollingElement?0:sc.getBoundingClientRect().top
        );

        sc.scrollTo({
            top:sc.scrollTop+(topFrame-topScroller)+topDestino-P.innerHeight*.2,
            behavior:'smooth'
        });
    };

    pdoc.addEventListener('click',onClick);

    P.__pfCleanup=function() {
        pdoc.removeEventListener('scroll',onScroll,true);
        pdoc.removeEventListener('click',onClick);
        P.removeEventListener('resize',onScroll);
        if (bar.parentNode) bar.parentNode.removeChild(bar);
    };

    actualizar();
    setTimeout(actualizar,400);
}


// ============================================================
// RENDERIZADO DE TARJETAS
// La actividad 7 tiene una estructura especial horizontal.
// ============================================================

const FOTO=(
    document.getElementById('foto-portada')||{}
).src||'Simon.jpeg';

function crearImagen(item) {
    const src=item.imagen||FOTO;
    const etiqueta=item.archivo?'Imagen no encontrada':'Fotografía '+item.id;
    const archivo=item.archivo||'Simon.jpeg';

    return `
        <div class="polaroid-img-wrapper">
            <img src="${src}"
                 alt="${item.titulo}"
                 class="polaroid-img"
                 onerror="this.onerror=null;this.parentElement.innerHTML='<div class=\\'img-fallback\\'><span class=\\'text-3xl\\'>✦</span><strong class=\\'text-sm mt-1\\'>${etiqueta}</strong><small class=\\'text-[11px]\\'>${archivo}</small></div>';">
        </div>
    `;
}

function crearContenido(item,index) {
    // Solo las actividades de la Parte 2 tienen "Lo que aprendí".
    const bloqueAprendizaje=item.aprendizaje?`
            <div class="bg-[#f5e9d6] p-3 rounded-lg border border-[#e2d0b5]">
                <strong class="text-[#38251d] block mb-0.5">
                    Lo que aprendí:
                </strong>
                ${item.aprendizaje}
            </div>`:'';

    return `
        <div class="flex justify-between items-center mb-2 font-mono-custom text-xs uppercase text-[#8d5b3d]">
            <span>${item.categoria}</span>
            <span class="num-badge w-7 h-7 rounded-full border border-[#d5b995] bg-[#f6e7d1] flex items-center justify-center font-bold text-xs">
                ${String(index+1).padStart(2,'0')}
            </span>
        </div>

        <h3 class="font-serif-custom font-bold text-xl leading-snug mb-2 text-[#38251d]">
            ${item.titulo}
        </h3>

        <p class="text-sm text-[#725942] leading-relaxed mb-3">
            ${item.resumen}
        </p>

        <div id="expand-${item.id}"
             class="expandable-content border-t border-[#e0ccb0] pt-3 text-xs md:text-sm text-[#614a37] space-y-2">

            <p>${item.descripcion}</p>
            ${bloqueAprendizaje}
        </div>
    `;
}

function crearBotones(item) {
    // Una actividad puede tener uno o varios enlaces.
    const enlaces=item.enlaces||[
        {texto:item.botonTexto||'Abrir recurso',url:item.url}
    ];

    const links=enlaces.map(e=>`
        <a href="${e.url}"
           target="_blank"
           rel="noopener noreferrer"
           class="btn-vintage btn-link">
            ↗ ${e.texto}
        </a>
    `).join('');

    return `
        <button type="button"
                onclick="toggleExpand(${item.id})"
                class="btn-vintage btn-read-more">
            <span id="btn-text-${item.id}">Leer más</span>
        </button>

        ${links}
    `;
}

function renderGrid(lista,contenedorId) {
    const container=document.getElementById(contenedorId);
    if (!container) return;

    container.innerHTML='';

    lista.forEach((item,index)=>{
        const card=document.createElement('article');

        card.className='polaroid-card reveal';

        if (item.ancha) {
            card.classList.add('polaroid-card-wide');

            // Tarjeta horizontal: foto izquierda; contenido y botones derecha.
            card.innerHTML=`
                <div class="wide-image">
                    ${crearImagen(item)}
                </div>

                <div class="wide-content">
                    ${crearContenido(item,index)}
                </div>

                <div class="wide-actions">
                    ${crearBotones(item)}
                </div>
            `;
        } else {
            // Estructura original para las demás actividades.
            card.classList.add('flex','flex-col','justify-between');

            card.innerHTML=`
                <div>
                    ${crearImagen(item)}
                    ${crearContenido(item,index)}
                </div>

                <div class="flex items-center justify-between gap-3 mt-5 pt-3 border-t border-[#ebd8bf]/70 flex-wrap">
                    ${crearBotones(item)}
                </div>
            `;
        }

        card.id='card-'+item.id;
        card.style.animationDelay=((index%2)*.12)+'s';

        container.appendChild(card);
        attachSparkles(card);
        revealObserver.observe(card);
    });
}

function renderCards() {
    renderGrid(actividadesParte1,'cardsContainerP1');
    renderGrid(actividadesParte2,'cardsContainer');
    fitFrame();
}


// ============================================================
// BOTÓN LEER MÁS / VER MENOS
// Cada card se abre y se cierra de forma independiente.
//
// La grilla usa align-items:stretch, así que al abrir una card
// las demás de su fila se estiraban con ella. Al abrir la primera
// card de una grilla se "congela" la altura original de las demás;
// al cerrar la última, se restaura todo. Cada grilla (Parte 1 y
// Parte 2) funciona de forma independiente.
// ============================================================

function tarjetasAbiertas(container) {
    return container.querySelectorAll('.expandable-content.open').length;
}

function tarjetasNormales(container) {
    return container.querySelectorAll('.polaroid-card:not(.polaroid-card-wide)');
}

function congelarAlturas(container) {
    // Se mide ANTES de abrir nada, con todas las cards en su estado original.
    tarjetasNormales(container).forEach(c=>{
        const h=c.offsetHeight;
        c.dataset.h=h;
        c.style.height=h+'px';
    });

    container.classList.add('has-open');
}

function liberarAlturas(container) {
    tarjetasNormales(container).forEach(c=>{
        c.style.height='';
        delete c.dataset.h;
    });

    container.classList.remove('has-open');
}

function toggleExpand(id) {
    const content=document.getElementById(`expand-${id}`);
    const btnText=document.getElementById(`btn-text-${id}`);
    const card=document.getElementById(`card-${id}`);

    if (!content || !btnText || !card) return;

    const container=card.parentElement;
    const esAncha=card.classList.contains('polaroid-card-wide');
    const isOpen=content.classList.contains('open');

    if (!isOpen) {
        // ABRIR: solo esta card crece; las demás conservan su altura.
        if (tarjetasAbiertas(container)===0) congelarAlturas(container);

        if (!esAncha) card.style.height='auto';

        content.classList.add('open');
        btnText.textContent='Ver menos';
    } else {
        // CERRAR: esta card vuelve a su estado original.
        content.classList.remove('open');
        btnText.textContent='Leer más';

        setTimeout(()=>{
            // Si la volvieron a abrir mientras tanto, no hacer nada.
            if (content.classList.contains('open')) return;

            if (tarjetasAbiertas(container)===0) {
                liberarAlturas(container);
            } else if (!esAncha && card.dataset.h) {
                card.style.height=card.dataset.h+'px';
            }

            fitFrame();
        },480);
    }

    // Actualiza la altura para que Streamlit no recorte el contenido.
    setTimeout(fitFrame,100);
    setTimeout(fitFrame,500);
}

// Si cambia el ANCHO de la ventana, las alturas congeladas dejan de
// ser válidas: se cierran todas las cards y se restauran las grillas.
// (Cambios de alto del iframe se ignoran a propósito.)
let anchoPrevio=window.innerWidth;

window.addEventListener('resize',()=>{
    if (window.innerWidth===anchoPrevio) return;
    anchoPrevio=window.innerWidth;

    document.querySelectorAll('.expandable-content.open').forEach(c=>{
        c.classList.remove('open');
    });

    document.querySelectorAll('[id^="btn-text-"]').forEach(b=>{
        b.textContent='Leer más';
    });

    document.querySelectorAll('.gallery-grid').forEach(liberarAlturas);
    fitFrame();
});


// ============================================================
// INICIALIZACIÓN
// ============================================================

window.addEventListener('DOMContentLoaded',()=>{
    renderCards();

    const portrait=document.querySelector('.portrait-frame');
    if (portrait) attachSparkles(portrait);

    fitFrame();

    if ('ResizeObserver' in window) {
        new ResizeObserver(fitFrame).observe(document.body);
    }

    window.addEventListener('load',fitFrame);
    window.addEventListener('resize',fitFrame);

    if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(fitFrame);
    }

    conectarConPaginaPadre();
});
</script>
</body>
</html>
"""


# ============================================================
# INCRUSTAR LAS IMÁGENES LOCALES EN EL HTML
# ============================================================

EXTENSIONES={".jpg",".jpeg",".png",".webp",".gif",".avif"}

MIME_EXTRA={".avif":"image/avif"}

PATRON_EXT=r"(?:jpe?g|png|webp|gif|avif)"


def buscar_imagen(nombre):
    """Busca la imagen junto a app.py, sin distinguir mayúsculas."""
    carpeta=Path(__file__).parent

    archivos=[
        f for f in carpeta.iterdir()
        if f.is_file() and f.suffix.lower() in EXTENSIONES
    ]

    for f in archivos:
        if f.name.lower()==nombre.lower():
            return f

    base=Path(nombre).stem.lower()

    for f in archivos:
        if f.stem.lower()==base:
            return f

    return None


def a_data_uri(nombre):
    """Devuelve la imagen como data URI, o None si no se encuentra."""
    f=buscar_imagen(nombre)

    if f is None:
        return None

    mime=(
        MIME_EXTRA.get(f.suffix.lower())
        or mimetypes.guess_type(f.name)[0]
        or "image/jpeg"
    )
    b64=base64.b64encode(f.read_bytes()).decode()

    return f"data:{mime};base64,{b64}"


def incrustar_imagenes(html):
    # 1) Imágenes escritas en el HTML:  src="Simon.jpeg"
    def reemplazo_src(m):
        uri=a_data_uri(m.group(1))
        return m.group(0) if uri is None else f'src="{uri}"'

    # 2) Imágenes de las actividades (datos JS):  imagen:"SnoopyP.jpg"
    def reemplazo_imagen(m):
        uri=a_data_uri(m.group(1))
        return m.group(0) if uri is None else f'imagen:"{uri}"'

    html=re.sub(
        r'src="([^"/:]+\.' + PATRON_EXT + r')"',
        reemplazo_src,
        html,
        flags=re.I
    )

    html=re.sub(
        r'imagen:"([^"/:]+\.' + PATRON_EXT + r')"',
        reemplazo_imagen,
        html,
        flags=re.I
    )

    return html


HTML=incrustar_imagenes(HTML)

# El iframe ajusta su altura al contenido mediante JavaScript.
components.html(HTML,height=3000,scrolling=False)
