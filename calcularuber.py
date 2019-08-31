class Calcularuber:
    distancia = float
    tempo = float
    uberx_distancia = 0.90
    uberx_tempo = 0.10

    def uber_x(self, distancia,tempo):
        self.uber_x = ((distancia * 0.90) + (0.10 * tempo)) + 1.88
        return self.uber_x


    def uber_select(self,distancia,tempo):
        self.uber_select = ((distancia * 0.90) + (0.10 * tempo)) + 2.10
        return self.uber_select


    def uber_vip(self,distancia, tempo):
        self.uber_vip = ((distancia * 0.90) + (0.10 * tempo)) + 1.88
        return self.uber_vip
