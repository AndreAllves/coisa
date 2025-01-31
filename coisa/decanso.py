class Decanso:
    def __init__(self, status, horas_de_descanso, semanas_de_descanso):
        self.status = 'cansado'
        self._horas_de_descanso = horas_de_descanso
        self._semanas_de_descanso = semanas_de_descanso

    def define_horas_de_descanso(self, valor):
        self._horas_de_descanso = valor

    def define_semanas_de_descanso(self, valor):
        self._semanas_de_descanso = valor

    def get_status_geral(self):
        self.status = "descansado" if self._semanas_de_descanso >= 1 and (self._horas_de_descanso/self._semanas_de_descanso) >= 26 else "cansado"
        return self.status