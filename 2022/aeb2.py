# faça um algoritmo que receba dois valores inteiros para A e B.
# O algoritmo deverá trocar os valores entre as variáveis
# apresente os novos valores contidos em A e B

print("Informe valor para A:")
a = int(input())   # recebeu 2

print("Informe valor para B:")
b = int(input())   # recebeu 7
#########
aux = a
a = b               # a recebeu 7
b = aux               # b recebeu 7
#########
print("valor de A: ", a)
print("valor de B: ", b)