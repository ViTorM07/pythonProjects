#Crie um programa que leia o dinheiro na sua carteira e diga quantos dolares voce pode comprar
#Conforme a cotaçao atual

n = float(input('Digite o quanto voce tem de dinheiro: '))
compraDol= n / 5.73
print(f'Você consegue com R${n:.2f} em dólar: U${compraDol:.2f}')