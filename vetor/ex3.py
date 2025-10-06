notas = [8.5, 7.0, 9.2, 6.3, 8.8]

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)

acima_media = 0
for nota in notas:
    if nota > media:
        acima_media += 1

print("Média da classe:", media)
print("Notas acima da média:", acima_media)