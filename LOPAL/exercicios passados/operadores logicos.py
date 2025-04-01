Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("oi usuario,vamos fazer uma soma de dois valores?")
oi usuario,vamos fazer uma soma de dois valores?
num = 7
print(num)
7
>>> print(num+2)
9
>>> soma= num+2
>>> print(soma)
9
>>> print("o valor da soma é")
o valor da soma é
>>> print("o valor da soma é: ",mas)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print("o valor da soma é: ",mas)
NameError: name 'mas' is not defined. Did you mean: 'max'?
>>> print("o valor da soma é: ",soma)
o valor da soma é:  9
>>> print("agora eu vou testar mais campos"), soma,"gostaram do resultado ?")
SyntaxError: unmatched ')'
>>> print("agora vou testar mais campos", soma, " gostaram do resultado?")
agora vou testar mais campos 9  gostaram do resultado?
>>> nome=imput("digite seu nome")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    nome=imput("digite seu nome")
NameError: name 'imput' is not defined. Did you mean: 'input'?
>>> nome= imput ('digite seu nome')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    nome= imput ('digite seu nome')
NameError: name 'imput' is not defined. Did you mean: 'input'?
>>> nome= input("digite seu nome')
...             
SyntaxError: unterminated string literal (detected at line 1)
>>> nome= input('digite seu nome')
...             
digite seu nomegabi
>>> num=int(input("digite sua idade:"))
...             
digite sua idade:16
>>> print(num)
...             
16
>>> num2=float(input("digite o valor do seu salario:"))
...             
digite o valor do seu salario:1200
>>> print(num2)
...             
1200.0
