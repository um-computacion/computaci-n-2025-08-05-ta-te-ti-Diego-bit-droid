from tateti import tateti
def main():
    print('Bienvenidos al tateti')
    juego=tateti()
    while True:
        print("tablero...")
        print(juego.tablero)
        print('Turno del jugador')
              
        fil=input(int('Ingrese fila: '))
        col=input(int('Ingrese columna: '))
        try:
            juego.ocupar_una_de_las_casillas(fil,col)
        except Exception as e:
            print(f'Error: {e}')
            continue
         

if __name__ == "__main__":
    main()