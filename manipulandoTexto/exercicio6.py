#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
#Ex:Ana Souza
n = str(input('Digite seu nome completo ')).strip()
nome = n.split()
print(nome[0])
print('Seu primeiro nome é {}'.format(nome[0]))
print('Prazer{}, muuito bom te conhecer!'.format(nome[0]))
print('Seu ultimo nome é {} '.format(nome[len(nome)-1]))
