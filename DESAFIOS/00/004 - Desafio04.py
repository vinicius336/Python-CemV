'''
    Escreva um código que leia algo pelo teclado e informe na tela o máximo de informações sobre o que foi digitado
'''
print()

var = input('\033[1;40mDigite algo:\033[m ')

print('\033[35mÉ alfanumérica?          - \033[40;34m ',var.isalnum(),'\033[m')       if(var.isalnum() == True)       else print('\033[35mÉ alfanumérica?           - \033[7;40;34m ', var.isalnum(),'\033[m')
print('\033[35mÉ Alfabética?            - \033[40;34m ',var.isalpha(),' \033[m')      if(var.isalpha() == True)       else print('\033[35mÉ Alfabética?             - \033[7;40;34m ', var.isalpha(),'\033[m')
print('\033[35mÉ da Tabela ASCII?       - \033[40;34m ',var.isascii(),' \033[m')      if(var.isascii() == True)       else print('\033[35mÉ da Tabela ASCII?        - \033[7;40;34m ', var.isascii(),'\033[m')
print('\033[35mÉ número decimal?        - \033[40;34m ',var.isdecimal(),' \033[m')    if(var.isdecimal() == True)     else print('\033[35mÉ número decimal?         - \033[7;40;34m ', var.isdecimal(),'\033[m')
print('\033[35mÉ um dígito numérico?    - \033[40;34m ',var.isdigit(),' \033[m')      if(var.isdigit() == True)       else print('\033[35mÉ um dígito numérico?     - \033[7;40;34m ', var.isdigit(),'\033[m')
print('\033[35mÉ identificador Python?  - \033[40;34m ',var.isidentifier(),' \033[m') if(var.isidentifier() == True)  else print('\033[35mÉ identificador Python?   - \033[7;40;34m ', var.isidentifier(),'\033[m')
print('\033[35mÉ tudo minúscula?        - \033[40;34m ',var.islower(),' \033[m')      if(var.islower() == True)       else print('\033[35mÉ tudo minúscula?         - \033[7;40;34m ', var.islower(),'\033[m')
print('\033[35mÉ tudo número?           - \033[40;34m ',var.isnumeric(),' \033[m')    if(var.isnumeric() == True)     else print('\033[35mÉ tudo número?            - \033[7;40;34m ', var.isnumeric(),'\033[m')
print('\033[35mÉ imprimível?            - \033[40;34m ',var.isprintable(),' \033[m')  if(var.isprintable() == True)   else print('\033[35mÉ imprimível?             - \033[7;40;34m ', var.isprintable(),'\033[m')
print('\033[35mÉ um espaço em branco?   - \033[40;34m ',var.isspace(),' \033[m')      if(var.isspace() == True)       else print('\033[35mÉ um espaço em branco?    - \033[7;40;34m ', var.isspace(),'\033[m')
print('\033[35mÉ título?                - \033[40;34m ',var.istitle(),' \033[m')      if(var.istitle() == True)       else print('\033[35mÉ título?                 - \033[7;40;34m ', var.istitle(),'\033[m')
print('\033[35mÉ tudo maiúscula?        - \033[40;34m ',var.isupper(),' \033[m')      if(var.isupper() == True)       else print('\033[35mÉ maiúscula?              - \033[7;40;34m ', var.isupper(),'\033[m')
print('')