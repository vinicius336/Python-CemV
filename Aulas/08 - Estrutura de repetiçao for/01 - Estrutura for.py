print()
for i in range(0, 6):
    print('Oi ', end=' ')
print()
for i in range(0, 5):
    print(i, end=' ')
print()
for i in range(6, 0, -1):
    print(i, end=' ')
print()
for i in range(0, 7, 1):
    print(i, end=' ')
print()
for i in range(0, 7, 2):
    print(i, end=' ')
print();print()
n = int(input('Digite um número: '))
for i in range(0, n):
    print(i, end=' ')
print()
for i in range(0, n + 1):
    print(i, end=' ')
print()
for i in range(n, 0, -2):
    print(i, end=' ')
print();print()
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for i in range(inicio, fim + 1, passo):
    print(i, end=' ')
print();print()
s = 0
for i in range(0, 3):
    n = int(input('Digite um número: '))
    s += n 
print(s)

print()