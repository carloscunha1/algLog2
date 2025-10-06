#verificar formação de triangulo e tipo do triangulo

x = float(input("Digite um número:"))
y = float(input("Digite outro número:"))
z = float(input("Digite outro número:"))
  
if x + y > z and x + z > y and y + z > x:
    if x == y == z:
        print("É um triângulo equilátero")
    elif x == y or y == z or x == z:
        print("É um triângulo isósceles")
    else:
        print("É um triângulo escaleno")
else:
    print("Os números não formam um triângulo")
