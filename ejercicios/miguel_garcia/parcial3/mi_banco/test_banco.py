import unittest

from cuenta import Cuenta
from banco import banco

class testintegracionbanco(unittest.TestCase):
    def setUp(self):
        self.cuenta1 = cuenta("fulanito perez","001",1000)
        self.cuenta2 = cuenta("Perecilia Sanchez","002")

        self.banco =self.banco()


    def test_tranferencia_exitosa(self):
        resultado = self.banco.transferir(self.cuenta1, self.cuenta2, 350)
