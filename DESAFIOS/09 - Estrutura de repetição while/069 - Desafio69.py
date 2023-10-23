'''
    Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    A)  Quantas pessoas tem mais de 18 anos.
    B)  Quantos homens foram cadastrados.
    C)  Quantas mulheres tem menos de 20 anos.
'''
while True:
    idade = int(input('\nEntre com a idade: '))
    sexo = str(input('[M]asculino [F]eminino: ')).lower().strip()
    escolha = str(input('Deseja continuar?\n[S]im [N]ão: ')).lower().strip()
    if escolha == 's':
        
        continue
    else:
        print()
        break