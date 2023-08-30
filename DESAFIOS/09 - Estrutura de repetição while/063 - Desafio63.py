'''
    Escreva um programa que leia um número 'n' inteiro qualque e mostre na tela os 'n' primeiros elementos de uma SEQUÊNCIA DE FIBONACCI.
    Ex: 0-1-1-2-3-5-8-...
'''
n = int(input('\nDigite um número: '))

print('Os {}ºs primeiros termos da sequência de Fibonacci são:' .format(n))

fib = 0
i = 1
while i < n:
    print('{}' .format(fib), end=' ')
    if i == 0 or i == 1:
        fib = 1
        fibAnt = 0
    else:
        termo = fib + fibAnt
        fibAnt = fib
        fib = termo
    i += 1
    
print('\n')