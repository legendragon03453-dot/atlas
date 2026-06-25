import re

with open('index.html', 'r') as f:
    content = f.read()

old_ps = """            <!-- P.S. Emocional -->
            <div class="w-full p-8 md:p-14 bg-[#F9F6F0] rounded-3xl relative overflow-hidden shadow-inner border border-[#e2dfd8]">
                <div class="absolute top-0 right-0 w-[40%] h-[40%] bg-gradient-to-bl from-[#367CF5]/20 to-transparent rounded-full blur-3xl pointer-events-none"></div>
                <div class="absolute bottom-0 left-0 w-[40%] h-[40%] bg-gradient-to-tr from-[#A3E635]/10 to-transparent rounded-full blur-3xl pointer-events-none"></div>
                
                <h4 class="font-playfair italic text-4xl text-[#367CF5] mb-8 font-normal">P.S.</h4>
                <div class="space-y-6 text-lg md:text-xl text-zinc-700 leading-relaxed font-medium relative z-10">
                    <p>Se você chegou até aqui é porque alguma coisa ressoou. Talvez seja o cansaço de não saber pra onde o dinheiro vai. Talvez seja o desejo de finalmente planejar aquela viagem, aquela casa, aquela aposentadoria — e não ficar adiando porque "será que dá?".</p>
                    <p>O Atlas não é a resposta. É o caminho. Os 7 dias grátis são pra você descobrir se ele serve pra você — sem risco, sem compromisso, sem cartão.</p>
                    <p class="font-bold text-[#1a1a1a]">Você não precisa decidir agora se vai usar o Atlas pelos próximos 10 anos. Só precisa decidir se vale clicar e testar 7 dias.</p>
                    <button class="mt-8 px-8 py-4 rounded-xl bg-gradient-to-r from-[#A3E635] via-[#8cdc18] to-[#A3E635] bg-[length:200%_auto] text-[#0B1A30] text-lg font-bold transition-all shadow-[0_4px_24px_0_rgba(163,230,53,0.4)] animate-[bg-scroll_3s_linear_infinite]">
                        Teste por 7 dias
                    </button>
                </div>
            </div>"""

new_ps = """            <!-- P.S. Emocional -->
            <div class="w-full p-8 md:p-14 bg-[#F9F6F0] rounded-3xl relative overflow-hidden shadow-inner border border-[#e2dfd8] text-center flex flex-col items-center">
                <div class="absolute top-0 right-0 w-[40%] h-[40%] bg-gradient-to-bl from-[#367CF5]/20 to-transparent rounded-full blur-3xl pointer-events-none"></div>
                <div class="absolute bottom-0 left-0 w-[40%] h-[40%] bg-gradient-to-tr from-[#A3E635]/10 to-transparent rounded-full blur-3xl pointer-events-none"></div>
                
                <h4 class="font-playfair italic text-4xl text-[#367CF5] mb-8 font-normal">P.S.</h4>
                <div class="space-y-6 text-lg md:text-xl text-zinc-700 leading-relaxed font-medium relative z-10 max-w-4xl mx-auto flex flex-col items-center">
                    <p>Se você chegou até aqui é porque alguma coisa ressoou. Talvez seja o cansaço de não saber pra onde o dinheiro vai. Talvez seja o desejo de finalmente planejar aquela viagem, aquela casa, aquela aposentadoria — e não ficar adiando porque "será que dá?".</p>
                    <p>O Atlas não é a resposta. É o caminho. Os 7 dias grátis são pra você descobrir se ele serve pra você — sem risco, sem compromisso, sem cartão.</p>
                    <p class="font-bold text-[#1a1a1a]">Você não precisa decidir agora se vai usar o Atlas pelos próximos 10 anos. Só precisa decidir se vale clicar e testar 7 dias.</p>
                    <a href="#section-8" class="mt-8 px-12 py-5 rounded-full font-bold text-2xl md:text-3xl bg-gradient-to-r from-[#AFFF00] via-[#8cdc18] to-[#AFFF00] bg-[length:200%_auto] text-[#1A2E05] transition-all shadow-[0_4px_24px_0_rgba(163,230,53,0.4)] animate-[bg-scroll_3s_linear_infinite] inline-block hover:-translate-y-1">
                        Teste por 7 dias
                    </a>
                </div>
            </div>"""

content = content.replace(old_ps, new_ps)

with open('index.html', 'w') as f:
    f.write(content)

