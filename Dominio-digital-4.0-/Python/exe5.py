nomes = ["","",""]

senhas = ["","",""]

tam = len(nomes)

for i in range(tam):
    nomes[i] = input("Digite um nome: ")
    senhas[i] = input("Digite uma senha: ")
    print()
for x in range(tam):
    input(f'Posição {x} - Nome: {nomes[x]} e a senha: {senhas[x]}')