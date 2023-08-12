'''
    Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    >> O primeiro número é maior.
    >> O segundo número é maior.
    >> Não existe valor maior, os dois são iguais.
'''
print()
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if(n1 == n2):
    print('Não existe valor maior, os dois são iguais.')
elif(n1 > n2):
    print('O primeiro número é maior.')
else:
    print('O segundo número é maior.')

print()