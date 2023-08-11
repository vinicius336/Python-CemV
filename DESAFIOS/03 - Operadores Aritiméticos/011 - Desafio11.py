'''
    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
'''
print()
largura = float(input('\033[1;37;40mDigite a \033[1;33mlargura \033[1;37;40m da parede:\033[m '))
altura = float(input('\033[1;37;40mDigite a \033[1;33maltura\033[1;37;40m da parede:\033[m '))
area = largura * altura
Litros = 2
print('\033[1;30;47mA parede tem \033[1;34;40m {}m² \033[1;30;47m de área.\033[m' . format(area))
print('\033[1;30;47mPara pintar  \033[1;34;40m {}m² \033[1;30;47m será(ão) necessário(s)\033[1;35;40m {} \033[1;30;47m Litro(s) de tinta.\033[m' .format(area, area / Litros))

print()