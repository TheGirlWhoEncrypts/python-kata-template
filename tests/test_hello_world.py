import unittest
from src.hello_world import greet


class TestHelloWorld(unittest.TestCase):
    def test_greet_returns_hello_world(self):
        self.assertEqual("Hello world!", greet())