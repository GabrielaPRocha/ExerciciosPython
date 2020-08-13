#x= int (input('digite um numero'))
#y=int(input('digite um segundo numero '))
#z= x+y
#print('a soma entre {0} e {1} vale {2}'.format(x, y ,z))
#---------------------------------------------------------------------
                          # SUCESSOR E ANTECESSSOR  
#x= int (input('digite um numero'))
#y= x+1
#z=x-1
#print('Numero digitado',x,'seu sucessor',y,'seu antecessor',z)
#-------------------------------------------------------------------
                        #DOBRO DO NUMERO
#x= int (input('digite um numero'))
#y= x*2
#print('Numero digitado {} seu dobro {}'.format(x,y))
#-------------------------------------------------------------------
                        #DOBRO TRIPLO RAIZ QUADRADA
#x=int(input('dgite um numero'))
#d= x*2
#t= x*3
#r= x ** (1/2)
#print('o dobro de: {} \n vale{}'.format(x,d))
#print('o triplo de {}\n vale {} \n sua raiz quadrada vale:{}'.format(x,t,r))
#-------------------------------------------------------------------
                        #MEDIA DO ALUNO
#nome=input ('Digite o nome do aluno:')
#x= float (input('digite a primeira nota do estudante:'))
#y=float(input('digite a segunda nota do estudante:'))
#z= x+y
#a= z/2;
#print('{} teve a primeira nota de {} e a segunda de {} totalizando a media em {}'
#     .format(nome,x,y,a))
#------------------------------------------------------------------------
                    #NÃO LEMBRO DAS MEDIDAS ENTÃO FOI SO TESTE
#media=float(input('digite uma distancia em metros'))
#hm = media * 100
#dam = media *10
#dm = media * 10
#cm = media * 10
#mm = media/1000
#print('result km {}\n hm {}\ndam{}\n dm {}\n cm{} \n mm{}'.format(km,hm,dam,dm,cm,mm))
#------------------------------------------------------------------------
#x = int(input('digite um numero para ver sua tabuada:'))
#print('{} x {} = {}'. format (x, 1, x*1 ))
#----------------------------------
                        #CONVERSÃO DE MOEDAS
#real=float(input('digite o quanto voce, para ser convertido'))
#dolar= real/5.33
#euro=real/6.07 
#print('A quantidade que voce tem R${}\n equivale á U${}\n e a {} euros'. format(real,dolar,euro))
#------------------------------------------------------------------------------
                        #PAREDE
#l=float(input('Qual a largura da parede que deseja pintar: '))
#a=float(input('e qual a altura?'))
#area=l*a
#tinta= area/2
#print('Sua parede tem as medidas de {} x {} então sua area é de {} m²'.format(l,a,area))
#print('Para pinta-la será necessario {} de tinta'.format(tinta))
#----------------------------------------------------------------------------
                          #DESCONTOS
#x=float (input('Digite o preço do produto: '))
#y =int(input('Qual a porcentagem de desconto, por favor, insira somente numeros: '))
#p =x*y/100
#final=x-p
#print('O produto tem o valor inteiro de {} com o desconto de {} % tem uma diminuição de R${}\n  passa a custar somente R${}'.format(x,y,p,final))
#----------------------------------------------------------------------------
                #AUMENTO DE SALARIO
#x=float(input('Salario do funcionario: '))
#y=int(input('Porcentagem do aumento: '))
#z=x*y/100
#atual=x+z
#print('O antigo salario era de {} com o aumento de {} passara a ser {}'.format(x,y,atual))
#----------------------------------------------------------------------------
                #JUST TRY
#name=input('qual o produto: ')
#x=float(input('Qual o preço do produto: '))
#y= x*5/100
#z=x-y
#j=x*10/100
#juros=x+j
#print('{} a vista {} a prazo {}'.format(name,z,juros))
#----------------------------------------------------------------------------
                #CONVERSOR DE TEMPERATURA
#x= float(input('Qual a temperatura °C: '))
#conv=9*x/5+32
#print('se esta {}°C logo em °F fica: {}°F'.format(x,conv))
#----------------------------------------------------------------------------
                    #ALUGUEL DE CARROS
#x=float(input('Quanto km foram rodados? '))
#y=int(input('quantos dias voce ficou com o carro'))
#km=x *0.15
#dias= y*60
#result= km+dias
#print('O valor a pagar sera de {}'.format(result))
#----------------------------------------------------------------------------
                    #SORTEANDO NUMERO ALEATORIO#
#import random
#num= random.randint(1,50)
#print('sera sorteado um numero de 1 a 50.Boa sorte\n numero sorteado é: {}'.format(num))
#-------------------------------------------------------------------------
#x= float(input('Por favor insira um valor: '))
#print('O valor digitado foi {} e sua parte inteira corresponde á {}'.format(x,int(x)))
#----------------------------------------------------------------------------
                    #CATETO E HIPOTENUSA
#x=float(input('comprimento do cateto oposto: '))
#y=float(input('comprimento do cateto adjacente: '))
#z= (x**2 + y**2) **(1/2)
#print('A hipotenusa vai medir {}.format(z))
#-------------------------------------------------------------------------------
                    #SENO COSSENO E TANGENTE
#import math
#angulo=float(input('digite o angulo desejado'))
#seno = math.sin(math.radians(angulo))
#print('o seno de {} é: {}'.format(angulo,seno))
#cos = math.cos(math.radians(angulo))
#print('o cosseno: {}'.format(cos))
#tan=math.tan(math.radians(angulo))
#print('Sua tangente: {}'.format(tan))
#-------------------------------------------------------------------------------
                    #SORTEANDO NOMES
#import random
#n1=input('Primeiro Aluno: ')
#n2=input('Segundo Aluno: ')
#n3=input('Terceiro Aluno: ')
#n4=input('Quarto Aluno: ')
#lista=[n1,n2,n3,n4]
#escolhide =random.choice(lista)
#print('O sorteado foi {}'.format(escolhide))
#------------------------------------------------------------------------------
                #SORTEANDO UMA ORDEM NA LISTA(ARRAY)
#from random import shuffle
#n1=input('Primeiro Aluno: ')
#n2=input('Segundo Aluno: ')
#n3=input('Terceiro Aluno: ')
#n4=input('Quarto Aluno: ')
#lista=[n1,n2,n3,n4]
#shuffle(lista)
#print('A ordem será:')
#print(lista)
#------------------------------------------------------------------------------
                                #mp3#
#------------------------------------------------------------------------------
#frase ="Cause as long you are the drive i'm your hitchhikker"
#print(frase.replace('hitchhikker','camarada'))
#------------------------------------------------------------------------------
#te='Testando algo so para ter certeza'
#print(te[5:])
#------------------------------------------------------------------------------
                        #Pessoa tem 'Silva' no nome#
#x=str(input("digite um  nome")).strip()
#print('silva' in x.lower())
#------------------------------------------------------------------------------
                        #analisador de tesxtos
#nome=str(input('Digite seu nome completo: '))
#print('Analisando seu nome..')
#print('Seu nome em minusculas: {}' .format(nome.lower()))
#print('seu nome em maiusculas: {}' .format(nome.upper()))
#print('seu nome tem ao todo {} letras' .format(len(nome)-nome.count(' ')))
#------------------------------------------------------------------------------
                    # mostra a quantidade de digitos separadamete
#x=int(input('digite um numero: '))
#u= x// 1 % 10
#d= x//10 %10
#c=x//100 %10
#m= x//1000 %10
#print('Analisando o nomero {}' .format(x))
#print('Unidade: {}'.format(u))
#print('Dezena: {}'.format(d))
#print('Centena: {}'.format(c))
#print('Milhar: {}'.format(m))
#------------------------------------------------------------------------------
                #Primeira e última ocorrência de uma string
#fr=str(input('Digite algo ')).strip().upper()
#print('letra A aparece {} vezes na frase'.format(fr.count('A')))
#print('A primeira vez que aparece é na posição {}'.format(fr.find('A')+1))
#print('A ultima vez que aparece é na posição {}'.format(fr.rfind('A')+1))
#---------------------------------------------------------------------------
                #Primeiro e último nome de uma pessoa
#nome=str(input('Por favor insira seu nome completo: ')).strip()
#n = nome.split()
#print('prazer em conhecelo(a) {}'.format(n[len(n)-1]))
#print('primeiro nome {} '.format(n[0]))
#------------------------------------------------------------------------------
                #REMEMBER IF AND ELSE
#pessoa=int(input('digite sua idade: '))
#if pessoa<18:
#    anos= 18-pessoa
#    print('Sinto muito,so daqui a {} anos'.format(anos))
#else:
#    print('Seja muito bem vindo(a)')
#---------------------------------------------------------------------------
#n1=int(input('digite a primeira nota: '))
#n2=int(input('digite a segunda nota: '))
#n3=int(input('digite a terceira nota: '))
#media= (n1+n2+n3)/3
#if media>8:
#    print('arrasou mana {}'.format(media))
#else:
#        print('melhore negah {}'.format(media))
#----------------------------------------------------------------------------
                #SORTEIO
import random
from time import sleep
sort=random.randint(0,5)
opiniao=int(input('qual foi o numero pensado: '))
print('PROCESSANDO..')
sleep(2)
if opiniao == sort:
    print('acertou realmente foi {}'.format(sort))
if opiniao>5:
    print('mana é so de 0 a 5')
else:
    print('errou,mas nao desista,o numero sorteado foi {}'.format(sort))
#----------------------------------------------------------------------------
                #MULTA acima de 80km com if and else
#km=int(input('qual a velocidade o carro esta? '))
#mul=(km-80)*7
#if km>80:
#    print("""o veiculo sera multado por excesso de velocidade, a multa sera de
#R$7,00 por km ultrapassado o que se soma {}""".format(mul))  
#else:
#    print('Você esta respeitando o limite')
#----------------------------------------------------------------------------
                    #VIAGEM 
#n1=int(input('digite a distancia da viagem: '))
#if n1>=200:
#    n2=n1* 0.50
#    print('sua viagem de {}km a passagem custara R${} '.format(n1,n2))
#else:
#    n3=n1*0.45
#    print('sua viagem de {}km custara R${} '.format(n1,n3))







