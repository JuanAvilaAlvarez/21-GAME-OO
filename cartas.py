class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def def_valor(self):
        if self.valor in ['J', 'Q', 'K']:
            return 10
        if self.valor == 'A':
            return 1
        return int(self.valor)
    
class Mazo:
    def __init__(self, jugador = False):
        if jugador:
            self.cartas = []
        else:
            self.cartas = [Carta(v,p)
                           for v in ['A', 'J', 'Q', 'K']+[str(x) for x in range(1,11)]
                           for p in ['picas', 'treboles', 'corazones', 'diamantes']]

    
#if __name__ == '__main__':
#   c = Carta()