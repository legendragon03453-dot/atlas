import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Delete the duplicated mobile timeline in the Hero Section
# It's between <!-- Conteúdo Principal Centralizado --> and <!-- Título -->
# Let's find <!-- Timeline Direta Mobile --> ... </div> \n        <!-- Título -->
# We will just regex sub it.
content = re.sub(r'<!-- Timeline Direta Mobile -->.*?<!-- Título -->', '<!-- Título -->', content, flags=re.DOTALL, count=1)


# 2. Extract S2 mobile grid and move it outside of pin-master
grid_start = '<div class="md:hidden grid grid-cols-2 gap-3 w-[90%] max-w-sm mt-8 pb-10">'
grid_end = '<!-- Bola Branca de Transição -->'

# We need to find this block and extract it
match = re.search(r'(\s*<div class="md:hidden grid grid-cols-2 gap-3 w-\[90%\] max-w-sm mt-8 pb-10">.*?</div>\s*)(?=<!-- Bola Branca de Transição -->)', content, re.DOTALL)
if match:
    mobile_grid = match.group(1)
    content = content.replace(mobile_grid, '') # remove from current place

    # wrap it in a proper section
    mobile_s2 = f"""
    <!-- S2 Mobile Version (No GSAP) -->
    <section id="s2-mobile" class="md:hidden w-full bg-[#367CF5] flex flex-col items-center pt-8 pb-4 relative z-20">
{mobile_grid}
    </section>
"""
    # insert right before <div id="pin-master"
    content = content.replace('<div id="pin-master" class="w-full bg-[#367CF5] relative">', mobile_s2 + '\n    <div id="pin-master" class="w-full bg-[#367CF5] relative">')

# 3. Fix #s2-container to be hidden on mobile
old_s2 = '<div id="s2-container" class="absolute top-0 left-0 w-full h-screen flex items-center justify-center z-30">'
new_s2 = '<div id="s2-container" class="hidden md:flex absolute top-0 left-0 w-full h-screen items-center justify-center z-30">'
content = content.replace(old_s2, new_s2)

# 4. Remove opacity-0 from #s3-content
old_s3 = '<div id="s3-content" class="w-full flex flex-col items-center pt-8 md:pt-12 opacity-0 z-20 pb-16">'
new_s3 = '<div id="s3-content" class="w-full flex flex-col items-center pt-8 md:pt-12 z-20 pb-16">'
content = content.replace(old_s3, new_s3)

# 5. Make GSAP pin desktop-only
old_gsap = """        let tl = gsap.timeline({
            scrollTrigger: {
                trigger: "#pin-master",
                start: "top top",
                end: "+=1200",
                scrub: 1,
                pin: true,
                anticipatePin: 1
            }
        });

        // Adiciona um tempo de "espera" para o usuário ler a Seção 2 antes da transição começar
        tl.to({}, {duration: 0.5})
          .to("#s2-container .center-box, #s2-container .circle-container", { opacity: 0, duration: 1 })
          .to("#snowball", { autoAlpha: 1, duration: 1 }, "<")
          .to("#snowball", { scale: 0.25, duration: 1 })
          .to("#snowball", { top: "100vh", ease: "power2.in", duration: 1.5 })
          .to("#snowball", { 
              scaleX: 15, 
              scaleY: 3, 
              borderRadius: "50% 50% 0 0", 
              duration: 1.5,
              ease: "power2.out"
          })
          .to("#s3-content", { autoAlpha: 1, duration: 1 })
          .to("#snowball", { opacity: 0, duration: 1 }, "<")
          .set("#s2-container", { display: "none" });"""

new_gsap = """        ScrollTrigger.matchMedia({
            "(min-width: 768px)": function() {
                // Seta opacidade 0 apenas no desktop, pois no mobile não haverá fade-in
                gsap.set("#s3-content", { opacity: 0 });

                let tl = gsap.timeline({
                    scrollTrigger: {
                        trigger: "#pin-master",
                        start: "top top",
                        end: "+=1200",
                        scrub: 1,
                        pin: true,
                        anticipatePin: 1
                    }
                });

                tl.to({}, {duration: 0.5})
                  .to("#s2-container .center-box, #s2-container .circle-container", { opacity: 0, duration: 1 })
                  .to("#snowball", { autoAlpha: 1, duration: 1 }, "<")
                  .to("#snowball", { scale: 0.25, duration: 1 })
                  .to("#snowball", { top: "100vh", ease: "power2.in", duration: 1.5 })
                  .to("#snowball", { 
                      scaleX: 15, 
                      scaleY: 3, 
                      borderRadius: "50% 50% 0 0", 
                      duration: 1.5,
                      ease: "power2.out"
                  })
                  .to("#s3-content", { autoAlpha: 1, opacity: 1, duration: 1 })
                  .to("#snowball", { opacity: 0, duration: 1 }, "<")
                  .set("#s2-container", { display: "none" });
            }
        });"""
content = content.replace(old_gsap, new_gsap)

with open(filepath, 'w') as f:
    f.write(content)

