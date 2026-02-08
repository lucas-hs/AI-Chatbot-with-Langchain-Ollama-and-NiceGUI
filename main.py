from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd
import json
from nicegui import ui

modelo = OllamaLLM(model="gemma2:2b")
template = """
    Responda as perguntas abaixo.

    Este é o contexto histórico da conversa: {contexto}

    Pergunta: {pergunta}

    Resposta:
"""
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | modelo

startup_exc = pd.read_csv("./data/startup_info.csv")
financials = json.load(open("./data/financials.json", "rb"))
financial_products = json.load(open("./data/financial_products.json"))


startup = startup_exc.iloc[0]
contexto = f"""
      NOME:{startup['nome']}
      EQUIPE:{startup['equipe']}
      RAMO:{startup['ramo']}
      OBJETIVO:{startup['objetivo']}
    """


ui.label("Chatbot Inteligente").classes("text-2xl font-bold")
chat_area = ui.column().classes("w-full")

def enviar_mensagem():
    global contexto 

    pergunta = user_input.value 
    if not pergunta:
        return 
    
    with chat_area:
        ui.chat_message(pergunta, name="Você", sent=True)

    resposta = chain.invoke({
        "contexto": contexto,
        "pergunta": pergunta
    })

    with chat_area:
        ui.chat_message(str(resposta), name="Agente", sent=False)

    contexto += f"\nUser: {pergunta}\nAgente: {resposta}"

    user_input.value = ""

user_input = ui.input(placeholder="Digite sua pergunte").classes("w-full")

ui.button("Enviar", on_click=enviar_mensagem).classes("mt-2")

ui.run()