#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
# até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distancia da viagem: '))
print('Você está prestes a começar a viagem de {}km. '.format(format(distancia)))
preco = distancia*0.50 if distancia<=200 else distancia*0.45
#condicional simplificada
print ('O preço da passsagem será de: R${:.2f}'.format(preco))
