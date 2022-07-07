nota1 = nota2 = media = 0

print("Informe a primeira nota: ")
nota1 = float(input())
print("Informe a segunda nota: ")
nota2 = float(input())

media = (nota1+nota2)/2

print("A média final é:", media)

if (media>=7.0):
  print("Parabéns, Aprovado!")  #quando verdadeiro
else:
  print("Reprovado")   #quando falso

  