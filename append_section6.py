import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

section6_html = """
    <!-- === SEÇÃO 6: Features Bento Grid === -->
    <section id="section-6" class="w-full bg-zinc-50 py-24 md:py-32 px-4 flex flex-col items-center border-t border-zinc-200">
        
        <!-- Header -->
        <div class="text-center mb-16 flex flex-col items-center max-w-3xl mx-auto">
            <div class="flex items-center gap-2 mb-6">
                <div class="w-1.5 h-1.5 rounded-full bg-red-500"></div>
                <span class="text-xs font-semibold tracking-widest text-zinc-500 uppercase">O que vem nos 7 dias</span>
            </div>
            <h2 class="text-[#1a1a1a] text-4xl md:text-5xl lg:text-6xl font-bold mb-6 leading-tight tracking-tight">
                Atlas inteiro, aberto, <span class="font-normal italic font-serif">na sua mão.</span>
            </h2>
            <p class="text-zinc-600 text-lg md:text-xl font-medium">
                12 ferramentas que viram um sistema único. Não você adivinhando — você decidindo.
            </p>
        </div>

        <!-- Bento Grid -->
        <div class="mx-auto w-full max-w-6xl">
            <div class="grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
                
                <!-- Card 1: Vista da Montanha (Ocupa 2 colunas no desktop) -->
                <div class="group relative bg-white border border-zinc-200 shadow-sm overflow-hidden flex flex-col justify-between lg:col-span-2">
                    <!-- Decorator -->
                    <span class="absolute -left-px -top-px block size-2 border-l-2 border-t-2 border-[#367CF5]"></span>
                    <span class="absolute -right-px -top-px block size-2 border-r-2 border-t-2 border-[#367CF5]"></span>
                    <span class="absolute -bottom-px -left-px block size-2 border-b-2 border-l-2 border-[#367CF5]"></span>
                    <span class="absolute -bottom-px -right-px block size-2 border-b-2 border-r-2 border-[#367CF5]"></span>
                    
                    <div class="p-8 pb-4">
                        <div class="flex items-center gap-2 text-zinc-500 font-bold mb-4 uppercase text-xs tracking-wider">
                            <svg class="size-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                            Vista da Montanha
                        </div>
                        <p class="text-2xl font-bold text-zinc-900 leading-snug max-w-md">Veja seu futuro financeiro mudar em tempo real. Cenários, não promessa.</p>
                    </div>

                    <!-- Ilustração SVG -->
                    <div class="relative w-full border-t border-dashed border-zinc-200 bg-zinc-50/50 h-56 md:h-64 overflow-hidden flex items-end justify-center pt-8 px-6 md:px-12 mt-6">
                        <div class="absolute inset-0 bg-[linear-gradient(to_right,#e5e7eb_1px,transparent_1px),linear-gradient(to_bottom,#e5e7eb_1px,transparent_1px)] bg-[size:24px_24px] opacity-60"></div>
                        <svg class="w-full h-full text-[#367CF5] drop-shadow-[0_10px_15px_rgba(54,124,245,0.4)] relative z-10" viewBox="0 0 500 120" preserveAspectRatio="none">
                            <path d="M0,120 C50,110 100,70 150,80 C200,90 250,30 300,50 C350,70 400,20 450,10 L500,0 L500,120 Z" fill="url(#mountainGrad)" stroke="currentColor" stroke-width="4"></path>
                            <defs>
                                <linearGradient id="mountainGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                                    <stop offset="0%" stop-color="rgba(54,124,245,0.3)"/>
                                    <stop offset="100%" stop-color="rgba(54,124,245,0)"/>
                                </linearGradient>
                            </defs>
                        </svg>
                    </div>
                </div>

                <!-- Card 2: Atlas Score -->
                <div class="group relative bg-white border border-zinc-200 shadow-sm overflow-hidden flex flex-col justify-between">
                    <span class="absolute -left-px -top-px block size-2 border-l-2 border-t-2 border-[#367CF5]"></span>
                    <span class="absolute -right-px -top-px block size-2 border-r-2 border-t-2 border-[#367CF5]"></span>
                    <span class="absolute -bottom-px -left-px block size-2 border-b-2 border-l-2 border-[#367CF5]"></span>
                    <span class="absolute -bottom-px -right-px block size-2 border-b-2 border-r-2 border-[#367CF5]"></span>
                    
                    <div class="p-8 pb-4">
                        <div class="flex items-center gap-2 text-zinc-500 font-bold mb-4 uppercase text-xs tracking-wider">
                            <svg class="size-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                            Atlas Score
                        </div>
                        <p class="text-xl font-bold text-zinc-900 leading-snug">Em 2 segundos você sabe onde está. Score que se atualiza com cada decisão.</p>
                    </div>

                    <!-- Ilustração CSS Gauge -->
                    <div class="relative w-full border-t border-dashed border-zinc-200 bg-zinc-50/50 h-48 overflow-hidden flex items-end justify-center pb-6 mt-6">
                        <div class="absolute inset-0 bg-[radial-gradient(125%_125%_at_50%_0%,transparent_40%,rgba(0,0,0,0.03)_100%)]"></div>
                        <div class="relative w-40 h-20 border-t-8 border-l-8 border-r-8 border-zinc-200 rounded-t-full flex items-end justify-center">
                            <!-- Ponteiro -->
                            <div class="absolute bottom-0 w-2 h-16 bg-[#367CF5] origin-bottom transform rotate-45 rounded-t-full shadow-lg"></div>
                            <!-- Centro do ponteiro -->
                            <div class="absolute -bottom-3 w-6 h-6 bg-zinc-800 rounded-full border-4 border-white shadow-sm"></div>
                            <!-- Divisões do painel -->
                            <div class="absolute bottom-1 -left-2 w-3 h-1 bg-zinc-300"></div>
                            <div class="absolute top-2 left-6 w-3 h-1 bg-zinc-300 transform -rotate-45"></div>
                            <div class="absolute -top-2 w-1 h-3 bg-zinc-300"></div>
                            <div class="absolute top-2 right-6 w-3 h-1 bg-zinc-300 transform rotate-45"></div>
                            <div class="absolute bottom-1 -right-2 w-3 h-1 bg-zinc-300"></div>
                        </div>
                    </div>
                </div>

                <!-- Card 3: Simulador de Decisão -->
                <div class="group relative bg-white border border-zinc-200 shadow-sm overflow-hidden flex flex-col justify-between">
                    <span class="absolute -left-px -top-px block size-2 border-l-2 border-t-2 border-[#367CF5]"></span>
                    <span class="absolute -right-px -top-px block size-2 border-r-2 border-t-2 border-[#367CF5]"></span>
                    <span class="absolute -bottom-px -left-px block size-2 border-b-2 border-l-2 border-[#367CF5]"></span>
                    <span class="absolute -bottom-px -right-px block size-2 border-b-2 border-r-2 border-[#367CF5]"></span>
                    
                    <div class="p-8 pb-4">
                        <div class="flex items-center gap-2 text-zinc-500 font-bold mb-4 uppercase text-xs tracking-wider">
                            <svg class="size-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"></path></svg>
                            Simulador de Decisão
                        </div>
                        <p class="text-xl font-bold text-zinc-900 leading-snug">Comprar a casa? Trocar o carro? Decisões grandes com dados, não impulso.</p>
                    </div>

                    <!-- Ilustração Caminhos -->
                    <div class="relative w-full border-t border-dashed border-zinc-200 bg-zinc-50/50 h-48 overflow-hidden flex items-center justify-center mt-6">
                        <div class="absolute inset-0 bg-[linear-gradient(45deg,#f4f4f5_25%,transparent_25%,transparent_75%,#f4f4f5_75%,#f4f4f5),linear-gradient(45deg,#f4f4f5_25%,transparent_25%,transparent_75%,#f4f4f5_75%,#f4f4f5)] bg-[length:20px_20px] bg-[position:0_0,10px_10px] opacity-40"></div>
                        <div class="relative z-10 flex items-center gap-3">
                            <div class="w-14 h-14 rounded-xl bg-white border border-zinc-200 shadow-sm flex items-center justify-center font-bold text-zinc-400">A</div>
                            <div class="flex flex-col gap-5 justify-center relative">
                                <div class="w-10 h-0.5 bg-zinc-300 transform -rotate-12 translate-y-3"></div>
                                <div class="w-10 h-0.5 bg-[#367CF5] transform rotate-12 -translate-y-3"></div>
                            </div>
                            <div class="flex flex-col gap-3">
                                <div class="w-14 h-14 rounded-xl bg-white border border-zinc-200 shadow-sm flex items-center justify-center font-bold text-zinc-400">B</div>
                                <div class="w-14 h-14 rounded-xl bg-blue-50 border border-blue-200 shadow-sm flex items-center justify-center font-bold text-[#367CF5] ring-2 ring-[#367CF5] ring-offset-2 ring-offset-zinc-50">C</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Card 4: Household -->
                <div class="group relative bg-white border border-zinc-200 shadow-sm overflow-hidden flex flex-col justify-between">
                    <span class="absolute -left-px -top-px block size-2 border-l-2 border-t-2 border-[#367CF5]"></span>
                    <span class="absolute -right-px -top-px block size-2 border-r-2 border-t-2 border-[#367CF5]"></span>
                    <span class="absolute -bottom-px -left-px block size-2 border-b-2 border-l-2 border-[#367CF5]"></span>
                    <span class="absolute -bottom-px -right-px block size-2 border-b-2 border-r-2 border-[#367CF5]"></span>
                    
                    <div class="p-8 pb-4">
                        <div class="flex items-center gap-2 text-zinc-500 font-bold mb-4 uppercase text-xs tracking-wider">
                            <svg class="size-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                            Household
                        </div>
                        <p class="text-xl font-bold text-zinc-900 leading-snug">Finanças do casal sem briga. Convide sem dar senha.</p>
                    </div>

                    <!-- Ilustração Overlapping Circles -->
                    <div class="relative w-full border-t border-dashed border-zinc-200 bg-zinc-50/50 h-48 overflow-hidden flex items-center justify-center mt-6">
                        <div class="flex -space-x-4">
                            <div class="w-16 h-16 rounded-full border-4 border-zinc-50 bg-[#367CF5]/10 flex items-center justify-center shadow-sm">
                                <svg class="w-6 h-6 text-[#367CF5]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
                            </div>
                            <div class="w-16 h-16 rounded-full border-4 border-zinc-50 bg-green-50 flex items-center justify-center shadow-sm">
                                <svg class="w-6 h-6 text-[#1A2E05]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Card 5: Atlas IA -->
                <div class="group relative bg-[#0B1A30] shadow-xl overflow-hidden flex flex-col justify-between">
                    <span class="absolute -left-px -top-px block size-2 border-l-2 border-t-2 border-[#A3E635]"></span>
                    <span class="absolute -right-px -top-px block size-2 border-r-2 border-t-2 border-[#A3E635]"></span>
                    <span class="absolute -bottom-px -left-px block size-2 border-b-2 border-l-2 border-[#A3E635]"></span>
                    <span class="absolute -bottom-px -right-px block size-2 border-b-2 border-r-2 border-[#A3E635]"></span>
                    
                    <div class="p-8 pb-4 relative z-10">
                        <div class="flex items-center gap-2 text-[#A3E635] font-bold mb-4 uppercase text-xs tracking-wider">
                            <svg class="size-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                            Atlas IA
                        </div>
                        <p class="text-xl font-bold text-white leading-snug">Pergunta como pra um amigo. Responde como um planejador. Conhece seus números.</p>
                    </div>

                    <!-- Ilustração IA Glow -->
                    <div class="relative w-full border-t border-white/10 bg-[#0B1A30] h-48 overflow-hidden flex items-center justify-center mt-6">
                        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(54,124,245,0.4)_0%,transparent_70%)]"></div>
                        <div class="absolute inset-0 bg-[linear-gradient(to_right,#ffffff05_1px,transparent_1px),linear-gradient(to_bottom,#ffffff05_1px,transparent_1px)] bg-[size:16px_16px]"></div>
                        <div class="relative">
                            <div class="absolute inset-0 animate-ping rounded-full bg-[#367CF5] opacity-30"></div>
                            <div class="w-14 h-14 bg-gradient-to-tr from-[#367CF5] to-blue-400 rounded-full shadow-[0_0_40px_rgba(54,124,245,0.8)] flex items-center justify-center">
                                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path></svg>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>
"""

# Extract position to insert
s5_start = content.find('<!-- Scripts GSAP e Tailwind -->')
if s5_start == -1:
    s5_start = content.find('<script>')

if s5_start != -1:
    content = content[:s5_start] + section6_html + content[s5_start:]
    with open(filepath, 'w') as f:
        f.write(content)

