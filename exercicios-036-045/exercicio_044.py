# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
from time import sleep
print(f'{"LOJAS GUANABARA":=^40} ')
valor = float(input('Digite o valor da compra:R$ '))
print()
opc = int(input(f'Escolha uma das formas de pagamento abaixo:'
      f'\n [1] - A vista (no dinheiro/cheque)'
      f'\n [2] - A vista (no cartão)'
      f'\n [3] - 2x no cartão'
      f'\n [4] - 3x ou Mais no cartão'
      f'\n\nDigite sua opção de forma de pagamento: '))
print()
print('Processando',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.')
sleep(0.5)
print()
if opc == 1:
    pagamento = 'A vista (no dinheiro/cheque)'
    total = valor - (valor*0.1)
    print(f'Opção escolhida: {opc}'
          f'\nForma de pagamento: {pagamento}'
          f'\nValor da compra:R$ {valor:.2f} reais'
          f'\nDesconto para a forma escolhida: 10% de desconto'
          f'\nValor do desconto:R$ {(valor*0.1):.2f} reais'
          f'\nTotal a pagar com desconto:R$ {total:.2f} reais')
elif opc == 2:
    pagamento = 'A vista (no cartão)'
    total = valor - (valor*0.05)
    print(f'Opção escolhida: {opc}'
          f'\nForma de pagamento: {pagamento}'
          f'\nValor da compra:R$ {valor:.2f} reais'
          f'\nDesconto para a forma escolhida: 5% de desconto'
          f'\nValor do desconto:R$ {(valor*0.05):.2f} reais'
          f'\nTotal a pagar com desconto:R$ {total:.2f} reais')
elif opc == 3:
    pagamento = '2x no cartão'
    parcelas = valor/2
    total = parcelas * 2
    print(f'Opção escolhida: {opc}'
          f'\nForma de pagamento: {pagamento}'
          f'\nValor da compra:R$ {valor:.2f} reais'
          f'\nDesconto para a forma escolhida: Não há descontos'
          f'\nValor das parcelas:R$ {parcelas:.2f} reais'
          f'\nTotal a ser pago:R$ {total:.2f} reais')
else:
    total = valor+(valor*0.2)
    vezes = int(input('Em quantas vezes, deseja dividir no cartão: '))
    pagamento = vezes
    parcelas = total/vezes
    print(f'Opção escolhida: {opc}'
          f'\nForma de pagamento: {pagamento}'
          f'\nValor da compra:R$ {valor:.2f} reais'
          f'\nDesconto para a forma escolhida: Não há descontos'
          f'\nQuantidade de parcelas: {vezes} x'
          f'\nJuros sobre as parcelas: 20%'
          f'\nValor das parcelas com juros:R$ {parcelas:.2f} reais'
          f'\nTotal a ser pago com juros:R$ {total:.2f} reais')


