# FAÇA UM ALGORITMO PARA CONVERTER DE DÓLARES PARA REAIS

dolar = 0.0 #atribuicao de valor a uma variável - dolar recebe 0.0
taxa = 0.0  #variável taxa recebe 0.0
reais = 0.0
########  E N T R A D A S ############
print("Informe o valor em dólares:") ## escreva("mensagem")
dolar = float(input())              ## leia(dolar)  

print("Informe a taxa de conversão")
taxa = float(input())   #float - numero real

########  P R O C E S S A M E N T O S ##########
reais = dolar * taxa

######## S A Í D A #########
print("O valor em Reais é R$ ", reais)