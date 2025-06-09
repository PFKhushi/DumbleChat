import streamlit as st
import DumbleChat as dc

OR_API_KEY = st.secrets["OR_API_KEY"]


st.set_page_config(page_title="DumbleChat", page_icon="🪄")
st.title("Dumblechat")
st.header("Fale com Dumbledore!")

# 1) Pega o nome do usuário
nome = st.text_input("Qual o seu nome?")

# 2) Inicializa session_state.messages e session_id apenas UMA VEZ
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    st.session_state.session_id = None

# 3) Se o usuário digitou o nome e ainda não há saudação, adiciona a primeira mensagem
if nome and not any(msg["role"] == "assistant" for msg in st.session_state.messages):
    saudacao = f"Prazer em conhecr-te, {nome}!"
    st.session_state.messages.append({
        "role": "assistant",
        "content": saudacao,
        "avatar": "🧙‍♂️"
    })

# 4) Exibe TODO o histórico de mensagens, sempre
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=msg.get("avatar")):
        st.markdown(msg["content"])

# 5) Input de chat — ao submeter, só FAZ APPEND, sem resetar nada
if nome:
    prompt = st.chat_input("Fale alguma coisa...")
    if prompt:
        # 5a) Exibe a mensagem do usuário imediatamente
        with st.chat_message("user", avatar="🙃"):
            st.markdown(prompt)
        # 5b) Armazena a mensagem no histórico
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "avatar": "🙃"
        })

        # 5c) Chama o DumbleChat e atualiza session_id
        response, new_sess = dc.chat_com_dumbledore(
            user=nome,
            content=prompt,
            session_id=st.session_state.session_id,
            key=OR_API_KEY
        )
        st.session_state.session_id = new_sess

        # 5d) Exibe a resposta do assistente
        with st.chat_message("assistant", avatar="🧙‍♂️"):
            st.markdown(response)
        # 5e) Armazena a resposta no histórico
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "avatar": "🧙‍♂️"
        })