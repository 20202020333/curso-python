
import os

os.system("cls")

print("exemplos porcemtage")
print("----------------------")

valor_total = float(input("digite seu valor: "))
porcemtage = float(input("digite o porcemtage a ser calculada: "))

valor_parte = valor_total * (porcemtage / 100)

print(f"o valor parte e: {valor_parte}")