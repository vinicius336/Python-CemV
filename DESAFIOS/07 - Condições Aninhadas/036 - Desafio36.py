'''
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    O programa vai perguntar o "valor da casa", o "salário com comprador" e em "quantos anos ele vai pagar".
    Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
print()
valorCasa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o valor do salário: R$ '))
anos = int(input('Digite o tempo de financiamento em anos: '))
qtdParcelas = anos * 12
prestacao = valorCasa / (qtdParcelas)

print()
print('O valor da casa é R$ {:.2f}' .format(valorCasa))
print('Seu financiamento será em {} parcelas.' .format(qtdParcelas))
print('O valor das prestações é de R$ {:.2f}' .format(prestacao))
print()

porcentagem = (prestacao * 100) / salario
print('{:.2f}' .format(porcentagem),'%')

print()
if(prestacao <= salario * .3):
    print('{:=^70}' .format('FINANCIAMENTO APROVADO'))
    print('| As parcelas de R$ {:.2f}' .format(prestacao), end=' ')
    print('não excedem 30% do salário de R$ {:.2f} |' .format(salario))
    print('=' * 70)
elif((prestacao > salario * .3) and (prestacao <= salario * .5)):
    print('{:=^64}' .format(' FINANCIAMENTO REPROVADO! '))
    print('| As parcelas de R$ {:.2f}' .format(prestacao), end=' ')
    print('e excedem {:.2f}%' .format(porcentagem - 30), end=' ')
    print('o valor permitido. |')
    print('| Busque outras opções de parcelamento: {:>24}' .format('|'))
    print('{:<1} 1 - Casa com valor menor!{:>37}' .format('|','|'))
    print('{:<1} 2 - Opção de renda maior!{:>37}' .format('|','|'))
    print('{:<1} 3 - Aumente o tempo do financiamento!{:>25}' .format('|','|'))
    print('=' * 64)
else:
    print('{:=^80}' .format(' FINANCIAMENTO REPROVADO! '))
    print('| Não é possível financiar uma casa de R$ {:.2f}' .format(valorCasa), end=' ')
    print('com prestação acima de R$ {:.2f}%' .format(prestacao), end=' ')
    print('de um salário de R$ {:.2f}! |' .format(salario))
    print('=' * 80)
    
print()