# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
titulo = ' CADASTRO DE PRODUTOS '
total = maior_1000 = menor = 0
cont = 1
mais_barato = ' '
print('='*25)
print(f'{titulo}')
while True:
    print('=' * 25)
    print(f'INFORMAÇÕES DO {cont}º PRODUTO ')
    produto = str(input('Digite o produto adquirido: ')).strip().upper()
    valor = float(input('Digite o valor do produto: R$ '))
    if cont == 1 or valor < menor:
        menor = valor
        mais_barato = produto
    total+=valor
    if valor > 1000:
        maior_1000 +=1
    sair = str(input('Deseja cadastrar mais algum produto?[S/N]: ')).strip()[0].upper()
    while sair != 'S' and sair != 'N':
        sair = str(input('Valor inválido! Deseja realmente cadstrar mais algum produto?[S/N]: ')).strip()[0].upper()
    if sair == 'N':
        break
    cont+=1
titulo2 = ' RELATÓRIO FINAL DA COMPRA '
print()
print('='*50)
print(f'{titulo2:-^50}')
print('='*50)
print(f'VALOR TOTAL DA COMPRA:R$ {total:.2f} '
      f'\nQUANT.DE PRODUTOS COM VALOR SUPERIOR A R$ 1000.00: {maior_1000} PRODUTO(S)'
      f'\nPRODUTO MAIS BARATO: {mais_barato} '
      f'\nVALOR DO PRODUTO MAIS BARATO:R$ {menor:.2f} ')
