### identificar ENTRADAS/PROCESSAMENTOS/SAÍDAS

# Faça um algoritmo que receba três notas de um estudante,
#calcule sua média, e informe se foi aprovado ou reprovado
#Considere que a média de aprovação é 7.0.

#ENTRADAS - três notas
def entradas(): #defini que exsite um modulo (procedimento)
    global nota1
    global nota2
    global nota3
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Terceira nota: "))


#PROCESSAMENTO - Como transformar as três notas em Apr/Rep
def mediaNotas(n1, n2, n3):
    soma = n1 + n2 + n3
    media = soma / 3
    return media







def situacaoEstudante(med):
    if med >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    return situacao


#SAÍDAS - Aprovado / Reprovado











######algoritmo principal
nota1 = nota2 = nota3 = 0.0
media = 0.0
situacao = ""

entradas()

media = mediaNotas(nota1, nota2, nota3)
situacao = situacaoEstudante(media)

print(situacao)