import re

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/funcionalidades.html', 'r') as f:
    content = f.read()

new_gsap_script = """        // GSAP: Animação de entrada nas seções de funcionalidades (Staggering em textos e cards)
        gsap.utils.toArray('.feature-section').forEach(section => {
            // Seleciona títulos, parágrafos, cards e grids dentro da seção
            const elements = section.querySelectorAll('h2, .mb-8 > p, .group, .bg-white, .bg-gradient-to-br, .bg-\\[\\#0B1A30\\]');
            
            // Filtramos para não animar elementos aninhados duas vezes
            const uniqueElements = Array.from(elements).filter(el => {
                // Remove elementos que já estão dentro de um .group ou .bg-white que está sendo animado
                return !el.parentElement.closest('.group, .bg-white, .bg-gradient-to-br, .bg-\\\\[\\\\#0B1A30\\\\]');
            });

            gsap.from(uniqueElements, {
                opacity: 0,
                y: 40,
                duration: 0.8,
                stagger: 0.15,
                ease: 'power3.out',
                scrollTrigger: {
                    trigger: section,
                    start: 'top 85%',
                }
            });
        });"""

old_gsap_script = """        // GSAP: Animação de entrada nas seções de funcionalidades
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
        });"""

content = content.replace(new_gsap_script, old_gsap_script)

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/funcionalidades.html', 'w') as f:
    f.write(content)
