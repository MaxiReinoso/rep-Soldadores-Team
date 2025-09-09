# Escribe un programa que calcule la suma de todos los elementos en una lista 
# bidimensional - Mailen Ortiz

lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0

#El (len(lista)) cuenta la cantidad de filas
#El range(len(lista)) genera una secuencia con la cantidad de listas
#Despues con i y lista[i] pasamos por las distintas listas
#Y con el sum(lista[i]) se suman los valores
i=0
for i in range(len(lista)):
    suma=sum(lista[i])
    print(f"La suma de la fila {i+1}: {suma}")