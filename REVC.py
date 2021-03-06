def dna_complement(dna_string):
    """

    @param dna_string: String DNA sequence of length <= 1000
    @return: Complementary DNA sequence
    """
    dna_complemented = ''

    for i in dna_string[::-1]:
        if i == 'A':
            dna_complemented += 'T'
        elif i == 'T':
            dna_complemented += 'A'
        elif i == 'C':
            dna_complemented += 'G'
        elif i == 'G':
            dna_complemented += 'C'

    return dna_complemented


