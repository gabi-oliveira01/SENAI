#-*-coding: UTF-8-*-
print("digite um numero que eu vou verificar se ele é primo")
num = int(input("digite um numero"))
          
def primo(x):
    cont = 0
    for i in range (1,x):
        if x%i==0:
            cont+=1
    if cont ==1:
        return f"{x} é primo"
    else:
        return f"{x} não é primo"

print (primo(num))
    
   
    
