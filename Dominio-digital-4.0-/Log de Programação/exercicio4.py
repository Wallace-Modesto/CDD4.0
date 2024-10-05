
soma = 0

alunos = int(input("Digite a quantidades de alunos existentes: "))

for aluno in range (alunos):
    notas = float(input("Digite as notas: "))
    soma += notas
media = soma /alunos
print(f"As médias dos alunos foram: {media}")