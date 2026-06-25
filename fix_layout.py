import re

with open('index.html', 'r') as f:
    content = f.read()

# We want to replace everything from <body> up to <section id="hero-section"> with just <body> and <header>.
# Wait, let's be more precise.
# We will remove `<section class="hero-container p-0">`
# We will move the snow particles inside hero-section.
# We will move <header> to be just inside <body>.

new_top = """<body>
    <!-- Navbar -->
    <header style="width: 100%; position: absolute; height: 70px; z-index: 50; top: 0;">
        <nav class="navbar-shape shadow-lg">
            <!-- Logo -->
            <div class="flex-shrink-0 flex justify-start items-center">
                <img src="https://github.com/legendragon03453-dot/atlas/blob/main/export_2026-06-04T03_26_23-606Z/Group%201_1x.webp?raw=true" alt="Atlas Logo" class="h-10">
            </div>

            <!-- Links de Navegação -->
            <div class="nav-links flex-1 hidden md:flex justify-center items-center gap-4 lg:gap-8 text-white font-medium text-[14px] lg:text-[16px] whitespace-nowrap px-4">
                <a href="#section-7" class="hover:text-blue-200 transition-colors">Sobre</a>
                <a href="#section-8" class="hover:text-blue-200 transition-colors">Preços</a>
                <a href="funcionalidades.html" class="hover:text-blue-200 transition-colors">Funcionalidades</a>
                <a href="#section-9" class="hover:text-blue-200 transition-colors">FAQ</a>
                <a href="#" class="hover:text-blue-200 transition-colors">Suporte</a>
            </div>

                            <!-- Botão Teste Grátis -->
            <div class="flex-shrink-0 flex justify-end items-center gap-2">
                <a href="#" class="btn-nav font-bold text-[13px] lg:text-[15px] items-center gap-2 whitespace-nowrap hidden md:flex">
                    <svg width="10" height="10" viewBox="0 0 10 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9.5 5.13397C10.1667 5.51887 10.1667 6.48113 9.5 6.86603L1.25 11.6292C0.583334 12.0141 -2.99723e-07 11.5329 -2.66089e-07 10.7631L1.50346e-07 1.23686C1.83981e-07 0.46706 0.583333 -0.0140645 1.25 0.370836L9.5 5.13397Z" fill="#1A2E44"/>
                    </svg>
                    <span>Teste 7 dias</span>
                </a>
                <button id="mobile-menu-btn" class="md:hidden flex items-center justify-center p-2 text-white/90">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                </button>
            </div>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="hero-section" class="relative w-full h-screen min-h-[600px] flex items-center overflow-hidden">
        
        <!-- Video de Fundo -->
        <div class="absolute inset-0 w-full h-full z-0 overflow-hidden">
            <!-- Camada preta esquerda -->
            <div id="video-curtain-left" class="absolute top-0 left-0 w-1/2 h-full bg-black z-20 origin-left"></div>
            <!-- Camada preta direita -->
            <div id="video-curtain-right" class="absolute top-0 right-0 w-1/2 h-full bg-black z-20 origin-right"></div>
            
            <div class="absolute inset-0 bg-[#0F172A] opacity-20 z-10"></div>
            <video id="hero-video" class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-full h-full object-cover" autoplay muted playsinline>
                <source src="https://github.com/legendragon03453-dot/atlas/raw/main/Zoom_into_mountain_peak_archway_202606040019.webm" type="video/webm">
            </video>
            
            <!-- Efeito de Neve / Poeira -->
            <div id="snowfall-container" class="absolute inset-0 z-10 pointer-events-none"></div>

            <!-- CSS Snow/Ice Particles -->
            <div class="absolute inset-0 pointer-events-none overflow-hidden z-10">
                <!-- Camada de trás -->
                <div class="absolute w-2 h-2 bg-white/50 rounded-sm top-[-5%] left-[10%] [animation:snowfall_12s_linear_infinite_0s]"></div>
                <div class="absolute w-1.5 h-1.5 bg-white/40 rounded-sm top-[-5%] left-[25%] [animation:snowfall_14s_linear_infinite_2s]"></div>
                <div class="absolute w-2 h-2 bg-white/60 rounded-sm top-[-5%] left-[40%] [animation:snowfall_11s_linear_infinite_4s]"></div>
                <div class="absolute w-1.5 h-1.5 bg-white/40 rounded-sm top-[-5%] left-[60%] [animation:snowfall_15s_linear_infinite_1s]"></div>
                <div class="absolute w-2 h-2 bg-white/50 rounded-sm top-[-5%] left-[80%] [animation:snowfall_13s_linear_infinite_5s]"></div>
                <div class="absolute w-1.5 h-1.5 bg-white/60 rounded-sm top-[-5%] left-[90%] [animation:snowfall_16s_linear_infinite_3s]"></div>
                
                <!-- Camada da frente -->
                <div class="absolute w-3 h-3 bg-white/80 rounded top-[-5%] left-[15%] shadow-[0_0_10px_white] [animation:snowfall_8s_linear_infinite_6s]"></div>
                <div class="absolute w-4 h-4 bg-white/70 rounded backdrop-blur-sm blur-[1px] top-[-5%] left-[35%] [animation:snowfall_10s_linear_infinite_8s]"></div>
                <div class="absolute w-2.5 h-2.5 bg-white/90 rounded top-[-5%] left-[55%] shadow-[0_0_8px_white] [animation:snowfall_7s_linear_infinite_7s]"></div>
                <div class="absolute w-5 h-5 bg-white/60 rounded-lg backdrop-blur-md blur-[2px] top-[-5%] left-[70%] [animation:snowfall_11s_linear_infinite_9s]"></div>
                <div class="absolute w-3 h-3 bg-white/80 rounded top-[-5%] left-[85%] shadow-[0_0_12px_white] [animation:snowfall_9s_linear_infinite_10s]"></div>
            </div>
            
            <!-- Efeito de Blur Inferior -->
            <div class="absolute bottom-0 left-0 w-full h-40 bg-gradient-to-t from-white via-white/80 to-transparent z-10 pointer-events-none"></div>
        </div>"""

pattern = re.compile(r'<body>.*?<!-- Hero Content \(Fixed Center\) -->', re.DOTALL)
content = pattern.sub(new_top + '\n\n        <!-- Hero Content (Fixed Center) -->', content)

with open('index.html', 'w') as f:
    f.write(content)

