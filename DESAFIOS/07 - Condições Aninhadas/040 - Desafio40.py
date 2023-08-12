'''
    Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:
    >> Média abaixo de 5.0: REPROVADO
    >> Média entre 5.0 e 6.9: RECUPERAÇÃO
    >> Média 7.0 ou superior: APROVADO
'''
print()
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print()
if(media < 5):
    print('REPROVADO')
elif((media >= 5) and (media < 7)):
    print('RECUPERAÇÃO')
else:
    print('APROVADO')

if 7 > media >= 5:
    print('RECUPERAÇÃO')
elif media < 5:
    print('REPROVADO')
else:
    print('APROVADO')


print()