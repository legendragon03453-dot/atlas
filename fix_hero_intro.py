import re

for filename in ['index.html', 'funcionalidades.html']:
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Add hidden md:block to curtains
    content = content.replace('id="video-curtain-left" class="absolute top-0 left-0 w-1/2 h-full bg-black z-20 origin-left"', 'id="video-curtain-left" class="hidden md:block absolute top-0 left-0 w-1/2 h-full bg-black z-20 origin-left"')
    content = content.replace('id="video-curtain-right" class="absolute top-0 right-0 w-1/2 h-full bg-black z-20 origin-right"', 'id="video-curtain-right" class="hidden md:block absolute top-0 right-0 w-1/2 h-full bg-black z-20 origin-right"')

    # 2. Wrap introTl in if(window.innerWidth >= 768)
    original_intro = """        // GSAP: Animação de Entrada (Intro Load)
        const introTl = gsap.timeline();
        introTl.from("header", { y: -50, opacity: 0, duration: 1, ease: "power3.out" })
               .from("h1", { y: 40, opacity: 0, duration: 1, ease: "power3.out" }, "-=0.5")
               .from("p", { y: 30, opacity: 0, duration: 1, ease: "power3.out" }, "-=0.7")
               .from(".btn-green", { scale: 0.5, opacity: 0, duration: 0.8, ease: "back.out(1.7)" }, "-=0.6")
               // Animar as cortinas pretas do vídeo abrindo
               .to("#video-curtain-left", { scaleX: 0, duration: 1.5, ease: "power3.inOut" }, "-=1")
               .to("#video-curtain-right", { scaleX: 0, duration: 1.5, ease: "power3.inOut" }, "<");"""

    new_intro = """        // GSAP: Animação de Entrada (Intro Load)
        if (window.innerWidth >= 768) {
            const introTl = gsap.timeline();
            introTl.from("header", { y: -50, opacity: 0, duration: 1, ease: "power3.out" })
                   .from("h1", { y: 40, opacity: 0, duration: 1, ease: "power3.out" }, "-=0.5")
                   .from("p", { y: 30, opacity: 0, duration: 1, ease: "power3.out" }, "-=0.7")
                   .from(".btn-green", { scale: 0.5, opacity: 0, duration: 0.8, ease: "back.out(1.7)" }, "-=0.6")
                   // Animar as cortinas pretas do vídeo abrindo
                   .to("#video-curtain-left", { scaleX: 0, duration: 1.5, ease: "power3.inOut" }, "-=1")
                   .to("#video-curtain-right", { scaleX: 0, duration: 1.5, ease: "power3.inOut" }, "<");
        }"""
        
    content = content.replace(original_intro, new_intro)

    with open(filename, 'w') as f:
        f.write(content)
