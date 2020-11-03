        #DESAFIO 40
n1=float(input('Digite a primeira nota do aluno: '))
n2=float(input('Digite a segunda nota do aluno: '))
soma= n1+n2
media= soma/2
if media<5.0:
    print('{} Reprovado'.format(media))
elif media<6.9:
    print('{} Recuperação '.format(media))
else:
    print('{} Aprovado'.format(media))


        
