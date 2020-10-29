                            #CASA
casa=int(input('Valor da casa'))
salario=int(input('Valor do seu salario'))
anos=int(input('Em quantos anos deseja pagar'))
temp = 12*anos
valor= casa/temp
n1=salario*30/100
if valor>n1:
    print('emprestimo negado pois seu salario corresponde a {}%'.format(n1))
    print('as prestações seriam de {} por isso,infelizmente, está fora do seu orçamento'.format(valor))
else:
    print('Parabens,as prestações serão de {}'.format(valor))

