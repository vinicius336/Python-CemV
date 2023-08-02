'''
    Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
'''
print()

m = float(input('Digite um valor em Metros: '))
cm = m * 100
mm = m * 1000
print('{} metros são {:0} centímetros, ou {:0} milímetros.\n{}M\n{:0}cm\n{:0}mm' .format(m, cm, mm, m, cm, mm))
print()
km = m * 0.001
hm = m * 0.01
dm = m * 0.1
dam = m * 10

print('{}km\n{}hm\n{}dam\n{}m\n{}dm\n{}cm\n{}mm' .format(km, hm, dam, m, dm, cm, mm))
print()