from modelos.producto import Producto

# Clase hija Bebida
class Bebida(Producto):
    def __init__(self, nombre, precio, volumen_ml, disponible=True):
        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml

    # Sobrescribe el método de la clase padre
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        print("=== BEBIDA ===")
        print("Nombre:", self.nombre)
        print("Precio: $", self.obtener_precio())
        print("Volumen:", self.volumen_ml, "ml")
        print("Estado:", estado)
        print("-" * 30)