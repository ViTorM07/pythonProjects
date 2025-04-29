# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA UM QUADRO.Faça um programa que ajude ele, lendo o nome deles e escolhendo o nome do escolhido
import random
print('ENTRE COM O NOME DOS ALUNOS ')
print('='*22)
nome1 =input('Ola: ')
nome2 =input('Ola: ')
nome3 =input('Ola: ')
nome4 =input('Ola: ')

lista = [nome1,nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: ',escolhido)
