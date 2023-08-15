'''
    Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
print()
soma = 0
cont = 0
for i in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print('A soma dos {} números pares digitados é {}' .format(cont, soma))

print()