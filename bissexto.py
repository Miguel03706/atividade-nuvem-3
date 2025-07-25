def main():
    ano = int(input("Digite um ano: "))

    ''' 
    Regras oficiais para determinar se um ano é bissexto:
        Se o ano é divisível por 4, pode ser bissexto;
        Mas se também é divisível por 100, então não é bissexto;
        A não ser que ele seja divisível por 400, aí é bissexto.
    '''

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")

main()