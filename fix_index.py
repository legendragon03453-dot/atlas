import re

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html', 'r') as f:
    content = f.read()

# 1. Fix the top GSAP script tags and duplicated inline JS
# The inline JS from lines 11 to 65 is currently wrapped in an invalid <script src="...">.
# But it's ALSO duplicated at the bottom! So we just safely remove the inline JS from the top
# and make sure the script tag is closed properly.
content = re.sub(r'<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js">.*?</script>', '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>', content, flags=re.DOTALL, count=1)

# 2. Fix the duplicate hero-video (remove the .webm video block)
webm_video_block = """        <!-- Vídeo de Fundo -->
        <video id="hero-video" class="video-bg" autoplay muted playsinline>
            <source src="https://github.com/legendragon03453-dot/atlas/raw/main/Zoom_into_mountain_peak_archway_202606040019.webm" type="video/webm">
            <!-- Fallback caso o webm não carregue ou se preferir imagem de erro -->
            Seu navegador não suporta vídeos HTML5.
        </video>"""
content = content.replace(webm_video_block, "")

# 3. Move mobile-menu-overlay outside of header to prevent transform inheritance bugs
mobile_menu_block = """            <!-- Menu Mobile Overlay -->
            <div id="mobile-menu-overlay" class="fixed inset-0 bg-[#367CF5] z-[100] transform translate-y-[-100%] transition-transform duration-300 ease-in-out flex flex-col items-center justify-center">
                <button id="mobile-menu-close" class="absolute top-6 right-6 text-white p-2">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
                <nav class="flex flex-col gap-8 text-white font-bold text-2xl text-center">
                    <a href="/#section-7" class="mobile-link">Sobre</a>
                    <a href="/#section-8" class="mobile-link">Preços</a>
                    <a href="funcionalidades.html" class="mobile-link">Funcionalidades</a>
                    <a href="/#section-9" class="mobile-link">FAQ</a>
                    <a href="#" class="mobile-link">Suporte</a>
                    <a href="https://app.atlas.com.br" class="bg-[#AFFF00] text-[#1A2E05] px-8 py-3 rounded-full font-bold text-lg mt-4 text-center justify-center">Começar Agora</a>
                </nav>
            </div>"""

content = content.replace(mobile_menu_block, "")

# Insert it right before the closing </body> tag
content = content.replace("</body>", mobile_menu_block + "\n</body>")


# 4. Fix the GSAP animation for the video curtains in the bottom script
# Currently, `introTl` does not animate the curtains. We will add the curtain animation!
# We also make sure the video zoom happens correctly
gsap_intro_old = """        // GSAP: Animação de Entrada (Intro Load)
        const introTl = gsap.timeline();
        introTl.from("header", { y: -50, opacity: 0, duration: 1, ease: "power3.out" })
               .from("main h1", { y: 40, opacity: 0, duration: 1, ease: "power3.out" }, "-=0.5")
               .from("main p", { y: 30, opacity: 0, duration: 1, ease: "power3.out" }, "-=0.7")
               .from("main button", { scale: 0.5, opacity: 0, duration: 0.8, ease: "back.out(1.7)" }, "-=0.6");"""

gsap_intro_new = """        // GSAP: Animação de Entrada (Intro Load)
        const introTl = gsap.timeline();
        introTl.from("header", { y: -50, opacity: 0, duration: 1, ease: "power3.out" })
               .from("h1", { y: 40, opacity: 0, duration: 1, ease: "power3.out" }, "-=0.5")
               .from("p", { y: 30, opacity: 0, duration: 1, ease: "power3.out" }, "-=0.7")
               .from(".btn-green", { scale: 0.5, opacity: 0, duration: 0.8, ease: "back.out(1.7)" }, "-=0.6")
               // Animar as cortinas pretas do vídeo abrindo
               .to("#video-curtain-left", { scaleX: 0, duration: 1.5, ease: "power3.inOut" }, "-=1")
               .to("#video-curtain-right", { scaleX: 0, duration: 1.5, ease: "power3.inOut" }, "<");"""

content = content.replace(gsap_intro_old, gsap_intro_new)


with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html', 'w') as f:
    f.write(content)

