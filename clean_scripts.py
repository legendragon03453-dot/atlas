import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Clean the Head <script> mess
# Find where the messy tailwind script starts
start_mess = content.find('<script src="https://cdn.tailwindcss.com">')
if start_mess != -1:
    # Find the closing tag of this first script mess
    end_mess = content.find('</script>', start_mess) + len('</script>')
    
    # We will replace all this mess with just the clean tailwind script
    clean_tailwind = '<script src="https://cdn.tailwindcss.com"></script>'
    content = content[:start_mess] + clean_tailwind + content[end_mess:]

# 2. Also remove the next gsapsrc mess that was right after it
start_mess_2 = content.find('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js">')
if start_mess_2 != -1:
    end_mess_2 = content.find('</script>', start_mess_2) + len('</script>')
    clean_gsap = '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>'
    content = content[:start_mess_2] + clean_gsap + content[end_mess_2:]

# 3. Add the logic to the bottom script
bottom_script_start = content.rfind('<script>')
if bottom_script_start != -1:
    # We will insert the logic right after <script>
    logic = """
        document.addEventListener('DOMContentLoaded', () => {
            // Mensal / Anual Toggle
            const btnMensal = document.getElementById('btn-mensal');
            const btnAnual = document.getElementById('btn-anual');
            const priceValues = document.querySelectorAll('.price-value');
            const pricePeriods = document.querySelectorAll('.price-period');

            if(btnMensal && btnAnual) {
                btnMensal.addEventListener('click', () => {
                    btnMensal.classList.add('bg-[#367CF5]', 'text-white', 'shadow-md');
                    btnMensal.classList.remove('text-zinc-500');
                    btnAnual.classList.remove('bg-[#367CF5]', 'text-white', 'shadow-md');
                    btnAnual.classList.add('text-zinc-500');
                    
                    priceValues.forEach(el => el.textContent = 'R$ ' + el.getAttribute('data-mensal'));
                    pricePeriods.forEach(el => el.textContent = '/mês');
                });

                btnAnual.addEventListener('click', () => {
                    btnAnual.classList.add('bg-[#367CF5]', 'text-white', 'shadow-md');
                    btnAnual.classList.remove('text-zinc-500');
                    btnMensal.classList.remove('bg-[#367CF5]', 'text-white', 'shadow-md');
                    btnMensal.classList.add('text-zinc-500');
                    
                    priceValues.forEach(el => el.textContent = 'R$ ' + el.getAttribute('data-anual'));
                    pricePeriods.forEach(el => el.textContent = '/ano');
                });
            }

            // FAQ Accordion
            const faqItems = document.querySelectorAll('.faq-item');
            faqItems.forEach(item => {
                const header = item.querySelector('.faq-header');
                const content = item.querySelector('.faq-content');
                const icon = item.querySelector('.faq-icon');
                
                header.addEventListener('click', () => {
                    const isOpen = content.style.maxHeight;
                    
                    // Close all others
                    faqItems.forEach(otherItem => {
                        const otherContent = otherItem.querySelector('.faq-content');
                        const otherIcon = otherItem.querySelector('.faq-icon');
                        otherContent.style.maxHeight = null;
                        otherIcon.style.transform = 'rotate(0deg)';
                        otherItem.classList.remove('border-[#367CF5]');
                        otherItem.classList.add('border-[#367CF5]/30');
                    });
                    
                    if (!isOpen) {
                        content.style.maxHeight = content.scrollHeight + "px";
                        icon.style.transform = 'rotate(180deg)';
                        item.classList.remove('border-[#367CF5]/30');
                        item.classList.add('border-[#367CF5]');
                    }
                });
            });
        });
"""
    insert_point = bottom_script_start + len('<script>')
    content = content[:insert_point] + logic + content[insert_point:]

with open(filepath, 'w') as f:
    f.write(content)

