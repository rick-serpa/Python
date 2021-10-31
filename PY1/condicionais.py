if ( not ( True ) ):
    print('Falso')
else:
    print('Verdadeiro')

a = 2
if (a == 1):
    print('O valor é 1')
elif (a == 2):
    print ('O valor é 2')
elif (a == 3):
    print ('O valor é 3')
else:
    print ('é outro valor')    


n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))


if ( n1 > n2):
    print(str(n1) + ' é maior que '  + str(n2))
elif ( n1 < n2):
    print(str(n2) + ' é maior que '  + str(n1))
else:
    print(str(n1) + 'é igual' + str(n2))


n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
n3 = int(input('Informe o terceiro valor: '))

if ((n1 >= n2) and (n1 >= n3) and (n2 == n3)):
    print('Os valores são iguais')
else:
    if ((n1 >= n2) and (n1 >= n3)):
        print('Maior valor: ' + str(n1))
    elif ((n2>=n1) and (n2 >= n3)):
        print('Maior valor: ' + str(n2))
    else:
        print('Maior valor: ' + str(n3))
       
