d = int(input('Informe quantas casa decimais deseja = '))
f = '%' + str(d) + 'f'
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

print('Opereção desejada')
op = int(input('1- Adição 2- Subtração  3- Multiplicação  4- Divisão  =  '))


if ( op == 1):
    ((n1 +'%.2f'))
    print ('Resultado da Adição ' + f % (n1 + n2))
elif ( op == 2):
    print ('Resultado da Subtração' + f % (n1 - n2))
elif ( op == 3):    
    print ('Resultado da Multiplicação' + f % (n1 * n2))
elif ( op == 4):
    if (n2 == 0):
        print('Impossivel dividir por zero')
    else:
        print ('Resultado da Divisão' + f % (n1 / n2))
else:
    print("Operação Invalida")

