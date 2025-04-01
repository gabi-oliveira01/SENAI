print("vamos calcular os gastos de alugar um carro")
# 1 dia R$ 60 / cada km R$ 0,15
distancia_km= float(input("digite a distancia percorrida:"))
dias= int(input("digite os dias utilizados"))
valor_a_pagar_ = dias *60 + distancia_km * 0.15
print("o valor a pagar é de:" , valor_a_pagar)
