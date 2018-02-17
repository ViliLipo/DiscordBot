import unittest
import GrandExhange

class TestGEMethods(unittest.TestCase):
    ge = GrandExhange.GrandExhangeService()
    def test_parseCommand(self):
        self.assertEqual(self.ge.parseCommand('!osrsGE ranarr'), 'ranarr')
        self.assertEqual(self.ge.parseCommand('!osrsGE Cannon base'), 'Cannon base')
        self.assertEqual(self.ge.parseCommand('!osrsGE guam potion (unf)'), 'guam potion (unf)')

    def test_findIdForName(self):
        self.assertEqual(self.ge.findIdForName("Cannon base"), [6])
        self.assertEqual(self.ge.findIdForName("sgagösdgjgep"), -1)

    def test_fetchItem(self):
        item = self.ge.fetchItem(6)
        self.assertEqual(item['item']['name'], "Cannon base" )
    def test_message(self):
        message = self.ge.message('!osrsGE abyssal')
        self.assertTrue(message.find("Abyssal whip") != -1)
