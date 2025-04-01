#-*-coding: UTF-8-*-

V= int(input("entre com numeros positivos e imprima quantos numeros foram digitados:"))
contador = contador + 1
while True:
    num = int(input("digite um numero: "))
    if num < 0 :
        print(" você escolheu sair")
        contador = contador + 1
        print("o numero foi contado")
