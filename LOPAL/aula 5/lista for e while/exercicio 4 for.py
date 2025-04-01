#-*-coding: UTF-8-*-
print(" digite um numero para que eu apresente os divisores deste")

numero = int(input("digite um numero para imprimir seus divisores:"))

for i in range (1,numero,+1):
    if numero % i ==0:
        print(i)
