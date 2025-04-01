#-*-coding: UTF-8-*-
cont = 0
Num=0
acum = 0

while True:
    Num = int(input("digite um valor :"))
    
    if Num < 0 :
        break
    
    
    acum= acum + Num
    cont = cont + 1

    media = cont/ Num
    print(media)
