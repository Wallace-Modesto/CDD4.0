print("-----------------------------------")
print("             TIMES                 ")
print("-----------------------------------")

time1 = input("Qual é seu time? ")
gols1 = int(input(f"Gols {time1}: "))

time2 = input("Qual é seu segundo time? ")
gols2 = int(input(f"Gols {time2}: "))

if gols1 > gols2:
    print("-----------------------------------")
    print(f"O time {time1} foi o ganhador. ")
    print("-----------------------------------")

elif gols2 == gols1:
    print("-----------------------------------")
    print ("             Empate               ")
    print("-----------------------------------")

else:
    print("-----------------------------------")
    print(f"O time {time2} foi o ganhador. ")
    print("-----------------------------------")
