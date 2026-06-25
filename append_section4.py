import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Locate the script tag to insert Section 4 just before it
script_start = content.find('<script>')

if script_start != -1:
    section4_html = """
    <!-- === SEÇÃO 4: Timeline === -->
    <section id="section-4" class="w-full bg-[#367CF5] flex flex-col items-center pt-24 pb-32 relative overflow-hidden">
        <!-- Título -->
        <h2 class="text-white text-3xl md:text-4xl lg:text-5xl font-bold mb-16 text-center px-4 max-w-4xl leading-tight drop-shadow-lg">
            Você não sai do caos para a maestria de uma noite.<br>
            Você sobe uma montanha, passo a passo.
        </h2>

        <!-- Container da Timeline -->
        <div class="relative w-full max-w-5xl h-[900px] md:h-[1200px] lg:h-[1600px] mx-auto mt-10">
            <!-- SVG Background -->
            <svg class="absolute inset-0 w-full h-full" viewBox="0 0 1000 1600" preserveAspectRatio="none">
                <!-- Linha fina transparente de fundo -->
                <path d="M 350 0 C 350 100, 350 100, 350 200 C 350 350, 750 350, 750 500 C 750 650, 250 650, 250 800 C 250 950, 700 950, 700 1100 C 700 1250, 450 1250, 450 1400 C 450 1500, 450 1600, 450 1600" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="3" />
                <!-- Linha animada branca sólida -->
                <path id="timeline-path" d="M 350 0 C 350 100, 350 100, 350 200 C 350 350, 750 350, 750 500 C 750 650, 250 650, 250 800 C 250 950, 700 950, 700 1100 C 700 1250, 450 1250, 450 1400 C 450 1500, 450 1600, 450 1600" fill="none" stroke="white" stroke-width="5" />
            </svg>

            <!-- Os pontos da timeline -->
            <!-- Passo 1 (X: 35%) -->
            <div class="absolute w-5 h-5 md:w-6 md:h-6 rounded-full bg-white transform -translate-x-1/2 -translate-y-1/2 shadow-[0_0_15px_rgba(255,255,255,0.8)] z-20" style="top: 12.5%; left: 35%;">
                <div class="absolute top-1/2 -translate-y-1/2 left-[calc(100%+15px)] md:left-auto md:right-[calc(100%+20px)] w-[180px] sm:w-[220px] md:w-[320px] text-left md:text-right">
                    <h3 class="text-white font-bold text-[16px] md:text-xl mb-2 leading-tight">Você vê o que aconteceu.<br>Começa a entender o padrão.</h3>
                    <p class="text-white/80 text-[13px] md:text-sm leading-relaxed">Seus primeiros passos. Você registra o mês, vê onde o dinheiro foi.</p>
                </div>
            </div>

            <!-- Passo 2 (X: 75%) -->
            <div class="absolute w-5 h-5 md:w-6 md:h-6 rounded-full bg-white transform -translate-x-1/2 -translate-y-1/2 shadow-[0_0_15px_rgba(255,255,255,0.8)] z-20" style="top: 31.25%; left: 75%;">
                <div class="absolute top-1/2 -translate-y-1/2 right-[calc(100%+15px)] md:right-auto md:left-[calc(100%+20px)] w-[180px] sm:w-[220px] md:w-[320px] text-right md:text-left">
                    <h3 class="text-white font-bold text-[16px] md:text-xl mb-2 leading-tight">Você registra e categoriza.<br>Começa a ter clareza.</h3>
                    <p class="text-white/80 text-[13px] md:text-sm leading-relaxed">Cada categoria revela um valor seu. Alimentação, educação, lazer. Você não corta gastos. Você alinha gastos com o que importa.</p>
                </div>
            </div>

            <!-- Passo 3 (X: 25%) -->
            <div class="absolute w-5 h-5 md:w-6 md:h-6 rounded-full bg-white transform -translate-x-1/2 -translate-y-1/2 shadow-[0_0_15px_rgba(255,255,255,0.8)] z-20" style="top: 50%; left: 25%;">
                <div class="absolute top-1/2 -translate-y-1/2 left-[calc(100%+15px)] md:left-auto md:right-[calc(100%+20px)] w-[180px] sm:w-[220px] md:w-[320px] text-left md:text-right">
                    <h3 class="text-white font-bold text-[16px] md:text-xl mb-2 leading-tight">Você projeta o futuro.<br>Começa a ter controle.</h3>
                    <p class="text-white/80 text-[13px] md:text-sm leading-relaxed">Você sai do presente e entra no futuro. Vê sua aposentadoria não como abstração, mas como meta</p>
                </div>
            </div>

            <!-- Passo 4 (X: 70%) -->
            <div class="absolute w-5 h-5 md:w-6 md:h-6 rounded-full bg-white transform -translate-x-1/2 -translate-y-1/2 shadow-[0_0_15px_rgba(255,255,255,0.8)] z-20" style="top: 68.75%; left: 70%;">
                <div class="absolute top-1/2 -translate-y-1/2 right-[calc(100%+15px)] w-[180px] sm:w-[220px] md:w-[320px] text-right">
                    <h3 class="text-white font-bold text-[16px] md:text-xl mb-2 leading-tight">Você decide com dados.<br>Começa a construir riqueza.</h3>
                    <p class="text-white/80 text-[13px] md:text-sm leading-relaxed">Agora você não decide por emoção. Você vê o impacto de cada escolha. Aumentar a reserva em R$ 100? Vê o resultado em 10, 20, 30 anos.</p>
                </div>
            </div>

            <!-- Passo 5 (X: 45%) -->
            <div class="absolute w-5 h-5 md:w-6 md:h-6 rounded-full bg-white transform -translate-x-1/2 -translate-y-1/2 shadow-[0_0_15px_rgba(255,255,255,0.8)] z-20" style="top: 87.5%; left: 45%;">
                <div class="absolute top-1/2 -translate-y-1/2 left-[calc(100%+15px)] md:left-auto md:right-[calc(100%+20px)] w-[160px] sm:w-[220px] md:w-[320px] text-left md:text-right">
                    <h3 class="text-white font-bold text-[16px] md:text-xl mb-2 leading-tight">Você vê a vida inteira.<br>Começa a viver com propósito</h3>
                    <p class="text-white/80 text-[13px] md:text-sm leading-relaxed">Você não pensa em meses. Você pensa em décadas. Sua vida financeira é uma história com começo, meio e fim claro.</p>
                </div>
            </div>
        </div>

        <a href="#" class="btn-green text-[#1A2E05] px-12 py-4 rounded-full font-bold text-xl flex items-center justify-center gap-3 mt-24 relative z-10 w-[90%] sm:w-auto transition-transform hover:-translate-y-1 shadow-2xl">
            <div class="w-3 h-3 bg-black"></div>
            Assinar Atlas
        </a>
    </section>

    """

    content = content[:script_start] + section4_html + content[script_start:]

# Inject GSAP logic for Section 4 inside the existing script
gsap_logic = """
        // GSAP: Animação de preenchimento da Timeline na Seção 4
        let path = document.querySelector('#timeline-path');
        if (path) {
            let length = path.getTotalLength();
            gsap.set(path, { strokeDasharray: length, strokeDashoffset: length });
            
            gsap.to(path, {
                strokeDashoffset: 0,
                ease: "none",
                scrollTrigger: {
                    trigger: "#section-4",
                    start: "top 60%", // Começa quando o topo da seção 4 passar pelo meio da tela
                    end: "bottom 80%", // Termina quando o final da seção estiver saindo
                    scrub: 1
                }
            });
        }
"""
content = content.replace('</script>', gsap_logic + '\n    </script>')

with open(filepath, 'w') as f:
    f.write(content)

