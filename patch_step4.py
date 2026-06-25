import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Replace the current Bento Grid (which has simple beige cards) with the highly animated rich cards.
new_grid = """        <!-- Bento Grid -->
        <div class="mx-auto w-full max-w-6xl">
            <div class="grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
                
                <!-- 1. Atlas Score (Restored) -->
                <div class="group relative bg-white border border-zinc-200 rounded-3xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div class="p-8 pb-4">
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Atlas Score</h3>
                        <p class="text-zinc-600 text-[15px] leading-relaxed">Em 2 segundos você sabe onde está. Score que se atualiza com cada decisão.</p>
                    </div>
                    <!-- UI Score Mockup -->
                    <div class="relative w-full border-t border-zinc-100 bg-zinc-50 h-48 overflow-hidden flex items-center justify-center p-6 mt-4">
                        <div class="bg-white rounded-2xl shadow-md border border-zinc-100 p-5 w-full max-w-[220px] flex flex-col items-center relative transform -rotate-2 group-hover:rotate-0 transition-transform duration-500">
                            <span class="text-[10px] text-zinc-400 font-bold uppercase tracking-widest mb-3">Atlas Score Atual</span>
                            <div class="relative w-24 h-24 mb-3 flex items-center justify-center">
                                <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                                    <path class="text-zinc-100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" stroke-width="2.5"></path>
                                    <path class="text-[#367CF5]" stroke-dasharray="85, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" class="animate-[dash_2s_ease-out_forwards]"></path>
                                </svg>
                                <div class="absolute flex flex-col items-center">
                                    <span class="text-3xl font-extrabold text-[#1a1a1a] tracking-tighter">850</span>
                                    <span class="text-[9px] font-bold text-green-600 bg-green-100 px-1.5 py-0.5 rounded-full -mt-1">+25 pts</span>
                                </div>
                            </div>
                            <div class="w-full bg-gradient-to-r from-blue-50 to-blue-100 text-[#367CF5] text-[10px] font-bold py-1.5 px-3 rounded-lg flex items-center justify-center gap-1.5 border border-blue-200">
                                Perfil: Mestre
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 2. Método Atlas (New) -->
                <div class="group relative bg-white border border-zinc-200 rounded-3xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div class="p-8 pb-4">
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Método Atlas</h3>
                        <p class="text-zinc-600 text-[15px] leading-relaxed">5 relatórios. Os mesmos diagnósticos que uso com clientes da Zephyr.</p>
                    </div>
                    <!-- Mockup: 5 stacked reports sliding up -->
                    <div class="relative w-full border-t border-zinc-100 bg-zinc-50 h-48 overflow-hidden flex items-end justify-center px-6 mt-4 perspective-[1000px]">
                        <div class="relative w-full max-w-[180px] h-32 transform-style-3d group-hover:rotate-x-12 transition-transform duration-500">
                            <div class="absolute bottom-0 w-full h-24 bg-white border border-zinc-200 rounded-t-xl shadow-md translate-y-4 group-hover:-translate-y-0 transition-transform duration-500 flex flex-col p-3 z-50">
                                <div class="w-8 h-1 bg-zinc-200 rounded mb-2"></div>
                                <div class="w-full h-1.5 bg-blue-100 rounded mb-1.5"></div>
                                <div class="w-2/3 h-1.5 bg-blue-100 rounded"></div>
                            </div>
                            <div class="absolute bottom-3 w-full h-24 bg-white/90 border border-zinc-200 rounded-t-xl shadow-sm scale-95 translate-y-4 group-hover:-translate-y-2 transition-transform duration-500 delay-75 z-40"></div>
                            <div class="absolute bottom-6 w-full h-24 bg-white/80 border border-zinc-200 rounded-t-xl shadow-sm scale-90 translate-y-4 group-hover:-translate-y-4 transition-transform duration-500 delay-100 z-30"></div>
                            <div class="absolute bottom-9 w-full h-24 bg-white/70 border border-zinc-200 rounded-t-xl shadow-sm scale-85 translate-y-4 group-hover:-translate-y-6 transition-transform duration-500 delay-150 z-20"></div>
                            <div class="absolute bottom-12 w-full h-24 bg-white/60 border border-zinc-200 rounded-t-xl shadow-sm scale-80 translate-y-4 group-hover:-translate-y-8 transition-transform duration-500 delay-200 z-10"></div>
                        </div>
                    </div>
                </div>

                <!-- 3. Vista da Montanha (Restored) -->
                <div class="group relative bg-white border border-zinc-200 rounded-3xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div class="p-8 pb-4">
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Vista da Montanha</h3>
                        <p class="text-zinc-600 text-[15px] leading-relaxed">Veja seu futuro financeiro mudar em tempo real. Cenários, não promessa.</p>
                    </div>
                    <!-- UI Dashboard Mockup -->
                    <div class="relative w-full border-t border-zinc-100 bg-zinc-50 h-48 overflow-hidden pt-4 px-6 mt-4">
                        <div class="flex items-center justify-between mb-2">
                            <div class="flex flex-col">
                                <span class="text-[8px] text-zinc-500 font-bold uppercase tracking-widest">Patrimônio Projetado</span>
                                <span class="text-lg font-extrabold text-[#1a1a1a] font-playfair tracking-tight">R$ 1.25M</span>
                            </div>
                        </div>
                        <div class="relative h-24 w-full flex items-end gap-1.5 px-2 pb-1 border-b border-zinc-200 z-10">
                            <div class="w-1/6 bg-blue-100 h-[20%] rounded-t relative group-hover:bg-blue-200 transition-colors"></div>
                            <div class="w-1/6 bg-blue-200 h-[35%] rounded-t group-hover:bg-blue-300 transition-colors delay-75"></div>
                            <div class="w-1/6 bg-blue-300 h-[50%] rounded-t group-hover:bg-blue-400 transition-colors delay-100"></div>
                            <div class="w-1/6 bg-blue-400 h-[65%] rounded-t relative group-hover:-translate-y-1 transition-transform">
                                <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-2.5 h-2.5 bg-white border-[2px] border-[#367CF5] rounded-full shadow-md z-20"></div>
                            </div>
                            <div class="w-1/6 bg-blue-500 h-[80%] rounded-t"></div>
                            <div class="w-1/6 bg-blue-600 h-[100%] rounded-t relative shadow-[0_0_10px_rgba(37,99,235,0.3)]"></div>
                            <svg class="absolute inset-0 w-full h-full pointer-events-none z-10" preserveAspectRatio="none" viewBox="0 0 100 100">
                                <path d="M 5,80 C 25,65 40,50 55,35 C 70,20 85,5 95,0" fill="none" stroke="rgba(54,124,245,0.5)" stroke-width="2" stroke-dasharray="4 4" class="[stroke-dashoffset:100] group-hover:animate-[dash_2s_linear_forwards]"></path>
                            </svg>
                        </div>
                    </div>
                </div>

                <!-- 4. Simulador de Decisão (Restored) -->
                <div class="group relative bg-white border border-zinc-200 rounded-3xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div class="p-8 pb-4">
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Simulador de Decisão</h3>
                        <p class="text-zinc-600 text-[15px] leading-relaxed">Comprar a casa? Trocar o carro? Decisões grandes com dados, não impulso.</p>
                    </div>
                    <!-- Caminhos A B C -->
                    <div class="relative w-full border-t border-zinc-100 bg-zinc-50 h-48 overflow-hidden flex items-center justify-center mt-4">
                        <div class="absolute inset-0 bg-[linear-gradient(45deg,#f4f4f5_25%,transparent_25%,transparent_75%,#f4f4f5_75%,#f4f4f5),linear-gradient(45deg,#f4f4f5_25%,transparent_25%,transparent_75%,#f4f4f5_75%,#f4f4f5)] bg-[length:20px_20px] bg-[position:0_0,10px_10px] opacity-40"></div>
                        <div class="relative z-10 flex items-center gap-3">
                            <div class="w-12 h-12 rounded-xl bg-white border border-zinc-200 shadow-sm flex items-center justify-center font-bold text-zinc-400">A</div>
                            <div class="flex flex-col gap-4 justify-center relative">
                                <div class="w-10 h-0.5 bg-zinc-300 transform -rotate-12 translate-y-2 relative overflow-hidden group-hover:bg-zinc-400 transition-colors"></div>
                                <div class="w-10 h-0.5 bg-[#367CF5] transform rotate-12 -translate-y-2 relative overflow-hidden">
                                    <div class="absolute top-0 left-0 h-full w-full bg-white opacity-50 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-1000"></div>
                                </div>
                            </div>
                            <div class="flex flex-col gap-3">
                                <div class="w-12 h-12 rounded-xl bg-white border border-zinc-200 shadow-sm flex items-center justify-center font-bold text-zinc-400 group-hover:scale-95 transition-transform">B</div>
                                <div class="w-12 h-12 rounded-xl bg-blue-50 border border-blue-200 shadow-md flex items-center justify-center font-bold text-[#367CF5] ring-2 ring-[#367CF5] ring-offset-2 ring-offset-zinc-50 group-hover:scale-110 transition-transform duration-300">C</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 5. Atlas IA (Restored) -->
                <div class="group relative bg-[#0B1A30] border border-blue-900 rounded-3xl shadow-md overflow-hidden flex flex-col justify-between">
                    <div class="p-8 pb-4">
                        <h3 class="text-xl font-bold text-white mb-3 flex items-center gap-2">
                            Atlas IA
                            <span class="relative flex h-2 w-2"><span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#A3E635] opacity-75"></span><span class="relative inline-flex rounded-full h-2 w-2 bg-[#A3E635]"></span></span>
                        </h3>
                        <p class="text-blue-100/70 text-[15px] leading-relaxed">Pergunta como pra um amigo. Responde como um planejador. Conhece seus números.</p>
                    </div>
                    <!-- Glow Animation -->
                    <div class="relative w-full border-t border-white/10 h-48 overflow-hidden flex items-center justify-center mt-4">
                        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(54,124,245,0.4)_0%,transparent_70%)]"></div>
                        <div class="relative group-hover:scale-110 transition-transform duration-700">
                            <div class="absolute inset-0 animate-ping rounded-full bg-[#367CF5] opacity-30 duration-1000"></div>
                            <div class="w-14 h-14 bg-gradient-to-tr from-[#367CF5] to-blue-400 rounded-full shadow-[0_0_40px_rgba(54,124,245,0.8)] flex items-center justify-center relative z-10">
                                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 6. Investimentos + Proventos (New) -->
                <div class="group relative bg-white border border-zinc-200 rounded-3xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div class="p-8 pb-4">
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Investimentos + Proventos</h3>
                        <p class="text-zinc-600 text-[15px] leading-relaxed">Carteira viva. Descubra quando sua renda passiva vai te libertar.</p>
                    </div>
                    <!-- Progress Bar to Freedom -->
                    <div class="relative w-full border-t border-zinc-100 bg-zinc-50 h-48 overflow-hidden flex flex-col items-center justify-center p-6 mt-4">
                        <div class="w-full flex justify-between text-[10px] font-bold text-zinc-400 uppercase tracking-widest mb-2">
                            <span>Renda Atual</span>
                            <span class="text-green-600">Liberdade</span>
                        </div>
                        <div class="w-full h-3 bg-zinc-200 rounded-full overflow-hidden relative">
                            <div class="h-full bg-[#367CF5] w-[40%] rounded-full group-hover:w-[80%] transition-all duration-1000 ease-out relative">
                                <div class="absolute top-0 right-0 bottom-0 w-4 bg-white/30 animate-pulse"></div>
                            </div>
                        </div>
                        <div class="mt-4 flex items-center gap-2 text-xs font-bold text-zinc-700 bg-white px-3 py-1.5 rounded-lg border border-zinc-200 shadow-sm transform group-hover:-translate-y-1 transition-transform">
                            <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                            R$ 4.500 / mês projetado
                        </div>
                    </div>
                </div>

                <!-- 7. Atlas Negócios (New) -->
                <div class="group relative bg-white border border-zinc-200 rounded-3xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div class="p-8 pb-4">
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Atlas Negócios</h3>
                        <p class="text-zinc-600 text-[15px] leading-relaxed">PF e PJ na mesma jornada. Para autônomos, MEIs e donos de empresa.</p>
                    </div>
                    <!-- PF / PJ Integration -->
                    <div class="relative w-full border-t border-zinc-100 bg-zinc-50 h-48 overflow-hidden flex items-center justify-center gap-6 mt-4">
                        <div class="flex flex-col items-center gap-2 group-hover:-translate-x-2 transition-transform duration-500">
                            <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center text-[#367CF5] border-2 border-white shadow-md font-bold text-sm">PF</div>
                        </div>
                        <div class="flex flex-col gap-1 items-center z-10 relative">
                            <div class="w-8 h-8 bg-white border border-zinc-200 rounded-full flex items-center justify-center shadow-sm group-hover:rotate-180 transition-transform duration-700">
                                <svg class="w-4 h-4 text-zinc-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"></path></svg>
                            </div>
                        </div>
                        <div class="flex flex-col items-center gap-2 group-hover:translate-x-2 transition-transform duration-500">
                            <div class="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center text-purple-600 border-2 border-white shadow-md font-bold text-sm">PJ</div>
                        </div>
                    </div>
                </div>

                <!-- 8. Household (Restored) -->
                <div class="group relative bg-white border border-zinc-200 rounded-3xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div class="p-8 pb-4">
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Household</h3>
                        <p class="text-zinc-600 text-[15px] leading-relaxed">Finanças do casal sem briga. Convide sem dar senha.</p>
                    </div>
                    <!-- Overlapping Avatars -->
                    <div class="relative w-full border-t border-zinc-100 bg-zinc-50 h-48 overflow-hidden flex items-center justify-center mt-4">
                        <div class="flex -space-x-4 group-hover:-space-x-2 transition-all duration-500">
                            <div class="w-16 h-16 rounded-full border-4 border-white bg-blue-50 flex items-center justify-center shadow-md relative z-20 group-hover:rotate-[-10deg] transition-transform">
                                <svg class="w-6 h-6 text-[#367CF5]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
                            </div>
                            <div class="w-16 h-16 rounded-full border-4 border-white bg-green-50 flex items-center justify-center shadow-md relative z-10 group-hover:rotate-[10deg] transition-transform">
                                <svg class="w-6 h-6 text-[#1A2E05]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 9. Plano da Liberdade (New) -->
                <div class="group relative bg-white border border-zinc-200 rounded-3xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div class="p-8 pb-4">
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3">Plano da Liberdade</h3>
                        <p class="text-zinc-600 text-[15px] leading-relaxed">33 aulas. O método em vídeo. Disponível no Elite.</p>
                    </div>
                    <!-- Video Player Mockup -->
                    <div class="relative w-full border-t border-zinc-100 bg-zinc-50 h-48 overflow-hidden flex items-center justify-center p-6 mt-4">
                        <div class="w-full max-w-[200px] bg-white border border-zinc-200 rounded-xl shadow-sm overflow-hidden group-hover:shadow-lg transition-shadow">
                            <!-- Video area -->
                            <div class="h-20 bg-zinc-800 relative flex items-center justify-center">
                                <div class="w-8 h-8 bg-[#367CF5] rounded-full flex items-center justify-center text-white shadow-lg group-hover:scale-110 transition-transform duration-300">
                                    <svg class="w-4 h-4 ml-0.5" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                                </div>
                            </div>
                            <!-- Controls -->
                            <div class="p-3 bg-white">
                                <div class="w-full h-1 bg-zinc-100 rounded-full mb-2 overflow-hidden">
                                    <div class="h-full bg-[#367CF5] w-[30%] group-hover:w-[100%] transition-all duration-2000 ease-out"></div>
                                </div>
                                <div class="w-1/2 h-2 bg-zinc-200 rounded"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>"""

content = re.sub(r'<!-- Bento Grid -->\s*<div class="mx-auto w-full max-w-6xl">.*?</div>\s*<!-- Footer Text -->', new_grid + '\n            \n            <!-- Footer Text -->', content, flags=re.DOTALL)

with open(filepath, 'w') as f:
    f.write(content)

