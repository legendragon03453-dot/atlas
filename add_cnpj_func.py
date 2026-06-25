import re

def add_cnpj_to_funcionalidades(content):
    target = """                <a href="#" class="hover:text-white transition-colors">Suporte</a>
                </nav>

            <!-- Menu Mobile Overlay -->
            
        </div>
    </footer>"""
    
    replacement = """                <a href="suporte.html" class="hover:text-white transition-colors">Suporte</a>
                </nav>

                <!-- Copyright -->
                <div class="text-center pt-4 md:pt-6 border-t border-white/20 w-full pb-2 md:pb-0">
                    <p class="text-sm text-white/60">
                        &copy; 2026 Atlas. Todos os direitos reservados.
                    </p>
                    <p class="text-xs text-white/50 mt-1">
                        CNPJ: 59.816.277/0001-30
                    </p>
                </div>
            
        </div>
    </footer>"""
    
    if target in content:
        return content.replace(target, replacement)
    else:
        # Regex fallback
        return re.sub(
            r'</nav>\s*<!-- Menu Mobile Overlay -->\s*</div>\s*</footer>',
            r'</nav>\n<!-- Copyright -->\n<div class="text-center pt-4 md:pt-6 border-t border-white/20 w-full pb-2 md:pb-0">\n<p class="text-sm text-white/60">&copy; 2026 Atlas. Todos os direitos reservados.</p>\n<p class="text-xs text-white/50 mt-1">CNPJ: 59.816.277/0001-30</p>\n</div>\n</div>\n</footer>',
            content,
            flags=re.DOTALL
        )

files = ['funcionalidades.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = add_cnpj_to_funcionalidades(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
