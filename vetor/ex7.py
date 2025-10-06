n = 10
fibonacci = [1, 1]

for i in range(2, n):
    proximo = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo)

print("Sequência de Fibonacci:", fibonacci)