'''
    Elabore um programa que alcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
    >> À vista: Dinheiro/Cheque: 10% de desconto
    >> À vista no cartão: 5% de desconto
    >> Em até 2x no cartão: Preço normal
    >> 3x ou mais no cartão: 20% de juros
'''
print()
preco = float(input('Preço do produto\nR$ '))
print('  >> Qual a forma de pagamento?')
print('1 >> À vista: Dinheiro/Cheque: 10% de desconto')
print('2 >> À vista no cartão: 5% de desconto')
print('3 >> Em até 2x no cartão: Preço normal')
print('4 >> 3x ou mais no cartão: 20% de juros')
pgto = int(input('Qual a forma de pagamento: '))
if pgto == 1:
    print('O preço é R$ {:.2f}' .format(preco * .9))
elif pgto == 2:
    print('O preço é R$ {:.2f}' .format(preco * .95))
elif pgto == 3:
    print('O preço é R$ {:.2f}' .format(preco))
elif pgto == 4:
    print('O preço é R$ {:.2f}' .format(preco * 1.2))
else:
    print('Opção inválida')

print()