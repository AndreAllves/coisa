class Disciplina:
    def __init__(self, nome_da_disciplina):
        self.nome_da_disciplina = nome_da_disciplina
        self.horas = 0
        self.notas = []
        self.nota = 0

    def cadastrar_horas(self, horas):
        self.horas = horas

    def cadastra_nota(self, nota, valor_nota):
        self.notas[nota-1] = valor_nota
        self.nota += 1

    def media_nota(self):
        media = 0.0
        soma = 0
        for nota in self.notas:
            soma += nota
        media = soma / len(self.notas)

        return media

    def aprovado(self):
        return self.media_nota() >= 7.0

    def __str__(self):
        return f'{self.nome_da_disciplina} {self.horas} {self.media_nota()} {self.notas}'

