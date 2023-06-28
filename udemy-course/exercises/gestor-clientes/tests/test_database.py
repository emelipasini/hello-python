import unittest

import database as db

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista = [
            db.Cliente("11111111A", "Marta", "Perez"),
            db.Cliente("22222222B", "Manuel", "Lopez"),
            db.Cliente("33333333C", "Ana", "Garcia"),
        ]

    def test_buscar_cliente_existente_funciona(self):
        cliente = db.Clientes.buscar("22222222B")

        if cliente:
            self.assertEqual(cliente.nombre, "Manuel")
            self.assertEqual(cliente.apellido, "Lopez")

    def test_buscar_cliente_inexistente_devuelve_none(self):
        cliente = db.Clientes.buscar("44444444D")

        self.assertIsNone(cliente)

    def test_crear_cliente_nuevo_funciona(self):
        cliente = db.Clientes.crear("44444444D", "Juan", "Gomez")

        self.assertEqual(cliente.nombre, "Juan")
        self.assertEqual(cliente.apellido, "Gomez")
        self.assertEqual(len(db.Clientes.lista), 4)

    def test_crear_cliente_existente_falla(self):
        self.assertRaises(Exception, db.Clientes.crear, "11111111A", "Juan", "Gomez")

    def test_modificar_cliente_existente_funciona(self):
        db.Clientes.modificar("11111111A", "Marta", "Gonzalez")
        cliente = db.Clientes.buscar("11111111A")

        if cliente:
            self.assertEqual(cliente.nombre, "Marta")
            self.assertEqual(cliente.apellido, "Gonzalez")

    def test_modificar_cliente_inexistente_falla(self):
        self.assertRaises(Exception, db.Clientes.modificar, "44444444D", "Juan", "Gomez")

    def test_borrar_cliente_existente_funciona(self):
        db.Clientes.borrar("11111111A")
        cliente_borrado = db.Clientes.buscar("11111111A")

        self.assertEqual(len(db.Clientes.lista), 2)
        self.assertIsNone(cliente_borrado)


    def test_borrar_cliente_inexistente_falla(self):
        self.assertRaises(Exception, db.Clientes.borrar, "44444444D")

    def tearDown(self) -> None:
        db.Clientes.lista = []
        db.Clientes.guardar()
