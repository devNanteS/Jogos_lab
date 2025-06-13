from random import shuffle

class Pergunta:
    def __init__(self, texto, opcoes, resposta):
        self.texto = texto
        self.opcoes = opcoes
        self.resposta = resposta

    def exibir(self):
        print("\n" + self.texto)
        for opcao in self.opcoes:
            print(opcao)

    def checar_resposta(self, resposta_usuario):
        return resposta_usuario.upper() == self.resposta


class Quiz:
    def __init__(self):
        self.perguntas = []
        self.pontuacao = 0

    def adicionar_pergunta(self, pergunta):
        self.perguntas.append(pergunta)

    def jogar(self):
        print("  QUIZ  ")
        shuffle(self.perguntas)

        for pergunta in self.perguntas:
            pergunta.exibir()
            resposta = input("Sua resposta: ").upper()

            if pergunta.checar_resposta(resposta):
                print("Correta!")
                self.pontuacao += 1
            else:
                print(f"Errada! Resposta correta: {pergunta.resposta}")

        print(f"\nPontuação final: {self.pontuacao} de {len(self.perguntas)}")


if __name__ == "__main__":
    quiz = Quiz()

    quiz.adicionar_pergunta(Pergunta(
        "Quem é o desgosto do pai?",
        ["A) Matheu", "B) Leo", "C) Pietro", "D) Fabrizio"],
        "D"
    ))

    quiz.adicionar_pergunta(Pergunta(
        "Quais são o menor e o maior país do mundo?",
        ["A) Vaticano e Rússia", "B) Mônaco e Rússia", "C) Malta e Estados Unidos", "D) Nauru e China"],
        "A"
    ))

    quiz.adicionar_pergunta(Pergunta(
        "Quantas casas decimais tem o número pi?",
        ["A) Duas", "B) Centenas", "C) Vinte", "D) Milhares", "E) Infinitas"],
        "C"
    ))

    quiz.adicionar_pergunta(Pergunta(
        "Qual é o mínimo de jogadores em cada time numa partida de futebol?",
        ["A) 8", "B) 10", "C) 9", "D) 5", "E) 7"],
        "E"
    ))

    quiz.adicionar_pergunta(Pergunta(
        "Qual é o país mais novo do mundo?",
        ["A) Timor Leste", "B) Kosovo", "C) Montenegro", "D) Sudão do Sul", "E) Palau"],
        "D"
    ))

    quiz.jogar()