tipo = input("Tipo de pedido (troca, devolução ou suporte): ").strip().lower()
prioridade = int(input("Insira a prioridade do seu pedido: "))

match (tipo, prioridade):
    case ("troca" | "devolução", 1):
        print("Setor: Pós venda | Prazo: atendimento imediato")
    case ("troca" | "devolução", 2):
        print("Setor: Pós venda | Prazo: Até 4 horas")
    case ("troca" | "devolução", 3):
        print("Setor: Pós venda | Prazo: Até 1 dia útilç")

    case ("suporte", 1):
        print("Setor: Suporte | Prazo: atendimento imediato")
    case ("suporte", 2):
        print("Setor: Suporte | Prazo: Até 4 horas")
    case ("suporte", 3):
        print("Setor: Suporte | Prazo: Até 1 dia útil")
    case _:
        print("Resposta inválida.")