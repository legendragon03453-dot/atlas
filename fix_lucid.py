import re

with open('index.html', 'r') as f:
    content = f.read()

lucid_cards = [
    {
        "icon": "eye",
        "title": "Visão do dinheiro",
        "sem": "Olha só para o que já gastou",
        "com": "Sabe exatamente o que vai gastar"
    },
    {
        "icon": "users",
        "title": "Dinheiro em casal",
        "sem": "Gera brigas e estresse",
        "com": "Decisões claras e tomadas juntos"
    },
    {
        "icon": "target",
        "title": "Suas metas",
        "sem": 'Vagas: "Quero guardar dinheiro"',
        "com": 'Claras: "Vou ter R$ 50 mil em 3 anos"'
    },
    {
        "icon": "git-branch",
        "title": "Efeito das escolhas",
        "sem": "Você não faz ideia",
        "com": "Você vê o impacto daqui a 20 anos"
    },
    {
        "icon": "key",
        "title": "Independência",
        "sem": "Fica refém do gerente do banco",
        "com": "Você mesmo sabe o que fazer"
    }
]

cards_html = ""
for card in lucid_cards:
    cards_html += f"""
            <div class="rounded-3xl overflow-hidden shadow-lg flex flex-col md:flex-row transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl">
                <!-- Left -->
                <div class="md:w-1/3 p-6 md:p-8 bg-[#2a5585] flex items-center justify-center md:justify-start border-b md:border-b-0 border-white/5 gap-3">
                    <i data-lucide="{card['icon']}" class="w-8 h-8 text-[#36DCF5] shrink-0"></i>
                    <h3 class="text-white font-bold text-xl md:text-2xl text-center md:text-left">{card['title']}</h3>
                </div>
                <!-- Middle & Right -->
                <div class="flex-1 flex flex-col sm:flex-row">
                    <!-- Sem Atlas -->
                    <div class="flex-1 p-6 md:p-8 bg-[#586282] border-b sm:border-b-0 sm:border-r border-white/5 flex flex-col justify-center items-center text-center">
                        <div class="flex items-center justify-center gap-2 mb-3">
                            <i data-lucide="x" class="w-4 h-4 text-rose-400"></i>
                            <span class="text-rose-400 font-bold text-xs tracking-wider uppercase">Sem Atlas</span>
                        </div>
                        <p class="text-white/90 font-medium text-lg leading-snug">{card['sem']}</p>
                    </div>
                    <!-- Com Atlas -->
                    <div class="flex-1 p-6 md:p-8 bg-[#2185b3] flex flex-col justify-center items-center text-center">
                        <div class="flex items-center justify-center gap-2 mb-3">
                            <i data-lucide="check" class="w-4 h-4 text-[#36DCF5]"></i>
                            <span class="text-[#36DCF5] font-bold text-xs tracking-wider uppercase">Com Atlas</span>
                        </div>
                        <p class="text-white font-bold text-lg leading-snug">{card['com']}</p>
                    </div>
                </div>
            </div>
"""

new_section_5 = f"""<section id="section-5" class="w-full bg-[#367CF5] py-24 px-4 relative flex flex-col items-center">
        <!-- Glow Overlay -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden z-0">
            <div class="absolute top-0 left-0 w-[60%] h-full bg-[#36DCF5]/60 blur-[150px] rounded-full animate-glow-sweep mix-blend-screen"></div>
        </div>

        <!-- Heading Fix (No more overlap, relative normal flow) -->
        <div class="w-full flex flex-col items-center justify-center relative z-10 mb-16">
            <h2 class="text-white text-3xl md:text-5xl lg:text-6xl font-bold text-center max-w-5xl leading-tight drop-shadow-md tracking-tight px-4">
                O que acontece quando você compra o Atlas ou <span class="font-normal italic font-playfair text-[#0B1A30]">Não compra o atlas</span>
            </h2>
        </div>

        <div class="w-full max-w-5xl mx-auto flex flex-col gap-6 md:gap-8 relative z-10">
{cards_html}
        </div>
    </section>"""

# Replace the whole section-5
pattern = re.compile(r'<section id="section-5".*?</section>', re.DOTALL)
content = pattern.sub(new_section_5, content)

with open('index.html', 'w') as f:
    f.write(content)
