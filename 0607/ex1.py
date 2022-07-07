### identificar ENTRADAS/PROCESSAMENTOS/SAÍDAS

# Faça um algoritmo que receba três notas de um estudante,
#calcule sua média, e informe se foi aprovado ou reprovado
#Considere que a média de aprovação é 7.0.
nota1 = nota2 = nota3 = 0.0
soma = 0.0
media = 0.0
situacao = ""
#ENTRADAS - três notas
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
#PROCESSAMENTO - Como transformar as três notas em Apr/Rep
#soma
soma = nota1 + nota2 + nota3
#dividir por 3
media = soma / 3
#comparar com 7.0 - #"calcular" a situacao
if media >= 7.0:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

#SAÍDAS - Aprovado / Reprovado
print(situacao)