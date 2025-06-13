import random

class Jokempo:
    def __init__(self):
        self.opcoes = ['pedra', 'papel', 'tesoura']

    def jogar(self):
        while True:
            jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
            
            if jogador == 'sair':
                print("Jogo encerrado!")
                break
            
            if jogador not in self.opcoes:
                print("Escolha inválida. Tente novamente.")
                continue

            computador = random.choice(self.opcoes)
            print(f"O computador escolheu {computador}!")

            if jogador == computador:
                print("Empate!")
            elif (jogador == 'pedra' and computador == 'tesoura') or \
                 (jogador == 'papel' and computador == 'pedra') or \
                 (jogador == 'tesoura' and computador == 'papel'):
                print("Você venceu!")
            else:
                print("Você perdeu!")

jogo = Jokempo()
jogo.jogar()
        
        
