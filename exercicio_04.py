consumo = float(input("Digite o consumo em kWh: "))

custo_base = consumo * 0.60

resposta_verao = input("Estamos no período de verão? (sim/não): "). strip().lower()

# A função strip() remove espaços em branco no início e no final da string, e a função lower() converte a string para letras minúsculas.

verao = not (resposta_verao == "não")

if consumo > 300 and verao:
    taxa_bandeira = 15.00
    print("Bandeira: vermelha (Consumo critico no período de verão)")
elif consumo > 200 or (consumo > 150 and verao):
        taxa_bandeira = 7.50
        print("Bandeira: amarela (Consumo elevado)")
else:
    taxa_bandeira = 0.00
    print("Bandeira: verde (Consumo normal)")

    valor_total = custo_base + taxa_bandeira
    print(f"Custo base do consumo: R$ {custo_base:.2f}")
    print(f"Taxa de bandeira: R$ {taxa_bandeira:.2f}")
    print(f"Valor total da conta: R$ {valor_total:.2f}")