class Estudiante:
    def __init__(self, nombre, nota):
        # Atributos básicos
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota
        self.estado = "No asignado"


def obtener_condicion(self, nombre, promedio):
    # Validación de robustez interna
    if not 1 <= self.nota <= 10:
        return "Datos inválidos"

    # Lógica de decisión
    if self.nota >= 7:
        self.estado = "Aprobado"
    elif self.nota >= 4:
        self.estado = "coloquio"
    else:
        self.estado = "Libre"

    return self.estado

