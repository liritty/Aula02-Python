cor = input("Digite uma cor: ").strip().lower()

match cor:
    case "vermelho":
        print("Pare.")
    case "amarelo":
        print("Dirija com atenção.")
    case "verde":
        print("Siga em frente.")
    case _:
        print("Cor inválida.")