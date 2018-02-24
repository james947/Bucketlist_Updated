import unittest
from views import app

class Routests(unittest.TestCase):

    
    def test_login_route(self):
        # assert addition(5,5) == 10
        self.assertEqual(addition(5,5),10)