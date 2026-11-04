import unittest
import os
import json
from src.sistema import SistemaGestion

class TestSistemaGestionBase(unittest.TestCase):
    def setUp(self):
        self.test_db = "test_data.json"
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        self.sistema = SistemaGestion(db_file=self.test_db)

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_registrar_solicitud(self):
        sid = self.sistema.reg_sol("E1", "Pedro", "pedro@mail.com", "CONSULTA", "Duda final", "BAJA")
        self.assertIsNotNone(sid)
        self.assertEqual(len(self.sistema.data), 1)

    def test_cambiar_estado(self):
        sid = self.sistema.reg_sol("E1", "Pedro", "pedro@mail.com", "CONSULTA", "Duda final", "BAJA")
        res = self.sistema.chg_st(sid, "EN_PROCESO")
        self.assertTrue(res)
        self.assertEqual(self.sistema.data[0]["estado"], "EN_PROCESO")

    def test_asignar_responsable(self):
        sid = self.sistema.reg_sol("E1", "Pedro", "pedro@mail.com", "CONSULTA", "Duda final", "BAJA")
        res = self.sistema.asig_resp(sid, "R1", "Ana", "Alumnos")
        self.assertTrue(res)
        self.assertIsNotNone(self.sistema.data[0]["responsable"])

    def test_buscar_solicitudes(self):
        self.sistema.reg_sol("E1", "Pedro", "pedro@mail.com", "CONSULTA", "Duda 1", "BAJA")
        self.sistema.reg_sol("E2", "Laura", "laura@mail.com", "TRAMITE", "Duda 2", "ALTA")
        res = self.sistema.buscar(k_prio="ALTA")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["estudiante"]["nombre"], "Laura")

if __name__ == "__main__":
    unittest.main()