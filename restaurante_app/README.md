# Sistema de Gestión de Productos de Restaurante

## Estudiante

**Nombre:** Michael Castillo

## Descripción

Este proyecto fue desarrollado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite registrar y mostrar productos de un restaurante mediante una estructura modular aplicando herencia, encapsulación y polimorfismo.

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
```

## Herencia

La clase **Producto** es la clase padre. Las clases **Platillo** y **Bebida** heredan sus atributos y métodos utilizando `super()`.

## Encapsulación

El atributo `__precio` está encapsulado en la clase `Producto`. Para acceder o modificar su valor se utilizan los métodos:

- `obtener_precio()`
- `cambiar_precio()`

El método `cambiar_precio()` valida que el precio sea mayor que cero.

## Polimorfismo

Las clases `Platillo` y `Bebida` sobrescriben el método `mostrar_informacion()`, mostrando información diferente según el tipo de producto.

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos

## Reflexión

La Programación Orientada a Objetos permite desarrollar aplicaciones más organizadas, reutilizando código mediante la herencia, protegiendo la información con encapsulación y facilitando la extensión del programa mediante el polimorfismo.