#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite o primeiro valor'))
b = int(input('Digite o segundo valor'))
c = int(input('Digite o terceiro valor'))
#verificando o menor
menor = a
if(b<a and b<c):
    menor = b
if(c<a and c<b):
    menor = c
#verificando o maior
maior = a
if(b>a and b>c):
    maior = b
if(c>a and c>b):
    maior = c

print('O numero menor é {}'.format(menor))
print('O numero maior é {}'.format(maior))
