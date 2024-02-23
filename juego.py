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
        
    def seguir_juego(self, seguir_j = False, seguir_c = False):
        while seguir_j:
            self.mostrar_juego(True)
            respuesta = input("¿Quieres seguir jugando? (s/n)\n")
            if respuesta == "s" and self.jugador.dar_valor() <= 21:
                self.jugador.agregar_carta(self.mazo.dar_carta())
            else:
                seguir_j = False
                self.mostrar_juego(True, True)
        while seguir_c:
            if self.casa.dar_valor() < self.jugador.dar_valor():
                self.casa.agregar_carta(self.mazo.dar_carta())
            else:
                seguir_c = False
                #self.casa.mostrar_cartas(True)
    
    def concluir(self):
        if self.jugador.dar_valor() > 21:
            print("\n\nTu mazo suma " + str(self.jugador.dar_valor()) + ", perdiste")
        elif self.jugador.dar_valor() > self.casa.dar_valor() and self.jugador.dar_valor() < 21:
            print("\n\nLe has ganado a la casa, tu mazo suma " + str(self.jugador.dar_valor()) + " y el mazo de la casa suma " + str(self.casa.dar_valor()))
        else:
            print("\n\nLa casa te ha ganado, el mazo de esta suma " + str(self.casa.dar_valor()) + " y tu mazo suma " + str(self.jugador.dar_valor()))