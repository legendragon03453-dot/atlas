import re

with open('index.html', 'r') as f:
    content = f.read()

lucid_cards = [
    {
        "icon": "rocket",
        "title": "O seu futuro",
        "sem": "Parece longe e irreal",
        "com": "Tem data, meta e valor exato"
    },
    {
        "icon": "shopping-cart",
        "title": "Decisões de compra",
        "sem": "Feitas no impulso ou emoção",
        "com": "Baseadas em números e realidade"
    },
    {
        "icon": "calculator",
        "title": "Controle de gastos",
        "sem": "Anota por anotar, sem focar",
        "com": "Gasta sem culpa no que te faz feliz"
    },
    {
        "icon": "book-open",
        "title": "Aprender sobre dinheiro",
        "sem": "Lê dicas, mas nunca aplica",
        "com": "Aprende na prática, no seu plano"
    },
    {
        "icon": "eye",
        "title": "Visão do dinheiro",
        "sem": "Olha só para o que já gastou",
        "com": "Sabe exatamente o que vai gastar"
    }
]

cards_html = ""
for card in lucid_cards:
    cards_html += f"""
            <!-- Card -->
            <div class="card-3d-reveal rounded-2xl overflow-hidden shadow-2xl flex flex-col md:flex-row transition-all duration-300 hover:-translate-y-2 hover:shadow-[0_20px_40px_rgba(0,0,0,0.4)] border border-white/5">
                <!-- Left -->
                <div class="md:w-1/3 p-6 md:p-8 bg-[#1e293b] flex items-center justify-center md:justify-start gap-4">
                    <i data-lucide="{card['icon']}" class="w-6 h-6 text-white shrink-0"></i>
                    <h3 class="text-white font-bold text-lg md:text-xl text-center md:text-left">{card['title']}</h3>
                </div>
                <!-- Middle & Right -->
                <div class="flex-1 flex flex-col sm:flex-row">
                    <!-- Sem Atlas -->
                    <div class="flex-1 p-6 md:p-8 bg-[#18181b] flex flex-col justify-center items-start text-left border-l border-white/5">
                        <div class="flex items-center gap-2 mb-3">
                            <div class="w-1.5 h-1.5 rounded-full bg-rose-500"></div>
                            <span class="text-rose-500 font-bold text-[10px] tracking-wider uppercase">Sem Atlas</span>
                        </div>
                        <p class="text-white/70 font-medium text-sm md:text-base leading-snug">{card['sem']}</p>
                    </div>
                    <!-- Com Atlas -->
                    <div class="flex-1 p-6 md:p-8 bg-[#1e293b] flex flex-col justify-center items-start text-left border-l border-white/5">
                        <div class="flex items-center gap-2 mb-3">
                            <div class="w-1.5 h-1.5 rounded-full bg-[#36DCF5]"></div>
                            <span class="text-[#36DCF5] font-bold text-[10px] tracking-wider uppercase">Com Atlas</span>
                        </div>
                        <p class="text-white font-bold text-sm md:text-base leading-snug">{card['com']}</p>
                    </div>
                </div>
            </div>
"""

new_section_5 = f"""<section id="section-5" class="w-full bg-[#367CF5] min-h-[200vh] px-4 relative flex flex-col items-center">
        <!-- Glow Overlay -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden z-0">
            <div class="absolute top-0 left-0 w-[60%] h-full bg-[#36DCF5]/60 blur-[150px] rounded-full animate-glow-sweep mix-blend-screen"></div>
        </div>

        <!-- Sticky Heading -->
        <div class="sticky top-0 w-full h-[100vh] flex flex-col items-center justify-center z-0 pointer-events-none">
            <h2 class="text-white text-3xl md:text-5xl lg:text-6xl font-bold text-center max-w-5xl leading-tight drop-shadow-2xl tracking-tight px-4 pb-[15vh]">
                O que acontece quando você compra o Atlas ou <span class="font-normal italic font-playfair text-[#0B1A30]">Não compra o atlas</span>
            </h2>
        </div>

        <!-- Cards container (Restored overlap margin) -->
        <div class="w-full max-w-5xl mx-auto flex flex-col gap-8 md:gap-12 relative z-10 mt-[-70vh] pb-[30vh]">
{cards_html}
        </div>
    </section>"""

# Find the current section-5
pattern = re.compile(r'<section id="section-5".*?</section>', re.DOTALL)
content = pattern.sub(new_section_5, content)

with open('index.html', 'w') as f:
    f.write(content)
