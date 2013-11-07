def point_mutations(dna_sequence1, dna_sequence2):

    hamming_distance = 0
    for i in range(len(dna_sequence1)):
        if dna_sequence1[i] != dna_sequence2[i]:
            hamming_distance += 1

    return hamming_distance

