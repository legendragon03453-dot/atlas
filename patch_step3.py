import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Remove dynamic border HTML
content = re.sub(r'<!-- Border overlay animada -->\s*<div id="dynamic-border"[^>]*></div>\s*', '', content)

# 2. Remove GSAP dynamic border logic
content = re.sub(r'// GSAP: Animação de borda dinâmica.*?gsap\.to\("#dynamic-border".*?\}\);', '', content, flags=re.DOTALL)

# 3. Revert body background
content = content.replace('background-color: #ffffff; /* Cor de fundo branca para o efeito de borda */', 'background-color: #367CF5; /* Cor de fundo base caso o vídeo falhe */')

# 4. Replace Bento Grid
new_grid = """        <!-- Bento Grid -->
        <div class="mx-auto w-full max-w-6xl">
            <div class="grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
                <!-- 1. Atlas Score -->
                <div class="bg-[#F6F4F0] rounded-3xl p-8 flex flex-col justify-start">
                    <div class="w-10 h-10 mb-8 text-[#1a1a1a]">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Atlas Score</h3>
                    <p class="text-zinc-600 text-[15px] leading-relaxed">Em 2 segundos você sabe onde está. Score que se atualiza com cada decisão.</p>
                </div>
                <!-- 2. Método Atlas -->
                <div class="bg-[#F6F4F0] rounded-3xl p-8 flex flex-col justify-start">
                    <div class="w-10 h-10 mb-8 text-[#1a1a1a]">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Método Atlas</h3>
                    <p class="text-zinc-600 text-[15px] leading-relaxed">5 relatórios. Os mesmos diagnósticos que uso com clientes da Zephyr.</p>
                </div>
                <!-- 3. Vista da Montanha -->
                <div class="bg-[#F6F4F0] rounded-3xl p-8 flex flex-col justify-start">
                    <div class="w-10 h-10 mb-8 text-[#1a1a1a]">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Vista da Montanha</h3>
                    <p class="text-zinc-600 text-[15px] leading-relaxed">Veja seu futuro financeiro mudar em tempo real. Cenários, não promessa.</p>
                </div>
                <!-- 4. Simulador de Decisão -->
                <div class="bg-[#F6F4F0] rounded-3xl p-8 flex flex-col justify-start">
                    <div class="w-10 h-10 mb-8 text-[#1a1a1a]">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Simulador de Decisão</h3>
                    <p class="text-zinc-600 text-[15px] leading-relaxed">Comprar a casa? Trocar o carro? Decisões grandes com dados, não impulso.</p>
                </div>
                <!-- 5. Atlas IA -->
                <div class="bg-[#F6F4F0] rounded-3xl p-8 flex flex-col justify-start">
                    <div class="w-10 h-10 mb-8 text-[#1a1a1a]">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Atlas IA</h3>
                    <p class="text-zinc-600 text-[15px] leading-relaxed">Pergunta como pra um amigo. Responde como um planejador. Conhece seus números.</p>
                </div>
                <!-- 6. Investimentos + Proventos -->
                <div class="bg-[#F6F4F0] rounded-3xl p-8 flex flex-col justify-start">
                    <div class="w-10 h-10 mb-8 text-[#1a1a1a]">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Investimentos + Proventos</h3>
                    <p class="text-zinc-600 text-[15px] leading-relaxed">Carteira viva. Descubra quando sua renda passiva vai te libertar.</p>
                </div>
                <!-- 7. Atlas Negócios -->
                <div class="bg-[#F6F4F0] rounded-3xl p-8 flex flex-col justify-start">
                    <div class="w-10 h-10 mb-8 text-[#1a1a1a]">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Atlas Negócios</h3>
                    <p class="text-zinc-600 text-[15px] leading-relaxed">PF e PJ na mesma jornada. Para autônomos, MEIs e donos de empresa.</p>
                </div>
                <!-- 8. Household -->
                <div class="bg-[#F6F4F0] rounded-3xl p-8 flex flex-col justify-start">
                    <div class="w-10 h-10 mb-8 text-[#1a1a1a]">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Household</h3>
                    <p class="text-zinc-600 text-[15px] leading-relaxed">Finanças do casal sem briga. Convide sem dar senha.</p>
                </div>
                <!-- 9. Plano da Liberdade -->
                <div class="bg-[#F6F4F0] rounded-3xl p-8 flex flex-col justify-start">
                    <div class="w-10 h-10 mb-8 text-[#1a1a1a]">
                        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477-4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                    </div>
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Plano da Liberdade</h3>
                    <p class="text-zinc-600 text-[15px] leading-relaxed">33 aulas. O método em vídeo. Disponível no Elite.</p>
                </div>
            </div>
            
            <!-- Footer Text -->
            <div class="mt-16 flex flex-wrap justify-center items-center gap-4 md:gap-8 text-[#1a1a1a] font-medium text-[13px] tracking-wide">
                <span class="flex items-center gap-2"><span class="text-zinc-400">+</span> Aposentadoria mapeada</span>
                <span class="flex items-center gap-2"><span class="text-zinc-400">+</span> Notificações inteligentes</span>
                <span class="flex items-center gap-2"><span class="text-zinc-400">+</span> Web + Celular (PWA)</span>
            </div>
        </div>
"""

content = re.sub(r'<!-- Bento Grid -->\s*<div class="mx-auto w-full max-w-6xl">.*?</div>\s*</div>\s*</section>', new_grid + '\n    </section>', content, flags=re.DOTALL)

# Also change section-6 background to #FAF8F5
content = content.replace('<section id="section-6" class="w-full bg-white', '<section id="section-6" class="w-full bg-[#FAF8F5]')

with open(filepath, 'w') as f:
    f.write(content)

