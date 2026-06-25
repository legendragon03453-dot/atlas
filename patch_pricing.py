import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Update color in Section 7
old_color_text = '<strong class="font-playfair italic font-normal text-3xl md:text-4xl text-[#36DCF5]">É o mapa que meus pais não tiveram quando precisaram.</strong>'
new_color_text = '<strong class="font-playfair italic font-normal text-3xl md:text-4xl text-[#367CF5]">É o mapa que meus pais não tiveram quando precisaram.</strong>'
content = content.replace(old_color_text, new_color_text)

# 2. Build Section 8
section8 = """
    <!-- === SEÇÃO 8: Pricing === -->
    <section id="section-8" class="w-full bg-gradient-to-b from-white to-[#f4f7fe] py-20 lg:py-32 px-4 relative border-t border-zinc-200">
        <div class="container mx-auto max-w-6xl">
            
            <!-- Header Pricing -->
            <div class="flex flex-col items-center text-center gap-6 mb-16">
                <div class="px-4 py-1.5 rounded-full border border-blue-200 bg-white shadow-sm text-sm font-semibold text-zinc-700">
                    Escolha o nível certo para sua jornada
                </div>
                <h2 class="text-4xl md:text-5xl lg:text-6xl font-bold text-[#1a1a1a] tracking-tight max-w-3xl">
                    E agora você também pode usar ele!
                </h2>
                
                <!-- Toggle Mensal/Anual -->
                <div class="flex items-center mt-4 bg-white border border-blue-100 p-1.5 rounded-full shadow-sm">
                    <button class="px-6 py-2 rounded-full bg-[#367CF5] text-white font-semibold text-sm transition-all shadow-md">Mensal</button>
                    <button class="px-6 py-2 rounded-full text-zinc-500 font-semibold text-sm hover:text-zinc-800 transition-all">Anual</button>
                </div>
            </div>

            <!-- 3 Cards Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8 max-w-5xl mx-auto mb-20 relative z-10">
                
                <!-- Essencial -->
                <div class="bg-white rounded-3xl p-8 border border-zinc-200 shadow-sm flex flex-col justify-between">
                    <div>
                        <h3 class="text-2xl font-bold text-[#1a1a1a] mb-2">Essencial</h3>
                        <p class="text-zinc-500 text-sm mb-6 h-10">Para quem quer começar a enxergar.</p>
                        <div class="flex items-end gap-1 mb-8">
                            <span class="text-4xl font-bold text-[#1a1a1a]">R$ 15,90</span>
                            <span class="text-zinc-500 font-medium mb-1">/mês</span>
                        </div>
                        <button class="w-full py-4 rounded-xl bg-[#0B1A30] text-white font-bold hover:bg-[#1a2e4f] transition-all shadow-[0_4px_14px_0_rgba(11,26,48,0.39)]">Assinar Plano</button>
                    </div>
                    
                    <ul class="mt-8 space-y-4">
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Controle financeiro do dia a dia</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Análises Básicas e Atlas Score</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Acesso à Comunidade</span></li>
                    </ul>
                </div>

                <!-- Pro (Destaque Animado) -->
                <div class="bg-[#eff4ff] rounded-3xl p-8 border-2 border-[#367CF5] shadow-[0_0_30px_rgba(54,124,245,0.2)] flex flex-col justify-between relative transform md:-translate-y-4 [animation:pulse_4s_ease-in-out_infinite]">
                    <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-[#367CF5] text-white text-xs font-bold px-4 py-1 rounded-full shadow-md uppercase tracking-wide">
                        Mais Escolhido
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-[#1a1a1a] mb-2">Pro</h3>
                        <p class="text-zinc-500 text-sm mb-6 h-10">Para quem quer planejar o futuro.</p>
                        <div class="flex items-end gap-1 mb-8">
                            <span class="text-4xl font-bold text-[#1a1a1a]">R$ 24,90</span>
                            <span class="text-zinc-500 font-medium mb-1">/mês</span>
                        </div>
                        <button class="w-full py-4 rounded-xl bg-[#A3E635] text-[#0B1A30] font-extrabold hover:bg-[#8cdc18] transition-all shadow-[0_4px_14px_0_rgba(163,230,53,0.39)]">Assinar Plano</button>
                    </div>
                    
                    <ul class="mt-8 space-y-4">
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm font-semibold text-[#1a1a1a]">Tudo do Essencial</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Planejamento longo prazo & Cenários</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Método Atlas (Relatórios IA)</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Atlas Negócios & Importações</span></li>
                    </ul>
                </div>

                <!-- Elite -->
                <div class="bg-white rounded-3xl p-8 border border-zinc-200 shadow-sm flex flex-col justify-between">
                    <div>
                        <h3 class="text-2xl font-bold text-[#1a1a1a] mb-2">Elite</h3>
                        <p class="text-zinc-500 text-sm mb-6 h-10">Para quem quer maestria financeira.</p>
                        <div class="flex items-end gap-1 mb-8">
                            <span class="text-4xl font-bold text-[#1a1a1a]">R$ 32,90</span>
                            <span class="text-zinc-500 font-medium mb-1">/mês</span>
                        </div>
                        <button class="w-full py-4 rounded-xl bg-[#0B1A30] text-white font-bold hover:bg-[#1a2e4f] transition-all shadow-[0_4px_14px_0_rgba(11,26,48,0.39)]">Assinar Plano</button>
                    </div>
                    
                    <ul class="mt-8 space-y-4">
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm font-semibold text-[#1a1a1a]">Tudo do Pro</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Cursos Avançados</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Plano da Liberdade Integrado</span></li>
                        <li class="flex items-start gap-3"><svg class="w-5 h-5 text-[#367CF5] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg><span class="text-sm text-zinc-700">Suporte Prioritário</span></li>
                    </ul>
                </div>

            </div>

            <!-- Tabela Comparativa (Desktop Only) -->
            <div class="hidden lg:block w-full mt-24">
                <h3 class="text-2xl font-bold text-center mb-10 text-[#1a1a1a]">Compare todas as funcionalidades</h3>
                
                <div class="grid grid-cols-4 divide-x divide-zinc-200 border-t border-b border-zinc-200 bg-white shadow-sm rounded-xl overflow-hidden text-sm">
                    <!-- Cabecalho da tabela -->
                    <div class="bg-zinc-50 p-6 font-bold text-zinc-700 flex items-center">Funcionalidades</div>
                    <div class="bg-zinc-50 p-6 font-bold text-center text-zinc-900 text-lg">Essencial</div>
                    <div class="bg-[#eff4ff] p-6 font-bold text-center text-[#367CF5] text-lg border-b-2 border-[#367CF5]">Pro</div>
                    <div class="bg-zinc-50 p-6 font-bold text-center text-zinc-900 text-lg">Elite</div>

                    <!-- Row 1 -->
                    <div class="p-4 px-6 text-zinc-700 font-medium">Controle do dia a dia</div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>

                    <!-- Row 2 -->
                    <div class="p-4 px-6 text-zinc-700 font-medium bg-zinc-50/50">Atlas Score & Simuladores Básicos</div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center bg-[#eff4ff]/50"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>

                    <!-- Row 3 -->
                    <div class="p-4 px-6 text-zinc-700 font-medium">Atlas Chat</div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>

                    <!-- Row 4 -->
                    <div class="p-4 px-6 text-zinc-700 font-medium bg-zinc-50/50">Planejamento Longo Prazo</div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50"><svg class="w-5 h-5 text-zinc-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"></path></svg></div>
                    <div class="p-4 flex justify-center items-center bg-[#eff4ff]/50"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>

                    <!-- Row 5 -->
                    <div class="p-4 px-6 text-zinc-700 font-medium">Método Atlas (Relatórios IA)</div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-zinc-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>

                    <!-- Row 6 -->
                    <div class="p-4 px-6 text-zinc-700 font-medium bg-zinc-50/50">Atlas Negócios & Importações</div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50"><svg class="w-5 h-5 text-zinc-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"></path></svg></div>
                    <div class="p-4 flex justify-center items-center bg-[#eff4ff]/50"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>

                    <!-- Row 7 -->
                    <div class="p-4 px-6 text-zinc-700 font-medium">Cursos Avançados (Liberdade)</div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-zinc-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-zinc-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    
                    <!-- Row 8 (Text) -->
                    <div class="p-4 px-6 text-zinc-700 font-medium bg-zinc-50/50">Suporte</div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50 text-zinc-500 font-medium">Comunidade</div>
                    <div class="p-4 flex justify-center items-center bg-[#eff4ff]/50 text-zinc-700 font-medium">Email</div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50 text-zinc-700 font-medium">Prioritário</div>

                </div>
            </div>

        </div>
    </section>
"""

# Append section 8
script_tag = content.find('<script>')
if script_tag != -1:
    content = content[:script_tag] + section8 + content[script_tag:]

with open(filepath, 'w') as f:
    f.write(content)
