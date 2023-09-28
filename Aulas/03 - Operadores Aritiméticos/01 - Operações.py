print()

print('Adição               +   - Soma')
print('Subtração            -   - Subtração')
print('Multiplicação        *   - Produto')
print('Divisão              /   - Divisão')
print('Potênciação         **   - Potência')
print('Divisão inteira     //   - Valor inteiro de uma divisão')
print('Resto da Divisão     %   - Módulo')
print()

print('ORDEM DE PRECEDÊNCIA!')
print('1º. ()')
print('2º. **')
print('3º. * ; / ; // ; %')
print('4º. + ; -')
print()
a = 5; b = 3; c = 2; d = 4
res = a + b * c
print('{} + {} * {} = {}' .format(a, b, c, res))
res = b * a + d ** c
print('{} * {} + {} ** {} = {}' .format(b, a, d, c, res))
res = b * (a + d) ** c
print('{} * ({} + {}) ** {} = {}' .format(b, a, d, c, res))

print()