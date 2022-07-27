# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
media_idade = soma_idade = mais_velho = cont_mulher = cont = nome_velho = 0
for c in range(1,5):
    cont+=1
    print('-'*5,end=' ')
    print(f'{c}º PESSOA',end=' ')
    print('-' * 5)
    n = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    soma_idade+=idade
    s = str(input('Digite o sexo[M/F]: '))
    if c == 1 and s in 'Mm':
        mais_velho = idade
        nome_velho = n
    if s in 'Mm' and idade > mais_velho:
        mais_velho = idade
        nome_velho = n
    if s  in 'Ff' and idade < 20:
        cont_mulher+=1
media_idade = soma_idade/cont
titulo = 'RESULTADO'

print(f'{titulo:^90}')

print(f'\nNome do homem mais velho: {nome_velho}.'
      f'\nIdade do homem mais velho: {mais_velho}.'
      f'\nQuantidade de mulheres com - de 20 anos: {cont_mulher}.'
      f'\nMédia de idade do grupo: {media_idade} anos.')






