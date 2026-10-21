import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Portafolio II | Interfaces Multimodales", layout="wide")

# Quita márgenes y cabecera de Streamlit
st.markdown(
    """
    <style>
      header, footer, #MainMenu {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HTML DEL PORTAFOLIO
# Para editar actividades: busca "const actividades" más abajo.
# ============================================================
HTML = r"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portafolio II | Interfaces Multimodales</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,400;0,500;1,400&family=DM+Sans:ital,opsz,wght@0,9..40,400..700;1,9..40,400..700&family=Playfair+Display:ital,wght@0,400..800;1,400..800&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>

    <style>
        :root {
            --dark-coffee: #38251d;
            --coffee: #65442f;
            --brown-accent: #916a49;
            --beige-dark: #d5bea0;
            --beige-light: #ead7bb;
            --cream-bg: #fff8ec;
            --cream-card: #fffaf0;
            --ink-text: #402d21;
            --terracotta: #a8583b;
        }

        body {
            background:
                radial-gradient(ellipse at 10% 10%, #fff9e9, transparent 40%),
                linear-gradient(135deg, #e4ceb0, #f6ead7 50%, #dfc4a0);
            font-family: 'DM Sans', sans-serif;
            color: var(--ink-text);
            min-height: 100vh;
        }

        h1, h2, h3, .font-serif-custom {
            font-family: 'Playfair Display', serif;
            color: var(--dark-coffee);
        }

        .font-mono-custom { font-family: 'DM Mono', monospace; }

        .sidebar {
            background: linear-gradient(170deg, #493025, #302019);
            color: #f8e9d2;
        }

        .vintage-divider {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, #98704e 20%, #e0c49e 50%, #98704e 80%, transparent);
            margin: 2.5rem 0;
        }

        .hero-box {
            background: linear-gradient(125deg, #fff9ed, #ead6b8);
            border: 1px solid #d2b99a;
            box-shadow: 0 18px 42px rgba(87, 58, 38, 0.12);
        }

        .portrait-frame {
            background: #fffaf0;
            box-shadow: 8px 12px 0 rgba(105, 72, 43, 0.12), 0 15px 30px rgba(64, 41, 25, 0.15);
            transform: rotate(-2.5deg);
            transition: transform 0.4s ease;
        }
        .portrait-frame:hover { transform: rotate(0deg) scale(1.02); }

        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 2.5rem;
            align-items: start;
        }
        @media (max-width: 868px) {
            .gallery-grid { grid-template-columns: 1fr; gap: 1.8rem; }
        }

        .polaroid-card {
            background: linear-gradient(145deg, #fffaf0, #f2e4cf);
            border: 2px solid #dcd0be;
            border-radius: 14px;
            padding: 16px 16px 20px;
            box-shadow: 0 10px 22px rgba(56, 37, 29, 0.1);
            transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1),
                        border-color 0.35s ease,
                        box-shadow 0.35s ease,
                        background-color 0.35s ease;
            position: relative;
            isolation: isolate;
        }
        .polaroid-card:nth-child(2n+1) { transform: rotate(-0.5deg); }
        .polaroid-card:nth-child(2n) { transform: rotate(0.5deg); }

        .polaroid-card:hover,
        .polaroid-card:focus-within {
            z-index: 20;
            transform: translateY(-8px) scale(1.035) rotate(0deg) !important;
            border-color: #65442f !important;
            background: #ffffff;
            box-shadow: 0 24px 40px rgba(56, 37, 29, 0.22), 0 0 0 3px rgba(101, 68, 47, 0.25);
        }

        .polaroid-img-wrapper {
            width: 100%;
            height: 250px;
            overflow: hidden;
            border-radius: 8px;
            border: 1px solid rgba(101, 68, 47, 0.15);
            background-color: #e8d7c1;
            position: relative;
        }
        .polaroid-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: grayscale(0.85) contrast(0.95);
            transition: filter 0.4s ease, transform 0.4s ease;
        }
        .polaroid-card:hover .polaroid-img {
            filter: grayscale(0.15) contrast(1);
            transform: scale(1.03);
        }

        .btn-vintage {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 600;
            transition: all 0.25s ease;
            cursor: pointer;
            user-select: none;
        }
        .btn-read-more { background-color: #ebd8bf; color: #523724; border: 1px solid #c5aa8a; }
        .btn-read-more:hover { background-color: #dfc3a1; color: #38251d; }
        .btn-link { background-color: #65442f; color: #fff8ec; border: 1px solid #4a3121; }
        .btn-link:hover { background-color: #38251d; color: #ffffff; box-shadow: 0 4px 10px rgba(56, 37, 29, 0.25); }

        .expandable-content {
            max-height: 0;
            overflow: hidden;
            opacity: 0;
            transition: max-height 0.4s cubic-bezier(0, 1, 0, 1), opacity 0.3s ease, margin-top 0.3s ease;
        }
        .expandable-content.open {
            max-height: 400px;
            opacity: 1;
            margin-top: 14px;
            transition: max-height 0.5s cubic-bezier(1, 0, 1, 0), opacity 0.4s ease, margin-top 0.3s ease;
        }

        .img-fallback {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 100%;
            background: repeating-linear-gradient(45deg, #f2e2cb, #f2e2cb 10px, #ead7bb 10px, #ead7bb 12px);
            color: #725942;
            text-align: center;
        }

        /* ============ TOQUES EXTRA ============ */
        html { scroll-behavior: smooth; }

        /* Textura de papel (grano) sobre toda la página */
        body::after {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 90;
            opacity: .16;
            mix-blend-mode: multiply;
            background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .3 0 0 0 0 .2 0 0 0 0 .12 0 0 0 .9 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
        }

        /* Barra de progreso de lectura */
        #progress {
            position: fixed; top: 0; left: 0; height: 4px; width: 0;
            background: linear-gradient(90deg, #a8583b, #d9a441, #e8c27a);
            box-shadow: 0 0 10px rgba(217,164,65,.7);
            z-index: 100; transition: width .1s linear;
        }

        /* Chispitas ✦ que salen del borde */
        .sparkle {
            position: absolute; pointer-events: none; z-index: 40; line-height: 1;
            text-shadow: 0 0 6px rgba(232,194,122,.9);
            animation: sparkle .95s ease-out forwards;
        }
        @keyframes sparkle {
            0%   { opacity: 0; transform: translate(-50%,-50%) scale(.2) rotate(0deg); }
            25%  { opacity: 1; }
            100% { opacity: 0; transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) scale(1.1) rotate(200deg); }
        }

        /* Aparición suave al hacer scroll */
        .reveal:not(.in) { opacity: 0; }
        .reveal.in { animation: reveal .8s cubic-bezier(.2,.8,.2,1) backwards; }
        @keyframes reveal { from { opacity: 0; translate: 0 38px; } }

        /* Cinta washi (cinta adhesiva) en polaroids */
        .portrait-frame { position: relative; }
        .polaroid-card::before, .washi {
            content: ''; position: absolute; top: -12px; left: 50%;
            width: 96px; height: 26px; margin-left: -48px; z-index: 3;
            background: repeating-linear-gradient(90deg, rgba(213,190,160,.75) 0 8px, rgba(240,224,198,.75) 8px 16px);
            border: 1px dashed rgba(145,106,73,.35);
            box-shadow: 0 2px 5px rgba(56,37,29,.15);
            transform: rotate(-3deg);
            transition: transform .35s ease;
        }
        .washi { content: none; }
        .polaroid-card:nth-child(2n)::before { transform: rotate(3deg); }
        .polaroid-card:hover::before { transform: rotate(0deg) translateY(-3px); }

        /* Brillo que cruza la foto + resplandor dorado en la card */
        .polaroid-img-wrapper::after {
            content: ''; position: absolute; inset: 0; pointer-events: none;
            background: linear-gradient(115deg, transparent 35%, rgba(255,248,230,.6) 50%, transparent 65%);
            transform: translateX(-130%); transition: transform .9s ease;
        }
        .polaroid-card:hover .polaroid-img-wrapper::after { transform: translateX(130%); }
        .polaroid-card:hover {
            box-shadow: 0 24px 40px rgba(56,37,29,.22), 0 0 0 3px rgba(101,68,47,.25), 0 0 34px rgba(217,164,65,.4);
        }

        /* Título con subrayado que se dibuja */
        .polaroid-card h3 {
            background: linear-gradient(var(--terracotta), var(--terracotta)) 0 100% / 0% 2px no-repeat;
            transition: background-size .5s ease; width: fit-content; padding-bottom: 2px;
        }
        .polaroid-card:hover h3 { background-size: 100% 2px; }

        /* Número que gira */
        .num-badge { transition: transform .6s cubic-bezier(.2,.8,.2,1), background-color .3s, color .3s; }
        .polaroid-card:hover .num-badge {
            transform: rotate(360deg) scale(1.15);
            background-color: #a8583b !important; color: #fff8ec !important; border-color: #a8583b !important;
        }

        /* Palabra "multimodales." con brillo dorado en movimiento */
        .shimmer-text {
            display: inline-block; padding: 0 .1em .12em 0;
            background: linear-gradient(100deg, #8d5b3d 20%, #d9a441 45%, #a8583b 55%, #8d5b3d 80%);
            background-size: 200% auto;
            -webkit-background-clip: text; background-clip: text;
            -webkit-text-fill-color: transparent; color: transparent;
            animation: shimmer 5s linear infinite;
        }
        @keyframes shimmer { to { background-position: -200% center; } }

        /* Estrellas flotantes en el hero */
        .float-star {
            position: absolute; pointer-events: none; color: #c99a5b; opacity: .75;
            animation: floaty 7s ease-in-out infinite;
        }
        @keyframes floaty {
            0%,100% { transform: translateY(0) rotate(0deg) scale(1); opacity: .45; }
            50%     { transform: translateY(-14px) rotate(25deg) scale(1.2); opacity: .95; }
        }

        /* Cinta animada (ticker) */
        .ticker-wrap { overflow: hidden; padding: .8rem 0; }
        .ticker {
            overflow: hidden; background: var(--dark-coffee); color: #e8d5bf;
            border-top: 2px solid #916a49; border-bottom: 2px solid #916a49;
            transform: rotate(-1deg); box-shadow: 0 8px 18px rgba(56,37,29,.25);
        }
        .ticker-track { display: flex; width: max-content; animation: marquee 30s linear infinite; }
        .ticker-track span {
            font-family: 'DM Mono', monospace; font-size: .78rem; letter-spacing: .25em;
            text-transform: uppercase; padding: .75rem 1.4rem; white-space: nowrap;
        }
        .ticker-track span b { color: #d9a441; font-weight: 500; }
        @keyframes marquee { to { transform: translateX(-50%); } }

        /* Menú lateral con vida */
        .nav-item { transition: transform .25s ease, color .25s ease; }
        .nav-item:hover { transform: translateX(7px); color: #fff; }
        .nav-item span { display: inline-block; transition: transform .4s ease, color .3s; }
        .nav-item:hover span { transform: rotate(180deg) scale(1.35); color: #e8c27a; }

        /* Estrellitas a los extremos del título */
        .title-star {
            display: inline-block; color: #65442f; font-size: .42em;
            vertical-align: middle; margin: 0 .5em 0 0;
            animation: twinkle 3.2s ease-in-out infinite;
        }
        .title-star.end { margin: 0 0 0 .35em; animation-delay: -1.6s; }
        @keyframes twinkle {
            0%,100% { transform: scale(1) rotate(0deg); opacity: .95; }
            50%     { transform: scale(1.4) rotate(90deg); opacity: .55; }
        }

        /* Tarjeta de reflexión sobre multimodalidad */
        .modal-note {
            background: linear-gradient(135deg, #fffaf0, #f2e4cf);
            border: 1px solid #d2b895; border-radius: 16px;
            box-shadow: 0 10px 24px rgba(56,37,29,.1);
        }
        .channel-chip {
            display: inline-flex; align-items: center; gap: .4rem;
            padding: .35rem .8rem; border-radius: 999px;
            background: #fff9ef; border: 1px solid #cdb393; color: #694a32;
            font-family: 'DM Mono', monospace; font-size: .75rem;
            transition: transform .25s ease, background-color .25s ease, color .25s ease;
        }
        .channel-chip:hover { transform: translateY(-3px) rotate(-2deg); background: #65442f; color: #fff8ec; }

        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after { animation: none !important; transition: none !important; }
            .reveal:not(.in) { opacity: 1; }
        }
    </style>
</head>
<body class="flex flex-col md:flex-row min-h-screen">
    <div id="progress"></div>

    <!-- SIDEBAR -->
    <aside class="sidebar w-full md:w-72 p-6 flex-shrink-0 flex flex-col justify-between border-r border-[#65442f]/30 md:sticky md:top-0 md:h-screen md:self-start md:overflow-y-auto">
        <div>
            <div class="mb-8">
                <h1 class="text-2xl font-bold text-[#f8e9d2] mb-1 font-serif-custom" style="color:#f8e9d2">Archivo Creativo</h1>
                <p class="font-mono-custom text-xs tracking-wider text-[#d5bea0] uppercase">Portafolio · Segunda Etapa</p>
            </div>
            <p class="text-sm text-[#dfc8ae] leading-relaxed mb-6 font-sans">
                Una colección de experimentos donde la voz, el gesto, el tacto y la imagen se combinan para crear formas más naturales de dialogar con la tecnología.
            </p>
            <div class="vintage-divider my-4"></div>
            <div class="space-y-3">
                <h3 class="font-serif-custom text-lg text-[#f8e9d2] mb-2" style="color:#f8e9d2">Dentro del cuaderno</h3>
                <ul class="space-y-2 text-sm text-[#e8d5bf] font-sans">
                    <li data-target="card-1" class="nav-item flex items-center gap-2 cursor-pointer"><span class="text-[#c7a47e]">✎</span> Dibujo y reconocimiento</li>
                    <li data-target="card-2" class="nav-item flex items-center gap-2 cursor-pointer"><span class="text-[#c7a47e]">◉</span> Sensores y simulación</li>
                    <li data-target="card-5" class="nav-item flex items-center gap-2 cursor-pointer"><span class="text-[#c7a47e]">⌘</span> Herramientas tecnológicas</li>
                    <li data-target="card-8" class="nav-item flex items-center gap-2 cursor-pointer"><span class="text-[#c7a47e]">↗</span> Repositorios y proyectos</li>
                    <li data-target="reflexiones" class="nav-item flex items-center gap-2 cursor-pointer"><span class="text-[#c7a47e]">✧</span> Reflexiones</li>
                </ul>
            </div>
        </div>
        <div class="mt-8 pt-4 border-t border-[#65442f]/40 font-mono-custom text-xs text-[#b89c7d]">
            Voz · Gesto · Tacto · Imagen · Sonido
        </div>
    </aside>

    <!-- CONTENIDO PRINCIPAL -->
    <main class="flex-1 p-4 md:p-10 max-w-[1600px] mx-auto w-full transition-all duration-300">

        <!-- HERO -->
        <section class="hero-box rounded-2xl p-6 md:p-8 relative mb-8">
            <span class="float-star" style="top:10px;right:28px;font-size:28px">✦</span>
            <span class="float-star" style="bottom:18px;right:46%;font-size:18px;animation-delay:-2s">✧</span>
            <span class="float-star" style="top:46%;left:-12px;font-size:22px;animation-delay:-4s">✦</span>
            <span class="float-star" style="bottom:10px;right:20px;font-size:24px;animation-delay:-1s">✶</span>
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                <div class="lg:col-span-4 flex justify-center lg:justify-start">
                    <div class="portrait-frame p-3 pb-4 max-w-[320px] w-full rounded-sm">
                        <div class="washi"></div>
                        <div class="w-full h-48 md:h-52 bg-[#e2d1b8] rounded overflow-hidden">
                            <img src="blanco.jpeg"
                                 onerror="this.onerror=null; this.parentElement.innerHTML='<div class=\'img-fallback\'><span class=\'text-2xl\'>✦</span><strong class=\'text-xs mt-1\'>Fotografía de prueba</strong><small class=\'text-[10px] opacity-75 font-mono-custom\'>blanco.jpeg</small></div>';"
                                 alt="Fotografía de portada"
                                 class="w-full h-full object-cover filter grayscale contrast-95">
                        </div>
                        <div class="text-center mt-3 font-mono-custom text-xs text-[#79583e] tracking-wider uppercase font-semibold">
                            TU NOMBRE · PORTAFOLIO II
                        </div>
                    </div>
                </div>

                <div class="lg:col-span-8 space-y-4">
                    <div class="font-mono-custom text-xs tracking-widest text-[#8d5b3d] uppercase">
                        Cuaderno digital · Semestre II · Edición 02
                    </div>
                    <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold leading-tight">
                        <span class="title-star">✦</span>Interfaces<br>
                        <span class="italic shimmer-text">multimodales.</span><span class="title-star end">✦</span>
                    </h1>
                    <div class="text-base md:text-lg text-[#65442f] leading-relaxed max-w-3xl">
                        Hola, soy <strong>Tu Nombre Aquí</strong>. Este espacio reúne mis experiencias, experimentos y aprendizajes de la segunda parte del semestre.
                        <br><br>
                        Aprender haciendo, experimentar sin miedo y transformar ideas en experiencias interactivas y multimodales.
                    </div>
                    <div class="flex flex-wrap gap-2 pt-2">
                        <span class="px-3 py-1 bg-[#fff9ef] border border-[#cdb393] rounded-full text-xs font-mono-custom text-[#694a32]">✳ Diseño interactivo</span>
                        <span class="px-3 py-1 bg-[#fff9ef] border border-[#cdb393] rounded-full text-xs font-mono-custom text-[#694a32]">⌘ Experimentación</span>
                        <span class="px-3 py-1 bg-[#fff9ef] border border-[#cdb393] rounded-full text-xs font-mono-custom text-[#694a32]">↗ Aprender haciendo</span>
                        <span class="px-3 py-1 bg-[#fff9ef] border border-[#cdb393] rounded-full text-xs font-mono-custom text-[#694a32]">☕ Edición vintage</span>
                    </div>
                </div>
            </div>
        </section>

        <div class="ticker-wrap" aria-hidden="true">
            <div class="ticker"><div class="ticker-track"><span>Diseño interactivo <b>✦</b></span><span>Experimentación <b>✦</b></span><span>Aprender haciendo <b>✦</b></span><span>Edición vintage <b>✦</b></span><span>Interfaces multimodales <b>✦</b></span><span>Curiosidad y café <b>✦</b></span><span>Diseño interactivo <b>✦</b></span><span>Experimentación <b>✦</b></span><span>Aprender haciendo <b>✦</b></span><span>Edición vintage <b>✦</b></span><span>Interfaces multimodales <b>✦</b></span><span>Curiosidad y café <b>✦</b></span></div></div>
        </div>
        <hr class="vintage-divider">

        <div class="mb-8">
            <div class="font-mono-custom text-xs tracking-widest text-[#8d5b3d] uppercase mb-1">Galería de procesos · 01—08</div>
            <h2 class="text-3xl md:text-4xl font-bold text-[#38251d]">Actividades prácticas realizadas</h2>
            <p class="text-sm text-[#725942] mt-2">
                Cada tarjeta es un experimento: una manera distinta de combinar sentidos y canales para que las personas interactúen con la tecnología.
            </p>
        </div>

        <div class="gallery-grid" id="cardsContainer"></div>

        <div id="reflexiones" class="modal-note mt-12 p-6 md:p-8">
            <div class="font-mono-custom text-xs tracking-widest text-[#8d5b3d] uppercase mb-2">Reflexión · Multimodalidad</div>
            <h3 class="font-serif-custom text-2xl md:text-3xl font-bold mb-3">Hablar con la tecnología con todos los sentidos</h3>
            <p class="text-[#65442f] leading-relaxed max-w-3xl mb-4">
                Una interfaz multimodal no depende de un solo canal: permite tocar, hablar, señalar, mirar o escuchar, y elegir en cada momento la forma más natural de comunicarse. Diseñar así es pensar en las personas, en sus contextos y en sus capacidades, para que la tecnología se adapte a ellas y no al revés.
            </p>
            <div class="flex flex-wrap gap-2">
                <span class="channel-chip">✋ Tacto</span>
                <span class="channel-chip">🎙 Voz</span>
                <span class="channel-chip">👁 Visión</span>
                <span class="channel-chip">☝ Gesto</span>
                <span class="channel-chip">🔊 Sonido</span>
            </div>
        </div>

        <footer class="mt-10 mb-6 text-center text-xs font-mono-custom text-[#80654d] tracking-widest uppercase">
            Fin de la página, no del proceso · Diseñado con curiosidad
        </footer>
    </main>

    <script>
        // ============================================================
        // EDITA AQUÍ: cambia titulo, resumen, descripcion, aprendizaje y url
        // de cada actividad cuando tengas tus contenidos reales.
        // ============================================================
        const actividades = [
            { id: 1, titulo: "Actividad 01: Reconocimiento Interactivo", categoria: "Práctica · 01",
              resumen: "Experimentación con lienzo digital y detección de patrones de dibujo libre.",
              descripcion: "En esta actividad se desarrolló una interfaz interactiva capaz de procesar trazos de dibujo en tiempo real. Se evaluaron respuestas visuales y retroalimentación auditiva suave al usuario.",
              aprendizaje: "Lógica de captura de coordenadas en Canvas y optimización de eventos de ratón.",
              url: "https://github.com", botonTexto: "Abrir recurso" },
            { id: 2, titulo: "Actividad 02: Simulación Multimodal", categoria: "Experimentación · 02",
              resumen: "Visualización de entrada de datos continuos simulando sensores de movimiento.",
              descripcion: "Implementación de dashboards de monitoreo con estética analógica donde los valores varían suavemente generando gráficos de respuesta rápida.",
              aprendizaje: "Manejo de estado asíncrono y mapeo de variables continuas.",
              url: "https://github.com", botonTexto: "Abrir recurso" },
            { id: 3, titulo: "Actividad 03: Interfaces Accesibles", categoria: "Interfaz · 03",
              resumen: "Integración de componentes de interacción por voz e imagen en una sola vista.",
              descripcion: "Exploración de prototipos centrados en la accesibilidad multimodal, permitiendo alternar entre interacción táctil y comandos de audio.",
              aprendizaje: "Diseño inclusivo y jerarquización de canales de entrada.",
              url: "https://github.com", botonTexto: "Abrir recurso" },
            { id: 4, titulo: "Actividad 04: Renderizado Espacial 3D", categoria: "Simulación · 04",
              resumen: "Pruebas de renderizado y manipulación de objetos tridimensionales.",
              descripcion: "Uso de canvas para construir un entorno miniatura interactivo con respuestas de iluminación física simulada.",
              aprendizaje: "Control de cámaras interactivas y transformaciones espaciales.",
              url: "https://github.com", botonTexto: "Abrir recurso" },
            { id: 5, titulo: "Actividad 05: Procesamiento de Imagen", categoria: "Tecnología · 05",
              resumen: "Procesamiento en blanco y negro para clasificación de bordes visuales.",
              descripcion: "Desarrollo de un flujo de análisis de imágenes que detecta contornos y contrastes, transformando lo que se ve en información que la interfaz puede interpretar.",
              aprendizaje: "Filtros de imagen mediante CSS/Canvas y matriz de convolución.",
              url: "https://github.com", botonTexto: "Abrir recurso" },
            { id: 6, titulo: "Actividad 06: Ergonomía y Estética Vintage", categoria: "Aprendizaje · 06",
              resumen: "Análisis de la estética retro y la ergonomía visual en la web moderna.",
              descripcion: "Documentación sobre cómo la paleta de tonos cálidos (café, crema, beige) genera mayor descanso visual y una experiencia de usuario nostálgica.",
              aprendizaje: "Armonía de color y tipografía de contraste Serif / Sans-Serif.",
              url: "https://github.com", botonTexto: "Abrir recurso" },
            { id: 7, titulo: "Actividad 07: Prototipado Físico y Sensores", categoria: "Hardware · 07",
              resumen: "Conexión de señales analógicas para manipular la interfaz gráfica.",
              descripcion: "Pruebas de comunicación serial recibiendo datos externos para transformar la opacidad y los tonos de la paleta en tiempo real.",
              aprendizaje: "Manejo de Web Serial API y respuesta en bucle directo.",
              url: "https://github.com", botonTexto: "Abrir recurso" },
            { id: 8, titulo: "Actividad 08: Proyecto Integrador Final", categoria: "Proyecto · 08",
              resumen: "Síntesis de los módulos trabajados durante el semestre en un único entorno.",
              descripcion: "Unificación de todas las pruebas conceptuales y ejercicios de diseño en este portafolio multimodal de estética vintage.",
              aprendizaje: "Estructuración limpia de código web monolítico y usabilidad.",
              url: "https://github.com", botonTexto: "Abrir recurso" }
        ];

        const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        // ✦ Chispitas que salen del borde de un elemento al pasar el cursor
        function attachSparkles(el) {
            const glyphs = ['✦', '✧', '✶', '✦', '·'];
            const colors = ['#d9a441', '#a8583b', '#916a49', '#e8c27a', '#c99a5b'];
            let timer = null;

            function spawn() {
                const s = document.createElement('span');
                s.className = 'sparkle';
                s.textContent = glyphs[Math.floor(Math.random() * glyphs.length)];
                const side = Math.floor(Math.random() * 4);
                const t = Math.random() * 100;
                const far = 18 + Math.random() * 28;
                const drift = (Math.random() - 0.5) * 34;
                let x, y, dx, dy;
                if (side === 0)      { x = t;   y = 0;   dx = drift; dy = -far; }
                else if (side === 1) { x = 100; y = t;   dx = far;   dy = drift; }
                else if (side === 2) { x = t;   y = 100; dx = drift; dy = far; }
                else                 { x = 0;   y = t;   dx = -far;  dy = drift; }
                s.style.left = x + '%';
                s.style.top = y + '%';
                s.style.setProperty('--dx', dx + 'px');
                s.style.setProperty('--dy', dy + 'px');
                s.style.fontSize = (10 + Math.random() * 14) + 'px';
                s.style.color = colors[Math.floor(Math.random() * colors.length)];
                s.addEventListener('animationend', () => s.remove());
                el.appendChild(s);
            }

            el.addEventListener('mouseenter', () => {
                if (reduceMotion) return;
                for (let i = 0; i < 7; i++) setTimeout(spawn, i * 40);
                timer = setInterval(spawn, 110);
            });
            el.addEventListener('mouseleave', () => { clearInterval(timer); timer = null; });
        }

        // Aparición de las cards al hacer scroll
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(e => {
                if (e.isIntersecting) { e.target.classList.add('in'); revealObserver.unobserve(e.target); }
            });
        }, { threshold: 0.12 });

        // Ajusta la altura del iframe de Streamlit a la pantalla (así el menú lateral y la barra de progreso funcionan)
        function fitFrame() {
            try {
                if (window.frameElement) window.frameElement.style.height = window.parent.innerHeight + 'px';
            } catch (e) {}
        }

        function renderCards() {
            const container = document.getElementById('cardsContainer');
            container.innerHTML = '';

            actividades.forEach((item, index) => {
                const card = document.createElement('article');
                card.className = 'polaroid-card reveal flex flex-col justify-between';
                card.id = 'card-' + item.id;
                card.style.animationDelay = ((index % 2) * 0.12) + 's';

                card.innerHTML = `
                    <div>
                        <div class="polaroid-img-wrapper mb-4">
                            <img src="blanco.jpeg"
                                 onerror="this.onerror=null; this.parentElement.innerHTML='<div class=\\'img-fallback\\'><span class=\\'text-3xl\\'>✦</span><strong class=\\'text-sm mt-1\\'>Fotografía ${item.id}</strong><small class=\\'text-[11px] opacity-75 font-mono-custom\\'>blanco.jpeg</small></div>';"
                                 alt="${item.titulo}"
                                 class="polaroid-img">
                        </div>

                        <div class="flex justify-between items-center mb-2 font-mono-custom text-xs uppercase text-[#8d5b3d]">
                            <span>${item.categoria}</span>
                            <span class="num-badge w-7 h-7 rounded-full border border-[#d5b995] bg-[#f6e7d1] flex items-center justify-center font-bold text-xs">
                                ${String(index + 1).padStart(2, '0')}
                            </span>
                        </div>

                        <h3 class="font-serif-custom font-bold text-2xl leading-snug mb-2 text-[#38251d]">${item.titulo}</h3>
                        <p class="text-sm text-[#725942] leading-relaxed mb-3">${item.resumen}</p>

                        <div id="expand-${item.id}" class="expandable-content border-t border-[#e0ccb0] pt-3 text-xs md:text-sm text-[#614a37] space-y-2">
                            <p>${item.descripcion}</p>
                            <div class="bg-[#f5e9d6] p-3 rounded-lg border border-[#e2d0b5]">
                                <strong class="text-[#38251d] block mb-0.5">Lo que me llevo:</strong>
                                ${item.aprendizaje}
                            </div>
                        </div>
                    </div>

                    <div class="flex items-center justify-between gap-3 mt-5 pt-3 border-t border-[#ebd8bf]/70">
                        <button onclick="toggleExpand(${item.id})" class="btn-vintage btn-read-more">
                            <span id="btn-text-${item.id}">Leer más</span>
                        </button>
                        <a href="${item.url}" target="_blank" rel="noopener noreferrer" class="btn-vintage btn-link">
                            ↗ ${item.botonTexto}
                        </a>
                    </div>
                `;
                container.appendChild(card);
                attachSparkles(card);
                revealObserver.observe(card);
            });
        }

        function toggleExpand(id) {
            const content = document.getElementById(`expand-${id}`);
            const btnText = document.getElementById(`btn-text-${id}`);
            const isOpen = content.classList.contains('open');
            content.classList.toggle('open', !isOpen);
            btnText.textContent = isOpen ? "Leer más" : "Ver menos";
        }

        window.addEventListener('DOMContentLoaded', () => {
            renderCards();

            // Chispitas también en la foto de portada
            const portrait = document.querySelector('.portrait-frame');
            if (portrait) attachSparkles(portrait);

            // Menú lateral: desplazamiento suave a cada sección
            document.querySelectorAll('.nav-item').forEach(li => {
                li.addEventListener('click', () => {
                    const target = document.getElementById(li.dataset.target);
                    if (target) target.scrollIntoView({ behavior: 'smooth', block: 'center' });
                });
            });

            // Barra de progreso
            const bar = document.getElementById('progress');
            function updateProgress() {
                const max = document.documentElement.scrollHeight - window.innerHeight;
                bar.style.width = (max > 0 ? (window.scrollY / max) * 100 : 0) + '%';
            }
            window.addEventListener('scroll', updateProgress, { passive: true });
            updateProgress();

            fitFrame();
            window.addEventListener('resize', fitFrame);
            try { window.parent.addEventListener('resize', fitFrame); } catch (e) {}
        });
    </script>
</body>
</html>
"""

# Incrusta blanco.jpeg (debe estar en la misma carpeta que app.py).
# Si no existe, se muestra el recuadro de respaldo del diseño.
img = Path(__file__).parent / "blanco.jpeg"
if img.exists():
    b64 = base64.b64encode(img.read_bytes()).decode()
    HTML = HTML.replace('src="blanco.jpeg"', f'src="data:image/jpeg;base64,{b64}"')

components.html(HTML, height=900, scrolling=True)
