notas = ["", "", "", "", ""]

tamanho = len(notas)
soma = 0
nota = 0
cont = 0
for i in range(tamanho):
    notas[i] = float(input('Digite a nota do aluno: '))

for x in range(tamanho):
    soma += notas[x]
media = soma/tamanho

for y in range(tamanho):
    if notas[y]>media:
        cont +=1

print(f'Temos {cont} alunos com a nota maior que a média. ')
