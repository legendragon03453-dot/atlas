import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

new_ice = """
        <!-- CSS Snow/Ice Particles -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden z-10">
            <!-- Camada de trás (menores, mais lentas, opacidade menor) -->
            <div class="absolute w-2 h-2 bg-white/50 rounded-sm top-[-5%] left-[10%] [animation:snowfall_12s_linear_infinite_0s]"></div>
            <div class="absolute w-1.5 h-1.5 bg-white/40 rounded-sm top-[-5%] left-[25%] [animation:snowfall_14s_linear_infinite_2s]"></div>
            <div class="absolute w-2 h-2 bg-white/60 rounded-sm top-[-5%] left-[40%] [animation:snowfall_11s_linear_infinite_4s]"></div>
            <div class="absolute w-1.5 h-1.5 bg-white/40 rounded-sm top-[-5%] left-[60%] [animation:snowfall_15s_linear_infinite_1s]"></div>
            <div class="absolute w-2 h-2 bg-white/50 rounded-sm top-[-5%] left-[80%] [animation:snowfall_13s_linear_infinite_5s]"></div>
            <div class="absolute w-1.5 h-1.5 bg-white/60 rounded-sm top-[-5%] left-[90%] [animation:snowfall_16s_linear_infinite_3s]"></div>
            
            <!-- Camada da frente (maiores, mais rápidas, com blur/reflexo) -->
            <div class="absolute w-3 h-3 bg-white/80 rounded top-[-5%] left-[15%] shadow-[0_0_10px_white] [animation:snowfall_8s_linear_infinite_6s]"></div>
            <div class="absolute w-4 h-4 bg-white/70 rounded backdrop-blur-sm blur-[1px] top-[-5%] left-[35%] [animation:snowfall_10s_linear_infinite_8s]"></div>
            <div class="absolute w-2.5 h-2.5 bg-white/90 rounded top-[-5%] left-[55%] shadow-[0_0_8px_white] [animation:snowfall_7s_linear_infinite_7s]"></div>
            <div class="absolute w-5 h-5 bg-white/60 rounded-lg backdrop-blur-md blur-[2px] top-[-5%] left-[70%] [animation:snowfall_11s_linear_infinite_9s]"></div>
            <div class="absolute w-3 h-3 bg-white/80 rounded top-[-5%] left-[85%] shadow-[0_0_12px_white] [animation:snowfall_9s_linear_infinite_10s]"></div>
        </div>
"""

# Insert right after hero-container
hero_idx = content.find('<section class="hero-container">')
if hero_idx != -1 and '<!-- CSS Snow/Ice Particles -->' not in content:
    insert_idx = hero_idx + len('<section class="hero-container">')
    content = content[:insert_idx] + new_ice + content[insert_idx:]

with open(filepath, 'w') as f:
    f.write(content)

