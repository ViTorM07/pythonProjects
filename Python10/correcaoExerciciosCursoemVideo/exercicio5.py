#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Digite o ano que quer analisar, iremos dizer se ele é bissexto'))
print('Digite 0 para saber do ano atual')
if(ano ==0):
    ano = date.today().year

if(ano %4 ==0 and  ano%100!=0 and ano%400==0):
    print('O ano {} é BISSEXTO! '.format(ano))
else:
    print('O ano {} não é BISSEXTO! '.format(ano))

