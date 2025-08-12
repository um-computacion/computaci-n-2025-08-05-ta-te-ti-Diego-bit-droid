from clases.tateti import Tateti
from clases.excepciones import PosOcupadaException, PosNoExistenteException




def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()
    while True:
        print("Tablero: filas 0-2, columnas 0-2")
        juego.get_tablero()
        print("Turno: ")
        print(juego.turno)
        try:
            fil = int(input("Ingrese fila: "))
            col = int(input("Ingrese columna: "))
            estado = juego.ocupar_una_de_las_casillas(fil, col)
            if estado == "GANADOR" or estado == "EMPATE":
                break

        except ValueError:
            print("Ingrese solo numeros enteros entre el 0 y 2")
        except PosOcupadaException:
            print("Posicion ocupada")
        except PosNoExistenteException:
            print("Posicion no existe")
        except Exception as e:
            print(e)
    


if __name__ == '__main__':
    main()
