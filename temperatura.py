def converter_temperatura(valor, origem, destino):
    if origem == "C":
        if destino == "F":
            return (valor * 9/5) + 32
        elif destino == "K":
            return valor + 273.15
    elif origem == "F":
        if destino == "C":
            return (valor - 32) * 5/9
        elif destino == "K":
            return (valor - 32) * 5/9 + 273.15
    elif origem == "K":
        if destino == "C":
            return valor - 273.15
        elif destino == "F":
            return (valor - 273.15) * 9/5 + 32
    return None

def main():
    valor = float(input("Digite a temperatura: "))
    origem = input("Unidade de origem (C, F, K): ").upper()
    destino = input("Unidade de destino (C, F, K): ").upper()

    resultado = converter_temperatura(valor, origem, destino)

    if resultado is not None:
        print(f"{valor}°{origem} = {resultado:.2f}°{destino}")
    else:
        print("Conversão inválida.")

main()