print()

nome = 'Vinícius Albuquerque Nóbrega'

print('{:=^120}' .format(' Primeira letra maiúscula '))
print('str.Capitalize()\n', nome.capitalize())

print('{:=^120}' .format(' Mais agressivo que o lower() '))
print('str.casefold()\n', nome.casefold())

print('{:=^120}' .format(' Centraliza a string preenchendo com um determinado caractere '))
print("str.center(( tamanho > len(str) ), 'char')\n", nome.center((len(nome)+10), '_'))

print("{:=^120}" .format(" Retorna quantas sequências de caracteres encontrou na string "))
print("{}" .format("str.count('char(s)', início, fim)", nome.count('ue', 0, len(nome))))

print('{:=^120}' .format(' Retorna a string codificada em bytes '))
print("Possíveis parâmetros para 'errors'\n{}" .format("['','strict','ignore','replace','xmlcharrefreplace','backslashreplace']"))
print("str.encode(encoding = 'utf-8', errors = '')")
print(nome.encode())

print('{:=^120}' .format(' Substitui tabulações por espaços (padrão 8 espaços). Faz quebra e retorno de linha '))
tabs = '\t' + nome; print("\\t + str.expandtabs() => Tabulação antes\n"  , tabs.expandtabs())
tabs = '\n' + nome; print("\\n + str.expandtabs() => Quebra de linha"    , tabs.expandtabs())
tabs = '\r' + nome; print("\\r + str.expandtabs() => Retorno de linha\n" , tabs.expandtabs())

print('{:=^120}' .format(' Posição inicial de sequência de caracteres '))
print(nome.find('Albuquerque', 0 ,len(nome)))

print('{:=^120}' .format(' Retorna se existe sequência de caracteres '))
print('u' in  nome)

print('{:=^120}' .format(" Formatação de texto "))
print('Nome: {}' .format(nome))
print('1 + 1 = {}' .format(1+1))
print('10 / 3 = {}'.format(10/3))
print('10 / 3 = {:.2f} {}' .format(10/3, '- Usando {:.2f}'))
print('10 % 3 = {}' .format(10%3))
print('10 // 3 = {}' .format(10//3))

print('{:=^120}' .format(' Semelhante a find(), mas dá erro quando não encontra a substring e sai do programa '))
print(nome.index('Nóbrega', 0, len(nome)))

print('{:=^120}' .format(' As funções "is" retornam True ou False para as suas respectivas funções '))
é = 'isalnum';      n = 'A10'
print(' {:.<30} :: {} : {}' .format('Caracteres AlphaNumérico', é.center(21, '_'), n.isalnum()))
é = 'isascii';      n = '123'
print(' {:.<30} :: {} : {}' .format('Caracteres ASCII', é.center(21, '_'), n.isascii()))
é = 'isdecimal';    n = '12'
print(' {:.<30} :: {} : {}' .format('Caracteres Decimal', é.center(21, '_'), n.isdecimal()))
é = 'isdigit';      n = '1'
print(' {:.<30} :: {} : {}' .format('Caracteres Dígito', é.center(21, '_'), n.isdigit()))
é = 'identifier';   n = 'format'
print(' {:.<30} :: {} : {}' .format('Identificadores', é.center(21, '_'), n.isidentifier()))
é = 'lower';        n = 'vinicius'
print(' {:.<30} :: {} : {}' .format('Minúsculas', é.center(21, '_'), n.islower()))
é = 'numeric';      n = '12'
print(' {:.<30} :: {} : {}' .format('Numérico', é.center(21, '_'), n.isnumeric()))
é = 'printable';    n = '³'
print(' {:.<30} :: {} : {}' .format('Imprimíveis', é.center(21, '_'), n.isprintable()))
é = 'space';        n = ' '
print(' {:.<30} :: {} : {}' .format('Espaços', é.center(21, '_'), n.isspace()))
é = 'title';        n = 'Vi Al'
print(' {:.<30} :: {} : {}' .format('1ª letra/palavra minúscula', é.center(21, '_'), n.istitle()))
é = 'upper';        n = 'VINICIUS'
print(' {:.<30} :: {} : {}' .format('Maiúsculas', é.center(21, '_'), n.isupper()))

print('{:=^120}' .format(' Concatenação de strings '))
concat = nome
concat.join('_')
print(concat)


print()