cartao = input("Você possui o Cartão Black?(sim/não): ").lower()
ingresso = input("Você comprou o ingresso vip?(sim/não): ").lower()

if cartao == "sim" or ingresso == "sim":
    print("Bem-vindo(a) a sala vip!")
else:
    print("Você não tem acesso a sala vip!")