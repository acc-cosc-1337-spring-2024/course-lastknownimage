def get_hamming_distance(dna1, dna2):
   # This defines the hamming distance.
# In the event that you take a break and forget what you did, you haven't done anything with it.

# Parameters per Rosalind:
# Two sequences must be of equal length
# Then and only then, return hamming distance.

    if len(dna1) != len(dna2):
        raise ValueError("You need the sequences to be of equal length.")

    distance = 0
    for side1, side2 in zip(dna1, dna2):
        if side1 != side2:
            distance += 1
    return distance

# At start, make sure the distances of each side of the sequence are of the same length.

def get_dna_complement(dna):
    complement_pairs = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    return ''.join(complement_pairs[nucleotide] for nucleotide in dna)

# Joins base nucleotides to form complement pairs.