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
print('{:=^60}' .format('\033[1;47m Com String \033[m'))
num = str(input('\033[1;40m Digite um número de 0 a 9999: \033[m '))
tamanho = len(num)
#print(num)
print('\033[1;36;40m Unidade: {} \033[m' .format(num[tamanho-1])) 
print('\033[1;36;40m Dezena:  {} \033[m' .format(num[tamanho-2]))
print('\033[1;36;40m Centena: {} \033[m' .format(num[tamanho-3]))
print('\033[1;36;40m Milhar:  {} \033[m' .format(num[tamanho-4]))
print('{:=^60}' .format('\033[1;31;41m Ainda não é possível fazer com String \033[m'))

print('\033[2;32;42m{:=^60}\033[m' .format(''))
print('{:=^60}' .format('\033[1;47m Com Inteiro \033[m'))
num = int(input('\033[1;40m Digite um número de 0 a 9999: \033[m '))
und = num % 10
num = num // 10
dez = num % 10
num = num // 10
cen = num % 10
num = num // 10
mil = num % 10
print('\033[1;34;40m Unidade: {} \033[m\n\033[1;34;40m Dezena:  {} \033[m\n\033[1;34;40m Centena: {} \033[m\n\033[1;34;40m Milhar:  {} \033[m' .format(und, dez, cen, mil))

print()