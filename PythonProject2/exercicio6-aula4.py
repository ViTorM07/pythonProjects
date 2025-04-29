#Faca u exercicio que leia a altura e largura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessaria para pintar a parede de 20 metros quadrados.
print('*' * 40)
print('Pintando a parede...')
alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
area = alt * larg
print('A área da parede em metros quadrados: {:.2f}m²'.format(area))

print('='*40)
demao = int(input('Digite quantas mãos de tinta vai precisar: '))
rendi = float(input('Digite o rendimento da tinta: '))
qtdTinta = (area*demao)/rendi

print('O quanto de tinta que será necessário para fazer o trabalho é de: {} litros de tinta'.format(qtdTinta))
