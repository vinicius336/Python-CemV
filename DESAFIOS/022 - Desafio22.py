'''
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    >> O nome com todas as letras maiúsculas;
    >> O nome com todas as letras minúsculas;
    >> Quantas letras ao todo (sem considerar espaços);
    >> Quantas letras tem o primeiro nome.
'''
print()
nomeCompleto = str(input('Digite seu nome completo: ')).strip()

print('{}' .format(nomeCompleto.upper()))
print('{}' .format(nomeCompleto.lower()))
print('{}' .format(len(nomeCompleto) - ' '.count(nomeCompleto)))
print('{}' .format(nomeCompleto.find(' ')))
nome = nomeCompleto.split()
print('{} {}' .format(nome[0], len(nome)))
print()

listaNomes = nomeCompleto.split() # [vi al no]
letras = ''.join(listaNomes)
print('{}' .format(len(letras)))
print('{}' .format(len(listaNomes[0])))

print()