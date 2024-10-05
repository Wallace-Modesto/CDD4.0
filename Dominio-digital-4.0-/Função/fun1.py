def piramide(n):
    for x in range(1,n+1):
        for y in range(x):
            print(x,end=" ")
        print()
n = 5
piramide(n)
