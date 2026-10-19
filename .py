
def resolver_laberinto():
    laberinto = [
        ['F', 1, 1, 3, 0, 1, 1, 1, 4],
        [3, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 3, 1, 1],
        [3, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 3, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 1, 0, 0, 4],
        ['I', 1, 3, 1, 0, 1, 1, 1, 1]
    ]

    filas = len(laberinto)
    columnas = len(laberinto[0])

    inicio = (8, 0)
    fin = (0, 0)

    movimientos = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    visitados = [[False] * columnas for _ in range(filas)]
    camino = []
    solucion = []

    def valor(celda):
        if celda == 'I' or celda == 'F':
            return 1
        return celda

    def backtracking(fila, columna, puntos):
        nonlocal solucion

        if (fila, columna) == fin:
            if puntos >= 23:
                solucion = camino + [(fila, columna)]
                return True
            return False

        visitados[fila][columna] = True
        camino.append((fila, columna))

        for movimiento in movimientos:
            df = movimiento[0]
            dc = movimiento[1]

            nf = fila + df
            nc = columna + dc

            if 0 <= nf < filas and 0 <= nc < columnas:
                if laberinto[nf][nc] != 0 and not visitados[nf][nc]:
                    nuevos_puntos = puntos + valor(laberinto[nf][nc])

                    if backtracking(nf, nc, nuevos_puntos):
                        return True

        camino.pop()
        visitados[fila][columna] = False

        return False

    puntos_iniciales = valor(laberinto[inicio[0]][inicio[1]])

    exito = backtracking(
        inicio[0],
        inicio[1],
        puntos_iniciales
    )

    print("LABERINTO ORIGINAL")

    for fila in laberinto:
        print(" ".join(str(celda) for celda in fila))

    matriz_solucion = [fila[:] for fila in laberinto]

    if exito:
        puntos_totales = 0

        for posicion in solucion:
            fila = posicion[0]
            columna = posicion[1]

            puntos_totales += valor(laberinto[fila][columna])

            if laberinto[fila][columna] != 'I' and laberinto[fila][columna] != 'F':
                matriz_solucion[fila][columna] = '*'

        print("\nEL RATON LOGRO SALIR DEL LABERINTO")
        print("Puntaje total:", puntos_totales)
        print("Puntaje minimo requerido: 23")
    else:
        print("\nNO SE ENCONTRO UN CAMINO CON 23 PUNTOS O MAS")

    print("\nMATRIZ CON EL CAMINO A SEGUIR")

    for fila in matriz_solucion:
        print(" ".join(str(celda) for celda in fila))


if __name__ == "__main__":
    resolver_laberinto()
