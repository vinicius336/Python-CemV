'''
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    >> O nome com todas as letras maiúsculas;
    >> O nome com todas as letras minúsculas;
    >> Quantas letras ao todo (sem considerar espaços);
    >> Quantas letras tem o primeiro nome.
'''
print()
nomeCompleto = str(input('\033[4;40m Digite seu nome completo:\033[m ')).strip()

print('\033[1;40m {} \033[m' .format(nomeCompleto.upper()))
print('\033[9;47m {} \033[m' .format(nomeCompleto.lower()))
print('\033[1;41m {} \033[m' .format(len(nomeCompleto) - ' '.count(nomeCompleto)))
print('\033[1;42m {} \033[m' .format(nomeCompleto.find(' ')))
nome = nomeCompleto.split()
print('\033[4;43m {} \033[m \033[1;44m {} \033[m' .format(nome[0], len(nome)))
print()

listaNomes = nomeCompleto.split() # [vi al no]
letras = ''.join(listaNomes)
print('\033[1;44m {} \033[m' .format(len(letras)))
print('\033[1;45m {} \033[m' .format(len(listaNomes[0])))

print()