
def piramide(n):
    for x in range(1,n+1):
        for y in range(x):
            print(x,end=" ")
        print()

def torre(n):
    for x in range(1,n+1):
        for y in range(x):
            print(x, end=" ")
        print()


def vogais (texto):
    cont=0
    for x in texto:
        if x in "aeiouAEIOU":
            cont+=1
    print(f'O texto digitado tem {cont} vogais')

def inverterNomes(nomes1,nomes2,nomes3,nomes4,nomes5):
    nomes=['']*5
    nomes[0]=nomes1
    nomes[1]=nomes2
    nomes[2]=nomes3
    nomes[3]=nomes4
    nomes[4]=nomes5
    print(nomes)
    nomes.reverse()
    print(nomes)

def somar(*numeros):
    t = len(numeros)
    soma = 0
    for x in range(t):
        soma = soma + numeros[x]
    print(soma)



