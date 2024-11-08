 
import unittest
from ..src.data_collection.collect_osint import get_osint_data

class TestDataCollection(unittest.TestCase):

    def test_get_osint_data(self):
        result = get_osint_data("https://api.example.com/osint")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()