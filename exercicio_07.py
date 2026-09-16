leituras = []
quantidade = int(input("Quantas leituras? "))

for i in range(quantidade):
    valor = float(input(f"leitura {i + 1}: "))
    leituras.append(valor)
    print(f"Lista atualizada: {leituras}\n")

print(len(leituras))  # Imprime a quantidade de elementos na lista

for i in range(len(leituras)):
    print(leituras[i])  # Imprime cada elemento da lista

maior = leituras[0]
menor = leituras[0]
soma = 0

for leitura in leituras:
    soma = soma + leitura

    if leitura > maior:
        maior = leitura
    if leitura < menor:
        menor = leitura

print(f"Maior leitura: {maior}")
print(f"Menor leitura: {menor}")  
print(f"Soma das leituras: {soma}")