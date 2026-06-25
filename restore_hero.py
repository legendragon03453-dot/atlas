import re

hero_start = """
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
                <source src="https://github.com/legendragon03453-dot/atlas/raw/refs/heads/main/Comp%201_3.mp4" type="video/mp4">
            </video>
            
            <!-- Efeito de Neve / Poeira -->
            <div id="snowfall-container" class="absolute inset-0 z-10 pointer-events-none"></div>
            
            <!-- Efeito de Blur Inferior -->
            <div class="absolute bottom-0 left-0 w-full h-40 bg-gradient-to-t from-white via-white/80 to-transparent z-10 pointer-events-none"></div>
        </div>

        <!-- Hero Content (Fixed Center) -->
        <div class="relative z-20 w-full px-4 flex flex-col items-center justify-center text-center mt-16 md:mt-0">
            
            <!-- Badge Superior -->
            <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-black/20 backdrop-blur-md border border-white/10 mb-8 transform hover:scale-105 transition-transform cursor-pointer">
                <div class="flex -space-x-2">
                    <img class="w-6 h-6 rounded-full border border-[#1a1a1a]" src="https://i.pravatar.cc/100?img=1" alt="User">
                    <img class="w-6 h-6 rounded-full border border-[#1a1a1a]" src="https://i.pravatar.cc/100?img=2" alt="User">
                    <img class="w-6 h-6 rounded-full border border-[#1a1a1a]" src="https://i.pravatar.cc/100?img=3" alt="User">
                </div>
"""

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html', 'r') as f:
    content = f.read()

# I will replace exactly <span class="text-white text-sm font-medium opacity-90">+100 Usuários</span>
# with hero_start + <span class="text-white text-sm font-medium opacity-90">+100 Usuários</span>

if '<section id="hero-section"' not in content:
    target = '<span class="text-white text-sm font-medium opacity-90">+100 Usuários</span>'
    content = content.replace(target, hero_start + target)

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html', 'w') as f:
    f.write(content)

