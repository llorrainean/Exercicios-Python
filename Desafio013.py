# #Lê o salário
salario = float(input('Digite o salário'))

#Calcule o novo salário com 15% de aumento
novo_salario = salario + (salario * 15 / 100)

#Mostre o resultado
print(f'O salário do funcionario era de R${salario:.2f} com aumento de 15% passa a ganhar  R${novo_salario:.2f}')
