            #DESAFIO 38
n1=int(input('Por favor, digite um valor: '))
n2=int(input('Digite outro valor: '))

if n1>n2:
    print('O primeito valor {}, é maior que {}'.format(n1,n2))

elif n2>n1:
    print('O segundo numero {} é maior que {}'.format(n2,n1))

else:
    print('Não há maior valor,pois ambos os numeros são iguais')

                #DESAFIO 39
#import datetime
#date=int(input('Digite seu ano de nascimento'))


            #DESAFIO 40
#n1=float(input('Digite a primeira nota do aluno'))
#n2=float(input('Digite a segunda nota do aluno'))
#soma= n1+n2
#media= soma/2
#if media<5.0:
#    print('{} Reprovado'.format(media))
#elif media<6.9:
#    print('{} Recuperação '.format(media))
#else:
#    print('{} Aprovado'.format(media))


                #DESAFIO 41
#import datetime 
#idade=int(input('Digite o ano de nascimento do(a) atleta'))
#if idade<=9:
#    print('{} se encaixa na categoria mirim'.format(idade))
#elif idade <=14:
#     print('{} se encaixa na categoria infantil'.format(idade))
#elif idade <=19:
#     print('{} se encaixa na categoria Junior'.format(idade))
#elif idade==20:
#     print('{} se encaixa na categoria senior'.format(idade))
#else:
 #    print('{} se encaixa na categoria master'.format(idade))
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

