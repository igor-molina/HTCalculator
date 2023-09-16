import unittest
from core.calculadora_horas import calcular_horas_trabalhadas


class TestCalculadoraHoras(unittest.TestCase):

    def test_formato_valido(self):
        self.assertTrue(calcular_horas_trabalhadas("8:30", "17:45") is not None)
        self.assertTrue(calcular_horas_trabalhadas("12:00", "18:30") is not None)

        self.assertTrue(calcular_horas_trabalhadas("830", "1745") is not None)
        self.assertTrue(calcular_horas_trabalhadas("1200", "1830") is not None)

    def test_formato_invalido(self):
        with self.assertRaises(ValueError):
            calcular_horas_trabalhadas("0830", "17:45")

    def test_calculo_horas_trabalhadas(self):
        self.assertEqual(calcular_horas_trabalhadas("08:30", "17:45"), "9:15")
        self.assertEqual(calcular_horas_trabalhadas("12:00", "18:30"), "6:30")

    def test_desconto_intervalo(self):
            self.assertEqual(calcular_horas_trabalhadas("08:30", "17:45", "01:00"), "8:15")
            self.assertEqual(calcular_horas_trabalhadas("12:00", "18:30", "00:30"), "6:00")

    def test_inverter_horarios(self):
        self.assertEqual(calcular_horas_trabalhadas("17:45", "08:30"), "9:15")
        self.assertEqual(calcular_horas_trabalhadas("18:30", "12:00"), "6:30")


if __name__ == '__main__':
    unittest.main()
