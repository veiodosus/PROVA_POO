# IFPI
# CURSO: TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
# DISCIPLINA: PROGRAMAÇÃO ORIENTADA À OBJETOS
# PROF: ROGÉRIO BATISTA
# NOME: Vinícius Silva Ribeiro

# 2ª AVALIAÇÃO!!!

# QUESTÃO 1. Assinale a alternativa incorreta:

# RESPOSTA: Alternativa - C

# QUESTÃO 2. Sobre polimorfismo, assinale a alternativa correta:

# RESPOSTA: Alternativa - A

# QUESTÃO 3. Escreva duas classes: Ponto e Reta. Crie uma hierarquia de classes entre elas. 
# Escreva seus respectivos métodos construtores (__init__) e __str__(). Reescreva o método
# str__ da classe Reta de forma que haja reuso. Crie 2 objetos de cada classe e depois imprima-os.

# RESPOSTA:

print('\nQUESTÃO 3:\n')

class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __str__(self) -> str:
        return f'Coordenadas (x, y): {self.__x}, {self.__y}'
    
class Reta:
    def __init__(self, ponto1: Ponto, ponto2: Ponto):
        if type(ponto1) == Ponto and type(ponto2) == Ponto:
            self.__ponto1 = ponto1
            self.__ponto2 = ponto2
        else:
            self.__ponto1 = Ponto(int(ponto1[0]), int(ponto1[1]))
            self.__ponto2 = Ponto(int(ponto2[0]), int(ponto2[1]))

    @property
    def ponto1(self):
        return self.__ponto1
    
    @property
    def ponto2(self):
        return self.__ponto2
    
    def __str__(self):
        return f'1º Ponto:\n{self.__ponto1}\n2º Ponto:\n{self.__ponto2}'
    
ponto1 = Ponto(2, 5)
ponto2 = Ponto(3, 6)

reta1 = Reta(ponto1, ponto2)
reta2 = Reta((7, 8), (8, 6))

print(ponto1)
print(ponto2)

print(reta1)
print(reta2)

# QUESTÃO 4. Reescreva as classes Ponto e Reta descritas na questão anterior, agora utilizando
# somente associação de classes. Saída (idem anterior)

# RESPOSTA:

print('\nQUESTÃO 4:\n')

class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __str__(self) -> str:
        return f'Coordenadas (x, y): {self.__x}, {self.__y}'
    
class Reta:
    def __init__(self, ponto1: Ponto, ponto2: Ponto):
        self.__ponto1 = ponto1
        self.__ponto2 = ponto2

    @property
    def ponto1(self):
        return self.__ponto1
    
    @property
    def ponto2(self):
        return self.__ponto2
    
    def __str__(self):
        return f'1º Ponto:\n{self.__ponto1}\n2º Ponto:\n{self.__ponto2}'
    
ponto1 = Ponto(2, 5)
ponto2 = Ponto(3, 6)

reta1 = Reta(ponto1, ponto2)
reta2 = Reta((7, 8), (8, 6))

print(ponto1)
print(ponto2)

print(reta1)
print(reta2)

# QUESTÃO 5. Complete o código abaixo, de forma a termos um polimorfismo com 2 métodos
# polimórficos implementados na classe ControleDeAnimais. CadastrarAnimais é
# responsável por cadastrar todos os tipos de animais. EmiteSonsDosAnimais é
# responsável por imprimir todos dos sons dos animais cadastrados. 

# RESPOSTA:

print('\nQUESTÃO 5:\n')

class Animal:
    def __init__(self, nome):
        self._nome = nome

    def emitir_som(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome, raca):
        self.__raca = raca
        super().__init__(nome)

    @property
    def raca(self):
        return self.__raca
    
    def emitir_som(self):
        print(f'O cachorro {self._nome} late!')

class Gato(Animal):
    def __init__(self, nome, raca):
        self.__raca = raca
        super().__init__(nome)

    @property
    def raca(self):
        return self.__raca
    
    def emitir_som(self):
        print(f'O gato {self._nome} mia!')

def fazer_barulho(animal: Animal):
    animal.emitir_som()

class ControleDeAnimais:
    def __init__(self, nome):
        self.__nome = nome
        self.__lista_de_animais = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def lista_de_animais(self):
        return self.__lista_de_animais
    
    def cadastrar_animais(self, animal: Animal):
        self.__lista_de_animais.append(animal)

    def emite_sons_dos_animais(self):
        for n in self.lista_de_animais:
            fazer_barulho(n)

animal_1 = Gato('Jorge', 'Vira-lata')
animal_2 = Gato('Marcelo', 'Spynhix')
animal_3 = Cachorro('Rex', 'Vira-lata')
animal_4 = Cachorro('Max', 'Doberman')

controle_de_animais = ControleDeAnimais('Zoo')

controle_de_animais.cadastrar_animais(animal_1)
controle_de_animais.cadastrar_animais(animal_2)
controle_de_animais.cadastrar_animais(animal_3)
controle_de_animais.cadastrar_animais(animal_4)

controle_de_animais.emite_sons_dos_animais()