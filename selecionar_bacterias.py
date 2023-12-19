# --- Importar a biblioteca --- #
from csv import reader


def selecionar_bacterias(porcentagem: str, quantidade: str):
    """
    Função responsável por ler o arquivo CSV e retornar as bactérias.
    :param porcentagem: Porcentagem da análise para ler o arquivo.
    :param quantidade: Quantidade de funções probióticas.
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
            total_funcoes = int(linha[-1])
            if total_funcoes >= int(quantidade):
                bacterias.append(linha[0])

    return bacterias
