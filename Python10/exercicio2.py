print('#'*40)
print('VELOCIDADE DO CARRO:')
bon = 0.0
vel = float(input('Digite a velocidade do carro: '))
if(vel>=80.0):
    print('TAXADD TE ACHOU, PLAYBOY!')
    print('Você recebeu uma multa!')
    if(vel>=80.0):
        bon = (vel - 80.0) *7.0
        print('Este sera um extra na sua multa deliciosa! Ui mais grana pra puxa-saco!')
        print('MULTA: R${:.2f}'.format(bon))
