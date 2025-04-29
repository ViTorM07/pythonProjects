print('PROGRAMA PRA QUEM QUER VIAJAR!')
via = float(input('Digite quantos quilômetros terá a sua viajem: '))
if(via < 200):
    preco = 0.50*via
    print('Voce pagara R${:.2f} por viagens de até 200 km '.format(preco))
else:
    preco = 0.45*via
    print('Você pagará R${:.2f} por viagens de até 150 km '.format(preco))