'''n1 = int(input('Informe o priemeiro numero: '))
n2 = int(input('Informe o segundo numero: '))

def somaValor(n1,n2):
    return n1 + n2
print(somaValor(n1,n2))



p1 = int(input('Informe o priemeiro numero: '))
p2 = int(input('Informe o segundo numero: '))

print('Opereção desejada')
op = int(input('1- Adição 2- Subtração  3- Multiplicação  4- Divisão  =  '))

if ( op == 1):
    print ('A soma dos valores é ' + str(p1+p2))
elif ( op == 2):
    print ('A subtração dos valores é ' + str(p1-p2))
elif ( op == 3):    
    print ('A multiplicação dos valores é ' + str(p1*p2))
elif ( op == 4):
    if (p2 == 0):
        print('Impossivel dividir por zero')
    else:
        print ('A divisão dos valores é ' + str(p1/p2))
else:
    print("Operação Invalida")'''

'''n = 1
while ( n <= 10 ):
    print(n)
    n+=1'''


'''def validaLogin(pLogin,pSenha):
    if (pLogin.upper() == 'ALUNO' and pSenha == 'proway'):
        return True
    return False

pLogin = input('Login: ')
pSenha = input('Senha: ')

if (validaLogin(pLogin, pSenha) ):
    print('Login efetuado com suacesso')
else:
    print('Login/Senha inválidos')'''

'''nome = input('Informe seu nome: ')
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
sexo = int(input('Informe seu sexo ' + ' 1 - Masculino 2 - Feminino: '))

def imc(pAltura,pPeso,pSexo):
    imc = pPeso / (pAltura * pAltura)
    if (pPeso == 1):
        if (imc < 20):
            return 'Abaixo do peso'   
    elif (imc < 24.9):
        return 'Normal'
    elif (imc < 29.9):
        return 'Obesidade Leve'
    elif (imc < 39.9):    
        return 'Obesidade Moderada'
    else:
        return 'Obesidade Mórbida'
     
    else:
       
    if (imc < 19):
          return 'Abaixo do peso'   
    elif (imc < 23.9):
        return 'Normal'
    elif (imc < 28.9):
        return 'Obesidade Leve'
    elif (imc < 38.9):    
        return 'Obesidade Moderada'
    else:
        return 'Obesidade Mórbida'''

'''valores = [1,2,3]
print(type(valores))
valores = (1,'2',True,10.4)
print(type(valores))
print(valores[0])
print(valores[1])'''

def saudacao(pNome):
   return 'Olá ' + pNome + ', seja bem-vindo'

def mensagem():
    return'função que retorna uma mensagem'