# O mesmo professor da ordem anterior quer sortear a ordem das apresentações.Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
print('ENTRE COM O NOME DOS ALUNOS ')
print('='*22)
nome1 =input('Ola: ')
nome2 =input('Ola: ')
nome3 =input('Ola: ')
nome4 =input('Ola: ')

lista = [nome1,nome2, nome3, nome4]
random.shuffle(lista)
print('A sequencia : ')
print('\n',lista)
