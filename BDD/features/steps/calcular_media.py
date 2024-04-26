def calcular_media(num1, num2):
    media = (num1 + num2) / 2
    return media

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

media = calcular_media(numero1, numero2)
print("A média dos dois números é:", media)
