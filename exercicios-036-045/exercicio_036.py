# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para
# a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos
# anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o
# empréstimo será negado.
from time import sleep
casa = float(input('Digite o valor da casa que pretende financiar:R$ '))
salario = float(input('Digite o salário do possível comprador:R$ '))
valor_aceitável = salario*0.30
fin_em_anos = int(input('Digite o tempo de financiamento pretendido: '))
fin_em_meses = fin_em_anos*12
sleep(0.5)
print()
print('Verificando',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.')
sleep(0.5)
print()
print()
print(f'Valor da casa:R${casa:.2f} reais'
      f'\nTempo pretendido de financiamento: {fin_em_anos} anos de financiamento '
      f'\nValor mínimo das parcelas por mês:R$ {(casa/fin_em_meses):.2f} reais!'
      f'\nValor possível para o comprador(com base em seu salário):R$ {valor_aceitável:.2f} reais!'
      f'\nStatus de aprovação: ',end='')
if casa/fin_em_meses > valor_aceitável:
      print(f'Emprestimo negado!')
else:
      print(f'Emprestimo aprovado!')

