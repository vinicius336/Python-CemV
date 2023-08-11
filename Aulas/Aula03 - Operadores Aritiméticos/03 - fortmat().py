print()

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:>20}!' .format(nome), 'Normal')
print('Prazer em te conhecer {:20}!' .format(nome), '20 espaços')
print('Prazer em te conhecer {:>20}!' .format(nome), 'Alinhado à direita')
print('Prazer em te conhecer {:<20}!' .format(nome), 'Alinhado à esquerda')
print('Prazer em te conhecer {:^20}!' .format(nome), 'Centralizado')
print('Prazer em te conhecer {:=^20}!' .format(nome), 'Centralizado entre símbolos de igual')
print('Prazer em te conhecer', end=' >>> ')
print('{}' .format(nome))

print()