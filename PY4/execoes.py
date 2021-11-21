#try:
   # comandoas que deseja executar
#except:
   # mensagem da excecão      

x=0
try:
    arq = open('x,text','r')
except NameError:
    print('Erro ao tentar dividir, Variável não declarada')
except ZeroDivisionError:
    print('Erro ao tentar dividir, Nãom existe divisão por zero!')
finally:
    print('continua o sistema')
#except:
    #print('Erro genérico')
#finally:
    #print('Aqui continua normalmente')
#try:
    #print('Tente fazer isso')
#finally:
    #print('aqui tudo continua')