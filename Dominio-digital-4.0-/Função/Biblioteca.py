
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









