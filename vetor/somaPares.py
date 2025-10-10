vetor = [1, 2, 3, 4, 5]

soma = 0
numPares = 0
for i in vetor:
  if i % 2 == 0:
    soma += i
    numPares += 1   

print("Soma dos pares:", soma)
