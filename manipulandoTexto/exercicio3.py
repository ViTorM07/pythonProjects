#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga
#
# se ela começa ou não com o nome “SANTO”.
cid = str(input('Digite o nome da cidade em que voce nasceu: ')).strip()
print(cid[:5] == 'Santo')
print(cid[:5].upper() == 'SANTO')
