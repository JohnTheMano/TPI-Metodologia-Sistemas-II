# Modelos de dominio basico
class Estudiante:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

class Responsable:
    def __init__(self, id, nombre, area):
        self.id = id
        self.nombre = nombre
        self.area = area

class Solicitud:
    def __init__(self, id, estudiante, tipo, descripcion, prioridad, estado="PENDIENTE", responsable=None):
        self.id = id
        self.estudiante = estudiante # Objeto o dict
        self.tipo = tipo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado
        self.responsable = responsable