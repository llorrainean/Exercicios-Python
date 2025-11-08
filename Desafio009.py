# Lê um numero inteiro

numero = int(input('Digite um numero inteiro para ver a sua tabuada: '))

# Mostre a tabuada de 1 a 10
print(f'\n tabuada do {numero}: ')
print('_' * 20)

for i in range(1, 11):
    print(f'{numero} x {i} - {numero * i}')

    print('_' * 20)
