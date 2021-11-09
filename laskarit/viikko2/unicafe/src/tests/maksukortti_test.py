import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)
        
    def test_saldo_vähenee(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)
        
    def test_saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(20)
        self.assertNotEqual(self.maksukortti, "Rahaa ei tule")