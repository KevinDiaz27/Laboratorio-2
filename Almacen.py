#Creamos la clase Celular
class Celular:
    def __init__(self, modelo, memoria, ram, precio_compra, megapixeles, gama):
        self.modelo = modelo
        self.memoria = memoria
        self.ram = ram
        self.precio_compra = float(precio_compra)
        self.megapixeles = megapixeles
        self.gama = gama
        self.precio_venta = self.calcular_precio_v()

#Calculamos el precio por el 1.7
    def calcular_precio_v(self):
        return self.precio_compra * 1.7
    #Mostramos la info
    def mostrar_informacion(self):
        print(f"Modelo: {self.modelo}")
        print(f"Memoria: {self.memoria}")
        print(f"RAM: {self.ram} GB")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Megapíxeles: {self.megapixeles}")
        print(f"Gama: {self.gama}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")

#Creamos la clase Tablet
class Tablet:
    def __init__(self, modelo, memoria, ram, precio_compra, megapixeles, gama):
        self.modelo = modelo
        self.memoria = memoria
        self.ram = ram
        self.precio_compra = float(precio_compra)
        self.megapixeles = megapixeles
        self.gama = gama
        self.precio_venta = self.calcular_precio_v()

    def calcular_precio_v(self):
        return self.precio_compra * 1.7
    #Mostramos la informacion
    def mostrar_informacion(self):
        print(f"Modelo: {self.modelo}")
        print(f"Memoria: {self.memoria}")
        print(f"RAM: {self.ram} GB")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Megapíxeles: {self.megapixeles}")
        print(f"Gama: {self.gama}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")

#Creamos la clase portatil
class Portatil:
    def __init__(self, modelo, memoria, ram, precio_compra, tarjeta_grafica, gama):
        self.modelo = modelo
        self.memoria = memoria
        self.ram = ram
        self.precio_compra = float(precio_compra)
        self.tarjeta_grafica = tarjeta_grafica
        self.gama = gama
        self.precio_venta = self.calcular_precio_v()

    def calcular_precio_v(self):
        return self.precio_compra * 1.7
    
    def mostrar_informacion(self):
        print(f"Modelo: {self.modelo}")
        print(f"Memoria: {self.memoria}")
        print(f"RAM: {self.ram} GB")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Tajeta grafica: {self.tarjeta_grafica}")
        print(f"Gama: {self.gama}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")

#Aqui le preguntamos al usuario que dispositivo desea ver
Dispositivo = input("¿que dispositivo desea ver?")
if Dispositivo == "Celular" or Dispositivo == "celular" or Dispositivo == "Telefono" or Dispositivo == "telefono":
    telefono = Celular("Xiaomi", "250 GB", 8, 300, "50 MP", "Gama media")
    telefono.mostrar_informacion()

elif Dispositivo == "Tablet" or Dispositivo == "tablet":
    tablet = Tablet("apple mini", "500 GB", 12, 500, "60 MP", "Gama alta")
    tablet.mostrar_informacion()

elif Dispositivo == "Portatil" or Dispositivo == "portatil" or Dispositivo == "Computadora" or Dispositivo == "computadora":
    portatil = Portatil("Huawei matebook 15", "500 GB", 16, 750, "ryzen 5", "Gama alta")
    portatil.mostrar_informacion()

else:
    print("Opcion invalida")



