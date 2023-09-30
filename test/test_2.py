# Importando as bibliotecas necessárias
import numpy as np
import pandas as pd

class DesempenhoAcademico:

    def _init_(self, aluno):
        self.nomeAluno = aluno
        self.notas = np.array([])
        self.media = 0
        self.situacao = ""

    def adicionarNota(self, nota):
        self.notas = np.append(self.notas, nota)
        
    def calcularMedia(self):
        if len(self.notas) == 0:
            return 0
        self.media = np.mean(self.notas) # Usando o método mean do numpy
        return self.media

    def situacaoAluno(self):
        if self.media >= 7.0:
            self.situacao = "Aprovado por média"
        elif self.media >= 5.0:
            self.situacao = "Aprovado na final"
        else:
            self.situacao = "Reprovado"
        return self.situacao

    def imprimirHistorico(self):
        print("Histórico do Aluno:", self.nomeAluno)
        
        df = pd.DataFrame({"Nota": self.notas})
        df["Número"] = df.index + 1
        df = df[["Número", "Nota"]]
  
        print(df.to_string(index=False))
        
        print(f"Média: {self.media:.2f}")
        print(f"Situação: {self.situacao}")

desempenho = DesempenhoAcademico('Natasha Pelizari')
desempenho.adicionarNota(9)
desempenho.adicionarNota(6)

media_atual = desempenho.calcularMedia()
situacao_atual = desempenho.situacaoAluno()
desempenho.imprimirHistorico()