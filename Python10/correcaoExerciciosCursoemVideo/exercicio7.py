#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print('Salário do funcionario')
salario = (float(input('Digite o salario do seu funcionario ')))
if(salario>= 1250):
    novo = salario + (salario * 10/100)
if(salario<1000):
    novo = salario + (salario * 15/100)
print('Quem ganhava R${:.2f}, agora está ganhando R${:.2f} '.format(salario, novo))

