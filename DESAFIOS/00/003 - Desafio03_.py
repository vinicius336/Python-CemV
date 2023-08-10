'''
    Escreva um código que leia dois números realize a soma e informe na tela o resultado
'''
print()
numero01 = int(input('\033[30;46mDigite um número:\033[m '))
numero02 = int(input('\033[30;45mDigite outro número:\033[m '))
resultado = numero01 + numero02
print('A soma de\033[46m', numero01,'\033[m e\033[45m', numero02,'\033[m é: \033[43m', resultado,'\033[m')
print()