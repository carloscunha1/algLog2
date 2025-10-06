notas = [8.5, 7.2, 9.1, 6.8, 8.9, 7.5, 9.3, 6.2, 8.1, 7.8, 9.0, 6.5, 8.4, 7.1, 9.2, 6.9, 8.6, 7.4, 9.4, 6.1, 8.3, 7.7, 8.8, 6.7, 9.5, 7.0, 8.2, 6.4, 8.7, 7.3, 9.6, 6.0, 8.0, 7.6, 8.9, 6.8, 9.1, 7.2, 8.5, 6.6, 9.3, 7.9, 8.4, 6.3, 9.0, 7.5, 8.1, 6.9, 8.8, 7.1]

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)
limite_acima = media * 1.1
limite_abaixo = media * 0.9

acima = 0
abaixo = 0

for nota in notas:
    if nota >= limite_acima:
        acima += 1
    elif nota <= limite_abaixo:
        abaixo += 1

print("Média:", media)
print("Notas 10% acima da média:", acima)
print("Notas 10% abaixo da média:", abaixo)