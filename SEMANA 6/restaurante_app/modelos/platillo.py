from modelos.producto import Producto

# Clase hija Platillo
class Platillo(Producto):
    def __init__(self, nombre, precio, calorias, disponible=True):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias

    # Sobrescribe el método de la clase padre
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        print("=== PLATILLO ===")
        print("Nombre:", self.nombre)
        print("Precio: $", self.obtener_precio())
        print("Calorías:", self.calorias)
        print("Estado:", estado)
        print("-" * 30)