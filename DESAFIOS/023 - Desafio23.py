'''
    Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
    Ex:
    Digite um número: 1834
    Unidade: 4
    Dezena: 3
    Centena: 8
    Milhar: 1
    
    Observação:. Fazer como string e como inteiro
'''
print()
print('{:=^60}' .format(' Com String '))
num = str(input('Digite um número de 0 a 9999: '))
tamanho = len(num)
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}' .format(num[tamanho-1], num[tamanho-2], num[tamanho-3], num[tamanho-4]))
print('{:=^60}' .format(' Ainda não é possível fazer com String '))

print('{:=^60}' .format(''))
print('{:=^60}' .format(' Com Inteiro '))
num = int(input('Digite um número de 0 a 9999: '))
und = num % 10
num = num // 10
dez = num % 10
num = num // 10
cen = num % 10
num = num // 10
mil = num % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}' .format(und, dez, cen, mil))

print()