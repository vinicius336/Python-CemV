print()
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('A soma vale {}' .format(n1 + n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o Produto é {}, a Divisão é {:.3f}' .format(s, m, d))
print('A Divisão Inteira é {}, a Exponenciação é {}' .format(di, e))
print()

print('Aqui temos uma linha que termina neste ponto.', end=' ')
print('E aqui continuamos na mesma linha com outro print através do método end=\' \'')
print()

print('Quebrar linha com \'\\n\' \nmesmo escrevendo em apenas uma linha.')

print()