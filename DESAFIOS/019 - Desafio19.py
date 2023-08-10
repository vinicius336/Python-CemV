'''
    Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
    Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
import random
print()
aluno1 = str(input('\033[1;37;41m Nome do primeiro aluno: \033[m ')).split()
aluno2 = str(input('\033[1;37;42m Nome do segundo  aluno: \033[m ')).split()
aluno3 = str(input('\033[1;37;43m Nome do terceiro aluno: \033[m ')).split()
aluno4 = str(input('\033[1;37;44m Nome do  quarto  aluno: \033[m ')).split()
alunos = aluno1 + aluno2 + aluno3 + aluno4

print('\033[1;35;40m Entre os alunos \033[m \033[4;31;40m{}\033[m' .format(alunos))
print('\033[1;35;40m O aluno sorteado para apagar o quadro é:\033[m \033[4;35;40m{}\033[m' .format(random.sample(alunos,1)))

print('\033[1;35;40m Entre os alunos \033[m \033[4;31;40m{}\033[m' .format(alunos))
print('\033[1;35;40m O aluno sorteado para apagar o quadro é:\033[m \033[0;40m \033[4;31;40m{}\033[0;40m \033[m' .format(random.choice(alunos)))

print()