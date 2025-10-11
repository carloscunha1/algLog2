def maior_valor(vet):
    maior = vet[0]
    for num in vet:
        if num > maior:
            maior = num
    return maior

def segundo_maior_valor(vet):
    maior = maior_valor(vet)
    segundo_maior = None
    for num in vet:
        if num != maior:
            if segundo_maior is None or num > segundo_maior:
                segundo_maior = num
    return segundo_maior

def main():
    vet = []
    tamanho = int(input('Digite a quantidade de números: '))
    for i in range(tamanho):
        vet.append(int(input('Digite um número: ')))
    maior = maior_valor(vet)
    segundo_maior = segundo_maior_valor(vet)
    print(f'Maior valor: {maior}')
    print(f'Segundo maior valor: {segundo_maior}')
main()