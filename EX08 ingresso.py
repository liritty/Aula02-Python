idade = int(input("Insira sua idade: "))

if idade < 0:
    print("Idade inválida")
elif idade <= 5:
    print("Entrada gratuita!")
elif idade <= 12:
    print("Ingresso R$12,00")
elif idade <= 59:
    print("Ingresso R$25,00")
else:
    print("Ingresso R$12,00")