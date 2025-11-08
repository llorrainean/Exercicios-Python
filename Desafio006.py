from sys import dont_write_bytecode

numero = float(input('Digite um numero:'))

#calcule o dobro, triplo e raiz quadrada

dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2) ** 0.5 # ou math.sqr(numero)

# Exibe os resultados
print(f'O dobro de {numero} é {dobro}')
print(f'O triplo de {numero} é {triplo}')
print(f'A raiz quadrada de {numero} é {raiz_quadrada}')
