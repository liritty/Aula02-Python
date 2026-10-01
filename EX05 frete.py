regiao = input("Digite a região da entrega: ").strip().lower()
valor = float(input("Digite o valor da compra: "))

match regiao:
    case "norte" | "nordeste" | "sul" | "sudeste" if valor >= 200:
        print("Frete grátis!")

    case "norte" | "nordeste":
        print("Frete de R$30,00")

    case "sul" | "sudeste":
        print("Frete de R$20,00")
        
    case _:
        print("Resposta inválida.")