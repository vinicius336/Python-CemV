'''
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
    >> Abaixo de 18.5: Abaixo do peso
    >> Entre 18.5 e 25: Peso ideal
    >> Entre 25 e 30: Sobrepeso
    >> Entre 30 e 40: Obesidade
    >> Acima de 40: Obesidade mórbida
'''
print()
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2

if imc < 18.5:
    print('ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA!')

print()