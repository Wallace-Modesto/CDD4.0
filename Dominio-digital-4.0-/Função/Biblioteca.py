
def piramide(n):
    for x in range(1,n+1):
        for y in range(x):
            print(x,end=" ")
        print()

def torre(n):
    for x in range(1,n+1):
        for y in range(x):
            print(x, end=" ")
        print()


def vogais (texto):
    cont=0
    for x in texto:
        if x in "aeiouAEIOU":
            cont+=1
    print(f'O texto digitado tem {cont} vogais')

def inverterNomes(nomes1,nomes2,nomes3,nomes4,nomes5):
    nomes=['']*5
    nomes[0]=nomes1
    nomes[1]=nomes2
    nomes[2]=nomes3
    nomes[3]=nomes4
    nomes[4]=nomes5
    print(nomes)
    nomes.reverse()
    print(nomes)

def somar(*numeros):
    t = len(numeros)
    soma = 0
    for x in range(t):
        soma = soma + numeros[x]
    print(soma)

class Pessoa:
    def __init__(self, nome, peso, idade, falando=False, comendo= False, dormindo= False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falando = falando
        self.comendo = comendo
        self.dormindo = dormindo
    def comer (self):
        print(f'{self.nome} foi comer')
    def dormir (self):
        print(f'{self.nome} foi comer')
    def falar (self):
        print(f'{self.nome} está falando')
    def comendo(self):
        print(f'{self.nome} está comendo')
    def falando (self):
        print(f'{self.nome} está falando')
    def dormindo(self):
        print(f'{self.nome} está falando')


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

    def aquecer (self):
        print(f'{self.nome}  pode aquecer... ')
        self.aquecido=True
    def aposentado (self):
       print(f'{self.aposentado} está na rede...')
       self.aposentado=True

class Corredor (Atleta):
    def __int__(self, nome, peso):
        super(). __init__(nome,peso)
    def correr (self):
        if self.aquecido == True:
            if self.aposentado==False:
                print(f'{self.nome} foi correr ...')
            else:
                print(f'{self.nome} não pode correr porque esta aposentado ...')

class Corredor (Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome,peso)
    def correr (self):
        print(f'O {self.nome} pode correr..')








