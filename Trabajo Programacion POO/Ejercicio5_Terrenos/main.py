from barrio import Barrio
from vivienda import Vivienda
from habitacion import Habitacion

def main():
    # crear barrio
    barrio = Barrio("Los Aromos", "Constructora del Valle S.A.")
    
    # manzana a
    vivienda1 = Vivienda("Calle Los Pinos", 123, "A", 1, 250.0)
    vivienda1.agregarHabitacion(Habitacion("Living", 30.0))
    vivienda1.agregarHabitacion(Habitacion("Cocina", 15.0))
    vivienda1.agregarHabitacion(Habitacion("Dormitorio principal", 20.0))
    vivienda1.agregarHabitacion(Habitacion("Dormitorio secundario", 15.0))
    vivienda1.agregarHabitacion(Habitacion("Baño", 8.0))
    barrio.agregarVivienda(vivienda1)
    
    vivienda2 = Vivienda("Calle Los Pinos", 125, "A", 2, 280.0)
    vivienda2.agregarHabitacion(Habitacion("Living-comedor", 35.0))
    vivienda2.agregarHabitacion(Habitacion("Cocina", 18.0))
    vivienda2.agregarHabitacion(Habitacion("Dormitorio 1", 22.0))
    vivienda2.agregarHabitacion(Habitacion("Dormitorio 2", 18.0))
    vivienda2.agregarHabitacion(Habitacion("Dormitorio 3", 16.0))
    vivienda2.agregarHabitacion(Habitacion("Baño principal", 10.0))
    vivienda2.agregarHabitacion(Habitacion("Baño secundario", 6.0))
    barrio.agregarVivienda(vivienda2)
    
    # manzana b
    vivienda3 = Vivienda("Calle Las Acacias", 456, "B", 1, 300.0)
    vivienda3.agregarHabitacion(Habitacion("Living", 40.0))
    vivienda3.agregarHabitacion(Habitacion("Cocina-comedor", 25.0))
    vivienda3.agregarHabitacion(Habitacion("Dormitorio principal", 25.0))
    vivienda3.agregarHabitacion(Habitacion("Dormitorio 2", 20.0))
    vivienda3.agregarHabitacion(Habitacion("Baño", 12.0))
    vivienda3.agregarHabitacion(Habitacion("Lavadero", 6.0))
    barrio.agregarVivienda(vivienda3)
    
    vivienda4 = Vivienda("Calle Las Acacias", 458, "B", 2, 320.0)
    vivienda4.agregarHabitacion(Habitacion("Living", 32.0))
    vivienda4.agregarHabitacion(Habitacion("Cocina", 20.0))
    vivienda4.agregarHabitacion(Habitacion("Comedor", 18.0))
    vivienda4.agregarHabitacion(Habitacion("Dormitorio 1", 24.0))
    vivienda4.agregarHabitacion(Habitacion("Dormitorio 2", 20.0))
    vivienda4.agregarHabitacion(Habitacion("Dormitorio 3", 18.0))
    vivienda4.agregarHabitacion(Habitacion("Baño 1", 10.0))
    vivienda4.agregarHabitacion(Habitacion("Baño 2", 8.0))
    barrio.agregarVivienda(vivienda4)
    
    # manzana c
    vivienda5 = Vivienda("Calle Los Olivos", 789, "C", 1, 220.0)
    vivienda5.agregarHabitacion(Habitacion("Living-comedor", 28.0))
    vivienda5.agregarHabitacion(Habitacion("Cocina", 14.0))
    vivienda5.agregarHabitacion(Habitacion("Dormitorio 1", 18.0))
    vivienda5.agregarHabitacion(Habitacion("Dormitorio 2", 16.0))
    vivienda5.agregarHabitacion(Habitacion("Baño", 9.0))
    barrio.agregarVivienda(vivienda5)
    
    print(f"Barrio: {barrio.nombre}")
    print(f"Empresa: {barrio.empresaConstructora}")
    print(f"Cantidad de viviendas: {len(barrio.viviendas)}\n")
    
    # ejecutar metodo a
    total = barrio.getSuperficieTotalTerreno()
    print(f"a) Superficie total terreno: {total} m2")
    
    # ejecutar metodo b
    print("\nb) Superficie por manzana:")
    manzanas = ["A", "B", "C"]
    for m in manzanas:
        sup = barrio.getSuperficieTotalTerrenoXManzana(m)
        print(f"   Manzana {m}: {sup} m2")
    
    # ejecutar metodo c para cada vivienda
    print("\nc) Metros cubiertos por vivienda:")
    for i, viv in enumerate(barrio.viviendas, 1):
        try:
            mc = viv.getMetrosCuadradosCubiertos()
            print(f"   Vivienda {i}: {mc} m2")
        except Exception as e:
            print(f"   Vivienda {i}: Error - {e}")
    
    # ejecutar metodo d
    print("\nd) Superficie total cubierta del barrio:")
    totalCubierto = barrio.getSuperficieTotalCubierta()
    print(f"   {totalCubierto} m2")
    
    # calculos extra
    print("\n--- Resumen ---")
    print(f"Total terreno: {total} m2")
    print(f"Total cubierto: {totalCubierto} m2")
    print(f"Sin construir: {total - totalCubierto} m2")

if __name__ == "__main__":
    main()