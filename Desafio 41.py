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
