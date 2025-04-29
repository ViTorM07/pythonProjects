#faça um programa que leia o cateto oposto e o adjacente de um triangulo retangulo.calcule e mostre o comprimento da hipotenusa

import math
co = float(input('Comprimento do cateto oposto '))
ca = float(input('Comprimento do cateto adjacente '))
hi = float(co**2 + ca**2)**(1/2)     #sem import
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))