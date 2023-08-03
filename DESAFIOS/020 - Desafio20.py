'''
    O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
    Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random 
print()
aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))
alunos = aluno1 + aluno2 + aluno3 + aluno4
alunos = aluno1.split() + aluno2.split() + aluno3.split() + aluno4.split()
print('Lista de alunos: ', alunos)
print('As apresentações serão na seguinte ordem: {}' .format(random.sample(alunos, 4)))
print()

listaAlunos = [aluno1, aluno2, aluno3, aluno4]
print('As apresentações serão na seguinte ordem: {}' .format(random.sample(listaAlunos, 4)))
print()

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação será: {}' .format(lista))
print()