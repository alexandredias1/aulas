#Conversão de temperatura

#Tratamento de erros
try:
    temp = float(input("Diga a temperatura atual: "))
    #Para o usuário escolher uma opção
    conversao = int(input("Converter a temperatura para\n1 - Celsius\n2 - Kelvin:  "))

    temp = float(temp)

#Conversão para celsius
    if conversao == 1:
        celsius = (temp + 273.15)
        print(f"A temperatura convertida para Kelvin ficaria de {celsius:,.2f}°K")
#Conversão para Kelvin
    elif conversao == 2:
        Kelvin = (temp - 273.15)
        print(f"A temperatura convertida para Celsius ficaria de {Kelvin:,.2f}°C")
    else:
        print("Valor inserido inválido")

except ValueError:
    print("Valor inserido inválido")