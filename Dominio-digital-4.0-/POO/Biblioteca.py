class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer (self):
        print(f'{self.nome} está comendo')

class Gato(Animal):
    def __int__(self, nome, cor):
       super(). __init__(nome, cor)
    def miar(self):
        print(f'O {self.nome} foi comer')

class Vaca(Animal):
    def __init__(self, nome, cor):

        super().__init__(nome,cor)

    def mugir (self):
        print(f'O {self.nome} está mujindo')

class Cachorro(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)

    def latir (self):
        print(f'O {self.nome} está latindo')

class Coelho(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)

    def Saltitando (self):
        print(f'O {self.nome} está saltitando')


class Atleta:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.aposentado = False
        self.aquecido = False

    def aposentado (self):
       print(f'{self.aposentado} está na rede...')
       self.aposentado=True

    def desaposentado(self):
        print('O atleta está aposentado')
        self.aposentado=False

    def aquecer (self):
        print(f'{self.nome}  pode aquecer... ')
        self.aquecido=True


class Corredor (Atleta):
    def __int__(self, nome, peso):
        super(). __init__(nome,peso)
    def correr (self):
        if self.aquecido == True:
            if self.aposentado==False:
                print(f'{self.nome} foi correr ...')
            else:
                print(f'{self.nome} não pode correr porque esta aposentado ...')
        else:
            print(f'O atleta {self.nome} não pode correr porque não aqueceu')

class Nadador (Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome,peso)
    def nadar (self):
        if self.aquecer == True:
            if self.aposentado() == False:
                print(f'O atleta {self.nome} foi nadar')
            else:
                print(f'O atleta {self.nome} não pode nadar porue está aposentado')
        else:
            print(f'O atleta {self.nome} não pode nadar porquer não aqueceu')
class Ciclista (Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)
    def pedalar(self):
        if self.aquecer == True:
            if self.aposentado == False:
                print(f"O atleta {self.nome} foi pedalar")
            else:
                print(f"O atleta {self.nome} não pode pedalar porque está aposentado")
        else:
            print(f"O atleta {self.nome} não pode pedalar porque não aqueceu")

class Triatleta(Ciclista,Corredor,Nadador,Atleta):
    def __init__(self, aposentado,peso):
        super().__init__(aposentado,peso)