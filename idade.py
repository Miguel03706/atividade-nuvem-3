def main():
    idade = int(input("Digite sua idade: "))

    if idade < 0:
        print("Idade inválida.")
    elif idade <= 12:
        print("Categoria: Criança")
    elif idade <= 17:
        print("Categoria: Adolescente")
    elif idade <= 59:
        print("Categoria: Adulto")
    else:
        print("Categoria: Idoso")

main()