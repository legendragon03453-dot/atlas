import re

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html', 'r') as f:
    content = f.read()

gsap_script = """        // GSAP: Animação de entrada na seção 6
        const sec6 = document.querySelector('#section-6');
        if (sec6) {
            const elements = sec6.querySelectorAll('h2, .mb-16 > p, .group');
            gsap.from(elements, {
                opacity: 0,
                y: 40,
                duration: 0.8,
                stagger: 0.15,
                ease: 'power3.out',
                scrollTrigger: {
                    trigger: sec6,
                    start: 'top 80%',
                }
            });
        }
        // GSAP: Animação de preenchimento da Timeline na Seção 4"""

content = content.replace(gsap_script, '// GSAP: Animação de preenchimento da Timeline na Seção 4')

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html', 'w') as f:
    f.write(content)
