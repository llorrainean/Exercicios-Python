# Lê o valor que a pessoa tem em reais
reais = float(input('Quanto dinheiro você tem na carteira? R$ '))

# Quantos Dolares você pode comprar
dolares = reais / 3.27

#Mostre o resultado
print(f'Com R${reais:.2f} você pode comprar US${dolares:.2f}.')



