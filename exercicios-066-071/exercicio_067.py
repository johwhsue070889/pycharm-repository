# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado
# for negativo.
titulo = 'TABUADA'
print('='*75)
print(f'{titulo:^75}')
print('='*75)
while True:
    c = 0
    n = int(input('DIGITE O Nº DA TABUADA PRETENDIDA'
                  ' OU UM VALOR NEGATIVO PARA ENCERRAR: '))
    if n < 0:
        break
    print(f'{titulo} DO: {n}')
    print('=' * 75)
    while c < 10:
            c+=1
            print(f'{n}  x {c:2} = {(n*c):3}')
    print('=' * 75)
print('\nPROGRAMA DE TABUADA ENCERRADO PELO USUÁRIO!'
      '\nSINTA-SE A VONTADE DE VOLTAR QUANDO NECESSITAR!')





