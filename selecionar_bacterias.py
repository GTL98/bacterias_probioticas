# --- Importar a biblioteca --- #
from csv import reader


def selecionar_bacterias(porcentagem: str):
    """
    Função responsável por ler o arquivo CSV e retornar as bactérias.
    :param porcentagem: Porcentagem da análise para ler o arquivo.
    :return: Lista com as bactérias presentes no arquivo CSV.
    """
    # --- Caminho do arquivo --- #
    caminho = f'./bacterias_{porcentagem}/probioticos/probioticos.csv'

    # --- Lista para armazenar as bactérias presentes no documento --- #
    bacterias = []

    # --- Ler o arquivo --- #
    with open(caminho, 'r') as doc:
        conteudo = reader(doc)
        next(conteudo)
        for linha in conteudo:
            bacterias.append(linha[0])

    return bacterias
