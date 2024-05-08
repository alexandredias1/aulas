atividades = {"Codificar em python", "Codificar em baco de dados", "Codificar em java", "Horario de almoço", "Codificar em X"}

hora = int(input("Diga o horario atual: "))

print("Lista de atividades: ")

for info in atividades:
    print(f"No horario de {hora} horas, alexandre realizará a seguinte atividade: ")
    print(info)
    hora = hora + 1