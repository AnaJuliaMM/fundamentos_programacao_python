# PROGRAMA:
# Esse programa recebe duas notas e calculada a média aritmética.
# Se a média for maior ou igual a 9, o aluno é considerado "EXCELENTE"
# Se a média for menor que 9 e maior ou igual a 7, o aluno é considerado "APROVADO"
# Se a média for menor que 7 e maior ou igual a 5, o aluno é considerado "EM RECUPERAÇÃO"
# Se a média for menor que 5, o aluno é considerado "REPROVADO"

# ENTRADAS
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# PROCESSAMENTO
media = (nota1 + nota1)/2

# DECISÃO E SAÍDA
if (media >= 9):
    print("ALUNO EXCELENTE")
elif (media >= 7):
    print("ALUNO APROVADO")
elif (media >= 5):
    print("ALUNO EM RECUPERAÇÃO")
else:
    print("ALUNO REPROVADO")