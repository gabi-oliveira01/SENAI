#-*-coding: UTF-8-*-
def volume():
    raio = float(input("digite o raio:"))
    altura= float(input("digite a altura:"))
    return 3.14 * (raio * raio) * altura

print(f"O volume é {volume():.2f}.")
