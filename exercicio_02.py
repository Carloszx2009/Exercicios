# Python é case sensitive, ou seja, a variação de letras maiúculas e minúsculas faz com que a linguagem interpreta as varuáveis como diferentes. Por isso que consumo != Consumo != CoNsUmO( na visão do Python, são três variáveis diferentes)
consumo = 180.5
Consumo = 200.0
CoNsUmO = 300.0
TARIFA = 0.85

custo = consumo * TARIFA
print(f"O custo estimado: R$ {custo:.2f}")

# O conteúdo da variável custo teve uma aplicação de máscara, ou seja, o 2F, que significa mostrar o valor com =, no máximo, duas casas após a vírgula.