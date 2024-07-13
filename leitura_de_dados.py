'''
Módulo responsável por realizar a leitura do arquivo, e converter de um csv para um dicionário
'''

import csv
from datetime import datetime


def configurar_data(data, dados):
    '''
    função auxiliar para configurar a data nos dados
    '''
    if data not in dados.keys(): 
        dados[data] = {}
        
 
def salvar_dados_bairro(bairro, data, dados_arquivo, dados):
    '''
    função auxiliar para salvar os dados dos bairros nas datas
    '''
    if bairro not in dados[data]:
        dados[data][bairro] = dados_arquivo


def configurar_dados(leitor):
    '''
    função auxiliar para salvar os dados no dicionário
    '''
    dados = {}
    for linha in leitor:
        bairro = linha.pop(1)
        data = linha.pop(0)
        dados_arquivo = linha
        configurar_data(data, dados)
        salvar_dados_bairro(bairro, data, dados_arquivo, dados)
    return dados


def orderna_dados(dados):
    datas = obter_datas_recentes(dados)
    dados_ordenados = {}
    for data in datas:
        dados_ordenados[data] = dados[data]
    return dados_ordenados


def obter_datas_recentes(dados):
    converte_datas_para_objeto = lambda data: datetime.strptime(data, "%d/%m/%Y")
    converte_objeto_para_data = lambda data_objeto: data_objeto.strftime('%d/%m/%Y')

    datas = list(dados.keys())
    datas_objeto = [converte_datas_para_objeto(data) for data in datas]
    datas_objeto.sort()
    datas = [converte_objeto_para_data(data) for data in datas_objeto]
    return datas

def obter_dados_formatados(caminho_arquivo):
    '''
    função principal que organiza o fluxo das funções auxiliares para obter dados do arquivo
    '''
    arquivo = abrir_arquivo(caminho_arquivo)
    leitor = csv.reader(arquivo)
    next(leitor) #pulando o cabeçalho
    dados = configurar_dados(leitor)
    dados_ordenados = orderna_dados(dados)
    fechar_arquivo(arquivo)
    
    return  dados_ordenados


def abrir_arquivo(nome_arquivo):
    '''
    função auxiliar para abrir o arquivo em formatado de leitura
    '''
    return open(nome_arquivo, "r")


def fechar_arquivo(arquivo):
    '''
    função auxiliar para fechar o arquivo
    '''
    arquivo.close()


if __name__ == '__main__':
    print('Módulo funcionando')
    print('Execute o main para iniciar o sistema.')