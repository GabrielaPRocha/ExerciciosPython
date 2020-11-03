                #Alista mento militar
from datetime import date
atual= date.today().year
nasc=int(input('Ano de nascimento: '))
idade = atual - nasc
print('''Voce é
[1]- HOMEM
[2]- MULHER''')
choice=int(input('digite sua opção: '))
if choice ==2:
           print('Não é necessario o alistamento para mulheres')
           print('Quem nasceu em {} tem {} em {}.'.format(nasc,idade,atual))
else:
    if idade ==18:
        print('Voce tem que se alistar IMEDIATAMENTE')
    elif idade<18:
        saldo=18-idade
        print('Voce ainda nao tem 18 anos. Estara apto para se alistar em {} anos'.format(saldo))
        ano=atual+saldo
        print('Seu alistamento será em {} '.format(ano))
    elif idade > 18:
        saldo= idade- 18
        print('Voce ja deveria ter se alistado a {} anos'.format(saldo))
        ano = atual- saldo
        print('Seu alistamento foi em {} '.format(ano))
