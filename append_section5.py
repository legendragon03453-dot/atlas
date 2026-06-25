import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Dados da tabela
data = [
    ("Visão do Futuro", "Aposentadoria é abstrata, distante", "Aposentadoria é meta concreta, com data e valor"),
    ("Decisões Financeiras", "Baseadas em palpite e emoção", "Baseadas em dados e simulações reais"),
    ("Registro de Gastos", "Esporádico, sem propósito", "Consciente, alinhado com valores"),
    ("Conhecimento Financeiro", "Consome conteúdo, mas não age", "Aprende enquanto planeja, com contexto"),
    ("Controle do Dinheiro", "Reativo (vê o que aconteceu)", "Proativo (vê o que vai acontecer)"),
    ("Comunicação em Casa", "Conflitos sobre dinheiro", "Clareza compartilhada, decisões conjuntas"),
    ("Objetivos", "Vagos (\\\"guardar mais\\\")", "Específicos (\\\"R$ 50k em 3 anos\\\")"),
    ("Impacto de Escolhas", "Desconhecido", "Visualizado em 10, 20, 30 anos"),
    ("Autonomia Financeira", "Dependência de consultores", "Independência com método claro"),
    ("Paz Mental", "Ansiedade, incerteza", "Clareza, confiança, propósito")
]

table_rows = ""
mobile_cards = ""

for row in data:
    aspecto, sem, com = row
    
    table_rows += f"""
                        <tr class="hover:bg-white/5 transition-colors">
                            <td class="p-5 font-semibold text-white">{aspecto}</td>
                            <td class="p-5">{sem}</td>
                            <td class="p-5 text-white bg-[#367CF5]/10 font-medium">{com}</td>
                        </tr>"""
    
    mobile_cards += f"""
                <div class="bg-[#111827] rounded-xl p-5 shadow-xl border border-white/10">
                    <h3 class="text-white font-bold text-lg mb-4 text-center border-b border-white/10 pb-3">{aspecto}</h3>
                    <div class="flex flex-col gap-4">
                        <div>
                            <span class="text-white/60 text-xs font-semibold uppercase tracking-wider block mb-1">Sem Atlas</span>
                            <p class="text-white/90 text-sm">{sem}</p>
                        </div>
                        <div class="bg-[#367CF5]/20 p-3 rounded-lg border border-[#367CF5]/30">
                            <span class="text-[#367CF5] text-xs font-bold uppercase tracking-wider block mb-1">Com Atlas</span>
                            <p class="text-white font-medium text-sm">{com}</p>
                        </div>
                    </div>
                </div>"""

section5_html = f"""
    <!-- === SEÇÃO 5: Tabela de Comparação === -->
    <section id="section-5" class="w-full bg-[#367CF5] py-24 px-4 flex flex-col items-center">
        <h2 class="text-white text-3xl md:text-4xl lg:text-5xl font-bold mb-16 text-center max-w-4xl leading-tight drop-shadow-lg tracking-tight">
            Veja como sua vida financeira muda<br>quando você tem um mapa.
        </h2>

        <div class="w-full max-w-6xl mx-auto">
            <!-- Tabela (Desktop) -->
            <div class="hidden md:block bg-[#111827] rounded-2xl overflow-hidden shadow-2xl border border-white/10">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="bg-white/5 border-b border-white/10">
                            <th class="p-6 text-white font-bold w-1/4">Aspecto</th>
                            <th class="p-6 text-white/80 font-semibold w-1/3">Sem Atlas</th>
                            <th class="p-6 text-white font-bold text-[#367CF5] w-5/12">Com Atlas</th>
                        </tr>
                    </thead>
                    <tbody class="text-white/80 text-sm lg:text-base divide-y divide-white/5">
                        {table_rows}
                    </tbody>
                </table>
            </div>

            <!-- Cards (Mobile) -->
            <div class="md:hidden flex flex-col gap-6">
                {mobile_cards}
            </div>
        </div>
    </section>
"""

# Insert just before the script tag
script_start = content.find('<script>')
if script_start != -1:
    content = content[:script_start] + section5_html + content[script_start:]
    with open(filepath, 'w') as f:
        f.write(content)

