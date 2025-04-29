#Fazer um program que lei as duas notas de um aluno e mostre a media
print("Digite o nome do aluno: ")
nome = input('Nome: ')

n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
me = ((n1+n2)/2)
print('A media do aluno: {} é de {}'.format(nome, me))