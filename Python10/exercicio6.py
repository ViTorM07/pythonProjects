#QUal é o maior?
#Leia 3 numero e diga qual é o maior
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
if(a>b):
    maior = a
    menor = b
    print('Maior = ', maior)
else:
    maior = b
    menor = a
    print('Menor = ', menor)
c = int(input('Digite um número: '))
if(c > maior):
    maior = c
    print('Agora é Maior = ', maior)
else:
    menor = c
    print('Agora é menor = ', maior)