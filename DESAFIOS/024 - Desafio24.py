'''
    Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
'''
print()
cidade = input('Digite o nome da cidade que você nasceu: ').strip().upper()
print(cidade[:5] == 'SANTO')

print()