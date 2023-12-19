# --- Importar a biblioteca --- #
import os


def obter_probioticos(valor_porc: int):
    """
    Função responsável por escrever em um arquivo CSV as bactérias e quais funções probióticas ela possui.
    :param valor_porc: Valor da porcentagem dos dados (50% ou 70%).
    """
    # --- Pasta com os arquivos --- #
    caminho = f'./bacterias_{valor_porc}'

    # --- Dicionário com as funções --- #
    dic_funcoes = {}

    # --- Abrir cada arquivo da função probiótica e obter as bactérias --- #
    for arquivo in os.listdir(caminho):
        if '.txt' in arquivo:
            funcao = arquivo.replace(f'_{valor_porc}.txt', '')
            dic_funcoes[funcao] = []  # criar uma lista vazia para cada função
            with open(f'{caminho}/{arquivo}', 'r') as txt:
                conteudo = txt.readlines()
                for linha in conteudo:
                    bacteria = linha.split('\n')[0]
                    dic_funcoes[funcao].append(bacteria)  # adicionar em cada função as bactérias que possuem essa função

    # --- Dicionário com as bactérias --- #
    dic_bacterias = {}
    for funcao, bacterias in dic_funcoes.items():
        for bacteria in bacterias:
            dic_bacterias[bacteria] = []  # criar uma lista vazia para cada bactéria

    # --- Obter as funções que cada bactéria possui --- #
    for funcao, bacterias in dic_funcoes.items():
        for bacteria in bacterias:
            if bacteria in dic_funcoes[funcao]:
                dic_bacterias[bacteria].append(funcao)  # adicionar a função probiótica da bactéria

    # --- Escrever em um arquivo CSV as bactérias e quais funções elas possuem ou não --- #
    with open(f'{caminho}/probioticos/probioticos.csv', 'a') as csv:
        csv.write('bacteria,eps,adesao,estresse,manosidase,fosfolipase,acido_folico,bacteriocina,'
                  'sais_biliares,betagalactosidase,tolerancia_gastro,metabolismo_carbono,total_funcoes\n')
        for bacteria, funcoes in dic_bacterias.items():
            eps = funcoes.count('eps')
            adesao = funcoes.count('adesao')
            estresse = funcoes.count('estresse')
            manosidase = funcoes.count('manosidase')
            fosfolipase = funcoes.count('fosfolipase')
            acido_folico = funcoes.count('acido_folico')
            bacteriocina = funcoes.count('bacteriocina')
            sais_biliares = funcoes.count('sais_biliares')
            betagalactosidase = funcoes.count('betagalactosidase')
            tolerancia_gastro = funcoes.count('tolerancia_gastro')
            metabolismo_carbono = funcoes.count('metabolismo_carbono')
            total_funcoes = eps + adesao + estresse + manosidase + fosfolipase + acido_folico + bacteriocina + sais_biliares + betagalactosidase + tolerancia_gastro + metabolismo_carbono
            if total_funcoes > 3:
                csv.write(f'{bacteria},{eps},{adesao},{estresse},{manosidase},{fosfolipase},{acido_folico},'
                          f'{bacteriocina},{sais_biliares},{betagalactosidase},{tolerancia_gastro},{metabolismo_carbono},{total_funcoes}\n')


# --- Chamar a função --- #
obter_probioticos(70)
