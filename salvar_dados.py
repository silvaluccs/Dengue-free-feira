'''
Módulo para desempacotar os dados e salvar no arquivo csv.
'''

from datetime import datetime

import csv


CABECALHO = ['Data','Bairros','Habitantes','Casos Suspeitos','Casos Negativos','Casos Confirmados']


def salvar_dados(nome_arquivo, dados):
    '''
    Função principal para salvar os dados no arquivo
    '''
    arquivo = abrir_arquivo(nome_arquivo)
    escritor = csv.writer(arquivo)
    escritor.writerow(CABECALHO)
    datas = organizar_datas_crescentes(dados)
    salvar_dados_data_bairro(escritor, datas, dados)
    fechar_arquivo(arquivo)


def abrir_arquivo(nome_arquivo):
    '''
    função auxiliar para abrir o arquivo em formato de escrita
    '''
    return open(nome_arquivo, 'w')


def fechar_arquivo(arquivo):
    '''
    função auxiliar para fechar o arquivo
    '''
    arquivo.close()


def organizar_datas_crescentes(dados):
    '''
    Organiza as datas em ordem crescente
    '''
    FORMATACAO_DATA = "%d/%m/%Y"
    converte_data_para_objeto = lambda data: datetime.strptime(data, FORMATACAO_DATA) #cria um objeto datetime para a data
    converte_objeto_para_data = lambda data: data.strftime(FORMATACAO_DATA)

    datas = list(dados.keys()) #pegando as datas dos dados
    datas_objetos = [converte_data_para_objeto(data) for data in datas] #percorre as datas e converte para objetos do datetime
    datas_objetos.sort()
    datas = [converte_objeto_para_data(data_objeto) for data_objeto in datas_objetos]  #percorre os objetos do datetime e converte para data
    
    return datas


def salvar_dados_data_bairro(escritor, datas, dados):
    '''
    função auxiliar para salvar os dados dos bairros junto com a data
    '''
    for data in datas:
        bairros_data = dados[data]
        for bairro, dados_bairros in bairros_data.items():
            dados_formatados = [data] + [bairro] + dados_bairros # formatando os dados como no arquivo
            escritor.writerow(dados_formatados)

if __name__ == "__main__":
    print('Módulo funcionando')
    print('Execute o main para iniciar o sistema.')