#Diga se 3 retas que forem de entrada formarão um triangulo

a = float(input('Digite o valor de uma reta: '))
b = float(input('Digite o valor de uma reta: '))
c = float(input('Digite o valor de uma reta: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print('Sim é possível formar uma reta ')
else:
    print('Não é possível formar uma reta com esses valores ')