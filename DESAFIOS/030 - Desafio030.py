'''
    Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
print()
num = int(input('\033[40m Digite um número:\033[m '))
if(num % 2 == 0):
    print('\033[45m O número é \033[m \033[44m PAR! \033[m')
else:
    print('\033[45m O número é \033[m \033[46m IMPAR! \033[m')

print()