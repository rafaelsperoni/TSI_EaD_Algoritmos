nota1 = nota2 = media = 0

print("Informe a primeira nota: ")
nota1 = float(input())
print("Informe a segunda nota: ")
nota2 = float(input())

media = (nota1+nota2)/2

print("A média final é:", media)

if (media>=7.0):
  print("Parabéns, Aprovado!")  # quando verdadeiro
else:
  print("Informe a nota do exame: ")  #quando falso
  exame = float(input())

  final = (media + exame)/2
  print("A média Final, após o exame: ", final)
  if (final>=5.0):
    print("Parabéns, Aprovado no Exame!")
  else:
    print("Reprovado")      #quando falso

  