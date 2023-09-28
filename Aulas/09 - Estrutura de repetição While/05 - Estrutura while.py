n = s = 0
print()
while True:
    n = int(input('Digite um núemro: '))
    if n == 999:
        break
    s += n
print(f'A soma dos números é {s}\n')