class Hanoi:
    def __init__(self):
        self.torrei = [5, 4, 3, 2, 1]
        self.torrem = []
        self.torref = []

    def mostrar_torres(self):
        print(f"Torre 1: {self.torrei}")
        print(f"Torre 2: {self.torrem}")
        print(f"Torre 3: {self.torref}")

    def mover_disco(self, torrea, torrep):
        torres = [self.torrei, self.torrem, self.torref]
        if torrea < 1 or torrea > 3 or torrep < 1 or torrep > 3:
            print("Inválido, digite um número de 1 a 3")
        else:
            origem = torres[torrea - 1]
            destino = torres[torrep - 1]
            if not origem:
                print("A torre de origem está vazia, escolha outra.")
            elif origem:
                disco = origem.pop()
                if not destino or destino[-1] > disco:
                    destino.append(disco)
                else:
                    print("Escolha um disco menor para movimentar.")
                    origem.append(disco)

    def vitoria(self):
        return self.torref == [5, 4, 3, 2, 1]

    def jogar(self):
        while True:
            self.mostrar_torres()
            try:
                torrea = int(input("Digite o movimento, dizendo de qual torre você quer retirar:"))
                torrep = int(input("Digite a torre que deseja colocar :"))
            except ValueError:
                print("Digite apenas números de 1 a 3.")
                continue
            self.mover_disco(torrea, torrep)
            if self.vitoria():
                print("Você venceu!")
                break


jogo = Hanoi()
jogo.jogar()
