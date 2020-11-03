                    #Converter
n1=int(input('digite o numero para ser convertido:'))
print('''Escolha uma das bases para a conversão:
[1] converter para BINARIO
[2]converter para OCTAL
[3]converter para HEXADECIMAL ''')
choice=int(input('Digite a opção: '))
if choice == 1:
    print('{} convertido para BINARIO é igual a {}'.format(n1,bin(n1)))
elif choice ==2:
   print('{} convertido para OCTAL é igual a {}'.format(n1,oct(n1)))
elif choice ==3:
   print('{} convertido para HEXADECIMAL é igual a {}'.format(n1,hex(n1)))
else:
    print('Opção invalida,por favor, tente novamente')
