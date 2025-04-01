#-*-coding: UTF-8-*-
grupospares = []
gruposimpares =[]

while True:
    valor = input('digite um numero(ou 1000 para sair):')

    valor = int(valor)
    
    if valor == 1000:
        break
    
    if valor % 2 == 0:
        grupospares.append(valor)
        
    elif valor % 2 != 0:
        gruposimpares.append(valor)
        
somai= sum(gruposimpares)
somap= sum(grupospares)

print(f'a soma dos valores impares é {somai} e a soma dos valores é {somap}')
