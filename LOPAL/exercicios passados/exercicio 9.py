print("vamos descobrir o tempo perdido de vida,fumando cigarros")
cigarros= int(input("digite a quantidade de cigarros fumados por dia:"))
anos_fumados=float(input("digite a quantidade de anos fumados: " ))
quantidade_total_cigarros= cigarros * anos_fumados * 365
tempo_minutos=quantidade_total_cigarros * 10
tempo_dias= tempo_minutos / 60/ 24 #1440
