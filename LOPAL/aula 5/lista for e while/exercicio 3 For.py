#-*-coding: UTF-8-*-
print("=" *83)
print(" digite um numero para que eu calcule o fatorial:")
print("=" *83)

numero= int(input("digite um numero para cacular o fatorial:"))

fatorial = 1

for i in range (1,numero + 1):
    fatorial *= i

print("")
print("=" *34)
print(f"fatorial de {numero} = {fatorial}")
print("=" *34)
