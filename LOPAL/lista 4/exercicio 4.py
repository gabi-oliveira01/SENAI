#-*-coding: UTF-8-*-
print("digite o numero que voce quer que inicie com sua contagem regressiva")
num = int(input("digite o numero para que eu posso iniciar:"))

def contagem (num):
    for i in range (num,-1,-1):
        print(f"{i}")

contagem (num)
print("BUMCHACALAKA")
