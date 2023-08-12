'''
    Escreva um programa que leia um número qualquer e peça para o usuário escolher qual será a "base de conversão":
    >> 1 para Binário
    >> 2 para Octal
    >> 3 para Hexadecimal
'''
print()
numero = int(input('Digite um número: '))
print('[1] Binário\n[2] Octal\n[3] Hexadecimal')
base = str(input('Digite a inicial da base para transformar: ')).upper()
print()

if(base == 1):
    print('O número {} em Binário é {}' .format(numero, bin(numero)[2:]))
elif(base == 2):
    print('O número {} em Octal é {} ' .format(numero, oct(numero)[2:]))
elif(base == 3):
    print('O número {} em Hexadecimal é {} ' .format(numero, hex(numero)[2:].upper()))
else:
    print('Opção inválida')

print()