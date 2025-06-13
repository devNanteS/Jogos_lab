import random

def jogar_forca():
    palavras = ['python', 'computador', 'programa', 'desenvolvedor', 'algoritmo', 'teclado', 'internet']
    palavra = random.choice(palavras)  
    descobertas = ['_' for _ in palavra]
    tentativas = 6
    tentadas = set()

    print("  JOGO DA FORCA  ")
    
    while tentativas > 0 and '_' in descobertas:
        print("\nPalavra:", ' '.join(descobertas))
        print("Letras tentadas:", ' '.join(sorted(tentadas)))
        print("Tentativas restantes:", tentativas)
        
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue

        if letra in tentadas:
            print("Você já tentou essa letra.")
            continue

        tentadas.add(letra)

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    descobertas[i] = letra
            print("Boa! Letra correta!")
        else:
            tentativas -= 1
            print("Letra incorreta.")

    if '_' not in descobertas:
        print("\n🎉 Parabéns! Você acertou a palavra:", palavra)
    else:
        print("\n💀 Você perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogar_forca()