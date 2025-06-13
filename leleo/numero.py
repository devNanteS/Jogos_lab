import random

class Numero:
    def __init__(self):
        self.numero = random.randint(1, 100)

    def advinhar(self):
        while True:
            try:
                anumero = int(input("Tente advinhar o número de 1 - 100: "))
                if anumero < 1 or anumero > 100:
                    print("Digite apenas números de 1 - 100")
                else:
                    if self.numero > anumero:
                        print("Seu número é menor do que o escolhido")
                    elif self.numero < anumero:
                        print("Seu número é maior do que o escolhido")
                    else:
                        print("Você venceu!")
                        break
            except ValueError:
                print("Digite apenas números inteiros.")

jogo = Numero()
jogo.advinhar()