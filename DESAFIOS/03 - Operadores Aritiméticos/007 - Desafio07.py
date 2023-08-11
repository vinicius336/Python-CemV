'''
    Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
'''
print()

nota1 = float(input('\033[1;32;43mDigite a primeira nota:\033[m '))
nota2 = float(input('\033[1;33;41mDigite a segunda nota:\033[m '))
média = (nota1 + nota2) / 2
print('\033[1;47mA média do aluno é:\033[m \033[1;33;40m {:.1f} \033[m' .format(média))

print('\033[m')