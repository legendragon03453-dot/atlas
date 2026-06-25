import re

with open('funcionalidades.html', 'r') as f:
    content = f.read()

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

grid_html += '                </div>\n'

pattern = r'(<div class="grid grid-cols-1 md:grid-cols-2 gap-6">.*?)(</section>)'

if re.search(pattern, content, flags=re.DOTALL):
    content = re.sub(pattern, grid_html + r'            \2', content, count=1, flags=re.DOTALL)
else:
    print("Pattern not found!")

# Optional: Also update the section title text if they wanted to rename "Método Atlas (Consultoria IA)" to something else. 
# They said "na head: Método Atlas (Consultoria IA) esses são os cursos", meaning inside that head. 

with open('funcionalidades.html', 'w') as f:
    f.write(content)

