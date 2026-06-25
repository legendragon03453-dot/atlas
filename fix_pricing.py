import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Remove "Funcionalidade Avançada X"
content = re.sub(r'<li class="flex items-start gap-3">.*?Funcionalidade Avançada \d.*?</li>\n*', '', content)

# 2. Remove Elite items
content = re.sub(r'<li class="flex items-start gap-3">.*?Mentoria Exclusiva Anual.*?</li>\n*', '', content)
content = re.sub(r'<li class="flex items-start gap-3">.*?Acesso VIP a Eventos.*?</li>\n*', '', content)

# 3. Add 4 more rows to the comparison table
table_end = """                    <!-- Row 8 (Text) -->
                    <div class="p-4 px-6 text-zinc-700 font-medium bg-zinc-50/50">Suporte</div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50 text-zinc-500 font-medium">Comunidade</div>
                    <div class="p-4 flex justify-center items-center bg-[#eff4ff]/50 text-zinc-700 font-medium">Email</div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50 text-zinc-700 font-medium">Prioritário</div>"""

new_rows = """
                    <!-- Row 9 -->
                    <div class="p-4 px-6 text-zinc-700 font-medium">Calculadoras Express</div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>

                    <!-- Row 10 -->
                    <div class="p-4 px-6 text-zinc-700 font-medium bg-zinc-50/50">Simulador de Decisão</div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50"><svg class="w-5 h-5 text-zinc-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"></path></svg></div>
                    <div class="p-4 flex justify-center items-center bg-[#eff4ff]/50"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>

                    <!-- Row 11 -->
                    <div class="p-4 px-6 text-zinc-700 font-medium">Aposentadoria: 3 Respostas</div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-zinc-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>

                    <!-- Row 12 -->
                    <div class="p-4 px-6 text-zinc-700 font-medium bg-zinc-50/50">Objetivos de Vida Mapeados</div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center bg-[#eff4ff]/50"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center bg-zinc-50/50"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>

                    <!-- Row 13 -->
                    <div class="p-4 px-6 text-zinc-700 font-medium">Calendário de Pagamentos</div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                    <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
"""

content = content.replace(table_end, table_end + new_rows)

# 4. Update FAQ question
old_faq_q = '<h3 class="text-base md:text-lg font-semibold text-[#1a1a1a] pr-4">O Plano da Liberdade está incluso?</h3>'
new_faq_q = '<h3 class="text-base md:text-lg font-semibold text-[#1a1a1a] pr-4">O Plano da Liberdade e os outros cursos estão inclusos?</h3>'
content = content.replace(old_faq_q, new_faq_q)

old_faq_a = 'Sim. Todos os alunos do Atlas têm acesso integral ao treinamento "Plano da Liberdade", além de todos os bônus e aulas futuras, dentro da nossa plataforma unificada.'
new_faq_a = 'Sim. Todos os alunos do Atlas Elite têm acesso integral aos treinamentos como "O Plano da Liberdade", "Manual do Dinheiro" e outros do nosso Ecossistema de Educação (alguns em breve), dentro da nossa plataforma unificada.'
content = content.replace(old_faq_a, new_faq_a)

with open('index.html', 'w') as f:
    f.write(content)

