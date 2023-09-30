def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero!"


# Interface do usuário
print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Recebendo entrada do usuário
escolha = input("Digite a opção (1/2/3/4): ")

# Candor se a entrada é válida
if escolha in ('1', '2', '3', '4'):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(num1, "+", num2, "=", adicao(num1, num2))

    elif escolha == '2':
        print(num1, "-", num2, "=", subtracao(num1, num2))

    elif escolha == '3':
        print(num1, "*", num2, "=", multiplicacao(num1, num2))

    elif escolha == '4':
        print(num1, "/", num2, "=", divisao(num1, num2))

else:
    print("Opção inválida")
