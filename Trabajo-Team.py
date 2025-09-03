# =========================
# Archivo de ejercicios - Rama de GitHub
# Cada sección corresponde a un integrante del grupo
# =========================

# 1. Maximiliano Méndez
# ---------------------------------

# ---------------------------------


# 2. Mailén Ortiz
# ---------------------------------

# ---------------------------------


# 3. Nicolás Ibañez
# ---------------------------------

# ---------------------------------


# 4. Lautaro Fernández
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 5. Maximiliano Reinoso
# ---------------------------------
oracion = input("Ingrese una oración: ")

print (oracion.replace(" ",""))
# ---------------------------------


# 6. Maximiliano Méndez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 7. Mailén Ortiz
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 8. Nicolás Ibañez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 9. Lautaro Fernández
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 10. Maximiliano Reinoso
# ---------------------------------
oracion = input("Ingrese una oración: ")
print("Elija a que quiere convertir el texto")
opcion = int(input("1)Mayusculas 2)Minusculas: "))

if opcion == 1:
    print(oracion.upper())
elif opcion ==2:
    print(oracion.lower())
else:
    print("Elija un numero entre las opciones")
# ---------------------------------


# 11. Maximiliano Méndez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 12. Mailén Ortiz
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 13. Nicolás Ibañez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 14. Lautaro Fernández
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 15. Maximiliano Reinoso
# ---------------------------------
x = None 
print(x)
#Al ejecutar imprime "None"
#None es un "valor" que se le asigna a una variable, este valor esta vacio, no tiene nada y por ende si ejecutamos en vez de dar 0 dice none
#Sirve para inicializar variables antes de asignarle un valor real como en el ejemplo a comtinuacion

#Inicializo variable
num = None

#Ingreso valor
num = int(input("Ingrese su edad: "))

#Muestro numero
print(num)
# ---------------------------------


# 16. Maximiliano Méndez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 17. Mailén Ortiz
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 18. Nicolás Ibañez
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 19. Lautaro Fernández
# ---------------------------------
# Escribí tu código acá
# ---------------------------------


# 20. Maximiliano Reinoso
# ---------------------------------
#Fracción
class fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    def sumar(self, f2):
        num= self.numerador * f2.denominador + f2.numerador * self.denominador
        den= self.denominador * f2.denominador
        return fraccion(num, den)
    
    def resta(self, f2):
        num= self.numerador * f2.denominador - f2.numerador * self.denominador
        den= self.denominador * f2.denominador
        return fraccion(num, den)
    
    def multiplicar(self, f2):
        num= self.numerador * f2.numerador
        den = self.denominador * f2.denominador
        return fraccion(num, den)
    
    def dividir(self, f2):
        num= self.numerador * f2.denominador
        den= self. denominador * f2.numerador
        return fraccion(num, den)
    
#Codigo principal

#fraccion 1
num1 = int(input("Ingrese el numerador de la primera fracción: "))
den1 = int(input("Ingrese el denominador de la primera fracción: "))
#fraccion 2
num2 = int(input("Ingrese el numerador de la segunda fracción: "))
den2 = int(input("Ingrese el denominador de la segunda fracción: "))

f1 = fraccion(num1, den1)
f2 = fraccion(num2, den2)

suma= f1.sumar(f2)
resta= f1.resta(f2)
multiplicacion= f1.multiplicar(f2)
division= f1.dividir(f2)

print(f"La suma de ambas fracciones es: {suma}")
print(f"La resta de ambas fracciones es: {resta}")
print(f"La multiplicacion de ambas fracciones es: {multiplicacion}")
print(f"La division de ambas fracciones es: {division}")
# ---------------------------------
