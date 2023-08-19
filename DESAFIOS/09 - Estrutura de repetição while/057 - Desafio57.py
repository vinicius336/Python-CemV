'''
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
print()
sexo = str(input('Digite o sexo: ')).upper().strip()[0]
while sexo not in 'MmFf':
    if sexo != 'M' or sexo != 'F':
        print('Valor incorreto! Digite novamente!')
    sexo = str(input('Digite o sexo: ')).upper().strip()[0]

print()