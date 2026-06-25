import re

def add_functionality_button(content):
    target = '</div> <!-- Fechamento do overflow-x-auto -->'
    replacement = '''</div> <!-- Fechamento do overflow-x-auto -->
                
                <div class="mt-12 flex justify-center w-full">
                    <a href="funcionalidades.html" class="inline-flex items-center gap-3 px-8 py-4 bg-white border-2 border-atlas-blue text-atlas-blue font-bold text-lg rounded-xl hover:bg-atlas-lightBlue/10 transition-colors shadow-sm hover:shadow-md">
                        Ver lista completa de funcionalidades
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </a>
                </div>'''
    content = content.replace(target, replacement)
    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = add_functionality_button(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
