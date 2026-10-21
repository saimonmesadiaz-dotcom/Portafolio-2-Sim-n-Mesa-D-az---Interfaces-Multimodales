
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
    section[data-testid="stSidebar"] {
    background: linear-gradient(170deg, #493025, #302019) !important;
    border-right: 1px solid rgba(101, 68, 47, .35);
}

section[data-testid="stSidebar"] > div {
    height: 100vh;
    overflow-y: auto;
}

section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
    padding-top: 1rem;
    overflow-y: auto;
}

section[data-testid="stSidebar"] .pf-side {
    display: block;
    visibility: visible;
    opacity: 1;
    color: #f8e9d2;
}
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
    <div class="pf-h">Dentro del cuaderno</div>

    <div class="nav-item" data-target="card-1"><span>✎</span> Dibujo y reconocimiento</div>
    <div class="nav-item" data-target="card-2"><span>◉</span> Sensores y simulación</div>
    <div class="nav-item" data-target="card-5"><span>⌘</span> Herramientas tecnológicas</div>
    <div class="nav-item" data-target="card-7"><span>↗</span> Repositorios y proyectos</div>
    <div class="nav-item" data-target="reflexiones"><span>✧</span> Reflexiones</div>

    <div class="pf-foot">Voz · Gesto · Tacto · Imagen · Sonido</div>
</div>
"""

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
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 2.2rem 1.8rem;
    align-items: start;
}

.polaroid-card {
    min-width: 0;
    align-self: start;
    height: fit-content;
    position: relative;
    isolation: isolate;
    padding: 16px 16px 20px;
    border: 2px solid #dcd0be;
    border-radius: 14px;
    background: linear-gradient(145deg, #fffaf0, #f2e4cf);
    box-shadow: 0 10px 22px rgba(56, 37, 29, .1);
    transition: transform .35s cubic-bezier(.2, .8, .2, 1),
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
                    <div class="w-full h-48 md:h-52 bg-[#e2d1b8] rounded overflow-hidden">
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

    <section class="mb-8">
        <div class="font-mono-custom text-xs tracking-widest text-[#8d5b3d] uppercase mb-1">
            Galería de procesos · 01—07
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
// La variable aprendizaje se conserva.
// ============================================================

const actividades = [
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
    return `
        <div class="polaroid-img-wrapper">
            <img src="${FOTO}"
                 alt="${item.titulo}"
                 class="polaroid-img"
                 onerror="this.onerror=null;this.parentElement.innerHTML='<div class=\\'img-fallback\\'><span class=\\'text-3xl\\'>✦</span><strong class=\\'text-sm mt-1\\'>Fotografía ${item.id}</strong><small class=\\'text-[11px]\\'>Simon.jpeg</small></div>';">
        </div>
    `;
}

function crearContenido(item,index) {
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

            <div class="bg-[#f5e9d6] p-3 rounded-lg border border-[#e2d0b5]">
                <strong class="text-[#38251d] block mb-0.5">
                    Lo que aprendí:
                </strong>
                ${item.aprendizaje}
            </div>
        </div>
    `;
}

function crearBotones(item) {
    return `
        <button type="button"
                onclick="toggleExpand(${item.id})"
                class="btn-vintage btn-read-more">
            <span id="btn-text-${item.id}">Leer más</span>
        </button>

        <a href="${item.url}"
           target="_blank"
           rel="noopener noreferrer"
           class="btn-vintage btn-link">
            ↗ ${item.botonTexto}
        </a>
    `;
}

function renderCards() {
    const container=document.getElementById('cardsContainer');
    container.innerHTML='';

    actividades.forEach((item,index)=>{
        const card=document.createElement('article');
        const esUltima=item.id===7;

        card.className='polaroid-card reveal';

        if (esUltima) {
            card.classList.add('polaroid-card-wide');

            // Actividad 7: foto izquierda; contenido y botones derecha.
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

    fitFrame();
}


// ============================================================
// BOTÓN LEER MÁS / VER MENOS
// ============================================================

function toggleExpand(id) {
    const content = document.getElementById(`expand-${id}`);
    const btnText = document.getElementById(`btn-text-${id}`);

    if (!content || !btnText) return;

    const isOpen = content.classList.contains('open');

    content.classList.toggle('open', !isOpen);
    btnText.textContent = isOpen ? 'Leer más' : 'Ver menos';

    requestAnimationFrame(() => {
        fitFrame();
        requestAnimationFrame(fitFrame);
    });

    setTimeout(fitFrame, 200);
    setTimeout(fitFrame, 500);
}


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

EXTENSIONES={".jpg",".jpeg",".png",".webp",".gif"}


def buscar_imagen(nombre):
    """Busca la imagen junto a app.py, sin distinguir mayúsculas."""
    carpeta=Path(__file__).parent

    archivos=[
        f for f in carpeta.iterdir()
        if f.is_file() and f.suffix.lower() in EXTENSIONES
    ]
import base64
import html
import mimetypes
import re
from pathlib import Path
from urllib.parse import urlparse

import streamlit as st

# ==========================================================
# PORTAFOLIO II — INTERFACES MULTIMODALES & SISTEMAS CIBERFÍSICOS
# ==========================================================

st.set_page_config(
    page_title="Portafolio II | Interfaces Multimodales",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# CONFIGURACIÓN Y DIRECTORIO DE ARCHIVOS
# ==========================================================

CARPETA = Path(__file__).resolve().parent
FOTO = "Blanco.jpg"


# ==========================================================
# FUNCIONES AUXILIARES (CON BÚSQUEDA INTELIGENTE DE IMÁGENES)
# ==========================================================

def esc(texto):
    """Evita que los textos introducidos rompan el HTML."""
    return html.escape(str(texto), quote=True)


def buscar_imagen(nombre):
    """Busca de forma flexible la imagen en el directorio."""
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
    """Reemplaza dinámicamente las rutas de imágenes en el HTML por Base64."""
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


def cargar_foto(nombre, clase):
    """Carga la foto principal de la portada de forma integrada."""
    ruta = buscar_imagen(nombre)

    if ruta and ruta.is_file():
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

hero_html = f"""
<section class="hero">
    <div class="hero-grid">
        <div class="portrait-frame">
            {foto_portada}
            <div class="caption">PORTAFOLIO II · IoT & CIBERFÍSICOS</div>
        </div>
        <div>
            <div class="eyebrow">Cuaderno digital · Semestre II · Edición 02</div>
            <h1>Interfaces<br><em>multimodales.</em></h1>
            <div class="hero-copy">
                Bienvenido a mi archivo de experimentación. Este espacio documenta la convergencia entre 
                el mundo digital y el entorno físico a través de <strong>Sistemas Ciberfísicos e Internet de las Cosas (IoT)</strong>. 
                Mediante protocolos de comunicación como MQTT, simulaciones interactivas en Wokwi y control por voz, 
                exploro cómo integrar actuadores, iluminación y servomotores en espacios inteligentes.
            </div>
            <div class="tags">
                <span class="tag">🌐 Protocolo MQTT</span>
                <span class="tag">⚡ Wokwi Simulación</span>
                <span class="tag">🎙️ Control por Voz</span>
                <span class="tag">🤖 Sistemas Ciberfísicos</span>
            </div>
        </div>
    </div>
</section>
"""

st.markdown(incrustar_imagenes(hero_html), unsafe_allow_html=True)


# ==========================================================
# BARRA LATERAL
# ==========================================================

with st.sidebar:
    st.markdown("# Archivo creativo")
    st.markdown("**PORTAFOLIO · ETAPA CIBERFÍSICA**")
    st.write("Recopilación de aplicaciones desplegadas y simulaciones virtuales de IoT.")
    st.markdown("---")
    st.markdown("### Contenido del Cuaderno")
    st.markdown("""
    - 📡 Recepción de Datos MQTT
    - 🕹️ Telecontrol Web & Actuadores
    - 🎙️ Control Multimodal por Voz
    - ⚙️ Simulación Wokwi (Servos y LEDs)
    - 📖 Documentación & Repositorios
    """)
    st.markdown("---")
    st.caption("Interfaces Multimodales · Desarrollado en Streamlit.")


# ==========================================================
# LÍNEA DIVISORIA ESTÉTICA Y TÍTULO
# ==========================================================

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    <div class="eyebrow">Galería de procesos · 01—08</div>
    <h2>Actividades prácticas realizadas</h2>
    <p>Pasa el cursor sobre las tarjetas tipo Polaroid para ver la animación y abre los enlaces para probar las aplicaciones en vivo.</p>
</div>
""", unsafe_allow_html=True)


# ==========================================================
# DATOS DE LAS 8 ACTIVIDADES
# ==========================================================

actividades = [
    {
        "titulo": "Recepción de Datos MQTT",
        "categoria": "IoT & Telemetría · 01",
        "resumen": "Monitoreo en tiempo real de telemetría desde un sensor analógico simulado en Wokwi hacia la app en Streamlit.",
        "descripcion": "Se organizó bajo la arquitectura cliente-broker: Wokwi actúa como cliente publicador enviando datos de un sensor a un broker MQTT en un tópico específico, mientras Streamlit funciona como cliente suscriptor leyendo ese mismo tópico.",
        "aprendizaje": "Entendí el patrón Publish/Subscribe, la intermediación del broker y la recepción continua de telemetría en un cliente web.",
        "url": "https://recepmqtt-c632mej72ce2uypzr9henl.streamlit.app/",
        "boton": "Abrir recurso"
    },
    {
        "titulo": "Publicación y Telecontrol MQTT",
        "categoria": "Ciberfísicos · 02",
        "resumen": "Telecontrol bidireccional desde la interfaz web para activar LEDs y un servomotor en el simulador Wokwi.",
        "descripcion": "La app en Streamlit funciona como cliente publicador enviando instrucciones a un tópico del broker MQTT. El microcontrolador en Wokwi actúa como cliente suscriptor en ese tópico para accionar luces y el servomotor en tiempo real.",
        "aprendizaje": "Aprendí a estructurar payload de control web y enviarlo a través de un broker MQTT hacia actuadores remotos.",
        "url": "https://sendcmqttsimon-5e3raacaadr2kz3jago5z9.streamlit.app/",
        "boton": "Abrir recurso"
    },
    {
        "titulo": "Control Multimodal por Voz",
        "categoria": "Voz & Actuadores · 03",
        "resumen": "Control de luces y puertas mediante comandos vocales procesados en la web y transmitidos al simulador.",
        "descripcion": "Un cliente web captura y traduce órdenes de voz en variables que se publican al broker MQTT dentro de un tópico de control. En Wokwi, el cliente suscriptor recibe la indicación y ejecuta la acción en el servomotor o LEDs.",
        "aprendizaje": "A integrar voz como entrada multimodal y mapear frases con comandos transmitidos por un broker MQTT.",
        "url": "https://ctrlvoicesimon-skzxvxkj3e8l323ky3i5bp.streamlit.app/",
        "boton": "Abrir recurso"
    },
    {
        "titulo": "Simulación Wokwi & Servomotor",
        "categoria": "Hardware · 04",
        "resumen": "Configuración del circuito electrónico y lógica del microcontrolador para señales analógicas.",
        "descripcion": "Montaje en el entorno de desarrollo Wokwi conectando sensores analógicos y servos en ESP32/Arduino, verificando la respuesta de los componentes antes del despliegue físico.",
        "aprendizaje": "Prototipado rápido de circuitos virtuales, programación de servomotores y depuración de señales analógicas.",
        "url": "",
        "boton": "Abrir recurso"
    },
    {
        "titulo": "Actividad práctica cinco",
        "categoria": "Práctica · 05",
        "resumen": "Espacio reservado para la quinta actividad del semestre.",
        "descripcion": "Descripción provisional de la actividad práctica desarrollada en clase.",
        "aprendizaje": "Reflexión y conceptos clave aprendidos durante la sesión.",
        "url": "",
        "boton": "Abrir recurso"
    },
    {
        "titulo": "Actividad práctica seis",
        "categoria": "Práctica · 06",
        "resumen": "Espacio reservado para la sexta actividad del semestre.",
        "descripcion": "Descripción provisional de la actividad práctica desarrollada en clase.",
        "aprendizaje": "Reflexión y conceptos clave aprendidos durante la sesión.",
        "url": "",
        "boton": "Abrir recurso"
    },
    {
        "titulo": "Actividad práctica siete",
        "categoria": "Práctica · 07",
        "resumen": "Espacio reservado para la séptima actividad del semestre.",
        "descripcion": "Descripción provisional de la actividad práctica desarrollada en clase.",
        "aprendizaje": "Reflexión y conceptos clave aprendidos durante la sesión.",
        "url": "",
        "boton": "Abrir recurso"
    },
    {
        "titulo": "Actividad práctica ocho",
        "categoria": "Proyecto Final · 08",
        "resumen": "Integración total del portafolio e interfaces multimodales.",
        "descripcion": "Consolidación de proyectos del semestre y presentación del portafolio integrando IoT y control por voz.",
        "aprendizaje": "Despliegue continuo en GitHub y Streamlit Cloud.",
        "url": "",
        "boton": "Abrir recurso"
    },
]


# ==========================================================
# FUNCIÓN PARA CREAR CADA TARJETA
# ==========================================================

def tarjeta(actividad, numero):
    foto = cargar_foto(FOTO, "polaroid")
    boton = crear_enlace(actividad["url"], actividad["boton"])

    card_html = f"""
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
    return incrustar_imagenes(card_html)


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
    ✦ <strong>Interfaces Multimodales & IoT:</strong> Código listo para sincronizar con GitHub y desplegar en Streamlit Cloud.
</div>
""", unsafe_allow_html=True)
# El iframe ajusta su altura al contenido mediante JavaScript.
components.html(HTML,height=3000,scrolling=False)
