class Calculadora:

    def __init__(self, somar, dividir, multiplicar, subtrair):
        self.somar = somar
        self.subtrair = subtrair
        self.multiplicar = multiplicar
        self.dividir = dividir

    def CalcularSoma(self):
        self.somar = self.a + self.b
        return self.somar

    def CalcularSubtracao(self):
        self.subtrair = self.a - self.b
        return self.subtrair

    def CalcularMultiplicacao(self):
        self.multiplicar = self.a * self.b
        return self.multiplicar

    def CalcularDivisao(self):
        self.dividir = self.a / self.b
        return self.dividir

    def ImprimindoNaTela(self):
        print(f'O resultado da soma, é: {self.somar}')

    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Recebendo entrada do usuário
    escolha = input("Digite a opção (1/2/3/4): ")

    # Candor se a entrada é válida
    if escolha in ('1', '2', '3', '4'):
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(a, "+", b, "=", CalcularSoma())
        elif escolha == '2':
            print(a, "-", b, "=", CalcularSubtracao())
        elif escolha == '3':
            print(a, "*", b, "=", CalcularMultiplicacao())
        elif escolha == '4':
            print(a, "/", b, "=", CalcularDivisao())
    else:
        print("Opção inválida")


resultado = Calculadora(somar=1, subtrair=2, multiplicar=3, dividir=4)

res_soma = resultado.CalcularSoma()
res_subtracao = resultado.CalcularSubtracao()
res_multiplicacao = resultado.CalcularMultiplicacao()
res_divisao = resultado.CalcularDivisao()
