n = int(input())
nome = []
sinal = []
for _ in range(n):
    a, b  = map(str, input().split())
    #adiciona os nomes na lista
    nome.append(b)
    sinal.append(a)
    #coloca em ordem alfabetica
nome.sort()
for name in nome: 
    print(name)
    
print("Se comportaram: %d | Nao se comportaram: %d" %(sinal.count('+'), sinal.count('-')))   
    