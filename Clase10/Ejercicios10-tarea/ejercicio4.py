class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def aumentar_cantidad(self, cantidad):
        self.cantidad += cantidad
        print(f"Se han añadido {cantidad} unidades de {self.nombre}.")

    def disminuir_cantidad(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
            print(f"Se han retirado {cantidad} unidades de {self.nombre}.")
        else:
            print(f"No hay suficientes unidades de {self.nombre} en inventario.")

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Productos en el inventario:")
        for producto in self.productos:
            print(f"- {producto.nombre}: {producto.cantidad} unidades, ${producto.precio} cada una.")

# Ejemplo de uso:
inventario = Inventario()

producto1 = Producto("Manzana", 1.5, 100)
producto2 = Producto("Banana", 0.8, 50)

inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

inventario.mostrar_productos()

# Aumentar y disminuir cantidad de un producto
inventario.productos[0].aumentar_cantidad(50)
inventario.productos[1].disminuir_cantidad(30)

inventario.mostrar_productos()
