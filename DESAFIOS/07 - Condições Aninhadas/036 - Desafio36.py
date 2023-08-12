'''
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    O programa vai perguntar o "valor da casa", o "salário com comprador" e em "quantos anos ele vai pagar".
    Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
print()
valorCasa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o valor do salário: R$ '))
anos = int(input('Digite o tempo de EMPESTIMO em anos: '))
qtdParcelas = anos * 12
prestacao = valorCasa / qtdParcelas

print()
print('Casa de R$ {:.2f}' .format(valorCasa), end=' ')
print('em {} parcelas.' .format(qtdParcelas), end=' ')
print('Prestação: R$ {:.2f}' .format(prestacao))
print()

porcentagem = (prestacao * 100) / salario
#print('{:.2f}' .format(porcentagem),'%'); print()

if(prestacao <= salario * .3):
    print('{:=^70}' .format('EMPESTIMO APROVADO'))
    print('Parcelas de R$ {:.2f}' .format(prestacao), end=' ')
    print('menor que 30% do salário de R$ {:.2f} ' .format(salario))
elif((prestacao > salario * .3) and (prestacao <= salario * .5)):
    print('{:=^70}' .format(' EMPESTIMO REPROVADO! '))
    print('Parcelas de R$ {:.2f}' .format(prestacao), end=' ')
    print('maior que 30% do salário de R$ {:.2f} em {:.2f}' .format(salario, porcentagem - 30))
    print('Busque outras opções:')
    print('1 - Casa com valor menor!')
    print('2 - Opção de renda maior!')
    print('3 - Aumente o tempo do financiamento!')
else:
    print('{:=^70}' .format(' EMPESTIMO REPROVADO! '))
    print('Não é possível financiar uma casa de R$ {:.2f}' .format(valorCasa))
    print('A Prestação de R$ {:.2f} é {:.2f}%' .format(prestacao, porcentagem), end=' ')
    print('acima do salário de R$ {:.2f}' .format(salario))
    
print()