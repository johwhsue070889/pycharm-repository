# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços, na sequência. No final, mostre uma
# listagem de preços, organizando os dados em forma tabular.
titulo = ' TABELA DE PREÇOS '
itens = ('Lápis',1.75,
         'Borracha',2.00,
         'Caderno',15.90,
         'Estojo',25.00,
         'Transferidor',4.20,
         'Compasso',10.00,
         'Mochila',120.00,
         'Caneta',22.30,
         'Livro',35.00)
print('='*45)
print(f'{titulo:^45}')
print('='*45)
for pos,c in enumerate(itens):
    if pos%2 == 0:
        print(f'{c:.<35}',end='')
    else:
        print(f'R$ {c:>7.2f}',end=' ')
        print()
print('='*45)

