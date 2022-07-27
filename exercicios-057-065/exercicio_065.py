# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n = sair = cont = media = soma = maior = menor = 0
while sair!= 'N' and sair != 'n':
        n = int(input('Digite um valor: '))
        if cont == 0:
            maior = menor = n
        elif cont!= 0:
            if n < maior:
                menor = n
            elif n > maior:
                maior = n
        if n!=0:
            cont+=1
            soma+=n
        sair = str(input('Deseja adicionar algum valor?[S/N]: ')).strip()[0]
        while sair != 'N' and sair != 'n' and sair != 'S' and sair != 's':
            sair = str(input('Valor inválido! Deseja realmente adicionar algum valor? Digite[S/N]: ')).strip()[0]
print(f'\nAo todo foram digitados: {cont} números.'
      f'\nA média entre eles foi: {(soma/cont):.1f}'
      f'\nO maior valor digitado foi: {maior}'
      f'\nO menor valor digitado foi: {menor}')
