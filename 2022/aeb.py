#exemplo 3 - python
A = B = aux = 0;

print("Informe o valor de A: ");
A = int(input());
print("Informe o valor de B: ");
B = int(input());
aux = A
A = B
B = aux

print("O valor atual de A:", A);
print("O valor atual de B:", B);