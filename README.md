# DumbleChat

DumbleChat é um chatbot interativo que permite conversar com Alvo Dumbledore, o diretor de Hogwarts, respeitando fielmente o universo canônico de Harry Potter. Ele utiliza Streamlit como interface e a OpenRouter API para gerar respostas contextuais e mágicas.

## Visão Geral

Este projeto cria uma experiência encantadora de conversa com Dumbledore, com respostas curtas, poéticas e tematicamente fiéis ao mundo bruxo. A aplicação tenta manter a continuidade da conversa utilizando um session_id exclusivo gerado para cada usuário, garantindo que Dumbledore lembre de interações anteriores durante a mesma sessão.

## Estrutura do Projeto

```
DumbleChat/
├── main.py          # Interface Streamlit
└── DumbleChat.py    # Comunicação com a OpenRouter API
```

## Requisitos

- Python 3.8+
- Conta e chave de API no OpenRouter
- Dependências:

```bash
pip install streamlit requests
```

## Configuração da API

Crie um arquivo chamado `.streamlit/secrets.toml` com sua chave da OpenRouter:

```toml
OR_API_KEY = "sua_chave_da_openrouter_aqui"
```

## Como usar

Execute o aplicativo localmente com o comando:

```bash
streamlit run main.py
```

O navegador será aberto automaticamente em `http://localhost:8501` (ou o link será exibido no terminal).

Passos:

1. Informe seu nome.
2. Envie uma mensagem para Dumbledore.
3. Ele responderá com sabedoria, mantendo o contexto da conversa.

## Comportamento de Dumbledore

A personalidade e comportamento do personagem são cuidadosamente definidos:

- Identidade: Alvo Percival Wulfrico Brian Dumbledore
- Universo: Estritamente canônico (sem invenções)
- Tom: Sereno, sábio, levemente enigmático
- Restrições:
  - Respostas sempre com exatamente duas frases
  - Vocabulário somente com termos do universo de Harry Potter
  - Nunca menciona o "mundo trouxa" ou a realidade externa
  - Nunca inventa feitiços, criaturas ou locais não existentes nos livros ou filmes
- Tratamento personalizado:
  - "meu caro bruxo {nome}" (masculino)
  - "minha jovem feiticeira {nome}" (feminino)
  - "meu jovem estudante {nome}" (neutro ou desconhecido)

Exemplo de resposta:

> "Ah, meu caro bruxo João, o Patronus é um encantamento de proteção que repele Dementadores através de memórias felizes concentradas. Você sabia que apenas bruxos verdadeiramente habilidosos conseguem conjurar um Patrono corporificado, como o cervo prateado que brilha com luz prateada pura?"

## Explicação dos Arquivos

### main.py

- Define a interface com o usuário usando Streamlit
- Solicita o nome e exibe mensagens anteriores
- Usa `st.session_state` para manter o histórico de conversa
- Chama `chat_dumbledore()` com os dados necessários
- Mostra as mensagens do usuário e do assistente com avatares personalizados

### DumbleChat.py

- Contém a função `chat_dumbledore(content, user, key, session_id=None)`
- Envia a requisição à API da OpenRouter
- Define um `system_prompt` com regras estritas de comportamento para Dumbledore
- Gera um `session_id` para manter o contexto entre interações
- Retorna a resposta do modelo e o `session_id` atualizado

## Exemplo de Uso da Função

```python
from DumbleChat import chat_dumbledore

response, new_session = chat_dumbledore(
    content="O que é um Patrono?",
    user="João",
    key="sua_chave_da_openrouter",
    session_id=None
)

print(response)
```

## Avisos

- Este projeto é não-oficial e não afiliado à J.K. Rowling, Warner Bros. ou à franquia Harry Potter.
- O uso da API da OpenRouter pode ter limites gratuitos ou custos, verifique no site oficial.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou pull request com melhorias, correções ou ideias novas.

## Feito com magia, código e um toque de sabedoria.
