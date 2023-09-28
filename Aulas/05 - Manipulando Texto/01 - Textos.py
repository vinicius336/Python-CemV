print('')
frase = 'Curso em Vídeo Python'
print(frase)
print(frase[15])
print(frase[:6])
print(frase[6:14])
print(frase[15:])
print(frase[6:14:3])
print(frase[:15:3])
print(frase[9::1])
print(frase[::2])
print("""
Oi! \o
Este é um texto explicativo!
    Aqui você pode fazer uma cadeia de caracteres extensa para mostrar texto exatamente como está no código.
    Para isso basta escrever o que se quer, seja texto longo, desenhos, menus, ou qualque coisa já no formato que aparecerá na tela.
    Assim toda a forma básica será preservada através das três aspas iniciais e finais
    As aspas podem ser tanto simples quanto duplas.
Valeu! o/
Até a próxima!
""")
print(frase.count('o'))
print(frase.upper().count('O'))
frase = '  ' + frase + '  '
print(len(frase))
print(len(frase.strip()))
frase = frase.strip().replace('Python', 'Android')
print(frase)
print('Android' in frase)
print(frase[0])
frase = frase.replace('Android', 'Python')
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

print('')