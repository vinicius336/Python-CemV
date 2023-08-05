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
print('{:=^20}' .format(' Com String '))
num = int(input('Digite um número de 0 a 9999: '))
num = str(num)
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}' .format(, , , ))

print('{:=^40}' .format(''))
print('{:=^20}' .format(' Com Inteiro '))
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