emprestimo = float(input("Qual o valor do emprestimo desejado: "))

taxa = (emprestimo * 8.333) / 100
taxaTotal = taxa * 12
emprestimoFinal = emprestimo + taxa
totalFinal = emprestimoFinal * 12

print(f"O valor da taxa: {taxa}\nO valor da taxa em 12 meses: {taxaTotal}")
print(f"O emprestimo atual é de: {emprestimoFinal}\nSeu emprestimo total daqui a 1 ano é de: {totalFinal}")