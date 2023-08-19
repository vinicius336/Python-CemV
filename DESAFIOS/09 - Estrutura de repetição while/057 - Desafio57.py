'''
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
print()
sexo = ''
while (sexo != 'M' or sexo != 'F'):
    sexo = str(input('Digite o sexo: ')).upper()
    print(sexo)
    if sexo != 'M' or sexo != 'F':
        print('Valor incorreto! Digite novamente!')
    else:
        print('Valor correto!')

print()