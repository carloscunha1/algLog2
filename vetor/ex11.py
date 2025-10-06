vetor = [12, 7, 23, 8, 15, 34, 9, 28, 41, 6, 19, 52, 13, 36, 5, 47, 18, 29, 11, 42]
pares = []
impares = []

for numero in vetor:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Vetor original:", vetor)
print("Números pares:", pares)
print("Números ímpares:", impares)