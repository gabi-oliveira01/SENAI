print("digite um temperatura em celsius e eu vou te retornar a temperatura em Fahrenheit, e vice-versa")

tempo = float(input("digite a temperatura: "))
temperatura = input("me de a temperatura em celsius ou Fahrenheit, C ou F:")
def contc (tempo,temperatura):
    if temperatura == "C":
        conct=(tempo - 32) *5/9
        print(" a temperatura em celsius é de :" , contc)
    elif temperatura == 'f':
        conft = 9/5 *tempo + 32
        print(" a temperatura em Fahreinheit é de:", contf)
    conct (tempo,temperatura)
