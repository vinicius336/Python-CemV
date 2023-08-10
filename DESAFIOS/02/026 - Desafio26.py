'''
    Faça um programa que leia uma frase pelo teclado e moestre:
    >> Quantas vezes aparece a letras "A"
    >> Em que posição ela aparece a primeria vez.
    >> Em que posição ela aparece a última vez.
'''
print()
frase = input('\033[1;37;40m Digite uma frase:\033[m ').strip().lower()
letra = input('\033[3;37;40m Digite uma letra:\033[m ').strip().lower()
print('\033[1;37;40m A letra \033[33m"{}"\033[37m aparece \033[36m{}\033[37;40m veze(s) na frase.\033[m' .format(letra, frase.count(letra)))
print('\033[4;37;40m A primeria letra \033[33m"{}"\033[37m apareceu na posição\033[36m {}.\033[m' .format(letra, frase.find(letra) + 1))
print('\033[7;30;47m A  última  letra \033[0;36;40m"{}"\033[7;30;47m apareceu na posição\033[0;36;40m {}\033[7;30;47m.\033[m' .format(letra, frase.rfind(letra) + 1))

print()