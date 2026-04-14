# PROGRAMA:
# Esse programa recebe dois números reais, soma-os e apenas mostra
# o total se ele for maior ou igual a 10

# ENTRADAS
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# PROCESSAMENTO
total = numero1 + numero2

# DECISÃO E SAÍDA
if (total >= 10):
    print(f"O resultado é {total}")