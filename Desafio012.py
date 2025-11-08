# Lê o preço do produto

preco = float(input('Digite o valor do prodruto (R$): '))

#Calcule o preço com 5% de desconto

novo_preco = preco - (preco * 5 / 100)

# Mostre o nome preço

print(f'O produto que custava R$ {preco:.2f}, passa a custar com desconto de R$ {novo_preco:.2f}')



