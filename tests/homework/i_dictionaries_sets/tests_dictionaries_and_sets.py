import unittest

from src.homework.i_dictionaries_sets import get_p_distance

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory = {}
        get_p_distance.add_inventory(inventory, "Widget1", 10)
        self.assertEqual(inventory["Widget1"], 10) 

        get_p_distance.add_inventory(inventory, "Widget1", 25)
        self.assertEqual(inventory["Widget1"], 35) 

        get_p_distance.add_inventory(inventory, "Widget1", -10)
        self.assertEqual(inventory["Widget1"], 25) 

    def test_remove_inventory_widget(self):
        inventory = {"Widget1": 10, "Widget2": 20}
        result = get_p_distance.remove_inventory_widget(inventory, "Widget1")
        self.assertEqual(len(inventory), 1)  
        self.assertNotIn("Widget1", inventory) 
        self.assertIn("Widget2", inventory) 

if __name__ == '__main__':
    unittest.main()
