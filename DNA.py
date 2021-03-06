def count_nucleotides(dna_sequence):
    """
    @param dna_sequence: Give type STRING of a DNA sequence.
    @return: Count of A C G and T
    """
    if len(dna_sequence) < 1001:
        nucleotide_count = [0, 0, 0, 0]
        for i in dna_sequence:
            if i == 'A':
                nucleotide_count[0] += 1
            elif i == 'C':
                nucleotide_count[1] += 1
            elif i == 'G':
                nucleotide_count[2] += 1
            elif i == 'T':
                nucleotide_count[3] += 1

        print str(nucleotide_count[0]) + ' ' + str(nucleotide_count[1]) \
              + ' ' + str(nucleotide_count[2]) + ' ' + str(nucleotide_count[3]) + ' '

    else:
        return None
