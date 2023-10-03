import numpy as np
import pandas as pd

class DesempenhoAcademico:

    def __init__(self, aluno=input('Digite seu nome: '), falta=int(input('Digite a quantidade de faltas: '))):
        """Inicializar os atributos da classe."""
        self.nome_aluno = aluno
        self.notas = np.array([])
        self.falta = falta
        self.media = 0
        self.situacao = ""

    def adicionar_nota(self, nota):
        """Adicionar uma nota ao array de notas."""
        self.notas = np.append(self.notas, nota)

    def calcular_media(self):
        """Calcular a média das notas."""
        if len(self.notas) == 0:
            return 0
        self.media = np.mean(self.notas)
        return self.media

    def situacao_aluno(self):
        """Determinar a situação do aluno de acordo com a média e as faltas."""
        if self.media >= 7 and self.falta <= 15:
            if self.media > 10:
                self.situacao = "Informações inválidas"
            else:
                self.situacao = "Aprovado"
        elif self.media >= 5:
            if self.media <= 7 and self.falta <= 15:
                self.situacao = "Exame final"
        elif self.media < 5 or self.falta > 15:
            self.situacao = "Reprovado"
        return self.situacao

    def imprimir_pontuacao(self):
        """Imprimir o histórico do aluno em um formato tabular."""
        print('\n'
              '============================================')
        print("Boletim Escolar")
        print("Pontuação do Aluno:", self.nome_aluno)
        print('============================================')
        df = pd.DataFrame({"Nota": self.notas})
        df["Número"] = df.index + 1
        df = df[["Número", "Nota"]]

        print(df.to_string(index=False))

        print(f"Média: {self.media:.2f}")
        print(f"Situação: {self.situacao}")
        print('============================================')


desempenho = DesempenhoAcademico()

desempenho.adicionar_nota(float(input('Digite a nota 1: ')))
desempenho.adicionar_nota(float(input('Digite a nota 2: ')))
desempenho.adicionar_nota(float(input('Digite a nota 3: ')))
desempenho.adicionar_nota(float(input('Digite a nota 4: ')))

media_atual = desempenho.calcular_media()
situacao_atual = desempenho.situacao_aluno()

desempenho.imprimir_pontuacao()
