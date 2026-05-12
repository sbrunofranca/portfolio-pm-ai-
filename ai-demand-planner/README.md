=========================================================
AI DEMAND PLANNER — SUPPLY CHAIN COPILOT
=========================================================

========================
VISÃO DO PROJETO
========================

O AI Demand Planner é um copiloto inteligente de supply chain que combina:

- Machine Learning para previsão de demanda
- Regras de negócio para geração de insights
- LLM (Groq) para explicações em linguagem natural

Objetivo:
Transformar dados operacionais em decisões acionáveis para times de negócio,
reduzindo dependência de dashboards e análises técnicas.

=========================================================

========================
PROBLEMA REAL
=========================

Times de supply chain enfrentam:

- Dependência de dashboards complexos
- Dificuldade para interpretar previsões
- Baixa acessibilidade para usuários não técnicos
- Atraso na tomada de decisão

=========================================================

========================
CONTEXTO (USUÁRIO E NEGÓCIO)
=========================

Usuários:
- Analistas de supply chain
- Planejadores de demanda
- Gestores de operações

Dor principal:
“Eu preciso entender rapidamente o que vai acontecer com a demanda e o que devo fazer.”

=========================================================

========================
HIPÓTESE
=========================

Se combinarmos:

- Forecast de demanda (ML)
- Regras de negócio
- Explicação via LLM

Então usuários conseguem tomar decisões mais rápidas e assertivas sem depender de dashboards.

=========================================================

========================
SOLUÇÃO (PRODUTO + TÉCNICA)
=========================

Fluxo do sistema:

1. Dados históricos são processados
2. Modelo de ML gera previsão
3. Engine de regras gera insights
4. LLM (Groq) gera explicações
5. Streamlit exibe tudo em UI

=========================================================

========================
ARQUITETURA
=========================

UI (Streamlit)
   ↓
Pipeline (app/pipeline.py)
   ↓
Forecast Model (ML)
   ↓
Insights Engine (Rules)
   ↓
LLM Layer (Groq)

=========================================================

========================
FUNCIONALIDADES
=========================

Forecast:
- Previsão de demanda baseada em histórico

Insights:
- Tendência (alta/queda)
- Risco de estoque
- Picos de demanda
- Recomendações

LLM:
- Explicações em linguagem natural
- Interpretação de previsões
- Sugestões de ação

UI:
- Dashboard interativo em Streamlit

=========================================================

========================
TECNOLOGIAS
=========================

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Groq API
- python-dotenv

=========================================================

========================
MÉTRICAS DE SUCESSO
=========================

- Redução do tempo de análise
- Melhor qualidade de decisão
- Redução de dependência de dashboards
- Adoção por usuários não técnicos

=========================================================

========================
IMPACTO ESPERADO
=========================

- Decisão mais rápida em supply chain
- Redução de overstock e stockout
- Democratização de dados
- Aumento de eficiência operacional

=========================================================

========================
COMO EXECUTAR
=========================

1. clonar repositório
git clone <repo>
cd ai-demand-planner

2. criar ambiente
python -m venv venv
source venv/bin/activate

3. instalar dependências
pip install -r requirements.txt

4. criar .env
GROQ_API_KEY=sua_chave_aqui

5. rodar app
streamlit run ui/streamlit_app.py

=========================================================

========================
TRADE-OFFS
=========================

- Simplicidade vs precisão (modelo simples no MVP)
- Regras vs aprendizado automático (híbrido)
- Latência vs inteligência (LLM adiciona custo)
- Escalabilidade futura já considerada

=========================================================

========================
PRÓXIMOS PASSOS (ETAPA 5)
=========================

MULTI-AGENT SYSTEM:

- Forecast Agent
- Risk Agent
- Business Strategy Agent
- Orchestrator Agent

Novas capacidades:

- Chat com dados
- Perguntas em linguagem natural
- Simulação de cenários
- Decisão assistida por IA

=========================================================

========================
VISÃO FINAL DO PRODUTO
=========================

AI Decision Intelligence System para Supply Chain

=========================================================

AUTOR:
Bruno França
Product Manager | AI | Analytics | GenAI Systems
=========================================================