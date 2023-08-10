'''
    Escreva um programa que converta uma temperatura digitada em graus Celcius (°C) para (°F) Fahrenheint
'''
print()
C = float(input('\033[1;37;40mDigite quantos graus Celsius:\033[m '))
F = C * 1.8 + 32
print('\033[1;40mA temperatura de\033[1;31;40m {:.2f}°C \033[m\033[1;40m corresponde a \033[1;36;40m {:.2f}°F \033[m' .format(C, F))

print()