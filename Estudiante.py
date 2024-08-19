
#creamos la clase Alumno
class Alumno:
    # Asignamos los atributos
    Nombre = ""
    Edad = ""
    Anio_Nacimiento = ""
    Nombre_Responsable = ""

# creamos los metodos
    def __init__(self, Nombre, Edad, Anio_Nacimiento, Nombre_Responsable):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Anio_Nacimiento = Anio_Nacimiento
        self.Nombre_Responsable = Nombre_Responsable
        self.estado = "NO MATRICULADO"
        self.Cambiar_estado()

    #el metodo Cambiar estado le asigna que esta matriculado una vez se registra

    def Cambiar_estado(self):
        self.estado = "MATRICULADO"
        
    def Mostrar_Informacion(self):
        print(f"Nombre: {self.Nombre}")
        print(f"Edad: {self.Edad}")
        print(f"Año de nacimiento: {self.Anio_Nacimiento}")
        print(f"Nombre del responsable: {self.Nombre_Responsable}")
        print(f"Estado: {self.estado}")

# le pedimos al usuario que registre los datos del estudiante
nombre = input("Ingrese el nombre del estudiante: ")
Edad = input("Ingrese la edad del estudiante: ")
Anio_Nacimiento = input("Ingrese el año de nacimiento del estudiante: ")
Nombre_Responsable = input("Ingrese el nombre del responsable del estudiante: ")

#Enviamos los valores a la variable y la imprimimos
Estudiante = Alumno(nombre, Edad, Anio_Nacimiento, Nombre_Responsable)
Estudiante.Mostrar_Informacion()


