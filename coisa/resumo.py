class Resumo:
    def __init__(self, nome, numero_de_resumos):
        self.numero_de_resumos = 0
        self.temas = []
        self.resumos = []
        self.i = 0

    def adicina(self, tema, resumo):
        posicao = self.i % self.numero_de_resumos
        self.temas[posicao] = tema
        self.resumos[posicao] = resumo
        self.i += 1

    def pega_resumo(self):
        out = []
        resumos_validos = self.conta()

        for i in range(0, resumos_validos):
            out[i] = self.temas[i] + " | " + self.resumos[i]

        return out

    def impreme_resumos(self):
        total_de_resumos = self.conta()
        out = f'- {total_de_resumos} resumo(s) cadastrado(s)\n'

        for i in range(0, total_de_resumos):
            out += self.temas[i] + ' | ' + self.resumos[i] + '\n'

        return out

    def conta(self):
        return self.i if self.i < self.numero_de_resumos else self.numero_de_resumos

    def tem_resumo(self, tema):
        total_de_resumos = self.conta()
        for i in range(0, total_de_resumos):
            if tema == self.temas[i]:
                return True
        return False