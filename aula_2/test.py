class DesempenhoAcademico():

 

  def __init__(self, aluno):

    self.nomeAluno = aluno

    self.notas = []

    self.media = 0

    self.situacao = ""

 

  def adicionarNota(self, nota):

    self.notas.append(nota)

 

  def calcularMedia(self):

    if len(self.notas) == 0:

      return 0

    self.media = sum(self.notas) / len(self.notas)

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

    for i, nota in enumerate(self.notas, start=1):

      print(f"Nota {i}: {nota}")

    print(f"Média: {self.media}")

    print(f"Situação: {self.situacao}")

 

 

desempenho = DesempenhoAcademico('Natasha Pelizari')

desempenho.adicionarNota(7)

desempenho.adicionarNota(8)

 

media_atual = desempenho.calcularMedia()

situacao_atual = desempenho.situacaoAluno()

desempenho.imprimirHistorico()

 