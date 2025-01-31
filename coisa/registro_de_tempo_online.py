class RegistroDeTempoOnline:
    def __init__(self):
        self.tempo_online_esperado = 120

    def __init__(self, nome_da_disciplina, tempo_online_esperado, tempo):
        self.nome_da_disciplina = nome_da_disciplina
        self.tempo_online_esperado = 0
        self.tempo = tempo

    def adiciona_tempo_online(self, tempo):
        self.tempo += tempo

    def atingiu_a_meta(self):
        return self.tempo_online_esperado <= self.tempo

    def __str__(self):
        return f"{self.nome_da_disciplina} {self.tempo}/{self.tempo_online_esperado}"