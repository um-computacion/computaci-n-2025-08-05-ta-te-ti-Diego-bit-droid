class tablero:
    def __init__(self):
        self.tablero=(["","",""],
                      ["","",""],
                      ["","",""])

    def colocar_ficha(self,fila,columna,ficha):
        if self.tablero[fila][columna]=="":
            self.tablero[fila][columna]=ficha
            return True
        else:
            raise PosOcupadaError("La posicion ya esta ocupada")


