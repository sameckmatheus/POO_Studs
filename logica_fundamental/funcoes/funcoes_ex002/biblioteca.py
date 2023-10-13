def menu(escolha_operacao, n1, n2):
    while True:
        if escolha_operacao == '1':
            somar(n1, n2)
        elif escolha_operacao == '2':
            subtrair(n1, n2)
        elif escolha_operacao == '3':
            multiplicar(n1, n2)
        elif escolha_operacao == '4':
            dividir(n1, n2)
        elif escolha_operacao == 'S' or escolha_operacao == 's':
            print('Obrigado por utilizar nosso programa...')
            break
        else:
            print('Entrada inválida para a execução do programa...')


def somar(n1, n2):
    soma = n1 + n2
    print(f'A soma entre {n1} e {n2}, é: {soma}')


def subtrair(n1, n2):
    sub = n1 - n2
    print(f'A subtração entre {n1} e {n2}, é: {sub}')


def multiplicar(n1, n2):
    multi = n1 * n2
    print(f'A multiplicação entre {n1} e {n2}, é: {multi}')


def dividir(n1, n2):
    div = n1 / n2
    print(f'A divisão entre {n1} e {n2}, é: {div}')
