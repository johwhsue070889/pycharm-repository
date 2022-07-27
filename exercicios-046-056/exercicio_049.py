# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for.

n = int(input('Digite o número que deseja a tabuada: '))
print(f'Tabuada do {n}:')
for c in range(1,11):
    print(f'{n}  x {c:2} = {n*c}')