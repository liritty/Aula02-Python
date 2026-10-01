valor = float(input("Insira o valor da compra: "))

if valor < 0:
    print("Valor inválido")
elif valor < 100:
    print("Desconto aplicado: 0%")
    print(f"Valor final: R${valor:.2f}")

elif valor < 300:
    print("Desconto aplicado: 5%")
    print(f"Valor final: R${valor * 0.95:.2f}")

elif valor < 500:
    print("Desconto aplicado: 10%")
    print(f"Valor final: R${valor * 0.90:.2f}")
    
else:
    print("Desconto aplicado: 15%")
    print(f"Valor final: R${valor * 0.85:.2f}")