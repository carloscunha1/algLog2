def somatorio(N):
    S = 0
    for i in range(1, N + 1):
        S += i / (i ** 2)
    return S

def main():
    N = int(input('Entre com um valor para N: '))
    resultado = somatorio(N)
    print("O somatório S é:", resultado)