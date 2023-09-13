'''
    Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a MÉDIA entre todos os valores e qual foi o MAIOR e o MENOR valores digitados. O programa deve perguntar ao usuário se ele quer ou não CONTINUAR a digitar valores.
'''
n = cont = media = maior = menor = 0
continuar = 'S'
while n != 'N':
    int(input('\nDigite um número: '))
    if cont == 0:
        maior = n
        menor = n
        media = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        media += n
    cont += 1
    
    if continuar != 'N':
        print('Deseja continuar a digitar valores?')
        continuar = str(input('[S]im ou [N]ão: ')).upper().strip()
        if continuar == 'S':
            continue
        else:
            while continuar != 'S':
                if continuar != 'N':
                    print('\nOpção inválida. Tente novamente!\nDeseja continuar a digitar valores?')
                    continuar = str(input('[S]im ou [N]ão: ')).upper().strip()
                    if continuar == 'S':
                        continue
                else:
                    media /= cont
                    print('\nO maior valor é {}.\nO menor valor é {}.\nA média dos valores é {}\n' .format(maior, menor, media))
                    exit()