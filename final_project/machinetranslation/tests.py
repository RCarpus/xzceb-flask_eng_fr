import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        # Test translation of a simple sentence
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

        # Test translation of an empty string
        result = english_to_french('')
        self.assertEqual(result, '')

    def test_frenchToEnglish(self):
        # Test translation of a simple sentence
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

        # Test translation of an empty string
        result = french_to_english('')
        self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()