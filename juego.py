from cartas import *

class juego:
    def __init__(self):
        self.mazo = Mazo()
        self.casa = Mazo(True)
        self.jugador = Mazo(True)
    
    def iniciar_juego(self):
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
    
    def mostrar_juego(self, turno_jugador = False, final = False):
        if turno_jugador:
            if final:
                print("Tu mazo final es: ")
                self.jugador.mostrar_cartas(True)
            else:
                print("Tu juego actual es:\n? ?")
                self.jugador.mostrar_cartas()
        else:
            self.casa.mostrar_cartas()
        
    def seguir_juego(self, seguir = True):
        while seguir:
            self.mostrar_juego(True)
            respuesta = input("¿Quieres seguir jugando? (s/n)\n")
            if respuesta == "s" and self.jugador.dar_valor() <= 21:
                self.jugador.agregar_carta(self.mazo.dar_carta())
            else:
                seguir = False
                self.mostrar_juego(True, True)

    
    def razon(self, razon):
        if self.jugador.dar_valor() > 21:
            return razon  