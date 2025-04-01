print ("vamos classificar um triangulo")
lado1= int(input("digite o lado 1:"))
lado2= int(input("digite o lado 2:"))
lado3 = int(input("digite o lado 3:"))

if lado1==lado2 and lado2==lado3:
    print("o triangulo é equilatero")
elif lado1==lado2 and lado2!=lado3:
        print("o triangulo é isosceles")
else:
    print("o triangulo é isosceles")
            
