import re

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/funcionalidades.html', 'r') as f:
    content = f.read()

# Add feature-section class to sections
content = content.replace('<section id=', '<section class="feature-section" id=')

# Add GSAP entrance animation
gsap_script = """
        // GSAP: Animação de entrada nas seções de funcionalidades
        gsap.utils.toArray('.feature-section').forEach(section => {
            gsap.from(section, {
                opacity: 0,
                y: 40,
                duration: 0.8,
                ease: 'power3.out',
                scrollTrigger: {
                    trigger: section,
                    start: 'top 85%',
                }
            });
        });
"""
content = content.replace('// GSAP: Animação de preenchimento da Timeline na Seção 4', gsap_script + '\n        // GSAP: Animação de preenchimento da Timeline na Seção 4')

# 1. Multi-Perfil Integrado -> Household Motion
multi_perfil_old = """<div class="w-10 h-10 bg-zinc-100 rounded-lg flex items-center justify-center text-zinc-600 mb-4">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                        </div>"""

multi_perfil_new = """<!-- Overlapping Avatars -->
                        <div class="w-full bg-zinc-50 h-32 rounded-xl mb-4 overflow-hidden flex items-center justify-center group-hover:bg-zinc-100 transition-colors">
                            <div class="flex -space-x-4 group-hover:-space-x-2 transition-all duration-500">
                                <div class="w-12 h-12 rounded-full border-4 border-white bg-blue-50 flex items-center justify-center shadow-md relative z-20 group-hover:rotate-[-10deg] transition-transform">
                                    <svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                                </div>
                                <div class="w-12 h-12 rounded-full border-4 border-white bg-green-50 flex items-center justify-center shadow-md relative z-10 group-hover:rotate-[10deg] transition-transform">
                                    <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                                </div>
                            </div>
                        </div>"""
content = content.replace(multi_perfil_old, multi_perfil_new)

# 2. Seletor de Visão -> Tabs motion
seletor_old = """<div class="w-10 h-10 bg-zinc-100 rounded-lg flex items-center justify-center text-zinc-600 mb-4">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                        </div>"""
seletor_new = """<div class="w-full bg-zinc-50 h-32 rounded-xl mb-4 flex items-center justify-center overflow-hidden">
                            <div class="flex bg-white rounded-full p-1 border border-zinc-200 shadow-sm">
                                <div class="px-4 py-1.5 text-xs font-bold text-zinc-500 rounded-full group-hover:text-transparent transition-colors">Pessoa 1</div>
                                <div class="px-4 py-1.5 text-xs font-bold text-white bg-[#367CF5] rounded-full shadow-sm transform group-hover:scale-105 transition-transform">Casal</div>
                                <div class="px-4 py-1.5 text-xs font-bold text-zinc-500 rounded-full group-hover:text-transparent transition-colors">Pessoa 2</div>
                            </div>
                        </div>"""
content = content.replace(seletor_old, seletor_new)

# 3. Atlas Score Motion
atlas_score_old = """<h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Atlas Score</h3>"""
atlas_score_new = """<!-- Score Ring -->
                        <div class="w-full bg-zinc-50 h-32 rounded-xl mb-4 flex items-center justify-center relative overflow-hidden group-hover:bg-blue-50/50 transition-colors">
                            <div class="relative w-20 h-20">
                                <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                                    <path class="text-zinc-200" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" stroke-width="3"/>
                                    <path class="text-[#367CF5] drop-shadow-md group-hover:stroke-[#AFFF00] transition-colors duration-500" stroke-dasharray="85, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round"/>
                                </svg>
                                <div class="absolute inset-0 flex items-center justify-center flex-col">
                                    <span class="text-2xl font-bold text-[#0F172A] leading-none">85</span>
                                </div>
                            </div>
                        </div>
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Atlas Score</h3>"""
content = content.replace(atlas_score_old, atlas_score_new)

# 4. Atlas Chat (IA)
atlas_chat_old = """<h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Atlas Chat (Sua IA)</h3>"""
atlas_chat_new = """<!-- IA Glow -->
                        <div class="w-full bg-[#0B1A30] h-32 rounded-xl mb-4 flex items-center justify-center relative overflow-hidden">
                            <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(54,124,245,0.4)_0%,transparent_70%)]"></div>
                            <div class="relative group-hover:scale-110 transition-transform duration-700">
                                <div class="absolute inset-0 animate-ping rounded-full bg-[#367CF5] opacity-30 duration-1000"></div>
                                <div class="w-12 h-12 bg-gradient-to-tr from-[#367CF5] to-blue-400 rounded-full shadow-[0_0_20px_rgba(54,124,245,0.8)] flex items-center justify-center relative z-10">
                                    <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                </div>
                            </div>
                        </div>
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Atlas Chat (Sua IA)</h3>"""
content = content.replace(atlas_chat_old, atlas_chat_new)

# 5. Investimentos + Proventos
investimentos_old = """<h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Investimentos & Proventos</h3>"""
investimentos_new = """<!-- Progress Bar to Freedom -->
                        <div class="w-full border border-zinc-100 bg-zinc-50 h-32 rounded-xl mb-4 overflow-hidden flex flex-col items-center justify-center px-6">
                            <div class="w-full flex justify-between text-[10px] font-bold text-zinc-400 uppercase tracking-widest mb-2">
                                <span>Renda Atual</span>
                                <span class="text-green-600">Liberdade</span>
                            </div>
                            <div class="w-full h-3 bg-zinc-200 rounded-full overflow-hidden relative">
                                <div class="h-full bg-[#367CF5] w-[40%] rounded-full group-hover:w-[80%] transition-all duration-1000 ease-out relative">
                                    <div class="absolute top-0 right-0 bottom-0 w-4 bg-white/30 animate-pulse"></div>
                                </div>
                            </div>
                        </div>
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Investimentos & Proventos</h3>"""
content = content.replace(investimentos_old, investimentos_new)

# 6. Atlas Negócios
negocios_old = """<h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Histórico de Transferências</h3>"""
negocios_new = """<!-- PF / PJ Integration -->
                        <div class="w-full border border-zinc-100 bg-zinc-50 h-32 rounded-xl mb-4 overflow-hidden flex items-center justify-center gap-6">
                            <div class="flex flex-col items-center gap-2 group-hover:-translate-x-2 transition-transform duration-500">
                                <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center text-[#367CF5] border-2 border-white shadow-md font-bold text-xs">PF</div>
                            </div>
                            <div class="flex flex-col gap-1 items-center z-10 relative">
                                <div class="w-6 h-6 bg-white border border-zinc-200 rounded-full flex items-center justify-center shadow-sm group-hover:rotate-180 transition-transform duration-700">
                                    <svg class="w-3 h-3 text-zinc-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"></path></svg>
                                </div>
                            </div>
                            <div class="flex flex-col items-center gap-2 group-hover:translate-x-2 transition-transform duration-500">
                                <div class="w-10 h-10 bg-purple-100 rounded-full flex items-center justify-center text-purple-600 border-2 border-white shadow-md font-bold text-xs">PJ</div>
                            </div>
                        </div>
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Histórico de Transferências</h3>"""
content = content.replace(negocios_old, negocios_new)

# Add group class to white boxes to trigger group-hover
content = content.replace('<div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">', '<div class="group bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm hover:shadow-md transition-shadow">')
content = content.replace('<div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm md:col-span-2">', '<div class="group bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm hover:shadow-md transition-shadow md:col-span-2">')


with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/funcionalidades.html', 'w') as f:
    f.write(content)
