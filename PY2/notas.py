no1 =(input('Qual é o seu nome: '))
n1 = int(input('Primeira nota de ' + no1 + ':'))
n2 = int(input('Segunda nota de ' + no1 + ':'))
n3 = int(input('Terceira nota de ' + no1 + ':'))
n4 = int(input('Quarta nota de ' + no1 + ':'))

media = (n1+n2+n3+n4)/4

if (media < 5 ):
    print('Média de ' + no1 + ': ' + str(media) + '. Situação Reprovado!')
if (media < 7 ):
    print('Média de ' + no1 + ': ' + str(media) + '. Situação Aprovado!')
else:
    print('Média de ' + no1 + ': ' + str(media) + '. Situação em Exame')