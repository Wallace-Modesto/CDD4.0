num=['']*5

tam=len(num)
media = 0
maior = 6
menor = 0
for x in range(tam):
    num[x] = int(input('Digite um valor: '))
for y in range(tam):
    if num[y]%2 == 0:
        print(num[y], end=' ')
maior = max(num)
menor = min(num)

import  numpy as np

media = np.mean(num)

print('='*5)

print(media)
print(media)
print(maior)
print(menor)

