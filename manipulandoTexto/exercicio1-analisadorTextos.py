#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome: ')).strip()
print("ANALISANDO SEU NOME...")
print("Seu nome em maiusculo é {} ".format(nome.upper()))
print("Seu nome em minusculo é {} ".format(nome.lower()))
print("Seu nome tem ao todo {} letras ".format(len(nome) - nome.count(' ')))
nome.find('Seu primeiro nome tem {} letras'. format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))