'''
    Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a CONDIÇÃO DE PARADA. No final, mostre quantos números foram digitados e qual foi a SOMA entre eles (DESCONSIDERANDO O FLAG (condição de saída)).
'''
n = soma = cont = 0
print()
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
        cont += 1
print('\nVocê digitou {} números e a soma deles é {}\n' .format(cont, soma))