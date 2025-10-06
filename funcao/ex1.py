def menor(x, y):
  if x < y:
    print("O menor número é: ",x)
  elif y < x:
    print("O menor número é: ",y)
  else:
    print("Os números são iguais!")
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
menor(x,y)