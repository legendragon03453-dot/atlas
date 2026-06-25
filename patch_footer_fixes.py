import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Update FAQ Title
old_faq_title = """<h2 class="text-4xl md:text-5xl font-bold text-[#1a1a1a] mb-2 text-center">FAQ</h2>
            <p class="text-lg md:text-xl text-zinc-500 mb-16 text-center">Tudo que você queria perguntar.</p>"""
new_faq_title = """<h2 class="text-4xl md:text-5xl lg:text-6xl font-bold text-[#1a1a1a] mb-16 text-center max-w-2xl mx-auto leading-tight tracking-tight">Ainda está com dúvidas sobre o Atlas?</h2>"""
content = content.replace(old_faq_title, new_faq_title)

# 2. Add Button to P.S. Section
old_ps_text = """<p class="font-bold text-[#1a1a1a]">Você não precisa decidir agora se vai usar o Atlas pelos próximos 10 anos. Só precisa decidir se vale clicar e testar 7 dias.</p>"""
new_ps_text = """<p class="font-bold text-[#1a1a1a]">Você não precisa decidir agora se vai usar o Atlas pelos próximos 10 anos. Só precisa decidir se vale clicar e testar 7 dias.</p>
                    <button class="mt-8 px-8 py-4 rounded-xl bg-gradient-to-r from-[#A3E635] via-[#8cdc18] to-[#A3E635] bg-[length:200%_auto] text-[#0B1A30] text-lg font-bold transition-all shadow-[0_4px_24px_0_rgba(163,230,53,0.4)] animate-[bg-scroll_3s_linear_infinite]">
                        Teste por 7 dias
                    </button>"""
content = content.replace(old_ps_text, new_ps_text)

# Add keyframes for bg-scroll if not exists
style_end = content.find('</style>')
bg_scroll_css = """
        @keyframes bg-scroll {
            0% { background-position: 0% center; }
            100% { background-position: -200% center; }
        }
"""
if 'keyframes bg-scroll' not in content:
    content = content[:style_end] + bg_scroll_css + content[style_end:]

# 3. Reduce size of CTA bottom image
old_img = '<img src="https://github.com/legendragon03453-dot/atlas/blob/main/Imagem%20de%20Fundo%204%20relatorios%202.webp?raw=true" alt="Jornada Atlas - O Topo da Montanha" class="w-full md:w-[90%] lg:w-full object-contain drop-shadow-2xl">'
new_img = '<img src="https://github.com/legendragon03453-dot/atlas/blob/main/Imagem%20de%20Fundo%204%20relatorios%202.webp?raw=true" alt="Jornada Atlas - O Topo da Montanha" class="w-[75%] md:w-[60%] lg:w-[65%] max-w-2xl object-contain drop-shadow-2xl mx-auto">'
content = content.replace(old_img, new_img)

# 4. Wrap the top script in DOMContentLoaded
# The script starts at <head> and ends around line 91. 
# We'll just replace "// Mensal / Anual Toggle" with "document.addEventListener('DOMContentLoaded', () => {\n        // Mensal / Anual Toggle"
# and add "});" before the first </script> tag.
if "document.addEventListener('DOMContentLoaded'" not in content[:content.find('</script>')]:
    content = content.replace('// Mensal / Anual Toggle', "document.addEventListener('DOMContentLoaded', () => {\n        // Mensal / Anual Toggle", 1)
    # find first </script>
    first_script_end = content.find('</script>')
    content = content[:first_script_end] + "        });\n" + content[first_script_end:]


# 5. Append Footer
footer_html = """
    <!-- === FOOTER === -->
    <footer class="w-full bg-[#367CF5] py-16 px-6 relative z-20">
        <div class="container mx-auto max-w-6xl">
            <div class="flex flex-col items-center">
                <!-- Logo -->
                <div class="mb-10">
                    <img src="https://github.com/legendragon03453-dot/atlas/blob/main/export_2026-06-04T03_26_23-606Z/Group%201_1x.webp?raw=true" alt="Atlas Logo" class="h-10 filter brightness-0 invert">
                </div>
                
                <!-- Links -->
                <nav class="mb-12 flex flex-wrap justify-center gap-6 lg:gap-10 text-white/90 font-medium text-sm md:text-base">
                    <a href="#" class="hover:text-white transition-colors">Início</a>
                    <a href="#" class="hover:text-white transition-colors">A Metodologia</a>
                    <a href="#" class="hover:text-white transition-colors">Preços</a>
                    <a href="#" class="hover:text-white transition-colors">Depoimentos</a>
                    <a href="#" class="hover:text-white transition-colors">Dúvidas Frequentes</a>
                </nav>
                
                <!-- Social Icons -->
                <div class="mb-12 flex space-x-6">
                    <a href="#" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center text-white hover:bg-white hover:text-[#367CF5] transition-all">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" /></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center text-white hover:bg-white hover:text-[#367CF5] transition-all">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z" /></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center text-white hover:bg-white hover:text-[#367CF5] transition-all">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd" /></svg>
                    </a>
                </div>
                
                <!-- Copyright -->
                <div class="text-center pt-8 border-t border-white/20 w-full">
                    <p class="text-sm text-white/60">
                        &copy; 2026 Atlas. Todos os direitos reservados.
                    </p>
                </div>
            </div>
        </div>
    </footer>
"""
main_end_idx = content.rfind('</section>') # last section is section 10
if main_end_idx != -1:
    insert_idx = main_end_idx + len('</section>')
    content = content[:insert_idx] + footer_html + content[insert_idx:]

with open(filepath, 'w') as f:
    f.write(content)

