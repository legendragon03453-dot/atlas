import re

with open('index.html', 'r') as f:
    content = f.read()

# Define the start and end of Section 5
start_marker = "<!-- === SEÇÃO 5: Tabela de Comparação === -->"
end_marker = "<!-- === SEÇÃO 6: Pricing / Planos === -->"

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    new_section_5 = """<!-- === SEÇÃO 5: Comparativo Cards === -->
    <section id="section-5" class="w-full bg-[#367CF5] py-24 px-4 flex flex-col items-center relative overflow-hidden">
        <!-- Glow Overlay -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden z-0">
            <div class="absolute top-0 left-0 w-[60%] h-full bg-[#36DCF5]/60 blur-[150px] rounded-full animate-glow-sweep mix-blend-screen"></div>
        </div>

        <h2 class="text-white text-2xl md:text-4xl lg:text-5xl font-bold mb-16 text-center max-w-4xl leading-tight drop-shadow-lg tracking-tight scroll-reveal">
            Veja como sua vida financeira muda<br>quando você tem <span class="font-normal italic font-playfair text-[#AFFF00]">um mapa.</span>
        </h2>

        <div class="w-full max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 relative z-10 scroll-reveal">
            
            <!-- Card Sem Atlas -->
            <div class="bg-[#0B1A30]/90 backdrop-blur-md rounded-3xl border border-white/10 p-8 md:p-12 shadow-2xl flex flex-col gap-6">
                <div class="border-b border-white/10 pb-6 mb-2">
                    <h3 class="text-white/60 font-bold text-2xl uppercase tracking-wider text-center">A Vida Sem Mapa</h3>
                </div>
                
                <div class="flex items-start gap-4">
                    <div class="w-6 h-6 rounded-full bg-red-500/20 flex items-center justify-center flex-shrink-0 mt-1"><span class="text-red-500 font-bold">✕</span></div>
                    <div><h4 class="text-white/80 font-bold mb-1">O seu futuro</h4><p class="text-white/50 text-sm">Parece longe e irreal.</p></div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-6 h-6 rounded-full bg-red-500/20 flex items-center justify-center flex-shrink-0 mt-1"><span class="text-red-500 font-bold">✕</span></div>
                    <div><h4 class="text-white/80 font-bold mb-1">Decisões de compra</h4><p class="text-white/50 text-sm">Feitas no impulso ou na emoção.</p></div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-6 h-6 rounded-full bg-red-500/20 flex items-center justify-center flex-shrink-0 mt-1"><span class="text-red-500 font-bold">✕</span></div>
                    <div><h4 class="text-white/80 font-bold mb-1">Controle de gastos</h4><p class="text-white/50 text-sm">Anota por anotar, sem foco no que importa.</p></div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-6 h-6 rounded-full bg-red-500/20 flex items-center justify-center flex-shrink-0 mt-1"><span class="text-red-500 font-bold">✕</span></div>
                    <div><h4 class="text-white/80 font-bold mb-1">Visão do dinheiro</h4><p class="text-white/50 text-sm">Olha só para o que já gastou (passado).</p></div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-6 h-6 rounded-full bg-red-500/20 flex items-center justify-center flex-shrink-0 mt-1"><span class="text-red-500 font-bold">✕</span></div>
                    <div><h4 class="text-white/80 font-bold mb-1">Efeito das escolhas</h4><p class="text-white/50 text-sm">Você não faz ideia de como afeta seu amanhã.</p></div>
                </div>
            </div>

            <!-- Card Com Atlas -->
            <div class="bg-gradient-to-b from-[#AFFF00] to-[#76CC00] rounded-3xl border border-[#AFFF00]/50 p-8 md:p-12 shadow-[0_0_50px_rgba(175,255,0,0.3)] flex flex-col gap-6 transform md:-translate-y-4">
                <div class="border-b border-[#1A2E05]/10 pb-6 mb-2">
                    <h3 class="text-[#1A2E05] font-black text-3xl uppercase tracking-wider text-center">Com o Atlas</h3>
                </div>
                
                <div class="flex items-start gap-4">
                    <div class="w-6 h-6 rounded-full bg-[#1A2E05]/20 flex items-center justify-center flex-shrink-0 mt-1"><span class="text-[#1A2E05] font-bold">✓</span></div>
                    <div><h4 class="text-[#1A2E05] font-bold mb-1">O seu futuro</h4><p class="text-[#1A2E05]/80 text-sm">Tem data, meta e valor exato.</p></div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-6 h-6 rounded-full bg-[#1A2E05]/20 flex items-center justify-center flex-shrink-0 mt-1"><span class="text-[#1A2E05] font-bold">✓</span></div>
                    <div><h4 class="text-[#1A2E05] font-bold mb-1">Decisões de compra</h4><p class="text-[#1A2E05]/80 text-sm">Baseadas em números e realidade.</p></div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-6 h-6 rounded-full bg-[#1A2E05]/20 flex items-center justify-center flex-shrink-0 mt-1"><span class="text-[#1A2E05] font-bold">✓</span></div>
                    <div><h4 class="text-[#1A2E05] font-bold mb-1">Controle de gastos</h4><p class="text-[#1A2E05]/80 text-sm">Gasta sem culpa no que te faz feliz.</p></div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-6 h-6 rounded-full bg-[#1A2E05]/20 flex items-center justify-center flex-shrink-0 mt-1"><span class="text-[#1A2E05] font-bold">✓</span></div>
                    <div><h4 class="text-[#1A2E05] font-bold mb-1">Visão do dinheiro</h4><p class="text-[#1A2E05]/80 text-sm">Sabe exatamente o que vai gastar (futuro).</p></div>
                </div>
                <div class="flex items-start gap-4">
                    <div class="w-6 h-6 rounded-full bg-[#1A2E05]/20 flex items-center justify-center flex-shrink-0 mt-1"><span class="text-[#1A2E05] font-bold">✓</span></div>
                    <div><h4 class="text-[#1A2E05] font-bold mb-1">Efeito das escolhas</h4><p class="text-[#1A2E05]/80 text-sm">Você vê o impacto palpável daqui a 20 anos.</p></div>
                </div>
            </div>

        </div>
    </section>
    
    """
    
    content = content[:start_idx] + new_section_5 + content[end_idx:]

    with open('index.html', 'w') as f:
        f.write(content)

