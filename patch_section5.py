import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Novos dados (simples e diretos)
data = [
    ("O seu futuro", "Parece longe e irreal", "Tem data, meta e valor exato"),
    ("Decisões de compra", "Feitas no impulso ou emoção", "Baseadas em números e realidade"),
    ("Controle de gastos", "Anota por anotar, sem focar", "Gasta sem culpa no que te faz feliz"),
    ("Aprender sobre dinheiro", "Lê dicas, mas nunca aplica", "Aprende na prática, no seu plano"),
    ("Visão do dinheiro", "Olha só para o que já gastou", "Sabe exatamente o que vai gastar"),
    ("Dinheiro em casal", "Gera brigas e estresse", "Decisões claras e tomadas juntos"),
    ("Suas metas", 'Vagas: "Quero guardar dinheiro"', 'Claras: "Vou ter R$ 50 mil em 3 anos"'),
    ("Efeito das escolhas", "Você não faz ideia", "Você vê o impacto daqui a 20 anos"),
    ("Independência", "Fica refém do gerente do banco", "Você mesmo sabe o que fazer"),
    ("Sentimento", "Ansiedade e medo de faltar", "Paz de espírito e muita confiança")
]

table_rows = ""
mobile_cards = ""

for row in data:
    aspecto, sem, com = row
    
    table_rows += f"""
                        <tr class="border-b border-white/10 hover:bg-white/[0.03] transition-colors">
                            <td class="p-5 font-bold text-white w-1/4 border-r border-white/10">{aspecto}</td>
                            <td class="p-5 text-white/60 text-center w-1/3 border-r border-white/10">{sem}</td>
                            <td class="p-5 text-white/90 font-medium text-center w-5/12">{com}</td>
                        </tr>"""
    
    mobile_cards += f"""
                <div class="bg-[#0B1A30] rounded-xl p-5 shadow-xl border border-white/10">
                    <h3 class="text-white font-bold text-lg mb-4 text-center border-b border-white/10 pb-3">{aspecto}</h3>
                    <div class="flex flex-col gap-4">
                        <div>
                            <span class="text-white/40 text-[10px] font-bold uppercase tracking-wider block mb-1">Sem Atlas</span>
                            <p class="text-white/70 text-sm">{sem}</p>
                        </div>
                        <div class="bg-gradient-to-r from-[#A3E635]/10 to-[#84cc16]/10 p-3 rounded-lg border border-[#A3E635]/20">
                            <span class="text-[#A3E635] text-[10px] font-bold uppercase tracking-wider block mb-1">Com Atlas</span>
                            <p class="text-white font-medium text-sm">{com}</p>
                        </div>
                    </div>
                </div>"""

new_section5 = f"""    <!-- === SEÇÃO 5: Tabela de Comparação === -->
    <section id="section-5" class="w-full bg-[#367CF5] py-24 px-4 flex flex-col items-center">
        <h2 class="text-white text-3xl md:text-4xl lg:text-5xl font-bold mb-20 text-center max-w-4xl leading-tight drop-shadow-lg tracking-tight">
            Veja como sua vida financeira muda<br>quando você tem um mapa.
        </h2>

        <div class="w-full max-w-5xl mx-auto">
            <!-- Tabela (Desktop) -->
            <div class="hidden md:flex flex-col relative w-full">
                <!-- Headers Row (fora da tabela para ter design customizado igual a referência) -->
                <div class="flex w-full items-end z-10 px-0">
                    <div class="w-1/4"></div>
                    <div class="w-1/3 bg-[#1F2937] text-white/70 text-center py-4 font-bold text-lg rounded-t-xl border-t border-l border-r border-white/10">
                        Sem Atlas
                    </div>
                    <div class="w-5/12 bg-gradient-to-r from-[#A3E635] to-[#84cc16] text-[#1A2E05] text-center py-5 font-extrabold text-xl rounded-t-xl shadow-[0_-10px_20px_rgba(163,230,53,0.3)]">
                        Com Atlas
                    </div>
                </div>
                
                <!-- Table Body Container -->
                <div class="bg-[#0B1A30] rounded-2xl rounded-tr-none shadow-2xl border border-white/10 z-0 overflow-hidden">
                    <table class="w-full text-left border-collapse table-fixed">
                        <tbody class="text-sm lg:text-base">
{table_rows}
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Cards (Mobile) -->
            <div class="md:hidden flex flex-col gap-6">
{mobile_cards}
            </div>
        </div>
    </section>
"""

# Extract Section 5 limits
s5_start = content.find('<!-- === SEÇÃO 5: Tabela de Comparação === -->')
s5_end = content.find('<script>', s5_start)

if s5_start != -1 and s5_end != -1:
    content = content[:s5_start] + new_section5 + content[s5_end:]
    with open(filepath, 'w') as f:
        f.write(content)

