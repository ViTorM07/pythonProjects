#Exercício Python 23:
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
# separados.

num = int(input('Digite um numero'))
n = str(num)
print('Analisando um numero {} '.format(num))
print('Unidade: {} '.format(n[3]))
print('Dezena: {} '.format(n[2]))
print('Centena {} '.format(n[1]))
print('Milhar {} '.format(n[0]))

#Outro metodo
u = num // 1 % 10
d = num // 10 % 10
c = num //  100%10
m = num //   1000%10

print('=========================================================')

num = int(input('Digite um numero '))
print('Analisando um numero {} '.format(num))
print('Unidade: {} '.format(u))
print('Dezena: {} '.format(d))
print('Centena {} '.format(c))
print('Milhar {} '.format(m))
