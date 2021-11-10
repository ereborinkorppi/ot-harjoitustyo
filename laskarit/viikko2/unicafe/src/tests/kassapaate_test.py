import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        
    def test_kassapaate_luotu(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_alkukassa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_edulliset_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_maukkaat_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_kassa_kasvaa_kateisella_edullisesti(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        
    def test_vaihtoraha_oikein_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        
    def test_edulliset_kasvaa_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kassa_kasvaa_kateisella_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        
    def test_vaihtoraha_oikein_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        
    def test_maukkaat_kasvaa_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_vaihtoraha_palautus_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(150), 150)
        
    def test_vaihtoraha_palautus_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(350), 350)
    
    def test_edulliset_lounaat_ei_kasva_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_edullisesti_kassa_ei_kasva_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukkaat_lounaat_ei_kasva_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_maukkaasti_kassa_ei_kasva_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_edullisesti_kortilla_toimii(self):
        self.maksukortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        
    def test_edullisesti_kortilla_saldo_vahenee(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 260)
    
    def test_edullisesti_kortilla_lounaat_kasvaa(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_maukkaasti_kortilla_toimii(self):
        self.maksukortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        
    def test_maukkaasti_kortilla_saldo_vahenee(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)
    
    def test_maukkaasti_kortilla_lounaat_kasvaa(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_edullisesti_kortilla_ei_rahaa(self):
        self.maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        
    def test_edullisesti_kortilla_saldo_ei_muutu(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)
    
    def test_edullisesti_kortilla_lounaat_ei_kasvaa(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_maukkaasti_kortilla_ei_toimi(self):
        self.maksukortti = Maksukortti(300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        
    def test_maukkaasti_kortilla_saldo_ei_muutu(self):
        self.maksukortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 300)
    
    def test_maukkaasti_kortilla_lounaat_ei_kasva(self):
        self.maksukortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_edullisesti_kortilla_kassa_ei_kasva(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_maukkaasti_kortilla_kassa_ei_kasva(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kortin_saldo_kasvaa(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.maksukortti.saldo, 700)
    
    def test_kassa_kasvaa_kortinlatauksella(self):
        self.maksukortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100300)
        
    def test_lataussumma_liian_pieni(self):
        self.maksukortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1), None)