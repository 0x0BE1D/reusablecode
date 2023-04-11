def str_to_bits(s):
    """
    Convert a string to a list of bits (0's and 1's).
    """
    bits = []
    for c in s:
        bits.extend([int(b) for b in format(ord(c), '08b')])
    return bits

def hamming_distance(s1, s2):
    """
    Calculate the Hamming distance between two strings by comparing their bits.
    """
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")

    bits1 = str_to_bits(s1)
    bits2 = str_to_bits(s2)

    distance = 0
    for i in range(len(bits1)):
        if bits1[i] != bits2[i]:
            distance += 1

    return distance
