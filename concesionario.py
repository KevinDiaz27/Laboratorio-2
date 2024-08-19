#Creamos la clase Carros
class Carro:
    Ruedas = 4
    capacidadP = 5
#Creamos sus metodos
    def __init__(self, modelo, año, color, tipo, precio_compra, combustible, transmision, kilometraje, pais):
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo = tipo
        self.precio_compra = precio_compra
        self.combustible = combustible
        self.transmision = transmision
        self.kilometraje = kilometraje
        self.pais = pais
        self.precio_venta = self.Calcular_precio_v()  
        
# Calculamos el precio de venta

    def Calcular_precio_v(self):
        # Calcular el precio de venta con un margen de ganancia del 40%
        return self.precio_compra * 1.40

    def mostrar_informacion(self):
        # Mostrar la información del carro
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")
        print(f"Combustible: {self.combustible}")
        print(f"Transmisión: {self.transmision}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Origen: {self.pais}")
        print(f"Ruedas: {self.Ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidadP}")

#Aqui le preguntamos al usuario si desea ver un auto nacional o uno importado
TipoAuto = input("Seleccione el tipo de auto que desea ver ¿nacional o importado?")

if TipoAuto == "Importado" or TipoAuto=="importado":
    auto1 = Carro("Toyota Corolla", 2021, "Rojo", "Importado", 20000, "Gasolina", "Automático", 15000, "Japon")
    auto1.mostrar_informacion()
elif TipoAuto == "Nacional" or TipoAuto == "nacional":
    auto2 = Carro("Honda", 2023,"Blanco", "Nacional", 30000, "Gasolina", "Estandar", 11000, "El Salvador")
    auto2.mostrar_informacion()
else:
    print("Opcion invalida")


    

