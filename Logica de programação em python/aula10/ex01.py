# Cafeteria

import time

cafe = int(input("Escolha o seu café\n1 - Expresso\n2 - Tradicional\n3 - Cappuccino\n4 - Latte\n5 - Descafeinado\n6 - Para encerrar o programa: "))

while True:

    if cafe == 1:
        for coffe1 in range(1, 11):
            print(F"O café estará pronto em 10s {coffe1}")
            time.sleep(1)
        print("O café Expresso está pronto!")
        cafe = int(input("Escolha o seu café\n1 - Expresso\n2 - Tradicional\n3 - Cappuccino\n4 - Latte\n5 - Descafeinado\n6 - Para encerrar o programa:  ")) 

    elif cafe == 2:
        for coffe2 in range(1, 16):
            print(F"O café estará pronto em 15s {coffe2}")
            time.sleep(1)
        print("O café Tradicional está pronto!")
        cafe = int(input("Escolha o seu café\n1 - Expresso\n2 - Tradicional\n3 - Cappuccino\n4 - Latte\n5 - Descafeinado\n6 - Para encerrar o programa:  ")) 
        
    elif cafe == 3:
        for coffe3 in range(1, 23):
            print(F"O café estará pronto em 22s {coffe3}")
            time.sleep(1)
        print("O café Cappuccino está pronto!")
        cafe = int(input("Escolha o seu café\n1 - Expresso\n2 - Tradicional\n3 - Cappuccino\n4 - Latte\n5 - Descafeinado\n6 - Para encerrar o programa:  ")) 
        
    elif cafe == 4:
        for coffe4 in range(1, 19):
            print(F"O café estará pronto em 18s {coffe4}")
            time.sleep(1)
        print("O café Latte está pronto!")
        cafe = int(input("Escolha o seu café\n1 - Expresso\n2 - Tradicional\n3 - Cappuccino\n4 - Latte\n5 - Descafeinado\n6 - Para encerrar o programa:  ")) 

    elif cafe == 5:
        for coffe5 in range(1, 21):
            print(F"O café estará pronto em 20s {coffe5}")
            time.sleep(1)
        print("O café Descafeinado está pronto!")
        cafe = int(input("Escolha o seu café\n1 - Expresso\n2 - Tradicional\n3 - Cappuccino\n4 - Latte\n5 - Descafeinado\n6 - Para encerrar o programa:  "))

    elif cafe == 6:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida")
        break 