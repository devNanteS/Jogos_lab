import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = 'super_secret_key_for_games'



class BatalhaNaval:
    def __init__(self, tamanho=10, navios=5):
        self.tamanho = tamanho
        self.tabuleiro = [['-' for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.navios = navios
        self.posicoes_navios = set()
        self._colocar_navios()
        self.acertos = 0
        self.historico_jogadas = [] #

    def _colocar_navios(self):
        while len(self.posicoes_navios) < self.navios:
            linha = random.randint(0, self.tamanho - 1)
            coluna = random.randint(0, self.tamanho - 1)
            self.posicoes_navios.add((linha, coluna))

    def fazer_jogada(self, linha, coluna):
        
        if not (0 <= linha < self.tamanho and 0 <= coluna < self.tamanho):
            return "Fora do tabuleiro! Tente novamente.", False

        if self.tabuleiro[linha][coluna] != '-':
            return "Você já jogou aqui. Tente outro local.", False

        self.historico_jogadas.append(f"Jogada em ({linha + 1},{coluna + 1})")

        if (linha, coluna) in self.posicoes_navios:
            self.tabuleiro[linha][coluna] = 'O' 
            self.acertos += 1
            return "Acertou um navio!", True
        else:
            self.tabuleiro[linha][coluna] = 'A'  
            return "Água!", False

    def jogo_terminado(self):
        return self.acertos == self.navios

    def obter_estado(self):
        return {
            'tabuleiro': self.tabuleiro,
            'tamanho': self.tamanho,
            'navios_restantes': self.navios - self.acertos,
            'mensagem': session.get('batalha_naval_message', ''),
            'historico_jogadas': self.historico_jogadas,
            'jogo_terminado': self.jogo_terminado()
        }

class Hanoi:
    def __init__(self):
        self.torrei = [5, 4, 3, 2, 1]
        self.torrem = []
        self.torref = []
        self.movimentos = 0
        self.mensagem = ""

    def mover_disco(self, torrea_idx, torrep_idx):
        torres = [self.torrei, self.torrem, self.torref]

        if not (0 <= torrea_idx < 3 and 0 <= torrep_idx < 3):
            self.mensagem = "Índice de torre inválido. Use 1, 2 ou 3."
            return

        origem = torres[torrea_idx]
        destino = torres[torrep_idx]

        if not origem:
            self.mensagem = "A torre de origem está vazia, escolha outra."
            return

        disco = origem.pop()
        if not destino or destino[-1] > disco:
            destino.append(disco)
            self.movimentos += 1
            self.mensagem = "" # Limpa a mensagem de erro
        else:
            self.mensagem = "Escolha um disco menor para movimentar."
            origem.append(disco) # Retorna o disco para a origem

    def vitoria(self):
        return self.torref == [5, 4, 3, 2, 1]

    def obter_estado(self):
        return {
            'torre1': list(self.torrei), # Criar cópias para evitar referência direta
            'torre2': list(self.torrem),
            'torre3': list(self.torref),
            'movimentos': self.movimentos,
            'mensagem': self.mensagem,
            'venceu': self.vitoria()
        }

# Forca
class Forca:
    def __init__(self):
        self.palavras = ['python', 'computador', 'programa', 'desenvolvedor', 'algoritmo', 'teclado', 'internet', 'flask', 'jinja', 'web']
        self.palavra = random.choice(self.palavras).upper()
        self.descobertas = ['_' for _ in self.palavra]
        self.tentativas = 6
        self.tentadas = set()
        self.mensagem = ""
        self.jogo_finalizado = False

    def tentar_letra(self, letra):
        letra = letra.upper()

        if len(letra) != 1 or not letra.isalpha():
            self.mensagem = "Entrada inválida. Digite apenas uma letra."
            return False

        if letra in self.tentadas:
            self.mensagem = "Você já tentou essa letra."
            return False

        self.tentadas.add(letra)

        if letra in self.palavra:
            for i, l in enumerate(self.palavra):
                if l == letra:
                    self.descobertas[i] = letra
            self.mensagem = "Boa! Letra correta!"
        else:
            self.tentativas -= 1
            self.mensagem = "Letra incorreta."
        
        self._verificar_fim_de_jogo()
        return True

    def _verificar_fim_de_jogo(self):
        if '_' not in self.descobertas:
            self.mensagem = f"🎉 Parabéns! Você acertou a palavra: {''.join(self.descobertas)}"
            self.jogo_finalizado = True
        elif self.tentativas == 0:
            self.mensagem = f"💀 Você perdeu! A palavra era: {self.palavra}"
            self.jogo_finalizado = True

    def obter_estado(self):
        return {
            'palavra_oculta': ' '.join(self.descobertas),
            'tentadas': ' '.join(sorted(list(self.tentadas))),
            'tentativas_restantes': self.tentativas,
            'mensagem': self.mensagem,
            'jogo_finalizado': self.jogo_finalizado,
            'palavra_revelada': self.palavra if self.jogo_finalizado else None
        }

# Jokempo (Pedra, Papel, Tesoura)
class Jokempo:
    def __init__(self):
        self.opcoes = ['pedra', 'papel', 'tesoura']
        self.resultado = ""
        self.jogador_escolha = ""
        self.computador_escolha = ""

    def jogar(self, jogador_escolha):
        self.jogador_escolha = jogador_escolha.lower()

        if self.jogador_escolha not in self.opcoes:
            self.resultado = "Escolha inválida. Tente novamente."
            return

        self.computador_escolha = random.choice(self.opcoes)
        self.resultado = f"O computador escolheu {self.computador_escolha}!\n"

        if self.jogador_escolha == self.computador_escolha:
            self.resultado += "Empate!"
        elif (self.jogador_escolha == 'pedra' and self.computador_escolha == 'tesoura') or \
             (self.jogador_escolha == 'papel' and self.computador_escolha == 'pedra') or \
             (self.jogador_escolha == 'tesoura' and self.computador_escolha == 'papel'):
            self.resultado += "Você venceu!"
        else:
            self.resultado += "Você perdeu!"

    def obter_estado(self):
        return {
            'opcoes': self.opcoes,
            'jogador_escolha': self.jogador_escolha,
            'computador_escolha': self.computador_escolha,
            'resultado': self.resultado
        }

# Adivinhe o Número
class Numero:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
        self.mensagem = "Tente adivinhar o número entre 1 e 100."
        self.jogo_vencido = False

    def advinhar(self, palpite):
        self.tentativas += 1
        try:
            palpite_int = int(palpite)
            if not (1 <= palpite_int <= 100):
                self.mensagem = "Digite apenas números de 1 a 100."
            elif self.numero_secreto > palpite_int:
                self.mensagem = "Seu número é menor do que o escolhido."
            elif self.numero_secreto < palpite_int:
                self.mensagem = "Seu número é maior do que o escolhido."
            else:
                self.mensagem = f"Você venceu em {self.tentativas} tentativas! O número era {self.numero_secreto}."
                self.jogo_vencido = True
        except ValueError:
            self.mensagem = "Digite apenas números inteiros."

    def obter_estado(self):
        return {
            'mensagem': self.mensagem,
            'tentativas': self.tentativas,
            'jogo_vencido': self.jogo_vencido
        }

# Quiz
class Pergunta:
    def __init__(self, texto, opcoes, resposta):
        self.texto = texto
        self.opcoes = opcoes
        self.resposta = resposta

    def checar_resposta(self, resposta_usuario):
        return resposta_usuario.upper() == self.resposta.upper()

    def para_dict(self):
        return {
            'texto': self.texto,
            'opcoes': self.opcoes
        }

class Quiz:
    def __init__(self):
        self.perguntas = []
        self._carregar_perguntas_padrao()
        random.shuffle(self.perguntas) # Embaralha as perguntas
        self.pontuacao = 0
        self.indice_pergunta_atual = 0
        self.mensagem = ""
        self.quiz_finalizado = False

    def _carregar_perguntas_padrao(self):
        self.perguntas.append(Pergunta(
            "Quem é o desgosto do pai?",
            ["A) Matheu", "B) Leo", "C) Pietro", "D) Fabrizio"],
            "D"
        ))
        self.perguntas.append(Pergunta(
            "Quais são o menor e o maior país do mundo?",
            ["A) Vaticano e Rússia", "B) Mônaco e Rússia", "C) Malta e Estados Unidos", "D) Nauru e China"],
            "A"
        ))
        self.perguntas.append(Pergunta(
            "Quantas casas decimais tem o número pi?",
            ["A) Duas", "B) Centenas", "C) Vinte", "D) Milhares", "E) Infinitas"],
            "E" # Corrigido para Infinitas, já que era a resposta correta no arquivo original.
        ))
        self.perguntas.append(Pergunta(
            "Qual é o mínimo de jogadores em cada time numa partida de futebol?",
            ["A) 8", "B) 10", "C) 9", "D) 5", "E) 7"],
            "E"
        ))
        self.perguntas.append(Pergunta(
            "Qual é o país mais novo do mundo?",
            ["A) Timor Leste", "B) Kosovo", "C) Montenegro", "D) Sudão do Sul", "E) Palau"],
            "D"
        ))

    def responder_pergunta(self, resposta_usuario):
        if self.quiz_finalizado:
            self.mensagem = "O quiz já terminou. Inicie um novo quiz."
            return

        pergunta_atual = self.perguntas[self.indice_pergunta_atual]
        if pergunta_atual.checar_resposta(resposta_usuario):
            self.mensagem = "Correta!"
            self.pontuacao += 1
        else:
            self.mensagem = f"Errada! Resposta correta: {pergunta_atual.resposta}"
        
        self.indice_pergunta_atual += 1
        
        if self.indice_pergunta_atual >= len(self.perguntas):
            self.quiz_finalizado = True
            self.mensagem += f"\nPontuação final: {self.pontuacao} de {len(self.perguntas)}"
        
    def obter_estado(self):
        pergunta_atual_dict = None
        if not self.quiz_finalizado:
            pergunta_atual_dict = self.perguntas[self.indice_pergunta_atual].para_dict()
        
        return {
            'pergunta_atual': pergunta_atual_dict,
            'pontuacao': self.pontuacao,
            'total_perguntas': len(self.perguntas),
            'mensagem': self.mensagem,
            'quiz_finalizado': self.quiz_finalizado
        }

# --- Rotas do Flask ---

@app.route('/')
def index():

    return render_template('carrosel.html')

# --- Rotas para Batalha Naval ---
@app.route('/batalha_naval', methods=['GET', 'POST'])
def batalha_naval():
    # Inicializa o jogo na sessão se não existir ou se for uma nova partida
    if 'batalha_naval_game' not in session or request.args.get('novo_jogo'):
        game = BatalhaNaval()
        session['batalha_naval_game'] = game.__dict__ # Armazena o __dict__ para persistir o estado
        session['batalha_naval_message'] = "Bem-vindo ao Batalha Naval! Tente encontrar todos os navios."
    else:
        # Recupera o estado do jogo da sessão
        game_state = session['batalha_naval_game']
        game = BatalhaNaval()
        game.__dict__.update(game_state)

    if request.method == 'POST':
        try:
            linha = int(request.form['linha']) - 1
            coluna = int(request.form['coluna']) - 1
            message, _ = game.fazer_jogada(linha, coluna)
            session['batalha_naval_message'] = message
            session['batalha_naval_game'] = game.__dict__
        except ValueError:
            session['batalha_naval_message'] = "Entrada inválida. Por favor, insira números."
        except KeyError:
            session['batalha_naval_message'] = "Erro: linha e coluna devem ser fornecidas."

    return render_template('batalha_naval.html', game_state=game.obter_estado())


@app.route('/hanoi', methods=['GET', 'POST'])
def hanoi():
    if 'hanoi_game' not in session or request.args.get('novo_jogo'):
        game = Hanoi()
        session['hanoi_game'] = game.__dict__
    else:
        game_state = session['hanoi_game']
        game = Hanoi()
        game.__dict__.update(game_state)

    if request.method == 'POST':
        try:
            torre_origem = int(request.form['torre_origem']) - 1
            torre_destino = int(request.form['torre_destino']) - 1
            game.mover_disco(torre_origem, torre_destino)
            session['hanoi_game'] = game.__dict__
        except ValueError:
            game.mensagem = "Entrada inválida. Digite apenas números inteiros."
            session['hanoi_game'] = game.__dict__

    return render_template('hanoi.html', game_state=game.obter_estado())


@app.route('/forca', methods=['GET', 'POST'])
def forca():
    if 'forca_game' not in session or request.args.get('novo_jogo'):
        game = Forca()
        session['forca_game'] = game.__dict__
    else:
        game_state = session['forca_game']
        game = Forca()
        game.__dict__.update(game_state)

    if request.method == 'POST':
        letra = request.form['letra'].strip()
        game.tentar_letra(letra)
        session['forca_game'] = game.__dict__

    return render_template('forca.html', game_state=game.obter_estado())


@app.route('/jokempo', methods=['GET', 'POST'])
def jokempo():
    if 'jokempo_game' not in session or request.args.get('novo_jogo'):
        game = Jokempo()
        session['jokempo_game'] = game.__dict__
    else:
        game_state = session['jokempo_game']
        game = Jokempo()
        game.__dict__.update(game_state)

    if request.method == 'POST':
        escolha_jogador = request.form['escolha'].strip()
        game.jogar(escolha_jogador)
        session['jokempo_game'] = game.__dict__

    return render_template('jokempo.html', game_state=game.obter_estado())

@app.route('/numero', methods=['GET', 'POST'])
def numero():
    if 'numero_game' not in session or request.args.get('novo_jogo'):
        game = Numero()
        session['numero_game'] = game.__dict__
    else:
        game_state = session['numero_game']
        game = Numero()
        game.__dict__.update(game_state)

    if request.method == 'POST':
        palpite = request.form['palpite'].strip()
        game.advinhar(palpite)
        session['numero_game'] = game.__dict__

    return render_template('numero.html', game_state=game.obter_estado())

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'quiz_game' not in session or request.args.get('novo_jogo'):
        game = Quiz()
        session['quiz_game'] = game.__dict__

        session['quiz_game']['perguntas'] = [p.para_dict() for p in game.perguntas]
    else:
        game_state = session['quiz_game']

        game = Quiz()
        game.__dict__.update(game_state)
        game.perguntas = [Pergunta(p['texto'], p['opcoes'], p['resposta']) for p in session['quiz_game']['perguntas']]

        game = Quiz()
        game._carregar_perguntas_padrao()

        game.pontuacao = game_state['pontuacao']
        game.indice_pergunta_atual = game_state['indice_pergunta_atual']
        game.mensagem = game_state['mensagem']
        game.quiz_finalizado = game_state['quiz_finalizado']

        if 'perguntas_serializadas' in session['quiz_game']:
             game.perguntas = [Pergunta(p['texto'], p['opcoes'], p['resposta_correta']) for p in session['quiz_game']['perguntas_serializadas']]
        else:

             pass


    if request.method == 'POST':
        resposta_usuario = request.form['resposta'].strip()
        game.responder_pergunta(resposta_usuario)
        session['quiz_game'] = game.__dict__

        session['quiz_game']['perguntas_serializadas'] = [{'texto': p.texto, 'opcoes': p.opcoes, 'resposta_correta': p.resposta} for p in game.perguntas]

        del session['quiz_game']['perguntas']

        return redirect(url_for('quiz'))

    return render_template('quizz.html', game_state=game.obter_estado())


if __name__ == '__main__':
    app.run(debug=True)