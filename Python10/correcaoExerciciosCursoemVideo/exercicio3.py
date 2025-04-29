#Exercício Python 30: Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Digite um numero: '))
res = numero %2
if res == 0 :
    print('O numero {} é par '.format(numero))
else:
    print('O numero {} é ímpar '.format(numero))
