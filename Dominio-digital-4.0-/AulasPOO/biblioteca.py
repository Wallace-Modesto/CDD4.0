class Pessoa:
    def __int__(self, nome, peso, idade, falando= False, comando= False, dormindo= False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falando = falando
        self.comando = comando
        self.dormindo = dormindo
    def comer (self):
        print(f'{self.nome} foi comer.')
    def dormir (self):
        print(f'{self.nome} foi dormir. ')
    def falar(self):
        print(f'{self.nome} foi falar. ')
    def comendo(self):
        print(f'{self.nome} está comendo.')
    def falando(self):
        print(f'{self.nome} está falando.')
    def dormindo(self):
        print(f'{self.nome} está dormindo. ')