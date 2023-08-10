'''
    Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
'''
print()
cidade = input('\033[1;47m Digite o nome da cidade que você nasceu:\033[m ').strip().upper()
boll = cidade[:5] == 'SANTO'
print('\033[3;42m {} \033[m' .format(boll)) if( boll == True) else print('\033[9;41m {} \033[m ' .format(boll))

print()