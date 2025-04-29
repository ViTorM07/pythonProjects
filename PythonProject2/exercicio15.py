# faça um programa que leia um angulo qualquer. Calcule e mostre o seno, cosseno e tangente desse angulo
import math
n = float(input('Digite o angulo que deseja: '))
seno = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('O angulo {} tem o seno de: {:.2f}'.format(n, seno))
print('O angulo {} tem o cosseno de: {:.2f}'.format(n, cos))
print('angulo {} tem a tangente de: {:.2f}'.format(n, tan))