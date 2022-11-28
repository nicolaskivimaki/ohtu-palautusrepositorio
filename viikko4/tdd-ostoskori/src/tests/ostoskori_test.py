import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.leipa = Tuote("Leipä", 5)


    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.leipa)
        self.assertEqual(self.kori.hinta(), 5)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_tavaroiden_maara_oikea(self):
        self.kori.lisaa_tuote(self.leipa)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_oikea(self):
        self.kori.lisaa_tuote(self.leipa)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_tuotteiden_maara_oikea(self):
        self.kori.lisaa_tuote(self.leipa)
        self.kori.lisaa_tuote(self.leipa)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_oikea(self):
        self.kori.lisaa_tuote(self.leipa)
        self.kori.lisaa_tuote(self.leipa)
        self.assertEqual(self.kori.hinta(), 2 * self.leipa.hinta())

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_tavaroita_kaksi(self):
        self.kori.lisaa_tuote(self.leipa)
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_tavaroita_yksi(self):
        self.kori.lisaa_tuote(self.leipa)
        self.kori.lisaa_tuote(self.leipa)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_oikea_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)
        