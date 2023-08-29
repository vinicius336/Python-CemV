'''
    Escreva um programa que leia um número 'n' inteiro qualque e mostre na tela os 'n' primeiros elementos de uma SEQUÊNCIA DE FIBONACCI.
    Ex: 0-1-1-2-3-5-8-...
'''
n = int(input('\nDigite um número: '))

fib = 0
i = 0

print('Os {}ºs primeiros termos da sequência de Fibonacci são:' .format(n))
while i < n:
    print('{}' .format(fib), end=' ')
    if fib == 0:
        fib = 1
        fibAnt = 0
    elif fib == 1:
        fib = fibAnt + fib
        fibAnt = 1
    else:
        fibAnt = fib
        fib = fibAnt + fib
    
        # 0 1 1 2 3 5 8 13 21 34 55 89 144 233    
    i += 1
    
print('\n')