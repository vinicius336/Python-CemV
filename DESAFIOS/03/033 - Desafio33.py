'''
    Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
print()
n1 = int(input('\033[1;40m Digite o \033[4m primeiro\033[1m número \033[m: '))
n2 = int(input('\033[1;40m Digite o \033[4m segundo\033[1m  número \033[m: '))
n3 = int(input('\033[1;40m Digite o \033[4m terceiro\033[1m número \033[m: '))
if(n1 > n2):
    if(n2 > n3):
        print('\033[3;42m {} \033[1;47m é o maior, e \033[1;41m {} \033[0;47m é o menor \033[m' .format(n1, n3)) 
    elif(n3 > n1):
        print('\033[3;42m {} \033[1;47m é o maior, e \033[1;41m {} \033[0;47m é o menor \033[m' .format(n3, n2)) 
    else:
        print('\033[3;42m {} \033[1;47m é o maior, e \033[1;41m {} \033[0;47m é o menor \033[m' .format(n1, n2))
else:
    if(n2 < n3):
        print('\033[3;42m {} \033[1;47m é o maior, e \033[1;41m {} \033[0;47m é o menor \033[m' .format(n3, n1))
    elif(n3 < n1):
        print('\033[3;42m {} \033[1;47m é o maior, e \033[1;41m {} \033[0;47m é o menor \033[m' .format(n2, n3))
    else:
        print('\033[3;42m {} \033[1;47m é o maior, e \033[1;41m {} \033[0;47m é o menor \033[m' .format(n2, n1))
print()