import unittest

from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        # Test translation of "Hello" to French
        result = englishToFrench("Hello")
        self.assertEqual(result, "Bonjour")

        # Test translation of empty string
        result = englishToFrench("")
        self.assertEqual(result, "")

    def test_frenchToEnglish(self):
        # Test translation of "Bonjour" to English
        result = frenchToEnglish("Bonjour")
        self.assertEqual(result, "Hello")

        # Test translation of empty string
        result = frenchToEnglish("")
        self.assertEqual(result, "")
        
if __name__ == '__main__':
    unittest.main()

