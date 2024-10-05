num = [""]*10
tam = len(num)
cont = 0
for x in range(tam):
   num[x] = int(input('Digite um numero: '))
p = int(input('numero p pesquisa: '))

for y in range(tam):
    if p == num[y]:
        cont+=1
print(cont)



