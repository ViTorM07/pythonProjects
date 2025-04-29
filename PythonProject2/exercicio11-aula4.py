#************Aluguel de carros**********
#Escreva um programa que pergunte a quantidade de dias que o carro foi alugado e qual a quilometragem
#Calcule o preço a pagar, sabendo que o carro custa $60 por dia e R$0,15 por quilometro rodado

km = float(input('Digite quantos Km foram percorridos: '))
dias = int(input('Digite quantos dias ele ficou com o carro: '))
totkm = km*0.15
totdias = dias *60
pago = totkm+totdias
print('Por ter usado tantos dias: {} dias e rodado:{}, deve-se: {}'.format(dias, km, pago))