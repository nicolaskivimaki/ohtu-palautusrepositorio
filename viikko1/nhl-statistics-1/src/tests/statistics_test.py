import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_etsi_pelaaja(self):
        pelaaja = self.statistics.search('Semenko')
        self.assertEqual(pelaaja.name, 'Semenko')
    
    def test_etsi_haamu_pelaaja(self):
        pelaaja = self.statistics.search('Semenka')
        self.assertEqual(pelaaja, None)
    
    def test_tiimin_pelaajat(self):
        lista = []
        pelaajat = self.statistics.team('PIT')
        for pelaaja in pelaajat:
            lista.append(pelaaja.name)
        self.assertEqual(lista, ['Lemieux'])
    
    def test_top(self):
        lista = []
        top = self.statistics.top(0)
        for pelaaja in top:
            lista.append(pelaaja.name)
        self.assertEqual(lista, ['Gretzky'])
    
    def test_top_2(self):
        lista = []
        top = self.statistics.top(0, 2)
        for pelaaja in top:
            lista.append(pelaaja.name)
        self.assertEqual(lista, ['Lemieux'])
    
    def test_top_3(self):
        lista = []
        top = self.statistics.top(0, 3)
        for pelaaja in top:
            lista.append(pelaaja.name)
        self.assertEqual(lista, ['Gretzky'])
    
    def test_top_4(self):
        lista = []
        top = self.statistics.top(0, 4)
        self.assertEqual(top, None)