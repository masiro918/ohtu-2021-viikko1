import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaa_negatiivinen_luku(self):
        self.varasto.lisaa_varastoon(-1)
        
        
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
        
    def test_alkusaldo_negatiivinen(self):
        varasto2 = Varasto(10, -1)
        #varasto2.saldo = -1
        
        self.assertAlmostEqual(varasto2.saldo, 0)

    def test_alku_tilavuus_negatiivinen(self):
        varasto2 = Varasto(-1)
        
        self.assertAlmostEqual(varasto2.tilavuus, 0.0)
        
    def test_maara_enemman_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(12)
        		
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)
        
    def test_ota_varastosta_negatiivinen_maara(self):
        return_value = self.varasto.ota_varastosta(-1)   
        
        self.assertAlmostEqual(return_value, 0)
        
    def test_maara_enemman_kuin_saldo(self):
        alkusaldo = 10
        self.varasto.saldo = alkusaldo
        return_value = self.varasto.ota_varastosta(11)
        
        self.assertAlmostEqual(return_value, alkusaldo)
        
    def test_to_string(self):
        alkusaldo = 5
        self.varasto.saldo = alkusaldo
        
        to_string = "saldo = 5, vielä tilaa 5"
        to_string2 = self.varasto.__str__()
        
        self.assertAlmostEqual(to_string, to_string2)
