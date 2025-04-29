#Faca um programam que leia a temperatura em celsius e retorne convertendo a mesma em
#Fahrenheit

celsius = float(input('Digite a temperatura em graus Celsius: °'))
fahr = ((9*celsius)/5)+32
print('A temperatura em Fahrenheit: {:.1f}°F'.format(fahr))