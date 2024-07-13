
'''
Módulo responsável por fazer todas as operações dos dados do sistema.
'''
from datetime import datetime


def ler_todos_dados(dados):
    '''
    Função principal para ler todos os dados do arquivo
    '''
    print()
    print('\tGerenciar dados/Ler dados/Todos os dados')
    print()
    
    
    printar_titulo()
    for data in dados:
        dados_data = obter_dados_data(data, dados)
        leitura_dados(dados_data)

    mostra_a_soma_total(dados)
    porcentagem_geral(dados)


def obter_dados_data(data, dados):
    '''
    Função auxiliar para buscar dados nas datas
    '''
    dados_data = dados.get(data, None) #verifica se existe dados para essa data
    if dados_data != None:
        return (data, dados_data)
    
    return dados_data


def printar_titulo():
    '''
    Função auxiliar para printar o cabeçalho dos dados
    '''
    print(f"\n\t{'Bairro:':<20}  {'Data:':^15}  {'Habitantes:':^20}  {'Casos Suspeitos:':^22}  {'Casos Negativos:':^22}  {'Casos Confirmados:':^22}")
    

def leitura_dados(dados_data):
    '''
    Função auxiliar para printar os dados do sistema
    '''

    data, bairros = dados_data # desempacotando os dados
    
    for bairro, dados_bairro in bairros.items():
        print(f'\t{bairro:<20}  {data:^15}  {dados_bairro[0]:^20}  {dados_bairro[1]:^22}  {dados_bairro[2]:^22}  {dados_bairro[3]:^22}')


def dados_por_data(dados):
    '''
    Função principal para Ler dados por data
    '''
    print()
    print('\tGerenciar dados/Ler dados/Dados por Data')
    print()

    print('\tFormato para digitar: dd/mm/yyyy')
    data = input('\tData que deseja buscar: ')

    dados_data = obter_dados_data(data, dados)
    if dados_data: #executa somente se existir dados
        printar_titulo()
        leitura_dados(dados_data)
        dados_data = {dados_data[0] : dados_data[1]} #transformando os dados em dicionário
        mostra_a_soma_total(dados_data)
        porcentagem_geral(dados)
        

    else:
        print('\n\tERRO: DATA NÃO ENCONTRADA')


def dados_por_bairro(dados):
   '''
   Função principal para ler dados por um bairro específico
   '''
   print('\n\tGerenciar dados/Ler dados/Dados por Bairro')
   print()
   bairro = input('\tBairro: ')
   print()
   
   fila_dados = obter_dados_por_bairro(bairro, dados) # procura os dados para esse bairro
   
   if fila_dados: # Caso existam dados, a variavél será verdadeira
       
       printar_titulo()
       for dados_bairro in fila_dados:
           leitura_dados(dados_bairro)

       mostra_a_soma_total(dict(fila_dados))
       porcentagem_bairro(bairro, dados)
       comparar_percentual_datas(bairro, fila_dados)

   else:
       print('\n\tERRO: NÃO EXISTEM DADOS PARA ESSE BAIRRO')


def comparar_percentual_datas(bairro, dados_bairro):
    '''
    Função auxiliar para comparar o percentual de duas datas de um mesmo bairro
    '''
    datas = [dados[0] for dados in dados_bairro]
    opcao = input("\n\tDeseja comparar datas desse bairro?\n\t[1] Sim\n\t[2] Não\n\tSelecione: ")
    if opcao != '1':
        return

    print("\n\tFormato para digitar a data: dd/mm/yyyy")

    data1 = input("\tDigite a primeira data: ")
    data2 = input("\tDigite a segunda data: ")

  
    if (data1 in datas) and (data2 in datas):
        for data, dados_data in dados_bairro:

            if data == data1: # pega os dados para essa respectiva data
                dados_data1 = dados_data.get(bairro) 
            elif data == data2:
                dados_data2 = dados_data.get(bairro)

    else:
        print('\n\tData não encontrada')
        return
    
    # Utiliza uma compreensão de lista para fazer a operação de percentual de dados
    diferenca_percentual = [(int(dados_data2[i]) - int(dados_data1[i])) / (int(dados_data1[i])) for i in range(4)]
    nome_dados = ['Habitantes','Casos Suspeitos','Casos Negativos','Casos Confirmados']

    # Cria um dicionário para formatar os valores, round está aproximando os valores
    diferenca_percentual_datas = {nome_dados[i] : round(diferenca_percentual[i], 2) for i in range(4)}
    print()

    for dados, valor in diferenca_percentual_datas.items(): # acessando os valores do dicionário
        if valor < 0:
            situacao = f"\tHouve uma diminuação de {valor*100*(-1)}% em {dados}"
        elif valor > 0:
            situacao = f"\tHouve um aumento de {(valor)*100}% em {dados}"
        else:
            situacao = f'\tNão houve alteração em {dados} entre essas datas'

        print(f'{situacao}')


def obter_dados_por_bairro(bairro, dados):
    '''
    Função auxiliar para buscar dados de um bairro nas datas
    '''
    fila_dados = []
    for data in dados:

        dados_bairro = dados[data].get(bairro, None) # verifica nas datas, se existe dados para o bairro procurado

        if dados_bairro: # salva somente se existir dados
            dados_bairro = {bairro:dados_bairro}
            fila_dados.append((data, dados_bairro)) # empacota data e dados

    return fila_dados


def porcentagem_geral(dados):
    '''
    Função auxiliar para mostrat a porcentagem geral dos dados
    '''
    ultimos_dados = obter_ultimos_dados_bairros(dados) #obtém os ultimos dados dos bairros
    soma_ultimos_dados = soma_casos(ultimos_dados) # soma todos os dados dos bairros
    
    casos_suspeitos= soma_ultimos_dados['casos suspeitos']
    casos_confirmados = soma_ultimos_dados['casos confirmados']
    casos_negativos = soma_ultimos_dados['casos negativos']

    total_notificados =  casos_suspeitos + casos_negativos + casos_confirmados 

    porcen_casos_suspeitos = (casos_suspeitos/total_notificados)*100
    porcen_casos_confirmados = (casos_confirmados/total_notificados)*100
    porcen_casos_negativos = (casos_negativos/total_notificados)*100

    print(f'\n\tDados atualizados de acordo com o total notificado:')
    print(f'\tCasos Suspeitos: {porcen_casos_suspeitos:.2f}%')
    print(f'\tCasos Confirmados: {porcen_casos_confirmados:.2f}%')
    print(f'\tCasos Negativos: {porcen_casos_negativos:.2f}%')


def porcentagem_bairro(bairro, dados):
    '''
    função auxiliar para mostrar a porcentagem dos dados do bairro em relação ao total
    '''
    ultimos_dados = obter_ultimos_dados_bairros(dados) # pega os ultimos dados de todos os bairros
    dados_bairro = ultimos_dados.get(bairro)
    soma_casos_feira = soma_casos(ultimos_dados)

    casos_suspeitos_bairro = int(dados_bairro[1])
    casos_confirmados_bairro = int(dados_bairro[3])
    
    #calculando a porcentagem e aproximando os valores para duas casas decimais
    porcen_casos_suspeitos = round((casos_suspeitos_bairro/soma_casos_feira['casos suspeitos'])*100, 2) 
    porcen_casos_confirmados = round((casos_confirmados_bairro/soma_casos_feira['casos confirmados'])*100, 2) 

    #Formatando os valores para o usuário
    porcen_casos_suspeitos_formatados = str(porcen_casos_suspeitos).replace(".", ",")
    porcen_casos_confirmados_formatados = str(porcen_casos_confirmados).replace(".", ",")

    print(f'\n\tO bairro {bairro} representa {porcen_casos_suspeitos_formatados}% dos Casos Suspeitos totais. ', end='')
    print(f'Além disso, ele representa {porcen_casos_confirmados_formatados}% dos Casos Confirmados totais.')


def obter_ultimos_dados_bairros(dados):
    '''v
    função auxiliar para obter os ultimos dados de cada bairro
    '''
    ultimos_dados = {}
    for bairros in dados.values():
        for bairro, dados_bairro in bairros.items():
            ultimos_dados[bairro] = dados_bairro
        
    return ultimos_dados


def soma_casos(ultimos_dados):
    '''
    função auxiliar para somar ultimos dados de todos os bairros
    '''
    soma_casos = {'habitantes':0, 'casos suspeitos':0, 'casos confirmados':0, 'casos negativos':0}
    for dados_bairro in ultimos_dados.values(): # realiza a soma de todos os bairros

        soma_casos['habitantes'] += int(dados_bairro[0])
        soma_casos['casos suspeitos'] += int(dados_bairro[1])
        soma_casos['casos negativos'] += int(dados_bairro[2])
        soma_casos['casos confirmados'] += int(dados_bairro[3])

    return soma_casos


def mostra_a_soma_total(dados):
    '''
    função auxiliar para mostrar a soma total dos dados
    '''
    ultimos_dados = obter_ultimos_dados_bairros(dados)
    soma_dados = soma_casos(ultimos_dados)

    print(f'\n\tTotal de dados:')
    print(f"\tHabitantes: {soma_dados['habitantes']}  ", end='')
    print(f"Casos Suspeitos: {soma_dados['casos suspeitos']}  ", end='')
    print(f"Casos Negativos: {soma_dados['casos negativos']}  ", end='')
    print(f"Casos Confirmados: {soma_dados['casos confirmados']}", end='')
    print()

def escrever_dados(dados):
    '''
    Função principal para escrever dados no arquivo
    '''
    print("\n\tGerenciar dados/Escrever dados")
    print()
    print('\tDigite os dados dessa forma:')
    print('\n\tBairro|Data|Habitantes|Casos Suspeitos|Casos Negativos|Casos Confirmados')
    dados_novos = input('\n\tDigite aqui: ')
    dados_novos = dados_novos.split("|")
    dados = inserir_dados(dados_novos, dados) 
    return dados


def inserir_dados(dados_novo, dados_atual):
    '''
    Função auxiliar para descompactar os dados do usuário e enviar para os dados do sistema
    '''
    bairro = dados_novo.pop(0)
    data = dados_novo.pop(0)
    

    if not verificar_data(data, dados_atual): #verfica se a data é maior que a ultima registrada
        print('\tOperação cancelada.')
        return dados_atual


    if not data in dados_atual: #verifica já existem dados para essa data

        dados_atual[data] = {bairro : dados_novo}
        print("\n\tDados adicionados")
        
    else:

        if not bairro in dados_atual[data]: # verifica se o bairro já existe para essa data
            dados_atual[data][bairro] = dados_novo
            print("\n\tDados adicionados")
        else:
            print(f"\n\tDados para o bairro {bairro} na data {data} já existem.")

    return dados_atual


def verificar_data(data, dados):

    FORMATACAO_DATA = "%d/%m/%Y"
    converte_data_para_objeto = lambda data: datetime.strptime(data, FORMATACAO_DATA) #cria um objeto datetime para a data
    converte_datas_para_objetos = lambda datas: [ converte_data_para_objeto(data) for data in datas]# cria uma lista de datetime para as datas

    datas = converte_datas_para_objetos(list(dados.keys()))
    ultima_data = max(datas)
    data_atual = converte_data_para_objeto(data)
    
    if data_atual >= ultima_data:
        return True
    else:
        print(f'\n\tA data inserida ({data}) é menor que a ultima registrada ({ultima_data.strftime(FORMATACAO_DATA)}).')
        return False


if __name__ == '__main__':
    print('Módulo funcionando')
    print('Execute o main para iniciar o sistema.')