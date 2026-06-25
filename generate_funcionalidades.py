import re

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html', 'r') as f:
    index_content = f.read()

head_match = re.search(r'<head>.*?</head>', index_content, re.DOTALL)
head = head_match.group(0) if head_match else '<head></head>'

nav_match = re.search(r'<nav.*?</nav>', index_content, re.DOTALL)
nav = nav_match.group(0) if nav_match else '<nav></nav>'

footer_match = re.search(r'<footer.*?</footer>', index_content, re.DOTALL)
footer = footer_match.group(0) if footer_match else '<footer></footer>'

page_content = f"""<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
{head.replace('<title>Atlas - Toda montanha precisa de um caminho</title>', '<title>Funcionalidades - Atlas</title>')}
<body class="bg-zinc-50 text-zinc-900 font-sans">
    {nav}

    <!-- Hero Section -->
    <header class="pt-32 pb-20 bg-white border-b border-zinc-200">
        <div class="max-w-7xl mx-auto px-6 text-center">
            <h1 class="text-4xl md:text-6xl font-playfair font-normal italic mb-4 text-[#0F172A]">O Mapa Completo.</h1>
            <p class="text-xl text-zinc-600 max-w-2xl mx-auto">Tudo que o Atlas faz para transformar a sua relação com o dinheiro, do dia a dia à sua aposentadoria.</p>
        </div>
    </header>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-6 py-16 flex flex-col lg:flex-row gap-12 relative">
        
        <!-- Sidebar Navigation -->
        <aside class="hidden lg:block w-1/4">
            <div class="sticky top-32 space-y-2">
                <h3 class="text-xs font-bold text-zinc-400 tracking-widest uppercase mb-4">Índice</h3>
                <nav class="flex flex-col space-y-1">
                    <a href="#fundacao" class="px-3 py-2 text-sm text-zinc-600 hover:text-[#367CF5] hover:bg-blue-50 rounded-lg transition-colors font-medium">Fundação e Família</a>
                    <a href="#dia-a-dia" class="px-3 py-2 text-sm text-zinc-600 hover:text-[#367CF5] hover:bg-blue-50 rounded-lg transition-colors font-medium">Controle do Dia a Dia</a>
                    <a href="#analise" class="px-3 py-2 text-sm text-zinc-600 hover:text-[#367CF5] hover:bg-blue-50 rounded-lg transition-colors font-medium">Análise e Inteligência</a>
                    <a href="#decisoes" class="px-3 py-2 text-sm text-zinc-600 hover:text-[#367CF5] hover:bg-blue-50 rounded-lg transition-colors font-medium">Decisões Estratégicas</a>
                    <a href="#planejamento" class="px-3 py-2 text-sm font-bold text-[#367CF5] bg-blue-50/50 hover:bg-blue-50 rounded-lg transition-colors flex justify-between items-center">Planejamento [PRO]</a>
                    <a href="#metodo" class="px-3 py-2 text-sm font-bold text-[#367CF5] bg-blue-50/50 hover:bg-blue-50 rounded-lg transition-colors flex justify-between items-center">Método Atlas [PRO]</a>
                    <a href="#negocios" class="px-3 py-2 text-sm font-bold text-[#367CF5] bg-blue-50/50 hover:bg-blue-50 rounded-lg transition-colors flex justify-between items-center">Atlas Negócios [PRO]</a>
                    <a href="#educacao" class="px-3 py-2 text-sm text-zinc-600 hover:text-[#367CF5] hover:bg-blue-50 rounded-lg transition-colors font-medium">Ecossistema de Educação</a>
                </nav>
            </div>
        </aside>

        <!-- Content -->
        <main class="w-full lg:w-3/4 space-y-24">
            
            <!-- Fundação e Família -->
            <section id="fundacao" class="scroll-mt-32">
                <div class="mb-8">
                    <h2 class="text-3xl font-bold text-[#0F172A] mb-2">Fundação e Família</h2>
                    <p class="text-zinc-500 text-lg">O Atlas foi feito para organizar a vida sozinho ou a dois, sem fricção.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <div class="w-10 h-10 bg-zinc-100 rounded-lg flex items-center justify-center text-zinc-600 mb-4">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                        </div>
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Multi-Perfil Integrado</h3>
                        <p class="text-zinc-600 text-sm">Cadastre Pessoa 1 e Pessoa 2. O Atlas separa automaticamente de quem é cada despesa e receita.</p>
                    </div>
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <div class="w-10 h-10 bg-zinc-100 rounded-lg flex items-center justify-center text-zinc-600 mb-4">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                        </div>
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Seletor de Visão</h3>
                        <p class="text-zinc-600 text-sm">Três botões no topo da tela: Pessoa 1, Pessoa 2 ou Casal. Alterne instantaneamente para ver os dados isolados ou juntos.</p>
                    </div>
                </div>
            </section>

            <!-- Controle do Dia a Dia -->
            <section id="dia-a-dia" class="scroll-mt-32">
                <div class="mb-8">
                    <h2 class="text-3xl font-bold text-[#0F172A] mb-2">Controle do Dia a Dia</h2>
                    <p class="text-zinc-500 text-lg">A fundação de tudo: o lançamento fácil, rápido e a visão do seu mês.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm md:col-span-2">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Lançamento Diário Organizado (8 Abas)</h3>
                        <p class="text-zinc-600 text-sm mb-4">Sua tela de Planejamento e Controle é dividida metodicamente:</p>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-3 py-1 bg-zinc-100 text-zinc-700 text-xs font-semibold rounded-full border border-zinc-200">Geral</span>
                            <span class="px-3 py-1 bg-zinc-100 text-zinc-700 text-xs font-semibold rounded-full border border-zinc-200">Orçamento</span>
                            <span class="px-3 py-1 bg-green-50 text-green-700 text-xs font-semibold rounded-full border border-green-200">Receitas</span>
                            <span class="px-3 py-1 bg-blue-50 text-blue-700 text-xs font-semibold rounded-full border border-blue-200">Fixas</span>
                            <span class="px-3 py-1 bg-orange-50 text-orange-700 text-xs font-semibold rounded-full border border-orange-200">Variáveis</span>
                            <span class="px-3 py-1 bg-purple-50 text-purple-700 text-xs font-semibold rounded-full border border-purple-200">Parcelas</span>
                            <span class="px-3 py-1 bg-red-50 text-red-700 text-xs font-semibold rounded-full border border-red-200">Dívidas</span>
                            <span class="px-3 py-1 bg-teal-50 text-teal-700 text-xs font-semibold rounded-full border border-teal-200">Economias</span>
                        </div>
                    </div>
                    
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Calendário de Pagamentos</h3>
                        <p class="text-zinc-600 text-sm">Visão diária do seu mês. Cada dia mostra o que tem para receber e o que tem para pagar. Evite surpresas no saldo e antecipe seu fluxo.</p>
                    </div>
                    <div class="bg-gradient-to-br from-blue-50 to-indigo-50 p-6 rounded-2xl border border-blue-200 shadow-sm relative overflow-hidden">
                        <div class="absolute top-4 right-4 bg-[#367CF5] text-white text-[10px] font-bold px-2 py-1 rounded">PRO</div>
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Fluxo de Caixa & Importação</h3>
                        <p class="text-zinc-600 text-sm">Visualize seu fluxo completo. Importe o extrato do seu banco via OFX ou traga os dados da sua planilha de uma vez só com nosso importador inteligente.</p>
                    </div>
                </div>
            </section>

            <!-- Análise e Inteligência -->
            <section id="analise" class="scroll-mt-32">
                <div class="mb-8">
                    <h2 class="text-3xl font-bold text-[#0F172A] mb-2">Análise e Inteligência</h2>
                    <p class="text-zinc-500 text-lg">Dado sem análise não muda nada. Transforme números em decisões.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Atlas Score</h3>
                        <p class="text-zinc-600 text-sm">Uma nota de 0 a 100 que resume sua saúde financeira em 7 pilares vitais: reserva, margem, disciplina, alocação, aposentadoria, evolução e saúde PJ.</p>
                    </div>
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Atlas Chat (Sua IA)</h3>
                        <p class="text-zinc-600 text-sm">Pergunte como para um amigo, ele responde como um planejador. "Qual foi minha maior despesa?" — A IA responde baseada nos seus dados reais e sabe separar você do seu parceiro(a).</p>
                    </div>
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm md:col-span-2">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">O Dashboard de Análises</h3>
                        <p class="text-zinc-600 text-sm mb-4">A tela onde você olha seu mês com profundidade, desenhada para ser lida na ordem do consultor:</p>
                        <ul class="text-sm text-zinc-600 space-y-2 list-disc list-inside">
                            <li><strong>Diagnóstico Automático:</strong> Parágrafo gerado pela leitura dos seus dados apontando o que funciona.</li>
                            <li><strong>Pontos de Atenção:</strong> Alertas diretos e específicos.</li>
                            <li><strong>Para Onde Vai:</strong> Quebra das suas despesas por categoria.</li>
                            <li><strong>Horizonte de Parcelamentos:</strong> A curva das parcelas pendentes projetada nos meses seguintes.</li>
                            <li><strong>Visão Anual:</strong> Evolução dos últimos 6 meses.</li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- Decisões Estratégicas -->
            <section id="decisoes" class="scroll-mt-32">
                <div class="mb-8">
                    <h2 class="text-3xl font-bold text-[#0F172A] mb-2">Decisões Estratégicas</h2>
                    <p class="text-zinc-500 text-lg">Simuladores de alto impacto para testar o futuro antes de assinar o contrato.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Simulador de Decisão</h3>
                        <p class="text-zinc-600 text-sm">Oito cenários práticos (comprar imóvel, trocar carro, novo filho, etc.). Insira os dados e veja o impacto exato na sua parcela, fluxo de caixa e no seu Atlas Score — e gere uma análise de viabilidade por IA.</p>
                    </div>
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Consórcio vs Financiamento</h3>
                        <p class="text-zinc-600 text-sm">Compare as duas opções lado a lado, avaliando não só juros e tempo, mas o custo de oportunidade real do seu dinheiro.</p>
                    </div>
                    <div class="bg-gradient-to-br from-blue-50 to-indigo-50 p-6 rounded-2xl border border-blue-200 shadow-sm md:col-span-2 relative overflow-hidden">
                        <div class="absolute top-4 right-4 bg-[#367CF5] text-white text-[10px] font-bold px-2 py-1 rounded">PRO</div>
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Calculadoras Express</h3>
                        <p class="text-zinc-600 text-sm">Respostas imediatas: <strong>Express Aposentadoria</strong> (quanto poupar hoje para sua renda do futuro) e <strong>Express Objetivos</strong> (quanto aportar por mês para juntar X em Y anos).</p>
                    </div>
                </div>
            </section>

            <!-- Planejamento Financeiro [PRO] -->
            <section id="planejamento" class="scroll-mt-32">
                <div class="mb-8 flex items-center gap-3">
                    <h2 class="text-3xl font-bold text-[#0F172A]">Planejamento Financeiro</h2>
                    <span class="bg-[#367CF5] text-white text-xs font-bold px-2.5 py-1 rounded-md">PRO</span>
                </div>
                <p class="text-zinc-500 text-lg mb-8">Construa o seu futuro. Módulos avançados que costuram seus investimentos, bens, metas e seguros em um plano de vida.</p>
                
                <div class="space-y-6">
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Aposentadoria: 3 Respostas Diferentes</h3>
                        <p class="text-zinc-600 text-sm mb-3">Preencha seu cenário real e descubra o quanto você precisa aportar hoje para alcançar os 3 caminhos:</p>
                        <ul class="text-sm text-zinc-600 list-disc list-inside">
                            <li><strong>Cenário Realidade:</strong> Onde você vai chegar mantendo o aporte atual.</li>
                            <li><strong>Cenário Consumo:</strong> Juntar para gastar consumindo o patrimônio até o fim da vida.</li>
                            <li><strong>Cenário Viver de Renda:</strong> O valor necessário para viver apenas de dividendos, sem encostar no principal.</li>
                        </ul>
                    </div>
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Objetivos de Vida Mapeados</h3>
                        <p class="text-zinc-600 text-sm">Saia do "um dia eu quero" para o "quanto e quando". Cadastre metas (carro, casamento, filho) e o Atlas calcula o aporte sugerido com juros. Se deixar de aportar, ele avisa que a meta está atrasando.</p>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                            <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Investimentos & Proventos</h3>
                            <p class="text-zinc-600 text-sm">Visão consolidada da carteira, Stock Guide, histórico, importação de notas e cálculo de Resultado de Imposto de Renda. Seus investimentos conversam com seu planejamento.</p>
                        </div>
                        <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                            <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Bens, Imóveis e Seguros</h3>
                            <p class="text-zinc-600 text-sm">Descubra seu Patrimônio Líquido real (descontando dívidas do bem). Calcule matematicamente o seu <strong>Seguro de Vida Ideal</strong> para proteger sua família.</p>
                        </div>
                    </div>
                    <div class="bg-[#0B1A30] text-white p-8 rounded-2xl border border-[#1e293b] shadow-xl relative overflow-hidden">
                        <div class="absolute inset-0 bg-[linear-gradient(to_right,#ffffff05_1px,transparent_1px),linear-gradient(to_bottom,#ffffff05_1px,transparent_1px)] bg-[size:24px_24px]"></div>
                        <div class="relative z-10">
                            <h3 class="text-2xl font-bold mb-3">Análise Atlas (O Clímax)</h3>
                            <p class="text-blue-100/80 text-sm mb-4">A tela onde toda a sua vida se cruza. Ela não te mostra dados isolados, ela faz as perguntas difíceis do consultor:</p>
                            <ul class="text-sm text-blue-100/80 space-y-2 list-disc list-inside font-medium">
                                <li>A sua reserva aguenta o seu estilo de vida?</li>
                                <li>Índice de Independência Financeira (o quanto já caminhou para viver de renda).</li>
                                <li>Suas metas batem com a sua realidade atual de poupança?</li>
                                <li>Trajetória do seu Atlas Score.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Método Atlas [PRO] -->
            <section id="metodo" class="scroll-mt-32">
                <div class="mb-8 flex items-center gap-3">
                    <h2 class="text-3xl font-bold text-[#0F172A]">Método Atlas (Consultoria IA)</h2>
                    <span class="bg-[#367CF5] text-white text-xs font-bold px-2.5 py-1 rounded-md">PRO</span>
                </div>
                <p class="text-zinc-500 text-lg mb-8">Cinco relatórios profundos gerados sob demanda por Inteligência Artificial sobre os seus dados. O trabalho de um planejador financeiro automatizado.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm md:col-span-2">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">1. A Vista da Montanha</h3>
                        <p class="text-zinc-600 text-sm">A projeção do seu patrimônio até o fim da vida em um gráfico vivo. Arraste o aporte ou a rentabilidade e veja a curva mudar na hora. Adicione "eventos" (ex: ter filho) e veja o tranco financeiro a longo prazo.</p>
                    </div>
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">2. Base da Montanha</h3>
                        <p class="text-zinc-600 text-sm">Raio-X da fundação: reserva em meses, liquidez, e um "Semáforo" dizendo a recomendação mais urgente que você deve seguir hoje.</p>
                    </div>
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">3. Estratégia de Subida</h3>
                        <p class="text-zinc-600 text-sm">Cruza sua capacidade com seus sonhos. Avalia a viabilidade do plano, aponta o "gap" financeiro e o que deve ser ajustado.</p>
                    </div>
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">4. Controle da Jornada</h3>
                        <p class="text-zinc-600 text-sm">O acompanhamento do fluxo de caixa: onde você está se desviando e alertas operacionais para manter o plano nos trilhos.</p>
                    </div>
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">5. Guia da Jornada</h3>
                        <p class="text-zinc-600 text-sm">O relatório integrado final: diagnóstico executivo, prioridades e um Plano de Ação concreto. Gere em PDF como se tivesse saído de uma reunião de consultoria.</p>
                    </div>
                </div>
            </section>

            <!-- Atlas Negócios [PRO] -->
            <section id="negocios" class="scroll-mt-32">
                <div class="mb-8 flex items-center gap-3">
                    <h2 class="text-3xl font-bold text-[#0F172A]">Atlas Negócios</h2>
                    <span class="bg-[#367CF5] text-white text-xs font-bold px-2.5 py-1 rounded-md">PRO</span>
                </div>
                <p class="text-zinc-500 text-lg mb-8">Gestão poderosa para empreendedores. A sua vida pessoal e a da sua empresa finalmente separadas, mas conectadas.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Regras de Alocação</h3>
                        <p class="text-zinc-600 text-sm">Defina quanto do que entra é pró-labore, quanto é distribuição de lucro e quanto fica no caixa da empresa de segurança.</p>
                    </div>
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Histórico de Transferências</h3>
                        <p class="text-zinc-600 text-sm">A ponte entre PJ e PF automatizada: o que sai da empresa entra no seu caixa pessoal categorizado, sem contar dinheiro dobrado.</p>
                    </div>
                    <div class="bg-white p-6 rounded-2xl border border-zinc-200 shadow-sm md:col-span-2">
                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Ferramentas de Gestão Embutidas</h3>
                        <ul class="text-sm text-zinc-600 list-disc list-inside mt-2 space-y-1">
                            <li><strong>Multi-empresas suportado.</strong></li>
                            <li><strong>Previsão de Caixa</strong> e Simulador de Fluxo.</li>
                            <li><strong>Templates recorrentes</strong> para assinaturas e contabilidade.</li>
                            <li><strong>Gestão de Clientes (CPF/CNPJ)</strong> controlando Receita Prevista vs Confirmada.</li>
                            <li><strong>Score de Saúde da Empresa</strong> alimentando diretamente a sua nota pessoal!</li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- Ecossistema de Educação -->
            <section id="educacao" class="scroll-mt-32">
                <div class="mb-8">
                    <h2 class="text-3xl font-bold text-[#0F172A] mb-2">Ecossistema de Educação</h2>
                    <p class="text-zinc-500 text-lg">Aprender a usar o app é a metade. Aprender a pensar diferente é a outra metade.</p>
                </div>
                <div class="bg-gradient-to-tr from-zinc-50 to-white p-8 rounded-2xl border border-zinc-200 shadow-sm">
                    <h3 class="text-xl font-playfair font-normal italic mb-6">Cursos dentro da plataforma:</h3>
                    <div class="space-y-4">
                        <div class="p-4 bg-white border border-zinc-200 rounded-xl relative overflow-hidden">
                            <div class="absolute left-0 top-0 bottom-0 w-1 bg-green-500"></div>
                            <h4 class="font-bold text-[#1a1a1a] flex items-center gap-2">Organização na Prática <span class="text-[10px] font-bold text-white bg-green-500 px-2 py-0.5 rounded uppercase">Onde começar</span></h4>
                            <p class="text-sm text-zinc-600 mt-1">O ritual diário, semanal e mensal de uso do Atlas para deixar sua organização no piloto automático em 2 semanas.</p>
                        </div>
                        <div class="p-4 bg-white border border-zinc-200 rounded-xl">
                            <h4 class="font-bold text-[#1a1a1a]">Manual do Dinheiro</h4>
                            <p class="text-sm text-zinc-600 mt-1">A base conceitual profunda sobre o funcionamento do dinheiro e mentalidade financeira.</p>
                        </div>
                        <div class="p-4 bg-white border border-zinc-200 rounded-xl">
                            <h4 class="font-bold text-[#1a1a1a]">Planejamento Financeiro & Plano da Liberdade</h4>
                            <p class="text-sm text-zinc-600 mt-1">Cursos avançados para destrinchar as lógicas de aposentadoria e alcance da independência financeira.</p>
                        </div>
                    </div>
                </div>
            </section>

        </main>
    </div>

    <!-- CTA Final -->
    <section class="bg-[#0B1A30] text-white py-24 text-center mt-12 border-t border-[#1e293b]">
        <div class="max-w-3xl mx-auto px-6">
            <h2 class="text-3xl md:text-5xl font-playfair font-normal italic mb-6">A maioria das pessoas falha por falta de clareza, não de dinheiro.</h2>
            <p class="text-blue-100 text-lg mb-10">O Atlas te entrega o mapa completo.</p>
            <a href="https://app.atlas.com.br" class="inline-flex items-center justify-center bg-[#367CF5] hover:bg-blue-600 text-white font-bold py-4 px-10 rounded-xl transition-all shadow-[0_0_20px_rgba(54,124,245,0.4)] hover:shadow-[0_0_30px_rgba(54,124,245,0.6)]">
                Assinar o Atlas
            </a>
        </div>
    </section>

    {footer}
</body>
</html>
"""

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/funcionalidades.html', 'w') as f:
    f.write(page_content)

