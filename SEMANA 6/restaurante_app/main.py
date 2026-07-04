from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

# Crear el restaurante
restaurante = Restaurante()

# Crear platillos
platillo1 = Platillo("Arroz con Pollo", 5.50, 650)
platillo2 = Platillo("Seco de Carne", 6.75, 720)

# Crear bebidas
bebida1 = Bebida("Jugo de Naranja", 2.00, 500)
bebida2 = Bebida("Gaseosa", 1.50, 355)

# Agregar productos al restaurante
restaurante.agregar_producto(platillo1)
restaurante.agregar_producto(platillo2)
restaurante.agregar_producto(bebida1)
restaurante.agregar_producto(bebida2)

# Cambiar el precio de un producto
platillo1.cambiar_precio(6.00)

# Mostrar todos los productos
restaurante.mostrar_productos()