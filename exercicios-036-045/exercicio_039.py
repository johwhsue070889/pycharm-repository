# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de
# acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de
# se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo
# que falta ou que passou do prazo.
from time import sleep
from datetime import date
ano = int(input('Digite seu ano de nascimento e\nverifique seu ano de alistamento: '))
ano_atual = date.today().year
idade = ano_atual - ano
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
print(f'Ano de nascimento: {ano}'
      f'\nAno atual: {ano_atual}'
      f'\nIdade atual: {idade} anos'
      f'\nAno que fez, deve fazer ou fará o alistamento: {ano+18}'
      f'\nstatus: ',end='')
if idade < 18:
    print(f'Ainda faltam {(ano+18)-ano_atual} anos para seu alistamento!')
elif idade == 18:
    print(f'Esse é seu ano de alistamento. Caso ainda não tenha se alistado'
          f'\nprocure um posto de alistamento o mais rápido possível!')
else:
    print(f'Caso não tenha se alistado, você está irregular há pelo menos'
          f'\n{ano_atual - (ano_atual - idade+18)} anos.Se esse for o caso procure um posto'
          f' de alistamento e se regulize!')