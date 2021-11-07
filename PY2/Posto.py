vl_Comum = 5,29
vl_Aditivada = 5,49
Etanol = 4.99

opcao = int (input('Combustivel desejado: '
                   ' 1- Gasolina aditivada'
                   ' 2- Gasolina Comum'
                   ' 3- Etanol'))
                   
if ( (opcao >= 4) or (opcao < 1)):
    print('Opção Inválida')
else:
    litros = float(input('Quantos litros deseja abastecer: '))
    if (opcao == 1):
        print('Total a pagar: %.2f' % (litros * vl_Aditivada))
    elif (opcao == 2):
        print('Total a pagar: %.2f' % (litros * vl_Comum))
    elif (opcao == 3):
        print('Total a pagar: %.2f' % (litros * Etanol))   
