import unittest
from src.homework.h_strings.value_return import get_hamming_distance
from src.homework.h_strings.value_return import get_dna_complement

class TestConfig(unittest.TestCase):
    def test_get_hamming_distance(self):
        result = get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
        self.assertEqual(result, 7)
    def test_get_dna_complement(self):
        result = get_dna_complement("AAAACCCGGT")
        self.assertEqual(result, "ACCGGGTTTT")

# In case you forget, you have:
    # Written the part needed for strings.py defining hamming distance, dna complement
    # Made sure that if the dna string distances do not match, an error will be thrown
    # Written a part to cause nucleotides to join
    # In tests_strings: imported hamming distance and dna complement scripts
    # Told python to test itself given some sequences of nucleotides
    # In run_tests: probably the wrong thing.
# The code doesn't work at this point and I'm not sure why. Will ask Viv for help tomorrow.
    # Error reads: no module named src, no module named homework.
    # Pretty sure this part usually runs fine so I'm not sure why it isn't now.