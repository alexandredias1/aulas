idade = int(input("Quantos anos você tem: "))

if idade < 16:
    print("Você não tem idade para votar!")
elif 18 <= idade < 70:
    print("Você deve votar!")
else:
    print("Você esta elegivel para votar, mas não é obrigatorio.")