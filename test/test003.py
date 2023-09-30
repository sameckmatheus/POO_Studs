class Calculadora:

    def __init__(self, somar, dividir, multiplicar, subtrair):
        self.somar = somar
        self.subtrair = subtrair
        self.multiplicar = multiplicar
        self.dividir = dividir
        self.a = 0
        self.b = 0

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


resultado = Calculadora()

res_soma = resultado.CalcularSoma()
res_subtracao = resultado.CalcularSubtracao()
res_multiplicacao = resultado.CalcularMultiplicacao()
res_divisao = resultado.CalcularDivisao()
