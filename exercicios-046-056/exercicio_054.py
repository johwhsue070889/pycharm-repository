# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
cont_maior= cont_menor=0

for c in range(1,8):
     ano = int(input(f'Digite em que ano a {c}º pessoa nasceu: '))
     idade = ano_atual - ano
     if idade > 18:
         cont_maior+=1
     else:
         cont_menor+=1
print(f'\nQuant. de pessoas maiores de 18 anos: {cont_maior}.'
      f'\nQuant. de pessoas menores de 18 anos: {cont_menor}.')