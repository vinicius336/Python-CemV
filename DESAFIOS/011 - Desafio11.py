'''
    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessa´ria para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
'''
print()
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
ap = l * a
L = 2
print('A parede tem {}m² de área.' . format(ap))
print('Para pintar {}m² será(ão) necessário(s) {} Litro(s) de tinta.' .format(ap, ap / L))

print()