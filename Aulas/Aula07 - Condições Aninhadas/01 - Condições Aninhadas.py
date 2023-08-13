print()
nome = str(input('Digite seu nome: ')).strip().lower()

if (nome == 'vinicius'):
    print('Que nome original!')
elif(nome == 'daniel'):
    print('Seu nome é comum!')
elif(nome in 'sarah lourdes fatima maria'):
    print('Seu nome é bonito!')
else:
    print('Seu nome é normal!')
print('Bom dia {}!' .format(nome.title()))

print()