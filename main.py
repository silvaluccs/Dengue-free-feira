'''
Autor: Lucas Oliveira da Silva
Componente Curricular: MI Algoritmos
Concluido em: 02/06/2024
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''


'''
Módulo principal que opera todos os outros do sistema.
'''

# importando as Funções principais de cada Módulo
from leitura_de_dados import obter_dados_formatados
from operacoes_dados import ler_todos_dados, dados_por_data, dados_por_bairro, escrever_dados 
from salvar_dados import salvar_dados


def mais_informacoes():
    '''
    Função auxiliar para mostrar a mensagem do mais informações na tela
    '''
    print('''\n\t 
A dengue é uma doença infecciosa que pode se apresentar de forma benigna ou grave dependendo de alguns fatores como: o sorotipo envolvido na infecção, infecções
anteriores por dengue ou fatores individuais como doenças crônicas.
É transmitida principalmente pelo mosquito Aedes Aegypti, portanto é classificada no meio científico como uma arbovirose (viroses transmitidas por artrópodes).

Seus principais sintomas são:

Febre
Dor de cabeça
Dores no corpo
Náuseas
Manchas Vermelhas na pele
Sangramento (no caso da dengue hemorrágica)

Após o aparecimento dos primeiros sintomas é de suma importância a procura de orientação médica para o devido tratamento.
A melhor forma de prevenção da doença é combater focos de água parada, visto que o ambiente é ideal para a proliferação do mosquito Aedes Aegypti Um exemplo disso é a verificação de caixas d'água em época de maiores casos de dengue.
Devido a essa problemática esse software foi criado.

O objetivo do 'Dengue Free Feira' é monitorar os bairros da cidade de Feira de Santana retornando para o usuário os valores gerais e por bairro de: Habitantes, Casos Suspeitos, Casos Negativos e Casos Confirmados.O programa também permite a atualização desses dados ao possibilitar o usuário a possibilidade de adicionar novas infomações a partir de uma nova data.
Todos esses dados ficam armazenados em um arquivo CSV que é lido e então reescrito pelo software.
Obrigado por usar o 'Dengue Free Feira'!\n
''')


def menu_mais_informacoes():
    '''
    Função auxiliar para criar um menu para o mais informações
    '''
    mais_informacoes()
    print("\n\tMais informações/")
    sair = False
    while not sair:
        print("\n\t[1] Sair")
        opcao = input("\tSelecione: ")
        if opcao == "1":
            sair = True
        else:
            print("\n\tOpção inválida.")


def menu_leitura_dados(dados):
    '''
    função menu para a opção Ler dados
    '''
    sair = False
    while not sair:
        
        print()
        print('\tGerenciar dados/Ler dados')
        print()
        print('\t[1] Todos os dados')
        print('\t[2] Dados por Data')
        print('\t[3] Dados por Bairro')
        print('\t[4] Retornar ao Menu Anterior')
        opcao = input('\tSelecione: ')

        if opcao == "1":
            ler_todos_dados(dados)
            print()
        elif opcao == "2":
            dados_por_data(dados)
            print()
        elif opcao == "3":
            dados_por_bairro(dados)
            print()
        elif opcao == '4':
            sair = True
            print()
        else:
            print("\n\tOpção inválida")


def menu_acessar_dados(dados):
    '''
    Função menu para a opção gerenciar dados
    '''
    sair = False
    while not sair:
        print()
        print('\tGerenciar dados/')
        print()
        print("\t[1] Ler dados\n\t[2] Escrever dados\n\t[3] Retornar ao menu principal")
        opcao = input('\tSelecione a operação: ')

        if opcao == "1":
            menu_leitura_dados(dados)
        elif opcao == '2':
            dados = escrever_dados(dados)
        elif opcao == '3':
            sair = True
        else:
            print('\n\tOpção inválida.')

    return dados


def main():
    '''
    Função menu principal do sistema
    '''
    dados = obter_dados_formatados("dengue.csv")
    sair = False 
    print()
    print('\tDENGUE FREE FEIRA')
    print("\n\tBem vindo(a) ao dengue free feira")
    
    while not sair:
        print()

        print('\tMenu principal:\n')
        print('\t[1] Gerenciar dados')
        print('\t[2] Mais informações')
        print('\t[3] Sair do sistema')

        opcao = input('\tSelecione: ')
        print()

        if opcao == '1':
            dados = menu_acessar_dados(dados)
        elif opcao == '2':
            menu_mais_informacoes()
        elif opcao == '3':
            

            salvar_dados("dengue.csv", dados)
            sair = True
        else:
            print('\tOpção inválida.')


if __name__ == "__main__":
    main()