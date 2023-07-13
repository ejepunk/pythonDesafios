nome = str(input('Qual é o seu? '))
    if nome == 'Gustavo':
        print('Que nome Bonito!')
    elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
        print('Seu nome e bem popular no Brasil.')
    elif nome in 'Ana Claúdia Jéssica Juliana':
        print('Belo nome feminino')
    else:
        print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
