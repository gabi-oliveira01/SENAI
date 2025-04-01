#-*-coding:UTF-8-*-
print("programa para calcular a soma e média dos numeros inseridos")
soma =0
contador = 0
while True:
    numero= float(input("digite um numero negativo para sair:"))
if numero < 0:
    media= soma / contador
    print(f"{soma} :")
    print(f"{media}:")
else:
    print("nenhum número foi inserido")
    
