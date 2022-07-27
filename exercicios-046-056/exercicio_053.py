# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços.
#
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite a frase que deseja verificar: ')).strip().upper()
print(f'Frase: {frase}')
palavras=frase.split()
junto=''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso+= junto[letra]
print(f'Frase na forma inversa: {inverso}')
print()
if junto == inverso:
    print('A Frase é um palíndromo!')
else:
    print('A Frase não é um palíndromo!')

