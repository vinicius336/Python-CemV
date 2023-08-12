'''
    Escreva um programa que leia um número qualquer e peça para o usuário escolher qual será a "base de conversão":
    >> 1 para Binário
    >> 2 para Octal
    >> 3 para Hexadecimal
'''
print()
numero = int(input('Digite um número: '))
print('(B)inário\n(O)ctal\n(H)exadecimal')
base = str(input('Digite a inicial da base para transformar: ')).upper()
print()

if(base == 'B'):
    print('O número {} em Binário é {}' .format(numero, bin(numero)[2:]))
elif(base == 'O'):
    print('O número {} em Octal é {} ' .format(numero, oct(numero)[2:]))
else:
    print('O número {} em Hexadecimal é {} ' .format(numero, hex(numero)[2:].upper()))

print()