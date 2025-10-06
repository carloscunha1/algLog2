  vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  soma_pares = 0
  quantidade_pares = 0

  for numero in vetor:
      if numero % 2 == 0: 
          soma_pares += numero
          quantidade_pares += 1

  if quantidade_pares > 0:
      media_pares = soma_pares / quantidade_pares
      print("Média dos números pares:", media_pares)
  else:
      print("Não há números pares no vetor!")
