'''
    O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
    Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random 
print()
aluno1 = str(input('\033[1;30;47mNome do primeiro aluno:\033[m '))
aluno2 = str(input('\033[1;30;47mNome do segundo  aluno:\033[m '))
aluno3 = str(input('\033[1;30;47mNome do terceiro aluno:\033[m '))
aluno4 = str(input('\033[1;30;47mNome do  quarto  aluno:\033[m '))
alunos = aluno1 + aluno2 + aluno3 + aluno4
alunos = aluno1.split() + aluno2.split() + aluno3.split() + aluno4.split()
print('\033[1;37;40m Lista de alunos: \033[m \033[1;37;40m {} \033[m' .format(alunos))
print('\033[1;36;40m As apresentações serão na seguinte ordem: \033[m \033[1;36;40m {} \033[m' .format(random.sample(alunos, 4)))

listaAlunos = [aluno1, aluno2, aluno3, aluno4]
print('\033[1;34;40m As apresentações serão na seguinte ordem:\033[m \033[1;34;40m {} \033[m' .format(random.sample(listaAlunos, 4)))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('\033[1;35;40m A ordem de apresentação será:\033[m \033[1;35;40m {} \033[m' .format(lista))
print()