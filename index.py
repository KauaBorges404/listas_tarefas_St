import streamlit as st

st.title("Listas de Tarefas")

if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

nova_tarefa = st.text_input("Digite uma tarefa")

if st.button("Adicionar"):

    if nova_tarefa != "":

        tarefa = {
            "nome": nova_tarefa,
            "concluida": False
        }

        st.session_state.tarefas.append(tarefa)

st.subheader("Minhas tarefas")


for i, tarefa in enumerate(st.session_state.tarefas):

    col1, col2 = st.columns([5, 1])

    with col1:
        concluida = st.checkbox(
            tarefa["nome"],
            value=tarefa["concluida"],
            key=i
        )

    with col2:
        if st.button("x", key=f"delete{i}"):
            st.session_state.tarefas.pop(i)
            st.rerun()
        