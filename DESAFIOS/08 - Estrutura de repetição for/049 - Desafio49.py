'''
    Refaça o desafio09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for
'''
print()
num = int(input('Digite um número para ver a tabuada de 0 a 10: '))
for i in range(0, 11):
    print('{} x {} = {}' .format(num, i, num * i))

print()