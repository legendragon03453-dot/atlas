import re

with open('funcionalidades.html', 'r') as f:
    content = f.read()

old_p = '<p class="text-zinc-500 text-lg mb-8">Cinco relatórios profundos gerados sob demanda por Inteligência Artificial sobre os seus dados. O trabalho de um planejador financeiro automatizado.</p>'
new_p = '<p class="text-zinc-500 text-lg mb-8">O mapa completo da sua jornada financeira. Tenha acesso a treinamentos profundos e práticos para dominar o seu dinheiro em cada estágio da vida.</p>'

content = content.replace(old_p, new_p)

with open('funcionalidades.html', 'w') as f:
    f.write(content)

