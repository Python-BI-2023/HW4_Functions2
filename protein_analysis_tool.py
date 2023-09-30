def get_amino_acid_sum(protein_sequences: list) -> None:
    """
    Counts the amount of each amino acid in the injected protein sequences

    Arguments:
    - protein_sequences (list): list of injected protein sequence

    Return:
    - None
    - Only print the amount of each amino acid in the injected protein sequences
    """
    for protein_sequence in range(len(protein_sequences)):
        dictionary = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
                      'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0,
                      'T': 0, 'V': 0, 'W': 0, 'Y': 0}
        for amino_acid in protein_sequences[protein_sequence]:
            dictionary[amino_acid] += 1
            clone = {
                'Alanin': dictionary['A'],
                'Cysteine': dictionary['C'],
                'Aspartic acid': dictionary['D'],
                'Glutamic acid': dictionary['E'],
                'Phenylalanine': dictionary['F'],
                'Glycine': dictionary['G'],
                'Histidine': dictionary['H'],
                'Isoleucine': dictionary['I'],
                'Lysine': dictionary['K'],
                'Leucine': dictionary['L'],
                'Methionine': dictionary['M'],
                'Aspargin': dictionary['N'],
                'Proline': dictionary['P'],
                'Glutamine': dictionary['Q'],
                'Arginine': dictionary['R'],
                'Serin': dictionary['S'],
                'Threonine': dictionary['T'],
                'Valin': dictionary['V'],
                'Tryptophan': dictionary['W'],
                'Tyrosine': dictionary['Y']
            }
        print('The number of amino acids in the sequence ', protein_sequence + 1, ':')
        for key, value in clone.items():
            print(key, value)


def beautiful_print(codon_optimization_list: list) -> None:
    """
            Makes a user-friendly output of a codon-optimized DNA sequence

            Arguments:
            - codon_optimization_list (list): list of codon-optimized protein sequence

            Return:
            - None
            - Only print the number of the introduced protein sequence and the codon-optimized DNA sequence
            """
    for nucleotide_sequence in range(len(codon_optimization_list)):
        print('Sequence ', nucleotide_sequence + 1)
        print(codon_optimization_list[nucleotide_sequence])


def codon_optimization(protein_sequences, cell_type=None):
    """
    Makes codon-optimized DNA based on the introduced amino acid sequences for 3 types of cells:
    Esherichia coli, Pichia pastoris, Mouse

    Arguments:
    - protein_sequences (list): list of injected protein sequence
    - cell_type (str): user-entered cell type for codon optimization

    Return:
    - None
    - Only print the number of the introduced protein sequence and the codon-optimized DNA sequence
    """

    if cell_type == 'Esherichia coli' or cell_type == 'E.coli':
        codon_optimization_Ecoli = []
        ecoli_triplets = {'A': 'GCG', 'C': 'TGC', 'D': 'GAT', 'E': 'GAA', 'F': 'TTT', 'G': 'GGC',
                          'H': 'CAT', 'I': 'ATT', 'K': 'AAA', 'L': 'CTG', 'M': 'ATG', 'N': 'AAC',
                          'P': 'CCG', 'Q': 'CAG', 'R': 'CGT', 'S': 'AGC', 'T': 'ACC', 'V': 'GTG',
                          'W': 'TGG', 'Y': 'TAT'}
        replacer_ecoli = ecoli_triplets.get
        for amino_acid in range(len(protein_sequences)):
            codon_optimization_Ecoli += [''.join([replacer_ecoli(n, n) for n in protein_sequences[amino_acid]])]
        return beautiful_print(codon_optimization_Ecoli)

    if cell_type == 'Pichia pastoris' or cell_type == 'P.pastoris':
        codon_optimization_ppastoris = []
        ppastoris_triplets = {'A': 'GCT', 'C': 'TGT', 'D': 'GAT', 'E': 'GAA', 'F': 'TTT', 'G': 'GGT',
                              'H': 'CAT', 'I': 'ATT', 'K': 'AAG', 'L': 'TTG', 'M': 'ATG', 'N': 'AAC',
                              'P': 'CCA', 'Q': 'CAA', 'R': 'AGA', 'S': 'TCT', 'T': 'ACT', 'V': 'GTT',
                              'W': 'TGG', 'Y': 'TAC'}
        replacer_ppastoris = ppastoris_triplets.get
        for amino_acid in range(len(protein_sequences)):
            codon_optimization_ppastoris += [''.join([replacer_ppastoris(n, n) for n in protein_sequences[amino_acid]])]
        return beautiful_print(codon_optimization_ppastoris)

    if cell_type == 'Mouse' or cell_type == 'mouse':
        codon_optimization_mouse = []
        mouse_triplets = {'A': 'GCC', 'C': 'TGC', 'D': 'GAC', 'E': 'GAG', 'F': 'TTC', 'G': 'GGC',
                          'H': 'CAC', 'I': 'ATC', 'K': 'AAG', 'L': 'CTG', 'M': 'ATG', 'N': 'AAC',
                          'P': 'CCC', 'Q': 'CAG', 'R': 'CGG', 'S': 'AGC', 'T': 'ACC', 'V': 'GTG',
                          'W': 'TGG', 'Y': 'TAC'}
        replacer_Mouse = mouse_triplets.get
        for amino_acid in range(len(protein_sequences)):
            codon_optimization_mouse += [''.join([replacer_Mouse(n, n) for n in protein_sequences[amino_acid]])]
        return beautiful_print(codon_optimization_mouse)
    else:
        print('The following types of organisms are available for codon optimization: Esherichia coli, Pichia pastoris,'
              'Mouse')



