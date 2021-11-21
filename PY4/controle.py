from arquivos import lerArquivo
from arquivos import gravaLogDados
from arquivos import listar, cadastrar, excluir, excluir2, alterar
itens = []
opcao = 0
while ( ( opcao >= 1 ) or ( opcao <= 8 ) ) :
    opcao = int(input('Selecione a opção desejada: \n' + 
                    '1- Listar  2- Cadastrar \n' + 
                    '3- Excluir  4- Alterar \n' +
                    '5- Exportar  6 - Carregar log \n' + 
                    '7- Carregar Dados 8- Sair'
                    '-----------------------------\n' ))  
    if ( opcao == 1 ):
        print(listar(itens))
    elif ( opcao == 2 ):
        item = input('Informe o nome do item para cadastrar: ')
        print(cadastrar(item,itens))
    elif ( opcao == 3 ):
        item = input('Informe o nome do item para excluir: ')        
        print(excluir2(item,itens))
    elif ( opcao == 4 ):
        if ( len(itens) == 0 ):
            print('A lista está vazia')
        else:
            item = input('Informe o nome do item que deseja alterar: ')
            print(alterar(item,itens))
    elif ( opcao == 5 ):
     if ( len(itens) > 0 ):
        #gravaLogDados('Dados Cadastrados\n',2)
        gravaLogDados('Dados Cadastrados\n' + str(itens) + str('\n'),2)
     else:
            print('Lista Vazia.')
    elif (opcao == 6):
        lerArquivo()
    elif (opcao == 7):
        lerArquivo()
    elif (opcao == 8):
        break
    else:
        print('Opção inválida')