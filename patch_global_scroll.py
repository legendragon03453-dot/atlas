import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

scroll_script = """
            // Animação Global de Entrada e Saída (Scroll)
            gsap.utils.toArray('section, footer').forEach((sec) => {
                // Não animar a hero (já animada na intro) nem o pin-master (quebra a timeline)
                if(sec.id !== 'pin-master' && !sec.classList.contains('hero-container')) {
                    // Selecionar os elementos filhos principais para animar em cascata (stagger)
                    const elements = sec.querySelectorAll('h2, h3, p, .faq-item, img:not(.video-bg), button:not(.btn-nav)');
                    
                    if(elements.length > 0) {
                        gsap.from(elements, {
                            scrollTrigger: {
                                trigger: sec,
                                start: "top 85%", // Dispara quando o topo da seção atinge 85% da tela
                                toggleActions: "play reverse play reverse" // Anima na entrada e reverte na saída
                            },
                            y: 40,
                            opacity: 0,
                            duration: 0.8,
                            stagger: 0.1, // Efeito cascata
                            ease: "power3.out"
                        });
                    }
                }
            });
"""

# Insert right after the intro animation
insert_marker = 'introTl.from("main button", { scale: 0.5, opacity: 0, duration: 0.8, ease: "back.out(1.7)" }, "-=0.6");'
if insert_marker in content:
    content = content.replace(insert_marker, insert_marker + "\n" + scroll_script)

with open(filepath, 'w') as f:
    f.write(content)

