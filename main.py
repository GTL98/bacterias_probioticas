# --- Importar as bibliotecas --- #
import streamlit as st
from ler_csv import ler_csv
from selecionar_bacterias import selecionar_bacterias


# --- Configuração da página --- #
st.set_page_config(page_title='Bactérias Probióticas', layout='wide')

with st.container():
    # --- Título da página --- #
    st.title('Bactérias probióticas')

with st.container():
    # --- Selecionar a porcentegem da análise --- #
    porcentagem = st.radio(
        'Escolha uma opção',
        (
            '50',
            '70'
        )
    )

    # --- Selecionar a quantidade de funções probioóticas --- #
    quantidade = st.radio(
        'Selecione a quantidade de funções probióticas',
        (
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11'
        ),
        horizontal=True
    )

    # --- Selectbox com as bactérias --- #
    bacterias = selecionar_bacterias(porcentagem, quantidade)
    bacteria = st.selectbox(
        'Bactérias:',
        bacterias,
        index=None,
        placeholder='Escolha uma bactéria'
    )

    # --- Botão para acessar as informações --- #
    acessar = st.button('Acessar')
    if acessar:
        with st.container():
            ler_csv(porcentagem, bacteria)
