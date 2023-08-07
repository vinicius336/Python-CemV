'''
    Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
print()
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if(n1 > n2):
    if(n2 > n3):
        print('{} é maior e {} é o menor' .format(n1, n3)) 
    elif(n3 > n1):
        print('{} é maior e {} é o menor' .format(n3, n2)) 
    else:
        print('{} é maior e {} é o menor' .format(n1, n2))
else:
    if(n2 < n3):
        print('{} é maior e {} é o menor' .format(n3, n1))
    elif(n3 < n1):
        print('{} é maior e {} é o menor' .format(n2, n3))
    else:
        print('{} é maior e {} é o menor' .format(n2, n1))
print()