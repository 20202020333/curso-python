
import os

os.system("cls")

print("exemplo imc")
print("---------------")

peso = int(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

imc = peso / (altura*altura)

print("Seu IMC e: ", imc)