from vivienda import Vivienda

class Barrio:
    def __init__(self, nombre: str, empresaConstructora: str):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []  # lista de objetos Vivienda

    def agregarVivienda(self, vivienda: Vivienda):
        """Agrega una vivienda al barrio"""
        self.viviendas.append(vivienda)

    def getSuperficieTotalTerreno(self) -> float:
        """Suma la superficie de terreno de todas las viviendas del barrio"""
        return sum(v.superficieTerreno for v in self.viviendas)

    def getSuperficieTotalTerrenoXManzana(self, manzana: str) -> float:
        """Suma la superficie de terreno de todas las viviendas de una manzana específica"""
        return sum(v.superficieTerreno for v in self.viviendas if v.manzana == manzana)

    def getSuperficieTotalCubierta(self) -> float:
        """Suma los metros cuadrados cubiertos de todas las viviendas del barrio"""
        total_cubierto = 0
        for v in self.viviendas:
            try:
                total_cubierto += v.getMetrosCuadradosCubiertos()
            except Exception as e:
                print(f"[Advertencia] En la vivienda {v.calle} {v.numero}: {e}")
        return total_cubierto
