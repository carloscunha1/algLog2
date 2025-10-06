vetor = [15, 3, 28, 7, 42, 91, 6, 33, 18, 55, 12, 67, 4, 89, 21, 36, 8, 74, 13, 45]

maior = vetor[0]
menor = vetor[0]

for numero in vetor:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("Maior número:", maior)
print("Menor número:", menor)