print()

'''nome = 'Vinícius Albuquerque Nóbrega'

print('{:=^120}' .format(' Primeira letra maiúscula '))
print(print('str.Capitalize()\n', nome.capitalize()))

print('{:=^120}' .format(' Mais agressivo que o lower() '))
print(print('str.casefold()\n', nome.casefold()))

print('{:=^120}' .format(' Centraliza a string preenchendo com um determinado caractere '))
print(print("str.center(( tamanho > len(str) ), 'char')\n", nome.center((len(nome)+10), '_')))

print("{:=^120}" .format(" Retorna quantas sequências de caracteres encontrou na string "))
print(print("{}" .format("str.count('char(s)', início, fim)", nome.count('ue', 0, len(nome)))))

print('{:=^120}' .format(' Retorna a string codificada em bytes '))
print("Possíveis parâmetros para 'errors'\n{}" .format("['','strict','ignore','replace','xmlcharrefreplace','backslashreplace']"))
print(print("str.encode(encoding = 'utf-8', errors = '')"))
print(nome.encode())

print('{:=^120}' .format(' Substitui tabulações por espaços (padrão 8 espaços). Faz quebra e retorno de linha '))
print(tabs = '\t' + nome; print("\\t + str.expandtabs() => Tabulação antes\n"  , tabs.expandtabs()))
print(tabs = '\n' + nome; print("\\n + str.expandtabs() => Quebra de linha"    , tabs.expandtabs()))
print(tabs = '\r' + nome; print("\\r + str.expandtabs() => Retorno de linha\n" , tabs.expandtabs()))

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
print(concat)'''

str = 'ViNiCiuS aLBuQueRQue NóBReGa'
print(str.capitalize())
print(str.casefold())
print(str.center(50))
print(str.count('A'))
print(str.encode())
print(str.endswith('A'))
print(str.find('i'))
print(str.format())
print(str.format_map('ó'))
print(str.index('e'))
print(str.isalnum())
print(str.isalpha())
print(str.isascii())
print(str.isdecimal())
print(str.isdigit())
print(str.isidentifier())
print(str.islower())
print(str.isnumeric())
print(str.isprintable())
print(str.isspace())
print(str.istitle())
print(str.isupper())
print(str.join('-'))
print(str.ljust(8,'V'))
print(str.lower())
print(str.lstrip())
print(str.maketrans('a' , 'b' , 'c' ))
print(str.partition('R'))
print(str.removeprefix('Vinícius'))
print(str.removesuffix('Nóbrega'))
print(str.replace(' ', '_'))
print(str.rfind('i'))
print(str.rindex('i'))
print(str.rjust(8,'V'))
print(str.rpartition(' '))
print(str.rsplit())
print(str.rstrip())
print(str.swapcase())
print(str.title())
print(str.translate('a'))
print(str.upper())
print(str.zfill(10))

print()