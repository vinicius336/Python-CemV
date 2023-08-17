'''
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    >>> A média de idade do grupo.
    >>> O nome do homem mais velhor.
    >>> Quantas mulheres têm menos de 20 anos.
'''
print()
media = 0
homem = ''
velho = 0
mulherMenor = 0

for i in range(0, 4):
    print('Digite os dados da {}ª pessoa.' .format(i + 1))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo - [M]asculino ou [F]eminino: ')).strip().upper()
    print()
    
    media += idade
    if sexo == 'M':
        if idade > velho:
            homem = nome
    if sexo == 'F' and idade < 20:
        mulherMenor += 1

print()
media = media / 4
print('A média de idade do grupo é de {:.2f}.' .format(media))
print('O nome do homem mais velho é {}.' .format(homem))
print('Há {} mulheres menores de 20 anos.' .format(mulherMenor))
print()