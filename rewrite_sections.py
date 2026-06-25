import re

with open('funcionalidades.html', 'r') as f:
    content = f.read()

metodo_html = """            <!-- Método Atlas [PRO] -->
            <section class="feature-section" id="metodo" class="scroll-mt-32">
                <div class="mb-8 flex items-center gap-3">
                    <h2 class="text-3xl font-bold text-[#0F172A]">Método Atlas (Consultoria IA)</h2>
                    <span class="bg-[#367CF5] text-white text-xs font-bold px-2.5 py-1 rounded-md">PRO</span>
                </div>
                <p class="text-zinc-500 text-lg mb-8">Cinco relatórios profundos gerados sob demanda por Inteligência Artificial sobre os seus dados. O trabalho de um planejador financeiro automatizado.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="group bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm hover:shadow-md transition-shadow md:col-span-2">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">1. A Vista da Montanha</h3>
                        <p class="text-zinc-600 text-sm">A projeção do seu patrimônio até o fim da vida em um gráfico vivo. Arraste o aporte ou a rentabilidade e veja a curva mudar na hora. Adicione "eventos" (ex: ter filho) e veja o tranco financeiro a longo prazo.</p>
                        <div class="h-48 bg-zinc-50 rounded-xl border border-zinc-200 mt-4 overflow-hidden relative group-hover:border-[#367CF5]/40 transition-colors duration-500 flex items-end">
                            <svg class="w-full h-full absolute inset-0" viewBox="0 0 400 150" preserveAspectRatio="none">
                                <defs>
                                    <linearGradient id="grad1" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="0%" stop-color="#367CF5" stop-opacity="0.2" />
                                        <stop offset="100%" stop-color="#367CF5" stop-opacity="0" />
                                    </linearGradient>
                                </defs>
                                <path fill="url(#grad1)" stroke="none" d="M0,150 C100,140 200,100 400,20 L400,150 L0,150 Z" opacity="0" class="group-hover:opacity-100 transition-opacity duration-1000 delay-300"></path>
                                <path class="text-[#367CF5]" stroke="currentColor" stroke-width="3" fill="none" d="M0,150 C100,140 200,100 400,20" stroke-dasharray="600" stroke-dashoffset="600">
                                    <animate attributeName="stroke-dashoffset" values="600;0" dur="2s" fill="freeze" begin="mouseover" />
                                </path>
                                <circle cx="400" cy="20" r="5" fill="#367CF5" opacity="0">
                                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="mouseover+1.8s" fill="freeze" />
                                    <animate attributeName="r" values="5;8;5" dur="1.5s" repeatCount="indefinite" begin="mouseover+1.8s" />
                                </circle>
                            </svg>
                        </div>
                    </div>
                    <div class="group bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm hover:shadow-md transition-shadow">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">2. Base da Montanha</h3>
                        <p class="text-zinc-600 text-sm">Raio-X da fundação: reserva em meses, liquidez, e um "Semáforo" dizendo a recomendação mais urgente que você deve seguir hoje.</p>
                        <div class="h-40 bg-zinc-50 rounded-xl border border-zinc-200 mt-4 overflow-hidden relative flex flex-col justify-center px-6 gap-6 group-hover:border-[#367CF5]/40 transition-colors duration-500">
                            <div>
                                <div class="flex justify-between text-xs font-bold text-zinc-500 mb-2"><span>Reserva de Emergência</span><span class="text-green-600">6 Meses</span></div>
                                <div class="h-3 bg-zinc-200 rounded-full overflow-hidden">
                                    <div class="h-full bg-green-500 w-0 transition-all duration-1000 ease-out group-hover:w-full"></div>
                                </div>
                            </div>
                            <div class="flex items-center gap-3">
                                <span class="text-xs font-bold text-zinc-400">Status:</span>
                                <div class="flex gap-2 p-2 bg-white rounded-lg border border-zinc-200 shadow-sm">
                                    <div class="w-3 h-3 rounded-full bg-zinc-200 group-hover:bg-red-500/20 transition-colors"></div>
                                    <div class="w-3 h-3 rounded-full bg-zinc-200 group-hover:bg-yellow-500/20 transition-colors"></div>
                                    <div class="w-3 h-3 rounded-full bg-zinc-200 group-hover:bg-green-500 group-hover:shadow-[0_0_8px_rgba(34,197,94,0.6)] transition-all delay-500"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="group bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm hover:shadow-md transition-shadow">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">3. Estratégia de Subida</h3>
                        <p class="text-zinc-600 text-sm">Cruza sua capacidade com seus sonhos. Avalia a viabilidade do plano, aponta o "gap" financeiro e o que deve ser ajustado.</p>
                        <div class="h-40 bg-zinc-50 rounded-xl border border-zinc-200 mt-4 overflow-hidden relative flex items-center justify-center group-hover:border-[#367CF5]/40 transition-colors duration-500">
                            <div class="relative w-28 h-28">
                                <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                                    <circle cx="18" cy="18" r="16" fill="none" class="stroke-zinc-200" stroke-width="3"></circle>
                                    <circle cx="18" cy="18" r="16" fill="none" class="stroke-[#367CF5]" stroke-width="3" stroke-dasharray="100" stroke-dashoffset="100">
                                        <animate attributeName="stroke-dashoffset" values="100;25" dur="1.5s" fill="freeze" begin="mouseover" />
                                    </circle>
                                </svg>
                                <div class="absolute inset-0 flex flex-col items-center justify-center">
                                    <span class="font-bold text-2xl text-zinc-800">75%</span>
                                    <span class="text-[8px] uppercase tracking-wider text-zinc-400 font-bold">Viável</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="group bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm hover:shadow-md transition-shadow">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">4. Controle da Jornada</h3>
                        <p class="text-zinc-600 text-sm">O acompanhamento do fluxo de caixa: onde você está se desviando e alertas operacionais para manter o plano nos trilhos.</p>
                        <div class="h-40 bg-zinc-50 rounded-xl border border-zinc-200 mt-4 overflow-hidden relative flex flex-col justify-center px-4 gap-3 group-hover:border-[#367CF5]/40 transition-colors duration-500">
                            <div class="bg-white border border-zinc-200 p-3 rounded-lg shadow-sm transform translate-y-4 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-500 delay-100 flex items-center gap-3">
                                <div class="w-8 h-8 rounded-full bg-red-100 flex items-center justify-center text-red-500">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                                </div>
                                <div>
                                    <div class="text-xs font-bold text-zinc-800">Alerta de Gastos</div>
                                    <div class="text-[10px] text-zinc-500">Orçamento de Lazer excedido.</div>
                                </div>
                            </div>
                            <div class="bg-white border border-zinc-200 p-3 rounded-lg shadow-sm transform translate-y-4 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-500 delay-300 flex items-center gap-3">
                                <div class="w-8 h-8 rounded-full bg-green-100 flex items-center justify-center text-green-500">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                </div>
                                <div>
                                    <div class="text-xs font-bold text-zinc-800">Meta Concluída</div>
                                    <div class="text-[10px] text-zinc-500">Reserva 100% preenchida.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="group bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm hover:shadow-md transition-shadow">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">5. Guia da Jornada</h3>
                        <p class="text-zinc-600 text-sm">O relatório integrado final: diagnóstico executivo, prioridades e um Plano de Ação concreto. Gere em PDF como se tivesse saído de uma reunião de consultoria.</p>
                        <div class="h-40 bg-zinc-50 rounded-xl border border-zinc-200 mt-4 overflow-hidden relative flex items-center justify-center group-hover:border-[#367CF5]/40 transition-colors duration-500">
                            <div class="flex flex-col items-center">
                                <div class="w-16 h-20 bg-white border-2 border-zinc-200 rounded-lg shadow-md flex flex-col items-center justify-center p-2 group-hover:border-[#367CF5] group-hover:shadow-[0_0_20px_rgba(54,124,245,0.2)] transition-all duration-500 relative transform group-hover:-translate-y-2">
                                    <div class="w-full flex justify-between px-1 mb-2">
                                        <div class="w-2 h-0.5 bg-zinc-200 rounded"></div>
                                        <div class="w-4 h-0.5 bg-zinc-200 rounded"></div>
                                    </div>
                                    <div class="w-8 h-8 rounded bg-[#367CF5]/10 flex items-center justify-center text-[#367CF5] mb-2">
                                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clip-rule="evenodd"></path></svg>
                                    </div>
                                    <div class="h-1 w-8 bg-zinc-200 rounded"></div>
                                    <div class="absolute -right-2 -bottom-2 w-6 h-6 bg-green-500 rounded-full border-2 border-white flex items-center justify-center text-white opacity-0 group-hover:opacity-100 transition-opacity duration-300 delay-300 scale-0 group-hover:scale-100">
                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""

# Re-generate the courses grid for the education section
courses = [
    ("Manual do Dinheiro", "M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"),
    ("Plano da Liberdade", "M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"),
    ("Organização na Prática", "M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"),
    ("Planejamento Financeiro", "M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"),
    ("Dominando o Variável", "M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"),
    ("Renda Passiva com FIIs", "M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"),
    ("Finanças do Casal", "M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"),
    ("Planejamento Tributário", "M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"),
    ("O Novo Mapa do Dinheiro", "M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9")
]

grid_html = '<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">\n'
for name, icon_path in courses:
    card = f'''                    <div class="group relative bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm hover:shadow-xl hover:border-[#367CF5]/30 transition-all duration-500 hover:-translate-y-2 overflow-hidden flex flex-col items-center text-center cursor-default">
                        <div class="absolute inset-0 bg-gradient-to-b from-[#eff4ff]/0 to-[#eff4ff]/50 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
                        <div class="w-16 h-16 mb-4 bg-zinc-50 rounded-full flex items-center justify-center group-hover:scale-110 group-hover:bg-[#367CF5] transition-all duration-500 shadow-inner group-hover:shadow-[0_0_20px_rgba(54,124,245,0.4)] relative z-10">
                            <svg class="w-8 h-8 text-zinc-400 group-hover:text-white transition-colors duration-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                                <path d="{icon_path}"></path>
                            </svg>
                        </div>
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2 group-hover:text-[#367CF5] transition-colors duration-500 relative z-10">{name}</h3>
                        <div class="h-1 w-8 bg-zinc-200 rounded-full mt-2 group-hover:w-16 group-hover:bg-[#367CF5] transition-all duration-500 relative z-10"></div>
                    </div>\n'''
    grid_html += card
grid_html += '                </div>'

educacao_html = f"""            <!-- Ecossistema de Educação -->
            <section class="feature-section" id="educacao" class="scroll-mt-32">
                <div class="mb-8 flex items-center gap-3">
                    <h2 class="text-3xl font-bold text-[#0F172A]">Ecossistema de Educação</h2>
                    <span class="bg-amber-400 text-[#1A2E05] text-xs font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">Em breve</span>
                </div>
                <p class="text-zinc-500 text-lg mb-8">O mapa completo da sua jornada financeira. Tenha acesso a treinamentos profundos e práticos para dominar o seu dinheiro em cada estágio da vida.</p>
                
                {grid_html}
            </section>
"""

# Now replace the two sections in content.
# The previous script replaced #metodo with the courses.
# The content currently has a #metodo section with courses grid.
# And an #educacao section with the old hardcoded list.

pattern_metodo = r'<!-- Método Atlas \[PRO\] -->.*?id="metodo".*?</section>'
pattern_educacao = r'<!-- Ecossistema de Educação -->.*?id="educacao".*?</section>'

content = re.sub(pattern_metodo, metodo_html.strip(), content, count=1, flags=re.DOTALL)
content = re.sub(pattern_educacao, educacao_html.strip(), content, count=1, flags=re.DOTALL)

with open('funcionalidades.html', 'w') as f:
    f.write(content)

