import re

def fix_support_page(content):
    # Fix form action
    content = content.replace(
        'action="https://formsubmit.co/SEU_EMAIL_AQUI"',
        'action="https://formsubmit.co/suporte@walterespindola.com.br"'
    )
    
    # Add direct email link below the form
    target_button = '''<button type="submit" class="btn-submit mt-2">
                        Enviar mensagem
                    </button>'''
    
    replacement = '''<button type="submit" class="btn-submit mt-2">
                        Enviar mensagem
                    </button>
                    <div class="text-center mt-6">
                        <p class="text-sm text-zinc-500">Ou envie um e-mail diretamente para:</p>
                        <a href="mailto:suporte@walterespindola.com.br" class="text-[#367CF5] font-semibold hover:underline">suporte@walterespindola.com.br</a>
                    </div>'''
    
    content = content.replace(target_button, replacement)
    return content

files = ['suporte.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = fix_support_page(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
