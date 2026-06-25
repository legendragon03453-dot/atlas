import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# --- Task 5: Bento Grid UI Mockups ---

# Card 1: Vista da Montanha
old_card_1_illustration = """                    <!-- Ilustração SVG -->
                    <div class="relative w-full border-t border-dashed border-zinc-200 bg-zinc-50/50 h-56 md:h-64 overflow-hidden flex items-end justify-center pt-8 px-6 md:px-12 mt-6">
                        <div class="absolute inset-0 bg-[linear-gradient(to_right,#e5e7eb_1px,transparent_1px),linear-gradient(to_bottom,#e5e7eb_1px,transparent_1px)] bg-[size:24px_24px] opacity-60"></div>
                        
                        <!-- Marcadores flutuantes -->
                        <div class="absolute bottom-6 left-[15%] animate-float z-20" style="animation-delay: 0s;">
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
                        </div>
                        <svg class="w-full h-full text-[#367CF5] drop-shadow-[0_10px_15px_rgba(54,124,245,0.4)] relative z-10" viewBox="0 0 500 120" preserveAspectRatio="none">

                            <path d="M0,120 C50,110 100,70 150,80 C200,90 250,30 300,50 C350,70 400,20 450,10 L500,0 L500,120 Z" fill="url(#mountainGrad)" stroke="currentColor" stroke-width="4"></path>
                            <defs>
                                <linearGradient id="mountainGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                                    <stop offset="0%" stop-color="rgba(54,124,245,0.3)"/>
                                    <stop offset="100%" stop-color="rgba(54,124,245,0)"/>
                                </linearGradient>
                            </defs>
                        </svg>
                    </div>"""

new_card_1_illustration = """                    <!-- UI Dashboard Mockup -->
                    <div class="relative w-full border-t border-zinc-200 bg-zinc-50 h-56 md:h-64 overflow-hidden pt-6 px-6 mt-6">
                        <!-- Top Bar UI -->
                        <div class="flex items-center justify-between mb-4">
                            <div class="flex flex-col">
                                <span class="text-[10px] text-zinc-500 font-bold uppercase tracking-widest">Patrimônio Projetado</span>
                                <span class="text-xl md:text-2xl font-extrabold text-[#1a1a1a] font-playfair tracking-tight">R$ 1.250.000</span>
                            </div>
                            <div class="px-2 py-1 bg-green-100 text-green-700 text-[10px] font-bold rounded flex items-center gap-1 shadow-sm">
                                +15% <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
                            </div>
                        </div>
                        
                        <!-- Chart Area Mockup -->
                        <div class="relative h-32 w-full flex items-end gap-2 px-2 pb-2 border-b border-zinc-200 z-10">
                            <!-- Bars -->
                            <div class="w-1/6 bg-blue-100 h-[20%] rounded-t relative group transition-all duration-500 hover:bg-blue-200"></div>
                            <div class="w-1/6 bg-blue-200 h-[35%] rounded-t transition-all duration-500 hover:bg-blue-300"></div>
                            <div class="w-1/6 bg-blue-300 h-[50%] rounded-t transition-all duration-500 hover:bg-blue-400"></div>
                            <div class="w-1/6 bg-blue-400 h-[65%] rounded-t relative transition-all duration-500">
                                <!-- Marker -->
                                <div class="absolute -top-3 left-1/2 -translate-x-1/2 w-3 h-3 bg-white border-[3px] border-[#367CF5] rounded-full shadow-md z-20"></div>
                                <div class="absolute -top-10 left-1/2 -translate-x-1/2 bg-[#367CF5] text-white text-[9px] font-bold px-2 py-1 rounded shadow-lg whitespace-nowrap z-20 animate-float">Você está aqui
                                   <div class="absolute -bottom-1 left-1/2 -translate-x-1/2 border-l-4 border-r-4 border-t-4 border-transparent border-t-[#367CF5]"></div>
                                </div>
                            </div>
                            <div class="w-1/6 bg-blue-500 h-[80%] rounded-t transition-all duration-500"></div>
                            <div class="w-1/6 bg-blue-600 h-[100%] rounded-t relative transition-all duration-500 shadow-[0_0_15px_rgba(37,99,235,0.4)]">
                                <div class="absolute -top-6 left-1/2 -translate-x-1/2 text-blue-700 text-[10px] font-bold">Meta</div>
                            </div>
                            
                            <!-- Projection Line Overlay -->
                            <svg class="absolute inset-0 w-full h-full pointer-events-none z-10" preserveAspectRatio="none" viewBox="0 0 100 100">
                                <path d="M 5,80 C 25,65 40,50 55,35 C 70,20 85,5 95,0" fill="none" stroke="rgba(54,124,245,0.6)" stroke-width="2" stroke-dasharray="4 4" class="[stroke-dashoffset:100] animate-[dash_3s_linear_forwards]"></path>
                            </svg>
                        </div>
                        <!-- X Axis Labels -->
                        <div class="flex justify-between px-2 mt-2 text-[9px] text-zinc-400 font-bold tracking-widest uppercase">
                            <span>Hoje</span>
                            <span>5 Anos</span>
                            <span>10 Anos</span>
                        </div>
                    </div>"""
content = content.replace(old_card_1_illustration, new_card_1_illustration)

# Card 2: Atlas Score
old_card_2_illustration = """                    <!-- Ilustração CSS Gauge -->
                    <div class="relative w-full border-t border-dashed border-zinc-200 bg-zinc-50/50 h-48 overflow-hidden flex items-end justify-center pb-6 mt-6">
                        <div class="absolute inset-0 bg-[radial-gradient(125%_125%_at_50%_0%,transparent_40%,rgba(0,0,0,0.03)_100%)]"></div>
                        <div class="relative w-40 h-20 border-t-8 border-l-8 border-r-8 border-zinc-200 rounded-t-full flex items-end justify-center">
                            <!-- Ponteiro -->
                            
                            <!-- Seu Score Label -->
                            <div class="absolute -top-6 left-1/2 -translate-x-1/2 bg-[#367CF5] text-white text-[10px] font-bold px-2 py-1 rounded shadow-md z-20 whitespace-nowrap animate-float">
                                Seu Score
                                <div class="absolute -bottom-1 left-1/2 -translate-x-1/2 border-l-4 border-r-4 border-t-4 border-transparent border-t-[#367CF5]"></div>
                            </div>
                            <!-- Ponteiro animado -->
                            <div class="absolute bottom-0 w-2 h-16 bg-[#367CF5] origin-bottom rounded-t-full shadow-lg animate-needle z-10"></div>

                            <!-- Centro do ponteiro -->
                            <div class="absolute -bottom-3 w-6 h-6 bg-zinc-800 rounded-full border-4 border-white shadow-sm"></div>
                            <!-- Divisões do painel -->
                            <div class="absolute bottom-1 -left-2 w-3 h-1 bg-zinc-300"></div>
                            <div class="absolute top-2 left-6 w-3 h-1 bg-zinc-300 transform -rotate-45"></div>
                            <div class="absolute -top-2 w-1 h-3 bg-zinc-300"></div>
                            <div class="absolute top-2 right-6 w-3 h-1 bg-zinc-300 transform rotate-45"></div>
                            <div class="absolute bottom-1 -right-2 w-3 h-1 bg-zinc-300"></div>
                        </div>
                    </div>"""

new_card_2_illustration = """                    <!-- UI Score Mockup -->
                    <div class="relative w-full border-t border-zinc-200 bg-zinc-50 h-48 overflow-hidden flex items-center justify-center p-6 mt-6">
                        <!-- Dots decorativos UI Mac -->
                        <div class="absolute top-3 left-3 flex gap-1.5 opacity-50">
                            <div class="w-2.5 h-2.5 rounded-full bg-red-400"></div>
                            <div class="w-2.5 h-2.5 rounded-full bg-yellow-400"></div>
                            <div class="w-2.5 h-2.5 rounded-full bg-green-400"></div>
                        </div>
                        
                        <div class="bg-white rounded-2xl shadow-lg border border-zinc-100 p-5 w-full max-w-[220px] flex flex-col items-center relative transform -rotate-2 hover:rotate-0 transition-transform duration-300 cursor-default">
                            <span class="text-[10px] text-zinc-400 font-bold uppercase tracking-widest mb-3">Atlas Score Atual</span>
                            
                            <!-- Circular Progress -->
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
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                Perfil: Mestre
                            </div>
                        </div>
                    </div>"""
content = content.replace(old_card_2_illustration, new_card_2_illustration)

with open(filepath, 'w') as f:
    f.write(content)

