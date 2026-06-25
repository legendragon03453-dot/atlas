import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Update Glow
old_glow = '<div class="absolute top-0 left-0 w-[50%] h-full bg-[#36DCF5]/20 blur-[120px] rounded-full animate-glow-sweep mix-blend-screen"></div>'
new_glow = '<div class="absolute top-0 left-0 w-[60%] h-full bg-[#36DCF5]/60 blur-[150px] rounded-full animate-glow-sweep mix-blend-screen"></div>'
content = content.replace(old_glow, new_glow)

# 2. Update Mountain Labels
old_mountain = """                        <div class="absolute top-16 left-[20%] animate-float z-20" style="animation-delay: 0s;">
                            <div class="bg-white border border-[#367CF5]/30 text-[#367CF5] text-xs font-bold px-3 py-1 rounded-full shadow-sm">Etapa 1</div>
                            <div class="w-1.5 h-1.5 bg-[#367CF5] rounded-full mx-auto mt-2"></div>
                        </div>
                        <div class="absolute top-24 left-[50%] animate-float z-20" style="animation-delay: 0.5s;">
                            <div class="bg-white border border-[#367CF5]/30 text-[#367CF5] text-xs font-bold px-3 py-1 rounded-full shadow-sm">Etapa 2</div>
                            <div class="w-1.5 h-1.5 bg-[#367CF5] rounded-full mx-auto mt-2"></div>
                        </div>
                        <div class="absolute top-[10px] right-[5%] animate-float z-20" style="animation-delay: 1s;">
                            <div class="bg-[#367CF5] text-white text-xs font-bold px-3 py-1.5 rounded-full shadow-md whitespace-nowrap">Etapa 3 [Seu objetivo final]</div>
                            <div class="w-1.5 h-1.5 bg-[#367CF5] rounded-full mx-auto mt-2"></div>
                        </div>"""
new_mountain = """                        <div class="absolute bottom-6 left-[15%] animate-float z-20" style="animation-delay: 0s;">
                            <div class="bg-white border border-[#367CF5]/30 text-[#367CF5] text-xs font-bold px-3 py-1 rounded-full shadow-sm">Etapa 1</div>
                            <div class="w-1.5 h-1.5 bg-[#367CF5] rounded-full mx-auto mt-2"></div>
                        </div>
                        <div class="absolute top-[55%] left-[50%] animate-float z-20" style="animation-delay: 0.5s; transform: translate(-50%, -50%);">
                            <div class="bg-white border border-[#367CF5]/30 text-[#367CF5] text-xs font-bold px-3 py-1 rounded-full shadow-sm">Etapa 2</div>
                            <div class="w-1.5 h-1.5 bg-[#367CF5] rounded-full mx-auto mt-2"></div>
                        </div>
                        <div class="absolute top-2 right-[2%] animate-float z-20" style="animation-delay: 1s;">
                            <div class="bg-[#367CF5] text-white text-[10px] md:text-xs font-bold px-3 py-1.5 rounded-full shadow-md whitespace-nowrap">Etapa 3 [Seu objetivo final]</div>
                            <div class="w-1.5 h-1.5 bg-[#367CF5] rounded-full mx-auto mt-2"></div>
                        </div>"""
content = content.replace(old_mountain, new_mountain)

# 3. Add CSS for snow
style_end = content.find('</style>')
snow_css = """
        @keyframes snowfall {
            0% { transform: translateY(-10vh) translateX(0) rotate(0deg); opacity: 0; }
            10% { opacity: 0.8; }
            90% { opacity: 0.8; }
            100% { transform: translateY(110vh) translateX(50px) rotate(360deg); opacity: 0; }
        }
"""
content = content[:style_end] + snow_css + content[style_end:]

# 4. Replace parallax ice blocks with pure CSS snow
old_ice = """        <!-- Parallax Ice Blocks -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden z-10">
            <div class="parallax-ice absolute top-[20%] left-[10%] w-8 h-8 bg-white/40 backdrop-blur-md rounded-lg shadow-lg rotate-12" data-speed="0.05"></div>
            <div class="parallax-ice absolute top-[60%] left-[5%] w-12 h-12 bg-white/20 backdrop-blur-sm rounded-xl shadow-lg -rotate-12 blur-[2px]" data-speed="0.02"></div>
            <div class="parallax-ice absolute top-[30%] right-[15%] w-6 h-6 bg-white/60 backdrop-blur-lg rounded shadow-lg rotate-45" data-speed="0.08"></div>
            <div class="parallax-ice absolute top-[70%] right-[10%] w-16 h-16 bg-white/30 backdrop-blur-md rounded-2xl shadow-xl rotate-6 blur-[1px]" data-speed="0.04"></div>
            <div class="parallax-ice absolute bottom-[10%] left-[40%] w-10 h-10 bg-white/50 backdrop-blur-lg rounded-xl shadow-lg -rotate-6" data-speed="0.06"></div>
        </div>"""

new_ice = """        <!-- CSS Snow/Ice Particles -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden z-10">
            <!-- Camada de trás (menores, mais lentas, opacidade menor) -->
            <div class="absolute w-2 h-2 bg-white/50 rounded-sm top-[-5%] left-[10%] [animation:snowfall_12s_linear_infinite_0s]"></div>
            <div class="absolute w-1.5 h-1.5 bg-white/40 rounded-sm top-[-5%] left-[25%] [animation:snowfall_14s_linear_infinite_2s]"></div>
            <div class="absolute w-2 h-2 bg-white/60 rounded-sm top-[-5%] left-[40%] [animation:snowfall_11s_linear_infinite_4s]"></div>
            <div class="absolute w-1.5 h-1.5 bg-white/40 rounded-sm top-[-5%] left-[60%] [animation:snowfall_15s_linear_infinite_1s]"></div>
            <div class="absolute w-2 h-2 bg-white/50 rounded-sm top-[-5%] left-[80%] [animation:snowfall_13s_linear_infinite_5s]"></div>
            <div class="absolute w-1.5 h-1.5 bg-white/60 rounded-sm top-[-5%] left-[90%] [animation:snowfall_16s_linear_infinite_3s]"></div>
            
            <!-- Camada da frente (maiores, mais rápidas, com blur/reflexo) -->
            <div class="absolute w-3 h-3 bg-white/80 rounded top-[-5%] left-[15%] shadow-[0_0_10px_white] [animation:snowfall_8s_linear_infinite_6s]"></div>
            <div class="absolute w-4 h-4 bg-white/70 rounded backdrop-blur-sm blur-[1px] top-[-5%] left-[35%] [animation:snowfall_10s_linear_infinite_8s]"></div>
            <div class="absolute w-2.5 h-2.5 bg-white/90 rounded top-[-5%] left-[55%] shadow-[0_0_8px_white] [animation:snowfall_7s_linear_infinite_7s]"></div>
            <div class="absolute w-5 h-5 bg-white/60 rounded-lg backdrop-blur-md blur-[2px] top-[-5%] left-[70%] [animation:snowfall_11s_linear_infinite_9s]"></div>
            <div class="absolute w-3 h-3 bg-white/80 rounded top-[-5%] left-[85%] shadow-[0_0_12px_white] [animation:snowfall_9s_linear_infinite_10s]"></div>
        </div>"""
content = content.replace(old_ice, new_ice)

# 5. Remove the Parallax JS script
parallax_script = """        // Parallax Ice Blocks
        document.addEventListener('mousemove', (e) => {
            const ices = document.querySelectorAll('.parallax-ice');
            const x = (window.innerWidth - e.pageX) / 2;
            const y = (window.innerHeight - e.pageY) / 2;
            
            ices.forEach(ice => {
                const speed = ice.getAttribute('data-speed');
                ice.style.transform = `translateX(${x * speed}px) translateY(${y * speed}px)`;
            });
        });"""
content = content.replace(parallax_script, '')

# 6. Append Section 7
section7 = """
    <!-- === SEÇÃO 7: A História Editorial === -->
    <section id="section-7" class="w-full bg-[#F9F6F0] py-24 md:py-40 px-6 lg:px-12 text-[#1a1a1a] relative border-t border-[#e2dfd8]">
        <div class="max-w-7xl mx-auto flex flex-col lg:flex-row gap-16 lg:gap-24 relative">
            
            <!-- Esquerda: Título Fixo -->
            <div class="w-full lg:w-5/12">
                <div class="lg:sticky lg:top-32">
                    <div class="flex items-center gap-3 mb-6">
                        <div class="w-8 h-px bg-zinc-400"></div>
                        <span class="text-xs font-semibold tracking-widest text-zinc-500 uppercase">A Origem</span>
                    </div>
                    <h2 class="text-5xl md:text-6xl lg:text-7xl font-playfair font-normal italic leading-[1.1] mb-8 text-[#0F172A]">
                        Como o Atlas<br>Surgiu?
                    </h2>
                    <!-- Visual Conceitual/Abstrato -->
                    <div class="w-full h-64 bg-gradient-to-br from-[#e2dfd8] to-[#d4d0c8] rounded-2xl relative overflow-hidden hidden lg:block shadow-inner">
                        <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(255,255,255,0.4)_0%,transparent_60%)]"></div>
                        <div class="absolute bottom-[-20%] left-[-10%] w-[120%] h-[120%] bg-[radial-gradient(circle_at_bottom_left,rgba(54,124,245,0.05)_0%,transparent_60%)]"></div>
                    </div>
                </div>
            </div>

            <!-- Direita: Texto Editorial -->
            <div class="w-full lg:w-7/12 flex flex-col gap-12 md:gap-16 text-lg md:text-xl lg:text-2xl text-zinc-700 font-medium leading-relaxed lg:mt-32">
                
                <p>
                    <span class="float-left text-7xl lg:text-8xl font-playfair font-normal italic text-[#367CF5] leading-[0.8] pr-3 pt-2">C</span>
                    resci em uma pousada no litoral de Santa Catarina. Meus pais tiveram o negócio por 25 anos sem planejamento. Em 2020, fechou.
                </p>

                <blockquote class="my-4 py-8 pl-8 md:pl-12 border-l-4 border-[#367CF5] bg-white/50 rounded-r-2xl shadow-sm relative overflow-hidden">
                    <div class="absolute top-0 left-0 w-full h-full bg-gradient-to-r from-white to-transparent opacity-80 pointer-events-none"></div>
                    <p class="text-3xl md:text-4xl font-playfair font-normal italic text-[#0F172A] leading-tight relative z-10">
                        "E agora? Estamos fazendo certo?"
                    </p>
                    <div class="mt-6 text-sm md:text-base font-bold text-zinc-500 tracking-widest uppercase relative z-10">— No segundo mês da pandemia</div>
                </blockquote>

                <p>
                    Era minha vez de responder.
                </p>

                <p>
                    Nos anos seguintes, ajudei mais de <strong class="text-[#0F172A]">300 clientes</strong>. Descobri que o problema raramente era ganhar pouco — era não enxergar o futuro. Não era falta de inteligência financeira. <span class="bg-[#A3E635]/30 px-2 py-0.5 rounded">Era falta de mapa.</span>
                </p>

                <p>
                    Comecei a criar um sistema. Primeiro para mim e minha esposa. Depois para família e amigos. Esse sistema virou o Atlas.
                </p>

                <div class="p-8 md:p-12 bg-[#0B1A30] text-white rounded-3xl shadow-2xl mt-4 relative overflow-hidden">
                    <!-- Detalhes do Card Dark -->
                    <div class="absolute inset-0 bg-[linear-gradient(to_right,#ffffff05_1px,transparent_1px),linear-gradient(to_bottom,#ffffff05_1px,transparent_1px)] bg-[size:24px_24px]"></div>
                    <div class="absolute top-0 right-0 w-[50%] h-[50%] bg-[#367CF5]/20 blur-[80px] rounded-full pointer-events-none"></div>
                    
                    <p class="relative z-10 text-xl md:text-2xl font-light leading-relaxed">
                        Ele não diz o que fazer. Mostra onde você está, o próximo passo e o que muda se seguir um caminho diferente. <br><br>
                        <strong class="font-playfair italic font-normal text-3xl md:text-4xl text-[#A3E635]">É o mapa que meus pais não tiveram quando precisaram.</strong>
                    </p>
                </div>
                
            </div>
        </div>
    </section>
"""

# Insert Section 7
script_tag = content.find('<script>')
if script_tag != -1:
    content = content[:script_tag] + section7 + content[script_tag:]

with open(filepath, 'w') as f:
    f.write(content)
