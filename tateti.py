from tablero import tablero 
class tateti:
    def __init__(self):
        self.turno='X'
        self.tablero=tablero()
    def ocupar_una_de_las_casillas(self,fila,columna):
        if self.tablero.colocar_ficha(fila,columna,self.turno):
            if self.turno=='X':
                self.turno='0'
            else:
                self.turno='X'
        else:
            print('La casilla ya esta ocupada, intente de nuevo')
