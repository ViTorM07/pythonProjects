class Pilha: #define a classe pilha
    def __init__(pizza): #construtor em python
        pizza.pilha = [] #inicializa com uma lista vazia
        
    #metodo para verificar se pilha esta vazia    
    def pilha_vazia(pizza):
        return len(pizza.pilha) == 0#retorna true se nao tiver elementos
    
    #metodo que retorna o tamanho atual da pilha
    def tamanho(pizza):
        return len(pizza.pilha)#Conta quantos elementos ha na pilha
    
    #metodo verifica o o topo da pilha sem remover
    def exibir(pizza):
        if pizza.pilha_vazia():#verifica se esta vazia
            return none;
        return pizza.pilha[-1]# retorna o ultimo elemento(topo da pilha)
        
    #metodo que remove retorna o valor no topo da pilha(pop)
    def desempilhar(pizza): #verifica se a pilha ficou vazia
        if pizza.pilha_vazia():
            return none; #se estiver, nao ha o que desempilhar
        return pizza.pilha.pop() #remover e retornar o ultima da pilha
    
    #metodo que insere um valor para a pilha  (push)   
    def empilhar(pizza, valor):
        if len(pizza.pilha)<10:
            pizza.pilha.append(valor)
        else:
            print("Pilha cheia!")
    
    
        
    
        
        
        
        
#main metodo principal

#Cria uma nova pilha
p1 = Pilha()

p1.empilhar("Quatroo queijos")
p1.empilhar("Calabresa") 
p1.empilhar("Queijo")
p1.empilhar("Frango")
p1.empilhar(10)


p2 = Pilha()

p2.empilhar("Calabresa")
p2.empilhar("Frutos marinhos")
p2.empilhar("Portuguesa")
p2.empilhar("Peperoni")
p2.empilhar("Atum")
p2.empilhar("Carne seca")
p2.empilhar("Camarão")
p2.empilhar("Palmito")
p2.empilhar(8)
#Enquanto nao estiver vazia
print("Pilha 1")
while not p1.pilha_vazia():
    #Desempilhar e imprime o topo
    print(p1.desempilhar())
    
print("\nPilha 2")
while not p2.pilha_vazia():
    print(p2.desempilhar())
    
       
