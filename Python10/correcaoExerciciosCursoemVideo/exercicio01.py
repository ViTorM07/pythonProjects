#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um
# número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
# número escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.
from random import randint
from time import sleep
pc = randint (0, 5)
print('-=-'*20)
print('Vou pensar em um numero de 0 a 5, tente adivinhar... ')
print('-=-'*20)

jogador = int(input('Vou tentar com esse numero '))
print('----------PROCESSANDO-------------')
sleep(2)
if jogador == pc:
    print('Parabens!!! VOCÊ VENCEU O DESAFIO!!! ')
else:
    print('PC:GANHEI! Eu pensei no numero {} e não no {} '.format(pc, jogador))