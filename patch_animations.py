import os
import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Add CSS animations
style_tag_end = content.find('</style>')
custom_css = """
        @keyframes glow-sweep {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        .animate-glow-sweep {
            animation: glow-sweep 8s linear infinite;
        }
        @keyframes needle-swing {
            0%, 100% { transform: rotate(20deg); }
            50% { transform: rotate(70deg); }
        }
        .animate-needle {
            animation: needle-swing 4s ease-in-out infinite;
        }
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        .animate-float {
            animation: float 3s ease-in-out infinite;
        }
"""
content = content[:style_tag_end] + custom_css + content[style_tag_end:]

# 2. Add Parallax Ice Blocks to Hero
hero_end = content.find('<!-- Botões e Logos -->') # A good insertion point in Hero
ice_blocks = """
        <!-- Parallax Ice Blocks -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden z-10">
            <div class="parallax-ice absolute top-[20%] left-[10%] w-8 h-8 bg-white/40 backdrop-blur-md rounded-lg shadow-lg rotate-12" data-speed="0.05"></div>
            <div class="parallax-ice absolute top-[60%] left-[5%] w-12 h-12 bg-white/20 backdrop-blur-sm rounded-xl shadow-lg -rotate-12 blur-[2px]" data-speed="0.02"></div>
            <div class="parallax-ice absolute top-[30%] right-[15%] w-6 h-6 bg-white/60 backdrop-blur-lg rounded shadow-lg rotate-45" data-speed="0.08"></div>
            <div class="parallax-ice absolute top-[70%] right-[10%] w-16 h-16 bg-white/30 backdrop-blur-md rounded-2xl shadow-xl rotate-6 blur-[1px]" data-speed="0.04"></div>
            <div class="parallax-ice absolute bottom-[10%] left-[40%] w-10 h-10 bg-white/50 backdrop-blur-lg rounded-xl shadow-lg -rotate-6" data-speed="0.06"></div>
        </div>
"""
content = content[:hero_end] + ice_blocks + content[hero_end:]

# 3. Add Glow to Section 4 and 5
glow_div = """
        <!-- Glow Overlay -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden z-0">
            <div class="absolute top-0 left-0 w-[50%] h-full bg-[#36DCF5]/20 blur-[120px] rounded-full animate-glow-sweep mix-blend-screen"></div>
        </div>
"""
# Sec 4 is <section id="section-4" class="w-full bg-[#367CF5] py-24 px-4 flex flex-col items-center overflow-hidden relative">
# Sec 5 is <section id="section-5" class="w-full bg-[#367CF5] py-24 px-4 flex flex-col items-center">
content = content.replace(
    '<section id="section-4" class="w-full bg-[#367CF5] py-24 px-4 flex flex-col items-center overflow-hidden relative">',
    '<section id="section-4" class="w-full bg-[#367CF5] py-24 px-4 flex flex-col items-center overflow-hidden relative">' + glow_div
)
content = content.replace(
    '<section id="section-5" class="w-full bg-[#367CF5] py-24 px-4 flex flex-col items-center">',
    '<section id="section-5" class="w-full bg-[#367CF5] py-24 px-4 flex flex-col items-center relative overflow-hidden">' + glow_div
)

# 4. Update Atlas Score Card
# Find the needle div: <div class="absolute bottom-0 w-2 h-16 bg-[#367CF5] origin-bottom transform rotate-45 rounded-t-full shadow-lg"></div>
needle_html = '<div class="absolute bottom-0 w-2 h-16 bg-[#367CF5] origin-bottom transform rotate-45 rounded-t-full shadow-lg"></div>'
new_needle_html = """
                            <!-- Seu Score Label -->
                            <div class="absolute -top-6 left-1/2 -translate-x-1/2 bg-[#367CF5] text-white text-[10px] font-bold px-2 py-1 rounded shadow-md z-20 whitespace-nowrap animate-float">
                                Seu Score
                                <div class="absolute -bottom-1 left-1/2 -translate-x-1/2 border-l-4 border-r-4 border-t-4 border-transparent border-t-[#367CF5]"></div>
                            </div>
                            <!-- Ponteiro animado -->
                            <div class="absolute bottom-0 w-2 h-16 bg-[#367CF5] origin-bottom rounded-t-full shadow-lg animate-needle z-10"></div>
"""
content = content.replace(needle_html, new_needle_html)

# 5. Update Vista da Montanha Card
# Find the SVG div
svg_html = '<svg class="w-full h-full text-[#367CF5] drop-shadow-[0_10px_15px_rgba(54,124,245,0.4)] relative z-10" viewBox="0 0 500 120" preserveAspectRatio="none">'
new_svg_html = """
                        <!-- Marcadores flutuantes -->
                        <div class="absolute top-16 left-[20%] animate-float z-20" style="animation-delay: 0s;">
                            <div class="bg-white border border-[#367CF5]/30 text-[#367CF5] text-xs font-bold px-3 py-1 rounded-full shadow-sm">Etapa 1</div>
                            <div class="w-1.5 h-1.5 bg-[#367CF5] rounded-full mx-auto mt-2"></div>
                        </div>
                        <div class="absolute top-24 left-[50%] animate-float z-20" style="animation-delay: 0.5s;">
                            <div class="bg-white border border-[#367CF5]/30 text-[#367CF5] text-xs font-bold px-3 py-1 rounded-full shadow-sm">Etapa 2</div>
                            <div class="w-1.5 h-1.5 bg-[#367CF5] rounded-full mx-auto mt-2"></div>
                        </div>
                        <div class="absolute top-[10px] right-[5%] animate-float z-20" style="animation-delay: 1s;">
                            <div class="bg-[#367CF5] text-white text-xs font-bold px-3 py-1.5 rounded-full shadow-md whitespace-nowrap">Etapa 3 [Seu objetivo final]</div>
                            <div class="w-1.5 h-1.5 bg-[#367CF5] rounded-full mx-auto mt-2"></div>
                        </div>
                        <svg class="w-full h-full text-[#367CF5] drop-shadow-[0_10px_15px_rgba(54,124,245,0.4)] relative z-10" viewBox="0 0 500 120" preserveAspectRatio="none">
"""
content = content.replace(svg_html, new_svg_html)

# 6. Add Parallax JS
script_end = content.find('</script>')
parallax_js = """
        // Parallax Ice Blocks
        document.addEventListener('mousemove', (e) => {
            const ices = document.querySelectorAll('.parallax-ice');
            const x = (window.innerWidth - e.pageX) / 2;
            const y = (window.innerHeight - e.pageY) / 2;
            
            ices.forEach(ice => {
                const speed = ice.getAttribute('data-speed');
                ice.style.transform = `translateX(${x * speed}px) translateY(${y * speed}px)`;
            });
        });
"""
content = content[:script_end] + parallax_js + content[script_end:]

with open(filepath, 'w') as f:
    f.write(content)

