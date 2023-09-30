import numpy as np
import pandas as pd

class DesempenhoAcademico:

    def __init__(self, aluno="Matheus Sameck", falta=10):
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
        if self.media >= 70 and self.falta <= 15:
            self.situacao = "Aprovado"
        elif 50 <= self.media < 70 and self.falta <= 15:
            self.situacao = "Exame final"
        elif self.media < 50 or self.falta > 15:
            self.situacao = "Reprovado"
        else:
            self.situacao = "Informações inválidas"
        return self.situacao

    def imprimir_historico(self):
        """Imprimir o histórico do aluno em um formato tabular."""
        print("Histórico do Aluno:", self.nome_aluno)

        df = pd.DataFrame({"Nota": self.notas})
        df["Número"] = df.index + 1
        df = df[["Número", "Nota"]]

        print(df.to_string(index=False))

        print(f"Média: {self.media:.2f}")
        print(f"Situação: {self.situacao}")


desempenho = DesempenhoAcademico()
desempenho.adicionar_nota(9)
desempenho.adicionar_nota(6)
media_atual = desempenho.calcular_media()
situacao_atual = desempenho.situacao_aluno()
desempenho.imprimir_historico()
