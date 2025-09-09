tamaño = int(input("Ingrese un tamaño de lista: "))

lista = []
i=0
for i in range(tamaño):
    valor = int(input(f"Ingrese el número {i+1}: "))
    lista.append(valor)
print("Ingrese un indice para borrar de la lista")
print("Al indice que desea borrar restele un número")
borrar = int(input("(Si quere borrar el 1 escriba 0): "))
if 0 <= borrar < len(lista):
    lista.pop(borrar)
    print("La lista nueva:", lista)
else:
    print("El indice no existe")