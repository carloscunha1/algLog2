vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
vetor2 = []

for i in range(len(vetor1)):
    vetor2.append(vetor1[len(vetor1) - 1 - i])

print("Vetor original:", vetor1)
print("Vetor invertido:", vetor2) 8, 3, 16, 9, 21, 7, 14, 11, 18, 6, 25, 4, 19]

maior_par = None
menor_impar = None

for numero in vetor:
    if numero % 2 == 0:  
        if maior_par is None or numero > maior_par:
            maior_par = numero
    else:  
        if menor_impar is None or numero < menor_impar:
            menor_impar = numero

print("Maior número par:", maior_par)
print("Menor número ímpar:", menor_impar)