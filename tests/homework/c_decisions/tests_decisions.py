import unittest

from src.homework.c_decisions import test_decisions
class Test_Config(unittest.TestCase):
    suite = unittest.TestLoader().loadTestsFromModule(test_decisions)