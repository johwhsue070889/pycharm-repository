# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from time import sleep
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Verifique sua categoria digitando aqui'
                           '\nseu ano de nascimento: '))
idade = ano_atual - ano_nascimento
if idade < 10:
    categoria = 'MIRIM'
elif idade < 15:
    categoria = 'INFANTIL'
elif idade < 20:
    categoria = 'JÚNIOR'
elif idade < 26:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

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
print(f'Resultado final:'
      f'\nAno atual: {ano_atual}'
      f'\nAno de nascimento: {ano_nascimento}'
      f'\nIdade (tem ou completará): {idade} anos'
      f'\nCompetidor categoria: {categoria}')
