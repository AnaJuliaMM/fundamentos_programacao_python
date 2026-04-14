# PROGRAMA:
# Esse programa soma todos os números informados pelo usuario
# ate que ele digite o numero 0. Quando isso acontecer, o programa exibe o total armazenado.

numero_digitado = 1
total = 0

while(numero_digitado != 0):
    numero_digitado = int(input("Insira um numero inteiro: "))
    total += numero_digitado
print(f"A soma dos números digitados é {total}")

