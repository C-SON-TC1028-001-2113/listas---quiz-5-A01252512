def matrizDiagonal(matrix):
    listaDiagonal = []
    for i in range(len(matrix)):
        listaDiagonal.append(matrix[i][i])
    return listaDiagonal


def main():
    
    matriz = []
    renglon = []

    renglones = int(input())
    columnas = int(input())

    if renglones != columnas:
        print('La matriz no es cuadrada')
    else:
        for i in range(renglones):
            renglon = []
            for j in range(columnas):
                dato = int(input())
                renglon.append(dato)
            matriz.append(renglon)
        print(matrizDiagonal(matriz))


if __name__=='__main__':
    main()
