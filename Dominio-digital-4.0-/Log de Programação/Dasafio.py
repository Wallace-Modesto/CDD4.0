hora1 = int(input("Digite o primeiro horario: "))
min1 = int(input("Digite os minutos: "))

hora2 = int(input("Digite o segundo horario: "))
min2 = int(input("Digite os minutos: "))

if hora1 > 12:
    hora1 -=12

if hora2 > 12:
    hora2 -= 12

horas = hora1 + hora2
minutos = min1 + min2

if minutos > 60:
    minutos = minutos - 60
    horas = horas + 1

if horas > 12:
    horas -= 12

print(f"{horas}:{minutos}")
    #print(f"A hora de saida foi:  {horas1}:{minutos}")
#elif 10 > minutos:
 #   print(f"A hora de saida foi:  {horas}: 0{minutos}")
#else:
 #   print(f"A hora de saida foi:  {horas}: {minutos}")









