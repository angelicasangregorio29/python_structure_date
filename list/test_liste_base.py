import unittest
from liste_base import build_server_list

class TestListeBase(unittest.TestCase):
    def test_lista_finale(self):
        server = build_server_list()
        self.assertEqual(server, ['proxy01', 'web01', 'db01', 'backup01'])

    def test_lunghezza_lista(self):
        server = build_server_list()
        self.assertEqual(len(server), 4)

if __name__ == '__main__':
    unittest.main()