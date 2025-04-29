#Calcule o salrio do funcionario  e calcule o seu aumento
#Se >1250, aumeto = 10%
#Para os inferiores ou iguais o aumento é de 15%
print('PROGRAMA EM PYTHON PARA CALCULAR SALÁRIO: ')
print('='*50)
sal = float(input('Digite seu salário: '))
if(sal>=1250.00):
    aumento = sal+(sal*0.10)
    print('SEU SALARIO AUMENTOU! R${:.2f}'.format(aumento))
if(sal<1000):
    aumento = sal + (sal * 0.15)
    print('SEU SALARIO AUMENTOU! R${:.2f}'.format(aumento))