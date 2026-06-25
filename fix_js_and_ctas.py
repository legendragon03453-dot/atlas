import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update GSAP animation speed S2->S3
# Current GSAP for scrub is `end: "+=1200", scrub: 1`
# I'll reduce scrub to 0.5 and end to +=800
content = content.replace('end: "+=1200",', 'end: "+=800",')
content = content.replace('scrub: 1,', 'scrub: 0.5,')

# 2. Add Scroll Listener for the header CTA
# Find the end of the script block and add the logic.
end_script_idx = content.rfind("}); // Fim do DOMContentLoaded")

scroll_logic = """
        // Mostrar CTA do menu após 20% do scroll
        window.addEventListener('scroll', () => {
            const scrollPercent = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
            const navCta = document.getElementById('nav-cta-btn');
            const header = document.getElementById('main-header');
            if (navCta) {
                if (scrollPercent > 20) {
                    navCta.classList.remove('opacity-0', 'pointer-events-none');
                    navCta.classList.add('opacity-100', 'pointer-events-auto');
                    if (header) header.classList.add('backdrop-blur-md', 'bg-[#0B1A30]/80');
                } else {
                    navCta.classList.add('opacity-0', 'pointer-events-none');
                    navCta.classList.remove('opacity-100', 'pointer-events-auto');
                    if (header) header.classList.remove('backdrop-blur-md', 'bg-[#0B1A30]/80');
                }
            }
        });
"""

content = content[:end_script_idx] + scroll_logic + content[end_script_idx:]

# 3. Fix all `<a href="#" class="btn-green` to `<a href="#section-8" class="btn-green`
content = content.replace('href="#" class="btn-green', 'href="#section-8" class="btn-green')

with open('index.html', 'w') as f:
    f.write(content)

