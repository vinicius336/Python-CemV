'''
    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
    Exs:
    APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAMA DATA DA MARATONA
'''
print()
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split(); junto = ''.join(palavras)

''' COM FOR
    inverso = ''
    for i  in range(len(junto) - 1, -1, -1):
        inverso += junto[i]
'''
#   SEM FOR
inverso = junto[::-1]
print(inverso)
if inverso == junto:
    print('-{}- é PALÍNDROMO de -{}-' .format(junto, inverso))
else:
    print('-{}- NÃO é PALÍNDROMO de -{}-' .format(junto, inverso))

print()