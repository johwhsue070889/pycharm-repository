# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

from time import sleep
print('Verifique abaixo se é possível ou não a formação de um triângulo'
      '\ndigitando o comprimento de 3 respectivos segmentos  :')
sleep(0.5)
print()
primeiro = float(input('Digite aqui o valor do primeiro segmento: '))
sleep(0.2)
segundo = float(input('Digite aqui o valor do segundo segmento: '))
sleep(0.2)
terceiro = float(input('Digite aqui o valor do terceiro segmento: '))
sleep(0.2)

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

valor1 = primeiro + segundo
valor2 = primeiro + terceiro
valor3 = segundo + terceiro

if valor1 > terceiro and valor2 > segundo and valor3 > primeiro:
    if primeiro == segundo and primeiro == terceiro and segundo == terceiro:
        categoria = 'EQUILÁTERO'
        lados = 'todos os lados iguais!'
    elif primeiro != segundo and primeiro != terceiro and segundo != terceiro:
        categoria = 'ESCALENO'
        lados = 'todos os lados diferentes!'
    else:
        categoria = 'ISÓSCELES'
        lados = 'dois lados iguais e um diferente!'
    print(f'Segmentos informados:'
          f'\nSegmento A: {primeiro};'
          f'\nSegmento B: {segundo};'
          f'\nSegmento C: {terceiro};'
          f'\nStatus: Triangulo possível!'
          f'\nTipo de triângulo: {categoria}'
          f'\nDefinição: Aquele que possui {lados}!!')
else:
    print(f'Segmentos informados:'
          f'\nSegmento A: {primeiro};'
          f'\nSegmento B: {segundo};'
          f'\nSegmento C: {terceiro};'
          f'\nStatus:Segmentos NÃO permitem a formação de um triangulo!!!')