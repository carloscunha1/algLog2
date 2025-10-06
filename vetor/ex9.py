vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
vetor2 = []

for i in range(len(vetor1)):
    if i % 2 == 0: 
        vetor2.append(vetor1[i] * 2)
    else: 
        vetor2.append(vetor1[i] * 3)

print("Vetor original:", vetor1)
print("Novo vetor:", vetor2)