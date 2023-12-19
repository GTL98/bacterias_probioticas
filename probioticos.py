# --- Importar as bibliotecas --- #
import csv


def probioticos(porcentagem: int, funcao: str, quantidade: int):
    """
    Função respónsável por retornar as bactérias que possuem as funções probióticas.
    :param porcentagem: Qual dos arquivos será lido (50% ou 70%).
    :param funcao: Função probiótica.
    :param quantidade: Quantidade de funções probióticas na bactéria.
    """
    # --- Caminho do arquico CSV --- #
    caminho = f'bacterias_{porcentagem}/probioticos'

    # --- Abrir o arquivo --- #
    with open(f'{caminho}/probioticos.csv', 'r') as doc:
        # --- Ler o arquivo CSV --- #
        linhas = csv.reader(doc)

        # --- Separar o cabeçalho do arquivo --- #
        cabecalho = next(linhas)

        # --- Criar o arquivo com as bactérias e as funções que elas NÃO tem --- #
        with open(f'{caminho}/arquivo_temp.csv', 'a') as d:
            d.write('bacteria,nao_tem_funcao\n')

            # --- Separar cada coluna do arquivo --- #
            for linha in linhas:
                bacteria = linha[0]
                eps = int(linha[1])
                adesao = int(linha[2])
                estresse = int(linha[3])
                manosidase = int(linha[4])
                fostolipase = int(linha[5])
                acido_folico = int(linha[6])
                bacteriocina = int(linha[7])
                sais_biliares = int(linha[8])
                betagalactosidase = int(linha[9])
                tolerancia_gastro = int(linha[10])
                metabolismo_carbono = int(linha[11])
                total_funcoes = int(linha[12])

                # String para a alimentação dos dados
                nao_tem_funcao = ''

                # Verificar se a quantidade de funções é igual ou maior que a desejada
                if total_funcoes >= quantidade:
                    d.write(f'{bacteria},{total_funcoes}\n')

        with open(f'{caminho}/arquivo_temp.csv', 'r') as d:
            linhas_temp = csv.reader(d)
            next(linhas_temp)
            dic_temp = {linha[0]: [] for linha in linhas_temp}

        with open(f'{caminho}/arquivo_temp.csv', 'r') as d:
            linhas_temp = csv.reader(d)
            next(linhas_temp)
            for linha_temp in linhas_temp:
                bacteria_temp = linha_temp[0]
                total_temp = int(linha_temp[1])
                dic_temp[bacteria_temp].append(total_temp)

    print(dic_temp)
            

probioticos(50, 'total_funcoes', 7)
