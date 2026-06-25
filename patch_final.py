import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

faq_and_cta = """
    <!-- === SEÇÃO 9: FAQ === -->
    <section id="section-9" class="w-full bg-white py-24 md:py-32 px-6 lg:px-12 relative border-t border-zinc-200">
        <div class="max-w-3xl mx-auto flex flex-col items-center">
            <h2 class="text-4xl md:text-5xl font-bold text-[#1a1a1a] mb-2 text-center">FAQ</h2>
            <p class="text-lg md:text-xl text-zinc-500 mb-16 text-center">Tudo que você queria perguntar.</p>

            <div class="w-full flex flex-col gap-4 mb-20" id="faq-container">
                
                <!-- Pergunta 1 -->
                <div class="faq-item group bg-white border border-[#367CF5]/30 rounded-2xl overflow-hidden shadow-sm hover:shadow-md transition-all cursor-pointer">
                    <div class="faq-header flex justify-between items-center p-5 md:p-6 bg-white">
                        <h3 class="text-base md:text-lg font-semibold text-[#1a1a1a] pr-4">Como funciona o trial gratuito?</h3>
                        <div class="w-8 h-8 rounded-full border border-zinc-200 flex items-center justify-center text-[#367CF5] transition-transform faq-icon shrink-0">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </div>
                    </div>
                    <div class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out bg-zinc-50/50">
                        <div class="p-5 md:p-6 pt-0 text-zinc-600 leading-relaxed border-t border-zinc-100 mt-2">
                            Você se cadastra com email e recebe acesso completo a todas as ferramentas (exceto cursos do Plano da Liberdade) por 7 dias. Os planos só aparecem dentro da plataforma quando o trial terminar — sem cartão, sem cobrança automática.
                        </div>
                    </div>
                </div>

                <!-- Pergunta 2 -->
                <div class="faq-item group bg-white border border-[#367CF5]/30 rounded-2xl overflow-hidden shadow-sm hover:shadow-md transition-all cursor-pointer">
                    <div class="faq-header flex justify-between items-center p-5 md:p-6 bg-white">
                        <h3 class="text-base md:text-lg font-semibold text-[#1a1a1a] pr-4">Preciso colocar cartão pra começar?</h3>
                        <div class="w-8 h-8 rounded-full border border-zinc-200 flex items-center justify-center text-[#367CF5] transition-transform faq-icon shrink-0">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </div>
                    </div>
                    <div class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out bg-zinc-50/50">
                        <div class="p-5 md:p-6 pt-0 text-zinc-600 leading-relaxed border-t border-zinc-100 mt-2">
                            Não. Você cria conta só com email. O Atlas só apresenta os planos depois que você experimentou, dentro da plataforma.
                        </div>
                    </div>
                </div>

                <!-- Pergunta 3 -->
                <div class="faq-item group bg-white border border-[#367CF5]/30 rounded-2xl overflow-hidden shadow-sm hover:shadow-md transition-all cursor-pointer">
                    <div class="faq-header flex justify-between items-center p-5 md:p-6 bg-white">
                        <h3 class="text-base md:text-lg font-semibold text-[#1a1a1a] pr-4">Quanto tempo por dia preciso usar o Atlas?</h3>
                        <div class="w-8 h-8 rounded-full border border-zinc-200 flex items-center justify-center text-[#367CF5] transition-transform faq-icon shrink-0">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </div>
                    </div>
                    <div class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out bg-zinc-50/50">
                        <div class="p-5 md:p-6 pt-0 text-zinc-600 leading-relaxed border-t border-zinc-100 mt-2">
                            A maioria dos usuários gasta 5 minutos por dia — pra conferir o painel, perguntar ao Atlas IA, ou ajustar o plano. O sistema trabalha em segundo plano.
                        </div>
                    </div>
                </div>

                <!-- Pergunta 4 -->
                <div class="faq-item group bg-white border border-[#367CF5]/30 rounded-2xl overflow-hidden shadow-sm hover:shadow-md transition-all cursor-pointer">
                    <div class="faq-header flex justify-between items-center p-5 md:p-6 bg-white">
                        <h3 class="text-base md:text-lg font-semibold text-[#1a1a1a] pr-4">Já tenho contador / assessor de investimentos. O Atlas substitui?</h3>
                        <div class="w-8 h-8 rounded-full border border-zinc-200 flex items-center justify-center text-[#367CF5] transition-transform faq-icon shrink-0">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </div>
                    </div>
                    <div class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out bg-zinc-50/50">
                        <div class="p-5 md:p-6 pt-0 text-zinc-600 leading-relaxed border-t border-zinc-100 mt-2">
                            Não — complementa. Seu contador cuida do imposto, seu assessor da carteira. O Atlas é o sistema que conecta tudo na sua vida pessoal e mostra o quadro completo.
                        </div>
                    </div>
                </div>

                <!-- Pergunta 5 -->
                <div class="faq-item group bg-white border border-[#367CF5]/30 rounded-2xl overflow-hidden shadow-sm hover:shadow-md transition-all cursor-pointer">
                    <div class="faq-header flex justify-between items-center p-5 md:p-6 bg-white">
                        <h3 class="text-base md:text-lg font-semibold text-[#1a1a1a] pr-4">Posso usar com meu parceiro ou parceira?</h3>
                        <div class="w-8 h-8 rounded-full border border-zinc-200 flex items-center justify-center text-[#367CF5] transition-transform faq-icon shrink-0">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </div>
                    </div>
                    <div class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out bg-zinc-50/50">
                        <div class="p-5 md:p-6 pt-0 text-zinc-600 leading-relaxed border-t border-zinc-100 mt-2">
                            Sim, em todos os planos. Você convida por email, cada um tem seu acesso próprio (sem compartilhar senha), ambos veem o mesmo plano financeiro.
                        </div>
                    </div>
                </div>

                <!-- Pergunta 6 -->
                <div class="faq-item group bg-white border border-[#367CF5]/30 rounded-2xl overflow-hidden shadow-sm hover:shadow-md transition-all cursor-pointer">
                    <div class="faq-header flex justify-between items-center p-5 md:p-6 bg-white">
                        <h3 class="text-base md:text-lg font-semibold text-[#1a1a1a] pr-4">O Plano da Liberdade está incluso?</h3>
                        <div class="w-8 h-8 rounded-full border border-zinc-200 flex items-center justify-center text-[#367CF5] transition-transform faq-icon shrink-0">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </div>
                    </div>
                    <div class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out bg-zinc-50/50">
                        <div class="p-5 md:p-6 pt-0 text-zinc-600 leading-relaxed border-t border-zinc-100 mt-2">
                            O Plano da Liberdade — curso de 33 aulas em 8 módulos — é exclusivo do plano Elite. Os planos Essencial e Pro têm acesso completo às ferramentas do sistema, mas não ao curso. (Tem outros cursos aqui tambem).
                        </div>
                    </div>
                </div>

                <!-- Pergunta 7 -->
                <div class="faq-item group bg-white border border-[#367CF5]/30 rounded-2xl overflow-hidden shadow-sm hover:shadow-md transition-all cursor-pointer">
                    <div class="faq-header flex justify-between items-center p-5 md:p-6 bg-white">
                        <h3 class="text-base md:text-lg font-semibold text-[#1a1a1a] pr-4">Como cancelo se não quiser continuar?</h3>
                        <div class="w-8 h-8 rounded-full border border-zinc-200 flex items-center justify-center text-[#367CF5] transition-transform faq-icon shrink-0">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                        </div>
                    </div>
                    <div class="faq-content max-h-0 overflow-hidden transition-all duration-300 ease-in-out bg-zinc-50/50">
                        <div class="p-5 md:p-6 pt-0 text-zinc-600 leading-relaxed border-t border-zinc-100 mt-2">
                            Você cancela direto nas configurações da conta — sem multa, sem ligação, sem burocracia. Mantém acesso até o fim do ciclo pago.
                        </div>
                    </div>
                </div>

            </div>

            <!-- P.S. Emocional -->
            <div class="w-full p-8 md:p-14 bg-[#F9F6F0] rounded-3xl relative overflow-hidden shadow-inner border border-[#e2dfd8]">
                <div class="absolute top-0 right-0 w-[40%] h-[40%] bg-gradient-to-bl from-[#367CF5]/20 to-transparent rounded-full blur-3xl pointer-events-none"></div>
                <div class="absolute bottom-0 left-0 w-[40%] h-[40%] bg-gradient-to-tr from-[#A3E635]/10 to-transparent rounded-full blur-3xl pointer-events-none"></div>
                
                <h4 class="font-playfair italic text-4xl text-[#367CF5] mb-8 font-normal">P.S.</h4>
                <div class="space-y-6 text-lg md:text-xl text-zinc-700 leading-relaxed font-medium relative z-10">
                    <p>Se você chegou até aqui é porque alguma coisa ressoou. Talvez seja o cansaço de não saber pra onde o dinheiro vai. Talvez seja o desejo de finalmente planejar aquela viagem, aquela casa, aquela aposentadoria — e não ficar adiando porque "será que dá?".</p>
                    <p>O Atlas não é a resposta. É o caminho. Os 7 dias grátis são pra você descobrir se ele serve pra você — sem risco, sem compromisso, sem cartão.</p>
                    <p class="font-bold text-[#1a1a1a]">Você não precisa decidir agora se vai usar o Atlas pelos próximos 10 anos. Só precisa decidir se vale clicar e testar 7 dias.</p>
                </div>
            </div>

        </div>
    </section>

    <!-- === SEÇÃO 10: CTA FINAL === -->
    <section id="section-10" class="w-full bg-gradient-to-b from-white via-[#eff4ff] to-[#d9e6ff] pt-32 pb-0 px-6 relative overflow-hidden flex flex-col items-center border-t border-blue-50">
        
        <!-- Background Blur/Glow da Montanha -->
        <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-full max-w-4xl h-64 bg-[#367CF5]/20 blur-[120px] rounded-full pointer-events-none"></div>

        <div class="text-center z-20 max-w-4xl mx-auto flex flex-col items-center relative">
            <h2 class="text-5xl md:text-6xl lg:text-7xl font-bold text-[#1a1a1a] mb-6 tracking-tight leading-tight">
                Pronto para encontrar <br class="hidden md:block"/><span class="text-[#367CF5]">seu caminho?</span>
            </h2>
            <p class="text-xl md:text-2xl text-zinc-600 font-medium max-w-2xl mx-auto mb-12 leading-relaxed">
                O Atlas mostra onde você está hoje, o próximo passo e o que muda se escolher um caminho diferente. Sua jornada começa aqui.
            </p>
            
            <button class="px-10 py-5 rounded-2xl bg-[#A3E635] text-[#0B1A30] text-xl md:text-2xl font-extrabold hover:bg-[#8cdc18] transition-all shadow-[0_4px_24px_0_rgba(163,230,53,0.5)] animate-heartbeat">
                Começar agora!
            </button>
        </div>

        <!-- Personagens Montanha -->
        <div class="w-full max-w-5xl mx-auto mt-16 md:mt-24 relative z-10 flex justify-center translate-y-2 md:translate-y-4">
            <img src="https://github.com/legendragon03453-dot/atlas/blob/main/Imagem%20de%20Fundo%204%20relatorios%202.webp?raw=true" alt="Jornada Atlas - O Topo da Montanha" class="w-full md:w-[90%] lg:w-full object-contain drop-shadow-2xl">
        </div>

    </section>
"""

js_faq = """
        // FAQ Accordion
        const faqItems = document.querySelectorAll('.faq-item');
        faqItems.forEach(item => {
            const header = item.querySelector('.faq-header');
            const content = item.querySelector('.faq-content');
            const icon = item.querySelector('.faq-icon');
            
            header.addEventListener('click', () => {
                const isOpen = content.style.maxHeight;
                
                // Close all others
                faqItems.forEach(otherItem => {
                    const otherContent = otherItem.querySelector('.faq-content');
                    const otherIcon = otherItem.querySelector('.faq-icon');
                    otherContent.style.maxHeight = null;
                    otherIcon.style.transform = 'rotate(0deg)';
                    otherItem.classList.remove('border-[#367CF5]');
                    otherItem.classList.add('border-[#367CF5]/30');
                });
                
                if (!isOpen) {
                    content.style.maxHeight = content.scrollHeight + "px";
                    icon.style.transform = 'rotate(180deg)';
                    item.classList.remove('border-[#367CF5]/30');
                    item.classList.add('border-[#367CF5]');
                }
            });
        });
"""

# Append sections right before the closing main tag or script tag
main_end_idx = content.rfind('</main>')
if main_end_idx != -1:
    content = content[:main_end_idx] + faq_and_cta + '\n' + content[main_end_idx:]

script_end = content.find('</script>')
if script_end != -1:
    content = content[:script_end] + js_faq + content[script_end:]

with open(filepath, 'w') as f:
    f.write(content)
