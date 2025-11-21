
# 1 passo - importar a biblioteca do os
 
import os

# 2 passo - limpar tela com os

os.system("cls")

print("exemplo desconto")
print("--------------------")

# 3 passo - solicitar as entradas

preco_original = float(input("digite preco original do producto: "))
porcemtage_desconto = float(input("digite o porcemtage desconto: "))

# 4 passo -  processamento

valor_desconto = preco_original * (porcemtage_desconto/100)

valor_desconto = preco_original - porcemtage_desconto
# 5 passo - saida


print(f"o resultado desconto e: {valor_desconto}")


