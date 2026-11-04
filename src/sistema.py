import json
import os
from src.models import Solicitud, Estudiante, Responsable

class SistemaGestion:
    def __init__(self, db_file="data_solicitudes.json"):
        self.f = db_file
        self.data = []
        self.estudiantes = []
        self.responsables = []
        self.counter = 1
        self.load()

    def load(self):
        if os.path.exists(self.f):
            try:
                fp = open(self.f, "r")
                raw = fp.read()
                fp.close()
                if raw:
                    d = json.loads(raw)
                    self.data = d.get("solicitudes", [])
                    self.counter = d.get("counter", 1)
            except Exception as e:
                print("Error al cargar")

    def save(self):
        try:
            fp = open(self.f, "w")
            d = {"solicitudes": self.data, "counter": self.counter}
            fp.write(json.dumps(d, indent=4))
            fp.close()
        except Exception as e:
            print("Error al guardar")

    # Operacion 1: Registrar Solicitud (Mezcla de responsabilidades, validaciones rudimentarias)
    def reg_sol(self, est_id, est_nom, est_mail, tipo, desc, prio):
        if not est_id or not est_nom or not est_mail:
            print("Datos invalidos")
            return None
        
        # Validacion de mail duplicada o primitiva
        if "@" not in est_mail:
            print("Email mal formado")
            return None

        # Feature envy / Primitive obsession
        sol_id = self.counter
        self.counter += 1
        
        # Estructura como diccionario suelto en lugar de objeto bien modelado
        s = {
            "id": sol_id,
            "estudiante": {"id": est_id, "nombre": est_nom, "email": est_mail},
            "tipo": tipo,
            "descripcion": desc,
            "prioridad": prio, # String "ALTA", "MEDIA", "BAJA"
            "estado": "PENDIENTE",
            "responsable": None
        }
        self.data.append(s)
        self.save()
        print("Registrada con exito: " + str(sol_id))
        return sol_id

    # Operacion 2: Cambiar estado
    def chg_st(self, sol_id, n_st):
        # Duplicacion de codigo de busqueda
        target = None
        for item in self.data:
            if item["id"] == sol_id:
                target = item
                break
        
        if target is not None:
            # Control de flujo rigido con Strings
            if n_st == "EN_PROCESO" or n_st == "RESUELTO" or n_st == "CANCELADO":
                target["estado"] = n_st
                self.save()
                return True
            else:
                print("Estado no valido")
                return False
        else:
            print("No se encontro la solicitud")
            return False

    # Operacion 3: Asignar responsable
    def asig_resp(self, sol_id, resp_id, resp_nom, resp_area):
        # Duplicacion de codigo de busqueda
        target = None
        for item in self.data:
            if item["id"] == sol_id:
                target = item
                break
        
        if target:
            target["responsable"] = {"id": resp_id, "nombre": resp_nom, "area": resp_area}
            self.save()
            return True
        return False

    # Operacion 4: Buscar/Filtrar solicitudes (Duplicacion interna y acoplamiento)
    def buscar(self, k_estado=None, k_prio=None):
        res = []
        for s in self.data:
            if k_estado and k_prio:
                if s["estado"] == k_estado and s["prioridad"] == k_prio:
                    res.append(s)
            elif k_estado:
                if s["estado"] == k_estado:
                    res.append(s)
            elif k_prio:
                if s["prioridad"] == k_prio:
                    res.append(s)
            else:
                res.append(s)
        return res

    # Operacion adicional / Reporte: Mezcla formato de consola con logica de consulta
    def rep_basico(self):
        print("=== REPORTE DE SOLICITUDES ===")
        c_pend = 0
        c_proc = 0
        c_res = 0
        for item in self.data:
            print("ID: " + str(item["id"]) + " | Est: " + item["estudiante"]["nombre"] + " | Est: " + item["estado"])
            if item["estado"] == "PENDIENTE":
                c_pend += 1
            elif item["estado"] == "EN_PROCESO":
                c_proc += 1
            elif item["estado"] == "RESUELTO":
                c_res += 1
        print("TOTAL: " + str(len(self.data)))
        print("Pendientes: " + str(c_pend) + " | En Proceso: " + str(c_proc) + " | Resueltas: " + str(c_res))