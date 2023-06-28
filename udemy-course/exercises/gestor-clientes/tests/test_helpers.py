import unittest

import database as db
from helpers import validar_dni


class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista = [
            db.Cliente("11111111A", "Marta", "Perez"),
            db.Cliente("22222222B", "Manuel", "Lopez"),
            db.Cliente("33333333C", "Ana", "Garcia"),
        ]

    def test_validar_dni_nuevo_devuelve_true(self):
        self.assertTrue(validar_dni("4444444D", db.Clientes.lista))

    def test_validar_dni_existente_devuelve_false(self):
        self.assertFalse(validar_dni("11111111A", db.Clientes.lista))

    def test_validar_dni_formato_incorrecto_devuelve_false(self):
        self.assertFalse(validar_dni("444444444D", db.Clientes.lista))
        self.assertFalse(validar_dni("AAAAAAA1", db.Clientes.lista))
        self.assertFalse(validar_dni("44444444", db.Clientes.lista))