class DesempenhoAcademico():

  # Método construtor
  def __init__(self, aluno):
    self.nomeAluno = aluno
    self.media = 0
    self.situacao = False

  # Calcula a média
  def calcularMedia(self, nota1, nota2):
    self.media = (nota1 + nota2) / 2
    if (self.media >= 7.00):
      self.situacao = True
    return self.media

  def calcularMediaAposFinal(self, notaFinal):
    self.media = (self.media + notaFinal) / 2
    if (self.media >= 5.00):
      self.situacao = True
    return self.media

  def situacaoAluno(self):
    if (self.situacao == True and self.media >= 5.00):
      print(f"Aluno {self.nomeAluno} está em situação Aprovado")
    else:
      print(f"Aluno {self.nomeAluno} está em situação Reprovado")


desempenho = DesempenhoAcademico('Natasha Pelizari')
desempenho.calcularMedia(7, 8)
desempenho.situacaoAluno()

"""
Exercício

Os alunos devem incrementar o código com variáveis e métodos, se acharem necessário e, ao final, imprimir na tela todo o histórico do aluno, com todas as notas e médias, inclusive informando se o status do aluno foi: "aprovado por média", "aprovado na final" ou "reprovado". Considerando que a média aritimética para aprovação é 7,0 (sete) e após final 5,0 (cinco).

"""
