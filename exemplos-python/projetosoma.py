
#1 passo - importar a biblioteca do os
import os

# passo - limpara tela com o os 
os.system("cls")

print("""
██████╗░██████╗░░█████╗░░░░░░██╗███████╗████████╗░█████╗░  ░██████╗░█████╗░███╗░░░███╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝╚══██╔══╝██╔══██╗  ██╔════╝██╔══██╗████╗░████║██╔══██╗
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░░░░██║░░░██║░░██║  ╚█████╗░██║░░██║██╔████╔██║███████║
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░░░░██║░░░██║░░██║  ░╚═══██╗██║░░██║██║╚██╔╝██║██╔══██║
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗░░░██║░░░╚█████╔╝  ██████╔╝╚█████╔╝██║░╚═╝░██║██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░░░╚═╝░░░░╚════╝░  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝
      """)

print("exemplo projeto soma")
print("--------------------------")

#3 passo - solicitar as entradas

numero_1 = int(input("digite o primeiro numero: "))
numero_2 = int(input("digite o segundo numero: "))

#4 passo - processamento

resultado = numero_1 + numero_2

#5 passo - saida - mostrar o resultado

print(f"O resultado da soma e: {resultado}")

input("pressione uma tecla para fechar")