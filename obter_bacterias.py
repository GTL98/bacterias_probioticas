# --- Importar as bibliotecas --- #
import os
from Bio import SeqIO

# --- Pasta com os documentos --- #
caminho_50 = './probioticos_50'
caminho_70 = './probioticos_70'

# --- Dicionários com os clusters --- # 
dic_cluster_50 = {
    'eps': [],
    'adesao': [],
    'estresse': [],
    'manosidase': [],
    'fosfolipase': [],
    'acido_folico': [],
    'bacteriocina': [],
    'sais_biliares': [],
    'betagalactosidase': [],
    'tolerancia_gastro': [],
    'metabolismo_carbono': []
    }

dic_cluster_70 = {
    'eps': [],
    'adesao': [],
    'estresse': [],
    'manosidase': [],
    'fosfolipase': [],
    'acido_folico': [],
    'bacteriocina': [],
    'sais_biliares': [],
    'betagalactosidase': [],
    'tolerancia_gastro': [],
    'metabolismo_carbono': []
    }

# --- Clusters com 50% --- #
for arquivo in os.listdir(caminho_50):
    for registro in SeqIO.parse(f'{caminho_50}/{arquivo}', 'fasta'):
        if 'EPS' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_50['eps']:
                dic_cluster_50['eps'].append(cluster)

        if 'acido biliar' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_50['sais_biliares']:
                dic_cluster_50['sais_biliares'].append(cluster)

        if 'adesao' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_50['adesao']:
                dic_cluster_50['adesao'].append(cluster)

        if 'metabolismo carbono' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_50['metabolismo_carbono']:
                dic_cluster_50['metabolismo_carbono'].append(cluster)

        if 'estresse calor' in registro.description or 'resistencia estresse' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_50['estresse']:
                dic_cluster_50['estresse'].append(cluster)

                
        if 'estresse calor' in registro.description or 'resistencia estresse' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_50['estresse']:
                dic_cluster_50['estresse'].append(cluster)

        if 'manosidase' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_50['manosidase']:
                dic_cluster_50['manosidase'].append(cluster)

        if 'fosfolipase' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_50['fosfolipase']:
                dic_cluster_50['fosfolipase'].append(cluster)

        if 'acido folico' in registro.description or 'cido folico' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_50['acido_folico']:
                dic_cluster_50['acido_folico'].append(cluster)

        if 'bacteriocina' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_50['bacteriocina']:
                dic_cluster_50['bacteriocina'].append(cluster)

        if 'tolerancia gastro' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_50['tolerancia_gastro']:
                dic_cluster_50['tolerancia_gastro'].append(cluster)

        if 'beta galactosidase' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_50['betagalactosidase']:
                dic_cluster_50['betagalactosidase'].append(cluster)

# --- Clusters com 70% --- #
for arquivo in os.listdir(caminho_70):
    for registro in SeqIO.parse(f'{caminho_70}/{arquivo}', 'fasta'):
        if 'EPS' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_70['eps']:
                dic_cluster_70['eps'].append(cluster)

        if 'acido biliar' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_70['sais_biliares']:
                dic_cluster_70['sais_biliares'].append(cluster)

        if 'adesao' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_70['adesao']:
                dic_cluster_70['adesao'].append(cluster)

        if 'metabolismo carbono' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_70['metabolismo_carbono']:
                dic_cluster_70['metabolismo_carbono'].append(cluster)

        if 'estresse calor' in registro.description or 'resistencia estresse' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_70['estresse']:
                dic_cluster_70['estresse'].append(cluster)

                
        if 'estresse calor' in registro.description or 'resistencia estresse' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_70['estresse']:
                dic_cluster_70['estresse'].append(cluster)

        if 'manosidase' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_70['manosidase']:
                dic_cluster_70['manosidase'].append(cluster)

        if 'fosfolipase' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_70['fosfolipase']:
                dic_cluster_70['fosfolipase'].append(cluster)

        if 'acido folico' in registro.description or 'cido folico' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_70['acido_folico']:
                dic_cluster_70['acido_folico'].append(cluster)

        if 'bacteriocina' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_70['bacteriocina']:
                dic_cluster_70['bacteriocina'].append(cluster)

        if 'tolerancia gastro' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_70['tolerancia_gastro']:
                dic_cluster_70['tolerancia_gastro'].append(cluster)

        if 'beta galactosidase' in registro.description:
            cluster = registro.description.split('|')[0].split('_')[1]
            if cluster not in dic_cluster_70['betagalactosidase']:
                dic_cluster_70['betagalactosidase'].append(cluster)

# --- Lista com os valores dos dicionários --- #
proteinas = [
    'eps',
    'adesao',
    'estresse',
    'manosidase',
    'fosfolipase',
    'acido_folico',
    'bacteriocina',
    'sais_biliares',
    'betagalactosidase',
    'tolerancia_gastro',
    'metabolismo_carbono'
    ]

# --- Dicionário com as bactérias --- #
dic_bacterias_50 = {
    'eps': [],
    'adesao': [],
    'estresse': [],
    'manosidase': [],
    'fosfolipase': [],
    'acido_folico': [],
    'bacteriocina': [],
    'sais_biliares': [],
    'betagalactosidase': [],
    'tolerancia_gastro': [],
    'metabolismo_carbono': []
    }

dic_bacterias_70 = {
    'eps': [],
    'adesao': [],
    'estresse': [],
    'manosidase': [],
    'fosfolipase': [],
    'acido_folico': [],
    'bacteriocina': [],
    'sais_biliares': [],
    'betagalactosidase': [],
    'tolerancia_gastro': [],
    'metabolismo_carbono': []
    }

# --- Iterar sobre cada item do dicionário de 50% --- #
for proteina in proteinas:
    for i in dic_cluster_50[proteina]:
        for registro in SeqIO.parse(f'{caminho_50}/Cluster_{i}.fasta', 'fasta'):
            bacteria = registro.description.split('[')[1][:-1]
            if bacteria not in dic_bacterias_50[proteina]:
                dic_bacterias_50[proteina].append(bacteria)


# --- Iterar sobre cada item do dicionário de 70% --- #
for proteina in proteinas:
    for i in dic_cluster_70[proteina]:
        for registro in SeqIO.parse(f'{caminho_70}/Cluster_{i}.fasta', 'fasta'):
            bacteria = registro.description.split('[')[1][:-1]
            if bacteria not in dic_bacterias_70[proteina]:
                dic_bacterias_70[proteina].append(bacteria)

# --- Escrever em um arquivo as bactérias que possuem as proteínas --- #
for proteina in proteinas:
    with open(f'./bacterias_50/{proteina}_50.txt', 'a') as txt_50:
        for bacteria in dic_bacterias_50[proteina]:
            txt_50.write(bacteria)
            txt_50.write('\n')
    with open(f'./bacterias_70/{proteina}_70.txt', 'a') as txt_70:
        for bacteria in dic_bacterias_70[proteina]:
            txt_70.write(bacteria)
            txt_70.write('\n')
