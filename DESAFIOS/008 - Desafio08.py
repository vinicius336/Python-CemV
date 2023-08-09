'''
    Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
'''
print()

m = float(input('\033[1;30;47mDigite um valor em metros:\033[m '))
km = m * 0.001
hm = m * 0.01
dam = m * 0.1

dm = m * 10
cm = m * 100
mm = m * 1000
print('\033[1;31;40m{}\033[m \033[4mmetros\033[m são \033[1;40m{:.0}\033[m \033[1;31mQuilômetros ' .format(m, km))
print('\033[1;32;40m{}\033[m \033[4mmetros\033[m são \033[1;40m{:.0}\033[m \033[1;32mHectômetros ' .format(m, hm))
print('\033[1;33;40m{}\033[m \033[4mmetros\033[m são \033[1;40m{:.0}\033[m \033[1;33mDecâmetros ' .format(m, dam))
print('\033[1;34;40m Você digitou \033[m \033[1;34;40m{}\033[m \033[1;34mMetros' .format(m))
print('\033[1;35;40m{}\033[m \033[4mmetros\033[m são \033[1;40m{:0}\033[m \033[1;35mDecímetros ' .format(m, dm))
print('\033[1;36;40m{}\033[m \033[4mmetros\033[m são \033[1;40m{:0}\033[m \033[1;36mCentímetros ' .format(m, cm))
print('\033[1;30;40m{}\033[m \033[4mmetros\033[m são \033[1;40m{:0}\033[m \033[1;37mMilímetros ' .format(m, mm))

print()