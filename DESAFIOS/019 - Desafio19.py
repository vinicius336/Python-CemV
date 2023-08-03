'''
    Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
    Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
import random
print()
aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))
alunos = aluno1 + aluno2 + aluno3 + aluno4
alunos = aluno1.split() + aluno2.split() + aluno3.split() + aluno4.split()
print('Entre os alunos', alunos)
print('O aluno sorteado para apagar o quadro é: {}' .format(random.sample(alunos,1)))
print()
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
print('Entre os alunos', listaAlunos)
print('O aluno sorteado para apagar o quadro é: {}' .format(random.choice(listaAlunos)))

print()