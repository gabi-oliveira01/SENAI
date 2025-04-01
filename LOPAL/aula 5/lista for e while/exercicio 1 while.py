#-*-coding:UTF-8-*-
print("vamos receber valores,vou somar e fazer a media!vai encerrar quando receber um numero negativo")
soma =  0
contador = 0
while True:
    valor= float(input("digite um valor:")

    if valor< 0:
        break
    soma = soma + valor
    contador = contador + 1
print(f'a soma dos valores sera:",soma)
print('a media dos valores é : ", soma / contador")
