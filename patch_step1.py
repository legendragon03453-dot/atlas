import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# --- Task 1: Background and Dynamic Padding ---
# Change body background-color from #367CF5 to #ffffff
content = content.replace('background-color: #367CF5; /* Cor de fundo base caso o vídeo falhe */', 'background-color: #ffffff; /* Cor de fundo branca para o efeito de borda */')

# Add dynamic border div right after <body>
dynamic_border_html = '\n    <!-- Border overlay animada -->\n    <div id="dynamic-border" class="fixed inset-0 pointer-events-none z-[9999] border-white transition-all duration-75" style="border-width: 0px;"></div>\n'
content = content.replace('<body>', f'<body>{dynamic_border_html}')

# Add GSAP logic for the border
gsap_script = """
        // GSAP: Animação de borda dinâmica
        gsap.to("#dynamic-border", {
            borderWidth: window.innerWidth < 768 ? "12px" : "24px",
            scrollTrigger: {
                trigger: "body",
                start: "top top",
                end: "300px top",
                scrub: 1
            }
        });
"""
content = content.replace('// GSAP: Animação de preenchimento da Timeline', gsap_script + '\n        // GSAP: Animação de preenchimento da Timeline')

# Remove padding from hero section just in case
# The hero container has no padding, but we ensure it's p-0
content = content.replace('class="hero-container"', 'class="hero-container p-0"')


# --- Task 2: Video Logic & Snowfall ---
# Remove loop from video, add id
content = content.replace('<video class="video-bg" autoplay loop muted playsinline>', '<video id="hero-video" class="video-bg" autoplay muted playsinline>')

# Add snowfall CSS
snowfall_css = """
        /* Snowfall effect */
        .snow-particle {
            position: absolute;
            top: -10px;
            background: white;
            border-radius: 50%;
            opacity: 0.8;
            animation: fall linear infinite;
        }
        @keyframes fall {
            0% { transform: translateY(-10px) translateX(0px); }
            100% { transform: translateY(100vh) translateX(20px); }
        }
"""
content = content.replace('</style>', f'{snowfall_css}\n    </style>')

# Add snowfall container
snowfall_html = """
        <!-- Snowfall effect (hidden initially) -->
        <div id="snowfall-container" class="absolute inset-0 pointer-events-none z-[-2] opacity-0 transition-opacity duration-1000"></div>
"""
content = content.replace('<div class="overlay-black"></div>', f'{snowfall_html}\n        <div class="overlay-black"></div>')

# Add JS for video logic
video_js = """
        // Lógica do Vídeo Hero
        const video = document.getElementById('hero-video');
        const snowfall = document.getElementById('snowfall-container');
        let playCount = 0;
        
        // Create snow particles
        for(let i=0; i<50; i++) {
            let p = document.createElement('div');
            p.className = 'snow-particle';
            p.style.left = Math.random() * 100 + 'vw';
            p.style.width = p.style.height = (Math.random() * 4 + 2) + 'px';
            p.style.animationDuration = (Math.random() * 3 + 2) + 's';
            p.style.animationDelay = (Math.random() * 5) + 's';
            snowfall.appendChild(p);
        }

        if (video) {
            video.addEventListener('ended', () => {
                playCount++;
                if(playCount === 1) {
                    // Dar reload e remover as bordas
                    video.style.transform = 'scale(1.35)'; // Escala para cortar bordas pretas
                    video.style.transition = 'transform 1.5s ease-in-out';
                    video.currentTime = 0;
                    video.play();
                } else {
                    // Fixar na imagem estática (já para no último frame) e mostrar neve
                    snowfall.style.opacity = '1';
                }
            });
        }
"""
content = content.replace('// GSAP: Animação de borda dinâmica', video_js + '\n        // GSAP: Animação de borda dinâmica')


# --- Task 3: Section 7 Sticky ---
# Add self-start to the sticky container
content = content.replace('<div class="lg:sticky lg:top-32">', '<div class="lg:sticky lg:top-32 self-start">')


# --- Task 4: Section 8 Pricing ---
# Remove Toggle Mensal/Anual
toggle_html = """                <!-- Toggle Mensal/Anual -->
                <div class="flex items-center mt-4 bg-white border border-blue-100 p-1.5 rounded-full shadow-sm">
                    <button id="btn-mensal" class="px-6 py-2 rounded-full bg-[#367CF5] text-white font-semibold text-sm transition-all shadow-md">Mensal</button>
                    <button id="btn-anual" class="px-6 py-2 rounded-full text-zinc-500 font-semibold text-sm hover:text-zinc-800 transition-all">Anual</button>
                </div>"""
content = content.replace(toggle_html, '')

# Add more items to Essencial
essencial_items = """                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Controle financeiro do dia a dia</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Análises Básicas e Atlas Score</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Acesso à Comunidade</span></li>
                        <!-- Placeholders -->
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700 font-medium">Funcionalidade Essencial 1</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700 font-medium">Funcionalidade Essencial 2</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700 font-medium">Funcionalidade Essencial 3</span></li>"""
content = re.sub(r'(<h3 class="text-2xl font-bold text-\[#1a1a1a\] mb-2">Essencial</h3>.*?<ul class="mt-14 space-y-4">).*?(</ul>)', r'\1\n' + essencial_items + r'\n                    \2', content, flags=re.DOTALL)

# Add more items to Pro
pro_items = """                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm font-semibold text-[#1a1a1a]">Tudo do Essencial</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Planejamento longo prazo & Cenários</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Método Atlas (Relatórios IA)</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Atlas Negócios & Importações</span></li>
                        <!-- Placeholders -->
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700 font-medium">Funcionalidade Avançada 1</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700 font-medium">Funcionalidade Avançada 2</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700 font-medium">Funcionalidade Avançada 3</span></li>"""
content = re.sub(r'(<h3 class="text-2xl font-bold text-\[#1a1a1a\] mb-2">Pro</h3>.*?<ul class="mt-14 space-y-4">).*?(</ul>)', r'\1\n' + pro_items + r'\n                    \2', content, flags=re.DOTALL)

# Add more items to Elite
elite_items = """                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm font-semibold text-[#1a1a1a]">Tudo do Pro</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Cursos Avançados</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Plano da Liberdade Integrado</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Suporte Prioritário</span></li>
                        <!-- Placeholders -->
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700 font-medium">Mentoria Exclusiva Anual</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700 font-medium">Acesso VIP a Eventos</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700 font-medium">Prioridade em Novas Features</span></li>"""
content = re.sub(r'(<h3 class="text-2xl font-bold text-\[#1a1a1a\] mb-2">Elite</h3>.*?<ul class="mt-14 space-y-4">).*?(</ul>)', r'\1\n' + elite_items + r'\n                    \2', content, flags=re.DOTALL)

# Ensure h-auto on card texts so they can expand without clipping
content = content.replace('mb-6 h-10', 'mb-6 h-auto min-h-[40px]')

with open(filepath, 'w') as f:
    f.write(content)

