import unittest
from src.homework.i_dictionaries_and_sets import (get_students_who_took_prog1_and_prog2, 
                                                  get_students_who_took_prog2_only, 
                                                  get_students_who_took_prog1_not_prog_2, 
                                                  get_students_who_took_prog2_not_prog_1)

class Test_Config(unittest.TestCase):
    prog1 = ('Student_1', 'Student_2', 'Student_3')
    prog2 = ('Student_3', 'Student_4', 'Student_5')
    def test_get_students_who_took_prog1_and_prog2(self):
        self.assertEqual(get_students_who_took_prog1_and_prog2(self.prog1, self.prog2), {'Student_3'})
    def test_get_students_who_took_prog2_only(self):
        self.assertEqual(get_students_who_took_prog2_only(self.prog1, self.prog2), {'Student_4', 'Student_5'})
    def test_get_students_who_took_prog1_not_prog_2(self):
        self.assertEqual(get_students_who_took_prog1_not_prog_2(self.prog1, self.prog2), {'Student_1', 'Student_2'})
    def test_get_students_who_took_prog2_not_prog_1(self):
        self.assertEqual(get_students_who_took_prog2_not_prog_1(self.prog1, self.prog2), {'Student_4', 'Student_5'})
    
    if __name__ == '__main__':
        unittest.main()