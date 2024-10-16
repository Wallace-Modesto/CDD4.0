from Biblioteca import *

while True:
    op = int(input('Digite sua opção: \n'
                   '1 para GRAVAR \n'
                   '2 para LER \n'
                   '3 para SAIR \n'))

    match op:
        case 1:
            t = input('Digite um texto: ')
            gravarTexto(t)
        case 2:
            lerTexto()
        case 3:
            break
        case _:
            print('Opção errada')