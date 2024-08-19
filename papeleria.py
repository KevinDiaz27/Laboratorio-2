#Creamos la clase Cuaderno
class Cuaderno:
    # Estos son sus atributos
    marca = "HOJITAS"
    tipo = ""
    precio_compra = "" 

    # Creamos sus metodos
    def __init__(self, tipo, precio_compra):
        self.tipo = tipo  
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
    # con este metodo calculamos el precio por el 1.30    
    def calcular_precio_venta(self):
        return self.precio_compra * 1.30
    
    #Mostramos la informacion
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")

#Creamos la clase Lapiz
class Lapiz:
    #sus atributos
    marca = "RAYAS"
    tipo = ""
    precio_compra = ""
    #Sus metodos
    def __init__(self, tipo, precio_compra):
        self.tipo = tipo  
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.30

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")


cuaderno1 = Cuaderno("50 hojas", 2.50)
cuaderno2 = Cuaderno("100 hojas", 4.00)
lapiz1 = Lapiz("Grafito", 0.50)
lapiz2 = Lapiz("Colores", 1.00)





Elegir = int(input("seleccione el tipo de cuaderno que quiere /n ¿50 o 100 pag?"))

if Elegir == 50:
    #cuaderno1 = Cuaderno("50 hojas", 2.50)
    cuaderno1.mostrar_informacion()

elif Elegir == 100:
    #cuaderno2 = Cuaderno("100 hojas", 4.00)
    cuaderno2.mostrar_informacion()
else:
    print("opcion invalida")


Elegir2 = input("seleccione que tipo de lapicero desea n/ ¿Grafito o de colores?")

if Elegir2 == "Grafito" or Elegir2 == "grafito":
    #lapiz1 = Lapiz("Grafito", 0.50)
    lapiz1.mostrar_informacion()

elif Elegir2 == "Colores" or Elegir2 == "colores":
    #lapiz2 = Lapiz("Colores", 1.00)
    lapiz2.mostrar_informacion()
else:
    print("opcion invalida")