            #DESAFIO 38
n1=int(input('Por favor, digite um valor: '))
n2=int(input('Digite outro valor: '))

if n1>n2:
    print('O primeito valor {}, é maior que {}'.format(n1,n2))

elif n2>n1:
    print('O segundo numero {} é maior que {}'.format(n2,n1))

else:
    print('Não há maior valor,pois ambos os numeros são iguais')
