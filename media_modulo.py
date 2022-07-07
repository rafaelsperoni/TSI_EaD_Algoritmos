nota1 = nota2 = media = 0

def entrada(): #definicao do modulo/funcao
    global nota1
    global nota2
    print("Informe a primeira nota: ")
    nota1 = float(input())
    print("Informe a segunda nota: ")
    nota2 = float(input())

def calculo(a, b): #definicao do modulo/funcao
    soma = a + b
    media = soma/2

    return media

def situacao(m): #definicao da funcao
    if (m >= 7.0):
        return "Parabéns, Aprovado!"
    else:
        return "Reprovado"  # quando falso


entrada() #chamada da funcao
media = calculo(nota1, nota2) #chamada da funcao
print(media)
situ = situacao(media) #chamada da funcao
print(situ)
