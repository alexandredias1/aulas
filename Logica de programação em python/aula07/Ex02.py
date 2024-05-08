hora_atual = int(input("Que horas são: "))

if hora_atual < 8 and hora_atual >= 18:
    print("Erro: Fora de horario de expediente.")
else:
    for horas in range(hora_atual, 18):
        atividade = input(f"O que você fez ou vai fazer as {horas}h?")
    else:
        print("Fim do expediente.")
