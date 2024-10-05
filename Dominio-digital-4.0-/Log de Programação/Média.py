print("------------------")
print("DIGITE SUAS NOTAS")
print("------------------")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print("--------------------------------")
    print("Status do aluno: Aprovado.")
    print("--------------------------------")

elif media >=4:
    print("--------------------------------")
    print("Status do aluno: Recuperação. ")
    print("--------------------------------")

else:
    print("--------------------------------")
    print("Você está em Reprovado. ")
    print("--------------------------------")


