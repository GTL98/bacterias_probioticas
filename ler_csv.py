# --- Importar as bibliotecas --- #
import streamlit as st
from csv import reader


def ler_csv(porcentagem: int, bacteria_selecionada: str):
    """
    Função responsável por ler os arquivos CSV com os probióticos.
    :param porcentagem: Porcentagem da análise para a leitura do arquivo CSV.
    :param bacteria_selecionada: Bactéria desejada para a análise.
    :return:
    """
    # --- Caminho do arquivo --- #
    caminho = f'./bacterias_{porcentagem}/probioticos/probioticos.csv'
    # --- Ler o arquivo --- #
    with open(caminho, 'r') as doc:
        conteudo = reader(doc)
        next(conteudo)
        for linha in conteudo:
            bacteria = linha[0]
            eps = int(linha[1])
            adesao = int(linha[2])
            estresse = int(linha[3])
            manosidase = int(linha[4])
            fosfolipase = int(linha[5])
            acido_folico = int(linha[6])
            bacteriocina = int(linha[7])
            sais_biliares = int(linha[8])
            betagalactosidase = int(linha[9])
            tolerancia_gastro = int(linha[10])
            metabolismo_carbono = int(linha[11])
            total_funcoes = int(linha[12])
            if bacteria == bacteria_selecionada:
                st.header('Funções')
                if eps == 1:
                    st.write('- EPS')
                if adesao == 1:
                    st.write('- Adesão')
                if estresse == 1:
                    st.write('- Estresse')
                if manosidase == 1:
                    st.write('- Manosidase')
                if fosfolipase == 1:
                    st.write('- Fosfolipase')
                if acido_folico == 1:
                    st.write('- Ácido fólico')
                if bacteriocina == 1:
                    st.write('- Bacteriocina')
                if sais_biliares == 1:
                    st.write('- Sais biliares')
                if betagalactosidase == 1:
                    st.write('- Betagalactosidase')
                if tolerancia_gastro == 1:
                    st.write('- Tolerância gastro')
                if metabolismo_carbono == 1:
                    st.write('- Metabolismo carbono')
                st.subheader(f'Total de funções probióticas: {total_funcoes}')
