import numpy as np
import pandas as pd

class DesempenhoAcademico:

    def __init__(self, aluno, falta=10):
        self.nomeAluno = aluno
        self.notas = np.array([])
        self.falta = falta
        self.media = 0
        self.situacao = ""

    def adicionarNota(self, nota):
        self.notas = np.append(self.notas, nota)

    def calcularMedia(self):
        if len(self.notas) == 0:
            return 0
        self.media = np.mean(self.notas)
        return self.media

    def situacaoAluno(self):
        if self.media >= 70 and self.falta <= 15:
            self.situacao = "Aprovado"
        elif 50 <= self.media < 70 and self.falta <= 15:
            self.situacao = "Exame final"
        elif self.notas > 50 and self.falta > 15:
            self.situacao = "Reprovado"
        elif self.notas > 100 or self.notas < 0:
            self.situacao = "Informações inválidas"
        return self.situacao

    def imprimirHistorico(self):
        print("Histórico do Aluno:", self.nomeAluno)

        df = pd.DataFrame({"Nota": self.notas})
        df["Número"] = df.index + 1
        df = df[["Número", "Nota"]]

        print(df.to_string(index=False))

        print(f"Média: {self.media:.2f}")
        print(f"Situação: {self.situacao}")


desempenho = DesempenhoAcademico('Matheus Sameck')
desempenho.adicionarNota(9)
desempenho.adicionarNota(6)

media_atual = desempenho.calcularMedia()
situacao_atual = desempenho.situacaoAluno()
desempenho.imprimirHistorico()
