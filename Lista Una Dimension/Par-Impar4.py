tamaño = int(input("Ingrese un tamaño de lista: "))

numero = []
i=0
for i in range(tamaño):
    valor = int(input(f"Ingrese el número {i+1}: "))
    numero.append(valor)

par = 0
impar = 0
num = 0
for num in numero:
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print(f"En total hay {par} numeros pares")
print(f"En total hay {impar} numeros impares")