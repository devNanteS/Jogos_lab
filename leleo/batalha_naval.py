import random

class BatalhaNaval:
    def __init__(self):
        self.tamanho = 10  
        self.tabuleiro = [['-' for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.navios = 5
        self.posicoes_navios = set() 
        self.colocar_navios()

    def colocar_navios(self):
        while len(self.posicoes_navios) < self.navios:
            linha = random.randint(0, self.tamanho - 1)
            coluna = random.randint(0, self.tamanho - 1)
            self.posicoes_navios.add((linha, coluna))

    def mostrar_tabuleiro(self):
        for linha in self.tabuleiro:
            print(' '.join(linha))

    def jogar(self):
        print("\nBem-vindo ao Batalha Naval")
        print(f"O tabuleiro é {self.tamanho}x{self.tamanho} e há {self.navios} navios escondidos.\n")

        acertos = 0

        while acertos < self.navios:
            self.mostrar_tabuleiro()

            try:
                linha = int(input(f"\nDigite a linha (1 a {self.tamanho}): ")) - 1
                coluna = int(input(f"Digite a coluna (1 a {self.tamanho}): ")) - 1

                if linha < 0 or linha >= self.tamanho or coluna < 0 or coluna >= self.tamanho:
                    print("Fora do tabuleiro! Tente novamente.")
                    continue

                if self.tabuleiro[linha][coluna] != '-':
                    print("Você já jogou aqui. Tente outro local.")
                    continue

                if (linha, coluna) in self.posicoes_navios:
                    print("Acertou um navio!")
                    self.tabuleiro[linha][coluna] = 'O'
                    acertos += 1
                else:
                    print("Água!")
                    self.tabuleiro[linha][coluna] = 'A'

            except ValueError:
                print("Digite números válidos.")
                continue

        print("\nParabéns! Você destruiu todos os navios!")
        self.mostrar_tabuleiro()

jogo = BatalhaNaval()
jogo.jogar()