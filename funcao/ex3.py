def mediaPares(vet):
  somaPares = 0
  qtdPares = 0
  for valor in vet:
    if valor % 2 == 0:
      qtdPares += 1
      somaPares += valor
  media = somaPares / qtdPares
  return media
vetor = [1, 2, 3, 4, 5, 6]
print(mediaPares(vetor))
    