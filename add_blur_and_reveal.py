import re

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/funcionalidades.html', 'r') as f:
    content = f.read()

# 1. Inject the blur CSS
css_to_inject = """
        /* Vignette Blur Effect */
        .blur-overlay-top {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 12vh;
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            mask-image: linear-gradient(to bottom, black 0%, transparent 100%);
            -webkit-mask-image: linear-gradient(to bottom, black 0%, transparent 100%);
            z-index: 5;
            pointer-events: none;
        }
        .blur-overlay-bottom {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 12vh;
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            mask-image: linear-gradient(to top, black 0%, transparent 100%);
            -webkit-mask-image: linear-gradient(to top, black 0%, transparent 100%);
            z-index: 5;
            pointer-events: none;
        }
    </style>
"""
content = content.replace('</style>', css_to_inject)

# 2. Inject the blur HTML divs right after <body>
html_blur_divs = """<body class="bg-zinc-50 text-zinc-900 font-sans">
    <!-- Fisheye Blur Overlays -->
    <div class="blur-overlay-top"></div>
    <div class="blur-overlay-bottom"></div>
"""
content = content.replace('<body class="bg-zinc-50 text-zinc-900 font-sans">', html_blur_divs)

# 3. Update the GSAP script
old_gsap_script = """        // GSAP: Animação de entrada nas seções de funcionalidades
        gsap.utils.toArray('.feature-section').forEach(section => {
            gsap.from(section, {
                opacity: 0,
                y: 40,
                duration: 0.8,
                ease: 'power3.out',
                scrollTrigger: {
                    trigger: section,
                    start: 'top 85%',
                }
            });
        });"""

new_gsap_script = """        // GSAP: Animação de entrada nas seções de funcionalidades (Staggering em textos e cards)
        gsap.utils.toArray('.feature-section').forEach(section => {
            // Seleciona títulos, parágrafos, cards e grids dentro da seção
            const elements = section.querySelectorAll('h2, .mb-8 > p, .group, .bg-white, .bg-gradient-to-br, .bg-\\[\\#0B1A30\\]');
            
            // Filtramos para não animar elementos aninhados duas vezes
            const uniqueElements = Array.from(elements).filter(el => {
                // Remove elementos que já estão dentro de um .group ou .bg-white que está sendo animado
                return !el.parentElement.closest('.group, .bg-white, .bg-gradient-to-br, .bg-\\\\[\\\\#0B1A30\\\\]');
            });

            gsap.from(uniqueElements, {
                opacity: 0,
                y: 40,
                duration: 0.8,
                stagger: 0.15,
                ease: 'power3.out',
                scrollTrigger: {
                    trigger: section,
                    start: 'top 85%',
                }
            });
        });"""

if old_gsap_script in content:
    content = content.replace(old_gsap_script, new_gsap_script)
else:
    print("Could not find old gsap script exactly.")

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/funcionalidades.html', 'w') as f:
    f.write(content)

