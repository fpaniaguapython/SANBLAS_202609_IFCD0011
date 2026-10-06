import unittest

from util.calculadora import division_entera, multiplicacion, resta, suma


class TestCalculadora(unittest.TestCase):
    """Pruebas unitarias para las operaciones de la calculadora."""

    @classmethod
    def setUpClass(cls):
        """Inicializa datos compartidos antes de ejecutar la clase de pruebas."""
        print('setUpClass --> Se ejecuta una única vez por clase')
        cls.nombre = "Calculadora"

    def setUp(self):
        """Inicializa el estado antes de cada prueba."""
        print('setUp --> Se ejecuta antesde cada prueba')
        self.operadores = {
            "suma": suma,
            "resta": resta,
            "multiplicacion": multiplicacion,
            "division_entera": division_entera,
        }

    def tearDown(self):
        """Limpia el estado después de cada prueba."""
        print('tearDown --> Se ejecuta antesde cada prueba')
        self.operadores.clear()

    @classmethod
    def tearDownClass(cls):
        """Limpia recursos compartidos al finalizar la clase de pruebas."""
        print('tearDownClass --> Se ejecuta una única vez por clase')
        cls.nombre = None

    def test_suma(self):
        """Debe devolver la suma correcta de dos números."""
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(-4, -6), -10)

    def test_resta(self):
        """Debe devolver la resta correcta de dos números."""
        self.assertEqual(resta(10, 4), 6)
        self.assertEqual(resta(5, 9), -4)

    def test_multiplicacion(self):
        """Debe devolver el producto correcto de dos números."""
        self.assertEqual(multiplicacion(3, 4), 12)
        self.assertEqual(multiplicacion(-2, 6), -12)

    def test_division_entera(self):
        """Debe devolver el cociente entero correcto."""
        self.assertEqual(division_entera(10, 3), 3)
        self.assertEqual(division_entera(20, 5), 4)
        self.assertEqual(division_entera(-9, 2), -5)

    def test_division_entera_divisor_cero(self):
        """Debe lanzar un ValueError cuando el divisor es cero."""
        with self.assertRaises(ValueError):
            division_entera(8, 0)


if __name__ == "__main__":
    unittest.main()
