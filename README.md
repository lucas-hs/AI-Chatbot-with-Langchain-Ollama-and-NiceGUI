# 🤖 Chatbot Inteligente com LangChain, Ollama e NiceGUI

Este repositório apresenta um **chatbot inteligente** desenvolvido em Python, utilizando **LangChain**, **Ollama (LLM local)**, **Pandas**, **NiceGUI** e arquivos estruturados como base de conhecimento.  
O objetivo é oferecer uma aplicação simples, extensível e orientada a contexto para responder perguntas sobre uma startup.

---

## 🧠 Visão Geral da Arquitetura

- **LLM**: Ollama (modelo `gemma2:2b`) executado localmente  
- **Orquestração de Prompt**: LangChain com `ChatPromptTemplate`  
- **Interface Web**: NiceGUI  
- **Base de Dados**:
  - Arquivo CSV para informações institucionais
  - Arquivos JSON para dados financeiros e produtos
- **Memória de Conversa**: Contexto mantido por concatenação de texto

### Fluxo da Aplicação

1. Carregamento dos dados estruturados (CSV e JSON)  
2. Construção do contexto inicial da startup  
3. Entrada da pergunta do usuário via interface gráfica  
4. Envio de contexto + pergunta ao modelo de linguagem  
5. Exibição da resposta e atualização do histórico da conversa  

---

## ✍️ Exemplo de Prompt

O prompt é estruturado de forma contextual para garantir que o modelo utilize tanto o histórico da conversa quanto os dados institucionais da startup.

Estrutura lógica do prompt:

Responda as perguntas abaixo.  
Este é o contexto histórico da conversa: {contexto}  
Pergunta: {pergunta}  

Resposta:  

Esse formato garante:

- Consistência nas respostas  
- Aproveitamento do histórico acumulado  
- Respostas alinhadas ao domínio da startup  

---

## 📚 Base de Conhecimento

A base de conhecimento do chatbot é composta por arquivos locais estruturados, utilizados para fornecer contexto ao modelo de linguagem.

### Informações Institucionais (CSV)

Arquivo: `startup_info.csv`

Campos utilizados:
- nome  
- equipe  
- ramo  
- objetivo  

Esses dados são carregados com Pandas e utilizados para construir o **contexto inicial da conversa**, servindo como base para todas as interações.

### Dados Financeiros (JSON)

Arquivo: `financials.json`

Contém informações financeiras relevantes da startup.  
Atualmente, esses dados não são injetados diretamente no prompt, mas estão preparados para futuras extensões do sistema.

### Produtos Financeiros (JSON)

Arquivo: `financial_products.json`

Estrutura destinada à descrição de produtos, serviços ou ofertas financeiras, permitindo evolução futura do chatbot para respostas mais especializadas.

---

## 📊 Avaliação e Métricas

No estágio atual, o projeto não implementa métricas automatizadas. A avaliação do chatbot é recomendada com base em critérios qualitativos e quantitativos.

### Métricas Qualitativas

- **Relevância da resposta**: aderência ao contexto fornecido  
- **Clareza**: objetividade e facilidade de compreensão  
- **Consistência**: manutenção das informações ao longo da conversa  

### Métricas Quantitativas (Sugestões Futuras)

- Tempo médio de resposta  
- Taxa de perguntas respondidas sem ambiguidade  
- Índice de satisfação do usuário (feedback manual)  

Essas métricas podem ser incorporadas futuramente por meio de logs, formulários ou ferramentas de observabilidade.

---

## 🚀 Pitch

O **Chatbot Inteligente para Startups** é uma solução leve, local e eficiente para centralizar informações institucionais e responder perguntas de forma contextualizada, utilizando modelos de linguagem executados sem dependência de serviços externos.

O projeto visa oferecer maior controle sobre os dados, reduzir custos operacionais e fornecer uma base sólida para aplicações internas, como suporte, onboarding, consulta institucional e análise preliminar de informações estratégicas.

Com uma arquitetura modular, interface simples e foco em extensibilidade, a solução se posiciona como um ponto de partida confiável para startups que desejam adotar inteligência artificial de forma prática, segura e escalável.

