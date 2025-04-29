#Mostre o preço de u produto e calcule o seu preço com o desconto de 5%
prod = float(input('Qual o valor do produto?, R$'))
desc = prod-(prod*(5/100))
print('O produto que custava R${:.2f} agora custa R${:.2f}'.format(prod, desc))
