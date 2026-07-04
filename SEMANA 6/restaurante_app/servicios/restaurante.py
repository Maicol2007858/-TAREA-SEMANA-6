# Clase que administra los productos del restaurante

class Restaurante:
    def __init__(self):
        # Lista donde se almacenan los productos
        self.productos = []

    # Agregar un producto a la lista
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Mostrar todos los productos (polimorfismo)
    def mostrar_productos(self):
        print("\n===== MENÚ DEL RESTAURANTE =====\n")

        if len(self.productos) == 0:
            print("No hay productos registrados.")
        else:
            for producto in self.productos:
                producto.mostrar_informacion()