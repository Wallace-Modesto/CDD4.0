def gravarTexto(texto):

    with open('arq.txt', 'a') as arquivo:
        arquivo.write(texto)

def lerTexto():
    with open('arq.txt', 'r') as arquivo2:
        texto = arquivo2.read()
        print(texto)


