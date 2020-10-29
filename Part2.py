nome= str(input('qual o seu nome?'))
if nome == 'Gabriela':
    print('Que nome bonito')
    
elif  nome== 'Olivia' or nome == 'paulo' or nome== 'pedro' or nome== 'maria' or nome == 'ana' or nome=='joao':
    print('{} é um nome bem popular no Brasil'.format(nome))
    
elif nome in 'Gabriela Fernanda Veronica Olivia ':
    print('Um belo nome para uma bela mulher sra.{}'.format(nome))
print('tenha um bom dia, {}'.format(nome))
