def mediaPares(vet):
  soma = 0
  qtdPares = 0
  for valor in vet:
    qtdPares += 1
    soma += valor
  media = soma / qtdPares
  return media
vetor = [1, 2, 3, 4, 5, 6]
print(mediaPares(vetor))