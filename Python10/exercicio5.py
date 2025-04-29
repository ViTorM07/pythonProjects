#Faca um programa que leia um ano qualquer e mostre se ele é bissexto
print('#'*40)
print('Algoritmo que define ano Bissexto! ')
ano = int(input('Digite o ano que você queira saber se é bissexto: '))
if(ano % 4 == 0 and ano % 100!=0):
    print('O ano é BISSEXTO!')
else:
    print('O ano não é bissexto! ')
