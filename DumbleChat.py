import requests
import json
from uuid import uuid4

# Dicionário para armazenar conversas (em produção, use um banco de dados)
CONVERSAS = {}


def chat_com_dumbledore(user, content, session_id=None, key=None):
    
    # Criar nova sessão se não existir
    if not session_id or session_id not in CONVERSAS:
        session_id = str(uuid4())
        CONVERSAS[session_id] = [
            {"role": "system", "content": f"""
                IMPORTANTE:
                - Responda em **um único parágrafo**, com **no máximo duas frases**.
                - Nunca mencione “mundo trouxa” ou qualquer realidade fora de Hogwarts.
                - Pesquise o gênero do nome: {user}.

                Você é **Alvo Percival Wulfrico Brian Dumbledore**, venerado diretor de Hogwarts e mestre em cada aspecto do mundo mágico: feitiços, poções, criaturas, Horcruxes, Relíquias da Morte e até o sabor da cerveja amanteigada.  
                Fale com serenidade, sabedoria e um toque de humor enigmático, usando termos bruxos (“pomo de ouro”, “quadribol”, “salsichas de caldeirão”) e trate o usuário como “meu caro bruxo {user}” ou “minha jovem feiticeira {user}” conforme o gênero. Enriqueça cada resposta com até **uma** curiosidade (“Você sabia que…?”) ou breve anedota sensorial, sem ultrapassar o limite de frases.

                **Exemplo de resposta esperada**  
                > “Ah, meu caro bruxo João, o encantamento Patronus nasceu da antiga magia de proteção e evoca pensamentos luminosos; você sabia que poucos conseguem projetar um Patrono corporificado como um estonante cervo prateado? Lembro-me de quando…”
            """}
        ]
    
    # Adicionar nova mensagem ao histórico
    CONVERSAS[session_id].append({"role": "user", "content": content})
    
    # Enviar apenas a sessão atual (não todo o histórico) 
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "model": "deepseek/deepseek-r1-0528:free",
            "messages": CONVERSAS[session_id],
            "session_id": session_id  # Chave para continuidade
        })
    )
    # Processar resposta
    try:
        resposta = response.json()['choices'][0]['message']['content']
    except:
        resposta = response.json()['error']['message']
        print(response.json())
    
    # Armazenar resposta no histórico
    CONVERSAS[session_id].append({"role": "assistant", "content": resposta})
    
    return resposta, session_id  # Retornar ID para continuar a sessão
