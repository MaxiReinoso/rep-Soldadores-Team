tamaño = int(input("Ingrese el tamaño de la matriz inversa: "))
matriz = []
i=0
while i < tamaño:
    fila =[]
    j=0
    while j < tamaño:
        if j == tamaño - 1 - i :
            fila.append(1)
        else:
            fila.append(0)
        j = j + 1
    matriz.append(fila)
    i = i + 1

for fila in matriz:
    print(fila)