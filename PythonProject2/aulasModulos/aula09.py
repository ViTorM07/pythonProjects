frase = 'Curso em Video Python'
print(frase)
print(frase[3])
print(frase[:13])
print(frase[9:])
print(frase[1:15])
print(frase[1:21:2])
print(frase[::2])
print('Quantas vezes alguma letra repete na string? ')
print(("Quantas vezes a letra o se repete?"),frase.count('o'))
print(("Quantas vezes a letra O se repete?"),frase.count('O'))
print(("Quantas vezes a letra o se repete?"),frase.upper().count('o'))
# a variavel frase como colocamos aqui é cadeia de caracteres, mas da maneira que colocamos aqui
# ela também n deixa de ser um objeto

print('='*30)
print(len(frase)) #tamanho da frase length
print('Agora frase tem: ')
frase = '   Curso em Video Python   '
print(len(frase))
print(frase.strip())
print(len(frase.strip()))

print('#'*30)
print(frase.replace('Python', 'Android'))#lembrndo que nessa instancia apenas a fraseira mudar a palavra
print(frase[0])
print(frase)#Veja que ela voltou ao normal, quando invocamos outra instancia
# E se eu quiser mudar para sempre?
frase = frase.replace('Python' ,'Android')
print(frase)
# Desta vez modificamos para sempre
print('')
print('Curso' in frase) #retornam com um ternario se é T or F
print('Python' in frase)
print('Android' in frase)
print('='*30)
print(frase.find('Curso'))# Diz quantas vezes aparece essa frase
print(frase.find('Python'))#-1 indica que n ha retornos
print(frase.find('curso'))
print(frase.lower().find('video'))
#Agora vamos dividir a frase
print(frase.split())#ela divide em lista
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[1])
print(dividido[2])
print(dividido[3])
print(dividido[2][3])#mostra na posicao 2 de divido a letra na posicao 3




