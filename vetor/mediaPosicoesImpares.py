vetor = [1, 2, 3, 4, 5]

soma = 0
numElementos = 0
for i in range(len(vetor)): # i nessa sintaxe é a posição, enquanto em "for i in vetor:" o mesmo i referencia o valor
    if i % 2 == 1: 
        soma += vetor[i] 
        numElementos += 1

media = soma / numElementos
print("Média dos elementos nas posições ímpares:", media)
