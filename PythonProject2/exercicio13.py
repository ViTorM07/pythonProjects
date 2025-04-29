# faça um programa que leia um numero decimal e mostre apenas a parte dele inteira
#faça um programa que leia o cateto oposto e o adjacente de um triangulo retangulo.calcule e mostre o comprimento da hipotenusa
# faça um programa que leia um angulo qualquer. Calcule e mostre o seno, cosseno e tangente desse angulo
# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA UM QUADRO.Faça um programa que ajude ele, lendo o nome deles e escolhendo o nome do escolhido
# O mesmo professor da ordem anterior quer sortear a ordem das apresentações.Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
# Faça um programa em python que abra e reproduza um audio em mp3
from math import trunc
from math import ceil
from math import floor
from math import fabs
from math import pow
from math import fmod
num = float(input("Digite um numero decimal(coloque . para separar as casa decimais: )"))
print("TRUNCADO(apenas a parte inteira)",trunc(num))
# print("Outro jeito de truncar em python: {}".format(num, int(num)))
print("Arredondamento cima: ",ceil(num))
print("Arredondamento baixo: ",floor(num))
print("Exponenciacao: ", pow(num, 2))
print("ABSOLUTO: ", fabs(num))
print("Remainder of division", fmod(num,2))


