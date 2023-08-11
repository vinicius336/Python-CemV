'''
    Crie um programa  que leia dois números e mostre a soma entre eles
    "Código Corrigido"
'''
print()
n1 = int(input('\033[41mDigite um número:\033[m '))
n2 = int(input('\033[42mDigite outro número:\033[m '))
res = n1 + n2
print('A soma entre\033[41m', n1,'\033[m e\033[42m', n2,'\033[m vale\033[43m', res,'\033[m')
print()
print('A soma entre \033[41m{}\033[m' .format(n1),'e \033[42m{}\033[m' .format(n2),'vale \033[43m{}\033[m' .format(res))
print()
print('A soma entre \033[41m{}\033[m e \033[42m{}\033[m vale \033[43m{}\033[m' .format(n1, n2, res))
print()