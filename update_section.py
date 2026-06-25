import re

with open('index.html', 'r') as f:
    content = f.read()

new_section = """    <!-- === SEÇÃO 8: Comparação de Planos (Premium) === -->
    <style>
        .pricing-section {
            background-color: #ffffff;
            color: #1a1a1a;
            font-family: 'Inter', sans-serif;
            overflow: hidden;
        }
        .pricing-card {
            border-radius: 20px;
            transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
            background: #ffffff;
            border: 1px solid #f0f0f0;
        }
        .pricing-card:hover {
            transform: scale(1.02) translateY(-4px);
            box-shadow: 0 20px 40px -10px rgba(0,0,0,0.08);
            border-color: #e5e5e5;
        }
        .pricing-card.pro-card {
            border: 2px solid #367CF5;
            box-shadow: 0 10px 30px -10px rgba(54,124,245,0.15);
            position: relative;
        }
        .pricing-card.pro-card::before {
            content: '';
            position: absolute;
            inset: -2px;
            border-radius: 22px;
            background: linear-gradient(135deg, rgba(54,124,245,0.4), rgba(54,124,245,0));
            z-index: -1;
            opacity: 0;
            transition: opacity 0.4s ease;
        }
        .pricing-card.pro-card:hover::before {
            opacity: 1;
        }
        
        .pricing-table-container {
            border-radius: 20px;
            border: 1px solid #f0f0f0;
            background: #ffffff;
            box-shadow: 0 4px 20px rgba(0,0,0,0.03);
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }
        
        .pricing-table {
            width: 100%;
            min-width: 800px;
            border-collapse: separate;
            border-spacing: 0;
        }
        
        .pricing-table th {
            position: sticky;
            top: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(12px);
            z-index: 10;
            padding: 24px 16px;
            border-bottom: 1px solid #f0f0f0;
            text-align: center;
        }
        .pricing-table th:first-child {
            text-align: left;
            padding-left: 32px;
            z-index: 11;
            left: 0;
        }
        
        .pricing-table td {
            padding: 16px;
            text-align: center;
            border-bottom: 1px solid #f5f5f5;
            transition: background-color 0.2s ease;
        }
        .pricing-table td:first-child {
            text-align: left;
            padding-left: 32px;
            font-weight: 500;
            color: #4a4a4a;
            position: sticky;
            left: 0;
            background: #ffffff;
            z-index: 5;
        }
        
        .pricing-table tr.category-row td {
            background: #fcfcfc;
            font-weight: 700;
            color: #1a1a1a;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-size: 0.75rem;
            padding-top: 32px;
            padding-bottom: 12px;
            border-bottom: 1px solid #eaeaea;
        }
        .pricing-table tr.category-row td:first-child {
            background: #fcfcfc;
        }
        
        .pricing-table tr:not(.category-row):hover td {
            background: #f9fafb;
        }
        .pricing-table tr:not(.category-row):hover td:first-child {
            background: #f9fafb;
        }
        
        .check-pop {
            display: inline-block;
            transform: scale(0);
            opacity: 0;
        }
        
        .table-row-stagger {
            opacity: 0;
            transform: translateY(10px);
        }
        
        .pro-col {
            background: rgba(239, 244, 255, 0.3);
        }
        .pricing-table th.pro-col {
            background: rgba(245, 248, 255, 0.95);
        }
        .pricing-table tr:not(.category-row):hover td.pro-col {
            background: rgba(239, 244, 255, 0.6);
        }
        
        .btn-manage {
            background: #f5f5f5;
            color: #1a1a1a;
            border: 1px solid #e5e5e5;
            transition: all 0.3s ease;
        }
        .btn-manage:hover {
            background: #ffffff;
            border-color: #d4d4d4;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
    </style>

    <section id="section-8" class="pricing-section w-full py-20 lg:py-32 px-4 relative border-t border-zinc-100">
        <div class="container mx-auto max-w-6xl">
            
            <!-- Header Pricing -->
            <div class="flex flex-col items-center text-center gap-4 mb-20">
                <h2 class="text-4xl md:text-5xl lg:text-6xl font-bold text-[#1a1a1a] tracking-tight max-w-3xl scroll-reveal">
                    Comparação de Planos
                </h2>
                <p class="text-xl text-zinc-500 max-w-2xl scroll-reveal">
                    Escolha o plano ideal para o seu momento financeiro.
                </p>
            </div>

            <!-- 3 Cards Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8 max-w-5xl mx-auto mb-16 relative z-10">
                
                <!-- Essencial -->
                <div class="pricing-card p-8 flex flex-col justify-between scroll-reveal">
                    <div>
                        <h3 class="text-2xl font-bold text-[#1a1a1a] mb-2">Atlas Essencial</h3>
                        <p class="text-zinc-500 text-sm mb-8 min-h-[40px]">Controle financeiro e organização da vida financeira.</p>
                        <div class="flex items-end gap-1 mb-8">
                            <span class="text-4xl font-bold text-[#1a1a1a]">R$ 15,90</span>
                            <span class="text-zinc-500 font-medium mb-1">/mês</span>
                        </div>
                    </div>
                </div>

                <!-- Pro -->
                <div class="pricing-card pro-card p-8 flex flex-col justify-between scroll-reveal" style="transition-delay: 100ms;">
                    <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-[#367CF5] text-white text-xs font-bold px-4 py-1.5 rounded-full shadow-sm uppercase tracking-wide whitespace-nowrap">
                        Seu plano atual
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-[#367CF5] mb-2">Atlas Pro</h3>
                        <p class="text-zinc-500 text-sm mb-8 min-h-[40px]">Planejamento financeiro completo + automações + Atlas Negócios + Mapa do Futuro.</p>
                        <div class="flex items-end gap-1 mb-8">
                            <span class="text-4xl font-bold text-[#1a1a1a]">R$ 24,90</span>
                            <span class="text-zinc-500 font-medium mb-1">/mês</span>
                        </div>
                    </div>
                </div>

                <!-- Elite -->
                <div class="pricing-card p-8 flex flex-col justify-between scroll-reveal" style="transition-delay: 200ms;">
                    <div>
                        <h3 class="text-2xl font-bold text-[#1a1a1a] mb-2">Atlas Elite</h3>
                        <p class="text-zinc-500 text-sm mb-8 min-h-[40px]">Tudo do Pro + educação financeira premium e conteúdos exclusivos.</p>
                        <div class="flex items-end gap-1 mb-6">
                            <span class="text-4xl font-bold text-[#1a1a1a]">R$ 32,90</span>
                            <span class="text-zinc-500 font-medium mb-1">/mês</span>
                        </div>
                        <div class="bg-amber-50 text-amber-700 text-xs font-medium px-3 py-2 rounded-lg border border-amber-100/50">
                            Inclui acesso ao Plano da Liberdade e conteúdos educacionais exclusivos.
                        </div>
                    </div>
                </div>

            </div>

            <!-- Gerenciar Assinatura -->
            <div class="max-w-3xl mx-auto bg-[#fafafa] rounded-2xl border border-zinc-200 p-6 md:p-8 flex flex-col md:flex-row items-center justify-between gap-6 mb-24 shadow-sm scroll-reveal">
                <div>
                    <h4 class="text-lg font-bold text-[#1a1a1a] mb-1">Gerenciar assinatura</h4>
                    <p class="text-sm text-zinc-500">Faça upgrade, cancele, atualize seu cartão ou veja suas faturas.</p>
                </div>
                <button class="btn-manage px-6 py-3 rounded-xl font-semibold whitespace-nowrap w-full md:w-auto">
                    Gerenciar assinatura
                </button>
            </div>

            <!-- Tabela Comparativa Moderna -->
            <div class="w-full max-w-5xl mx-auto scroll-reveal" id="pricing-table-wrapper">
                <div class="pricing-table-container">
                    <table class="pricing-table">
                        <thead>
                            <tr>
                                <th>Funcionalidade</th>
                                <th>Essencial</th>
                                <th class="pro-col border-b-2 border-[#367CF5] text-[#367CF5]">Pro</th>
                                <th>Elite</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Controle Financeiro -->
                            <tr class="category-row">
                                <td colspan="4">Controle Financeiro</td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Planejamento e Controle</td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Lançamentos</td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Calendário de Pagamentos</td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Análises</td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Assistente Atlas (IA)</td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>

                            <!-- Automação Financeira -->
                            <tr class="category-row">
                                <td colspan="4">Automação Financeira</td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Fatura do Cartão</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Importar Extrato Bancário</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Importar OFX</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Importar Planilha</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>

                            <!-- Planejamento Estratégico -->
                            <tr class="category-row">
                                <td colspan="4">Planejamento Estratégico</td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Planejamento de Vida</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Simulação de Objetivos</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Projeções Financeiras</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Planejamento de Aposentadoria</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Simulador de Decisão</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Simulador de Financiamento</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>

                            <!-- Planejamento de Futuro -->
                            <tr class="category-row">
                                <td colspan="4">Planejamento de Futuro</td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Mapa do Futuro</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Vista da Montanha</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Eventos da Vida na linha do tempo</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Simulação de cenários patrimoniais</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>

                            <!-- Patrimônio e Investimentos -->
                            <tr class="category-row">
                                <td colspan="4">Patrimônio e Investimentos</td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Controle Patrimonial</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Controle de Investimentos</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Evolução Patrimonial</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Proteção & Seguros</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Bens e Imóveis</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Renda Passiva com FIIs <span class="text-[10px] bg-zinc-100 text-zinc-500 px-1.5 py-0.5 rounded ml-2">EM BREVE</span></td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>

                            <!-- Atlas Negócios -->
                            <tr class="category-row">
                                <td colspan="4">Atlas Negócios</td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Controle Financeiro Empresarial</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Fluxo de Caixa Empresarial</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Análise Financeira do Negócio</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>

                            <!-- Relatórios Inteligentes -->
                            <tr class="category-row">
                                <td colspan="4">Relatórios Inteligentes</td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Relatório de Vida Financeira</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>

                            <!-- Educação Financeira -->
                            <tr class="category-row">
                                <td colspan="4">Educação Financeira</td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Organização na Prática</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Manual do Dinheiro</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Planejamento Financeiro (curso)</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Plano da Liberdade</td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                            <tr class="table-row-stagger">
                                <td>Conteúdos exclusivos <span class="text-[10px] bg-zinc-100 text-zinc-500 px-1.5 py-0.5 rounded ml-2">EM BREVE</span></td>
                                <td><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td class="pro-col"><i data-lucide="x" class="w-5 h-5 text-zinc-300 mx-auto"></i></td>
                                <td><i data-lucide="check" class="w-5 h-5 text-emerald-500 mx-auto check-pop"></i></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- GSAP Animations for this section -->
            <script>
                document.addEventListener("DOMContentLoaded", function() {
                    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
                        gsap.registerPlugin(ScrollTrigger);
                        
                        // Animate rows
                        const rows = document.querySelectorAll('.table-row-stagger');
                        if (rows.length > 0) {
                            gsap.to(rows, {
                                scrollTrigger: {
                                    trigger: "#pricing-table-wrapper",
                                    start: "top 80%",
                                },
                                opacity: 1,
                                y: 0,
                                duration: 0.4,
                                stagger: 0.03,
                                ease: "power2.out"
                            });
                        }

                        // Animate checks pop in
                        const checks = document.querySelectorAll('.check-pop');
                        if (checks.length > 0) {
                            gsap.to(checks, {
                                scrollTrigger: {
                                    trigger: "#pricing-table-wrapper",
                                    start: "top 70%",
                                },
                                scale: 1,
                                opacity: 1,
                                duration: 0.5,
                                stagger: 0.01,
                                ease: "back.out(1.7)",
                                delay: 0.2
                            });
                        }
                    }
                });
            </script>

        </div>
    </section>"""

pattern = re.compile(r'<!-- === SEÇÃO 8: Pricing === -->.*?</section>', re.DOTALL)
new_content = pattern.sub(new_section, content)

with open('index.html', 'w') as f:
    f.write(new_content)
