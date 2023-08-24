'''
    Faça um programa que leia um número qualquer e mostre o seu FATORIAL.
    Ex: 5! = 5x4x3x2x1 = 120
    Obs: Fazer com While e com for.
'''
fat = 1
num = int(input('\nDigite um número para calcular o seu fatorial: '))
print('\n{:=^20}' .format(' for '))
for i in range(num, 0, -1):
    fat = fat * i
    print('{} x ' .format(i), end='') if i > 1 else print('{}' .format(i))
print('O fatorial de {} é {}\n' .format(num, fat))

#print('\n{:=^20}\n' .format(' while '))
