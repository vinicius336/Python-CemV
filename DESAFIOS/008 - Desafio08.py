'''
    Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
'''
print()

m = float(input('Digite um valor em Metros: '))
cm = m / 0.01
mm = m / 0.001
print('{} metros são {:0} centímetros, ou {:0} milímetros.\n{}M\n{:0}cm\n{:0}mm' .format(m, cm, mm, m, cm, mm))

print()