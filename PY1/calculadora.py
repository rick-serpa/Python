n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
print (n1+n2)

n1 = 10
print(type(n1))
print("Valor em inteiro: " + str(n1))
n1 = str(n1)
print(type(n1))
print("Valor em string: " + str(n1))

n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

print('Opereção desejada')
op = int(input('1- Adição  2- Subtração  3- Multiplicação  4- Divisão'))

if ( op == 1):
    print ('A soma dos valores é ' + str(n1+n2))
elif ( op == 2):
    print ('A subtração dos valores é ' + str(n1-n2))
elif ( op == 3):    
    print ('A multiplicação dos valores é ' + str(n1*n2))
elif ( op == 4):
    if (n2 == 0):
        print('Impossivel dividir por zero')
    else:
        print ('A divisão dos valores é ' + str(n1/n2))
else:
    print("Operação Invalida")







