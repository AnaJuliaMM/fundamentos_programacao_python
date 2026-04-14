# PROGRAMA:
# Nesse programa, o aluno informa qual turma ele pertence, e 
# recebe a localização das aulas na escola

# ENTRADAS
print("Qual turma você pertence?")
print("1 - TSESI1-A")
print("2 - TSESI1-B")
print("3 - TSESI1-C")
turma = input("Digite a opção: ")

# DECISÃO E SAÍDA
match turma:
    case "1":
        print("LAB INFO 1")
    case "2":
        print("LAB INFO 2")
    case "3":
        print("LAB INFO 3")
    case _:
        print("OPÇÃO INVÁLIDA")
