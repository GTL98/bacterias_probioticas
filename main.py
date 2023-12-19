# --- Importar as bibliotecas --- #
import streamlit as st
from ler_csv import ler_csv
from selecionar_bacterias import selecionar_bacterias


# --- Configuração da página --- #
st.set_page_config(page_title='Bactérias Probióticas')

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

    # --- Selectbox com as bactérias --- #
    bacterias = selecionar_bacterias(porcentagem)
    bacteria = st.selectbox(
        'Bactérias:',
        bacterias,
        index=None,
        placeholder='Escolha uma bactéria'
    )

    # --- Botão para acessar as informações --- #
    acessar = st.button('Acessar')
    if acessar:
        ler_csv(porcentagem, bacteria)
