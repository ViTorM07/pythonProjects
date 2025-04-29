import random
print('Vamos fazer o computador escolher um numero: ')
numero = random.randint(0, 5)
print('Agora você escolhe um numero: ')
n = int(input('Sua vez de digitar: '))
if(n == numero):
    print('PARABÉNS! O valor é igual!')
else:
    print('Não foi dessa vez...')