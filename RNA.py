def DNA_to_RNA(dna_string):
    rna_string = ''

    for i in dna_string:
        if i == 'T':
            rna_string += 'U'
        else:
            rna_string += i

    return rna_string

