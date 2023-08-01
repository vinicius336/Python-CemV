'''
    Escreva um código que leia algo pelo teclado e informe na tela o máximo de informações sobre o que foi digitado
'''
print()

var = input('Digite algo: ')
print('A variável digitada é do tipo', type(var))
print('É alfabética ou numérica? ',var.isalnum())
print('É Alfabética?             ',var.isalpha())
print('É da Tabela ASCII?        ',var.isascii())
print('É número decimal?         ',var.isdecimal())
print('É um dígito numérico?     ',var.isdigit())
print('É um identificador Python?',var.isidentifier())
print('É tudo letra minúscula?   ',var.islower())
print('É tudo número?            ',var.isnumeric())
print('É imprimível?             ',var.isprintable())
print('É um espaço em branco?    ',var.isspace())
print('É um título?              ',var.istitle())
print('É tudo maiúscula?         ',var.isupper())
print()