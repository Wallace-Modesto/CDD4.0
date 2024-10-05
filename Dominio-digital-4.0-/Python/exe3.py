vetorA = ["","","","","","","","","",""]

varM = ["","","","","","","","","",""]
tamanho = len(vetorA)
soma = 0
X = 0
for i in range(tamanho):
    vetorA[i]=int(input('Digite o numero: '))
x=int(input('Digite o valor multiplicador: '))

for y in range(tamanho):
   varM[y] = vetorA[y] *x
print(vetorA)
print(x)
print(varM)



