class Producto:
    def __init__(self, nombre, marca, precio, imagen):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.imagen = imagen
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_precio(self, precio):
        self.precio = precio

    def set_marca(self, marca):
        self.marca = marca

    def set_imagen(self, imagen):
        self.imagen = imagen

    def get_imagen(self):
        return self.imagen

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio
    
    def get_marca(self):
        return self.marca

class Ropa(Producto):
    def __init__(self, nombre, marca, precio, imagen, color, talla):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.imagen = imagen
        self.color = color
        self.talla = talla
    
    def __str__(self):
        return "Producto {}, Marca {}, Precio {}, Color {}, Talla {}".format(self.nombre, self.marca, self.precio, self.color, self.talla)