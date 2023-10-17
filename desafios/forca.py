import random

name_art = (r"""
 ######   #####   ######     ####     ###
 ##      ##   ##  ###  ##   ##  ##   ## ##
 ##      ##   ##  ##   ##  ##       ##   ##
 #####   ##   ##  ##  ##   ##       ##   ##
 ##      ##   ##  #####    ##       #######
 ##      ##   ##  ## ###    ##  ##  ##   ##
 ##       #####   ##  ###    ####   ##   ##
""")
print(name_art)


class Forca:
    def __init__(self):
        self.palavras = ['python', 'java', 'javascript', 'ruby', 'html', 'css', 'php', 'swift']
        self.palavra_secreta = ""
        self.erros = 0
        self.acertos = 0
        self.fim = False
        self.letras_corretas = []
        self.letras_erradas = []

    def definir_palavra_secreta(self):
        self.palavra_secreta = random.choice(self.palavras).lower()
        self.letras_corretas = ["_" for _ in self.palavra_secreta]

    def verificar_chute(self, chutes):
        if len(chutes) == 1 and chutes.isalpha() and chutes.islower():
            if chutes in self.letras_corretas:
                return "Você já tentou essa letra antes!"
            if chutes in self.letras_erradas:
                return "Você já tentou essa letra antes e errou!"
            if chutes in self.palavra_secreta:
                for i, letra in enumerate(self.palavra_secreta):
                    if letra == chutes:
                        self.letras_corretas[i] = chutes
                        self.acertos += 1
                if self.acertos == len(self.palavra_secreta):
                    self.fim = True
                    return ("Parabéns, você venceu!..."
                            f" A palavra era {self.palavra_secreta}")
            else:
                self.letras_erradas.append(chutes)
                self.erros += 1
                if self.erros >= 6:
                    self.fim = True
                    return f"Infelizmente, você perdeu... a palavra era: {self.palavra_secreta}"
        else:
            return "Por favor, digite apenas uma letra minúscula válida."

    def desenhar_forca(self):
        if self.erros == 0:
            return """
           _____ 
           |   |
           |
           |
           |
           |
        ___|___
        """
        elif self.erros == 1:
            return """
           _____ 
           |   |
           |   O
           |
           |
           |
        ___|___
        """
        elif self.erros == 2:
            return """
           _____ 
           |   |
           |   O
           |   |
           |
           |
        ___|___
        """
        elif self.erros == 3:
            return """
           _____ 
           |   |
           |   O
           |  /|
           |
           |
        ___|___
        """
        elif self.erros == 4:
            return """
           _____ 
           |   |
           |   O
           |  /|\
           |
           |
        ___|___
        """
        elif self.erros == 5:
            return """
           _____ 
           |   |
           |   O
           |  /|\
           |  /
           |
        ___|___
        """
        else:
            return """
           _____ 
           |   |
           |   O
           |  /|\
           |  / \
           |
        ___|___
        """


forca = Forca()
forca.definir_palavra_secreta()

while not forca.fim:
    print("Palavra: " + " ".join(forca.letras_corretas))
    print("Letras erradas: " + ", ".join(forca.letras_erradas))
    print(forca.desenhar_forca())
    chute = input('Digite uma letra: ').lower()
    resultado = forca.verificar_chute(chute)
    if resultado:
        print(resultado)
        break