maior = None
menor = None

while True:
    numero= int(input("digite um numero : "))
    if numero< 0:
         break

    if maior is None or numero > maior:
        maior= numero
    if menor is None or numero < menor:
        menor = numero

print(f'Maior numero: {maior}')
print(f'menor numero: {menor}')
