# PROGRAMA:
# Esse programa recebe dois números reais e soma-os
# Se o total for maior ou igual a 10, 10 unidades serão acrescidas ao resultado
# Caso contrário, 10 unidades serão subtraídas do resultado

# ENTRADAS
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# PROCESSAMENTO
total = numero1 + numero2

# DECISÃO E SAÍDA
if (total >= 10):
    print(f"O resultado é {total + 10}")
else:
    print(f"O resultado é {total - 10}")