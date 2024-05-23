nota1 = nota2 = media = 0

for i in range(300):
    print("Informe a primeira nota: ")
    nota1 = float(input())
    print("Informe a segunda nota: ")
    nota2 = float(input())

    media = (nota1+nota2)/2

    print("A média final é:", media)
    if (media>=7):
        print("Aprovado")
    