#-*-coding: UTF-8-*-
print(" digite dois valores e eu farei um calculo de acordo com o operador desejado")
num1= float(input("digite o numero:"))
num2= float(input("digite o  segundo numero:"))
operador= input("escolha  a operação que ira usar '+','-','*', '/' os sinais de cada operação")

def calculo (num1,num2,operador):
    resultado =0
    if operador == "+":
       resultado = num1+num2
       print(resultado)
    elif operador == "-":
        resultado=num1-num2
        print(resultado)
    elif operador == "*":
        resultado=num1*num2
        print(resultado)
    elif operador == "/":
        resultado = num1/num2
        print(resultado)
    
    
    
    
calculo(num1,num2,operador)
