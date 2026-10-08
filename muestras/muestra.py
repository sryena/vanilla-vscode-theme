"""Docstring: es un texto, así que va en MENTA."""

# Comentario: gris cálido en cursiva
import os
from dataclasses import dataclass

saludo = "Adiós"      # esta línea cambia tras el commit


@dataclass            # decorador: ROSA en cursiva
class Alumno:         # class: LAVANDA · nombre de la clase: ROSA
    nombre: str       # tipo (str): ROSA
    nota: float = 0.0  # número: MELOCOTÓN

    def aprobado(self) -> bool:     # def: LAVANDA · función: CELESTE · self: LAVANDA cursiva
        return self.nota >= 5 and not self.nombre == ""


def media(notas: list[float]) -> float:   # parámetro (notas): café en cursiva
    if not notas:
        return 0
    total = sum(notas)                    # sum(): función integrada, CELESTE
    return round(total / len(notas), 2)


# Esta línea se borra tras el commit
for i in range(3):
    print(f"Vuelta {i}\n", None, True)    # \n: MELOCOTÓN · None y True: MELOCOTÓN

ruta = os.path.join("M4", "RA2")
try:
    alumno = Alumno("Yenai", 7.5)
    print(alumno.aprobado(), media([7.5, 8, 6]))
except ValueError as error:
    print("Error:", error)
