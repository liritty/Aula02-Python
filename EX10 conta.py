consumo = float(input("Insira seu consumo de enegia em kWh: "))

if consumo < 0:
    print("Resposta inválida.")
elif consumo <= 100:
    faixa = "Até 100kWh"
    tarifa = 0.60
    print(f"Faixa: {faixa} | Tarifa: R${tarifa:.2f} por kWh")
    print(f"Total: R${consumo * tarifa:.2f}")

elif consumo <= 200:
    faixa = "De 101kWh até 200kWh"
    tarifa = 0.75
    print(f"Faixa: {faixa} | Tarifa: R${tarifa:.2f} por kWh")
    print(f"Total: R${consumo * tarifa:.2f}")

elif consumo <= 300:
    faixa = "De 301kWh até 400kWh"
    tarifa = 0.90
    print(f"Faixa: {faixa} | Tarifa: R${tarifa:.2f} por kWh")
    print(f"Total: R${consumo * tarifa:.2f}")

else:
    faixa = "Acima de 300kWh"
    tarifa = 1.05
    print(f"Faixa: {faixa} | Tarifa: R${tarifa:.2f} por kWh")
    print(f"Total: R${consumo * tarifa:.2f}")

