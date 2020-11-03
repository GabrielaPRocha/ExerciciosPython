               #DESAFIO 41
from datetime import date
atual =date.today().year
nasc=int(input('Digite o ano de nascimento do(a) atleta:'))
idade = atual-nasc
if idade<=9:
    print('{} anos se encaixa na categoria mirim'.format(idade))
elif idade <=14:
     print('{} anos se encaixa na categoria infantil'.format(idade))
elif idade <=19:
     print('{} anos se encaixa na categoria Junior'.format(idade))
elif idade==20:
     print('{} anos se encaixa na categoria senior'.format(idade))
else:
    print('{} anos se encaixa na categoria master'.format(idade))
#------------------------------------------------------------

                #CALCULAR IMC
#n1=float(input('digite sua altura'))
#n2=float(input('digite seu peso'))
#imc =n2/(n1*n1)
#if imc<18.5:
    #print('{} este imc esta abaixo do peso'.format(imc))
#elif imc<25:
      #print('{} este imc esta ideal'.format(imc))
#elif imc== 25 or imc<30:
      #print('{} este imc esta com sobrepeso'.format(imc))
#elif imc==31 or imc<40:
 #     print('{} este imc esta obeso'.format(imc))
#else:
#      print('{} este imc esta em obesidade morbita'.format(imc))
 
#________________________________________________________________
                        #DESAFIO 44
#valor=float(input('digite o preço do produto'))
#condis=str(input('condição de pagamento'))
#if condis== 'dinheiro' or 'cheque':
#    preco = valor*10/100
#    price =valor-preco
#    print('o valor do produto é {} porem com 10% de desconto fica {}'.format(valor,price))
#elif condis == 'a vista no cartão':
#     preco = valor*5/100
#     price =valor-preco
#     print('o valor do produto é {} porem com 10% de desconto fica {}'.format(valor,price))
#elif condis =='até 2x no cartão':
#    print('Preço normal,continua sendo {} '.format(valor))
#else:
#    preco = valor*20/100
#    price =valor+preco
#    print('O valor é {} porem com 20% de juros passa a ser {}'.format(valor,price))
    
                #DESAFIO 45 pedra papel e tesoura
import random



