def count_possible_number_of_disulfide_bonds(sequence: str) -> int:
    """
    takes an amino acid sequence as input and returns the
    number of possible combinations of two different cysteines to form a disulfide bond
    :param sequence: str
    :return: int
    """
    bond_count = 0
    cysteine_positions = []

    for index, aa in enumerate(sequence):
        if aa == "C":
            cysteine_positions.append(index + 1)

    # If there is more than 2 aminoacids between cysteins,
    # they could form disulfide bond
    for i in range(len(cysteine_positions)):
        for j in range(i + 1, len(cysteine_positions)):
            if cysteine_positions[j] - cysteine_positions[i] > 2:
                bond_count += 1
    return bond_count


def count_molecular_weight(sequence: str) -> int:
    """
    takes an amino acid sequence as input and returns the molecular weight of the protein
    :param sequence: str
    :return: int
    """
    sequence_upper = sequence.upper()
    amino_acid_weights = {
        'A': 89, 'R': 174, 'N': 132, 'D': 133, 'C': 121,
        'E': 147, 'Q': 146, 'G': 75, 'H': 155, 'I': 131,
        'L': 131, 'K': 146, 'M': 149, 'F': 165, 'P': 115,
        'S': 105, 'T': 119, 'W': 204, 'Y': 181, 'V': 117
    }
    molecular_weight = sum(amino_acid_weights.get(aa, 0) for aa in sequence_upper)
    # Count the molecular weight of protein with using dictionary
    return molecular_weight


def convert_amino_acid_seq_to_dna(sequence: str) -> str:
    """
    takes an amino acid sequence as input and returns the optimal DNA sequence for E.coli
    :param sequence: str
    :return: str
    """
    most_frequent_codon_for_amino_acid_e_coli = {
        'A': 'GCT', 'R': 'CGT', 'N': 'AAC', 'D': 'GAC', 'C': 'TGC',
        'E': 'GAA', 'Q': 'CAG', 'G': 'GGC', 'H': 'CAC', 'I': 'ATC',
        'L': 'CTG', 'K': 'AAA', 'M': 'ATG', 'F': 'TTC', 'P': 'CCG',
        'S': 'TCT', 'T': 'ACC', 'W': 'TGG', 'Y': 'TAC', 'V': 'GTT',
        'a': 'gct', 'r': 'cgt', 'n': 'aac', 'd': 'gac', 'c': 'tgc',
        'e': 'gaa', 'q': 'cag', 'g': 'ggc', 'h': 'cac', 'i': 'atc',
        'l': 'ctg', 'k': 'aaa', 'm': 'atg', 'f': 'ttc', 'p': 'ccg',
        's': 'tct', 't': 'acc', 'w': 'tgg', 'y': 'tac', 'v': 'gtt'
    }
    # This function selects the optimal DNA sequence with which protein
    # will be produced in the E. coli bacterium. 
    # Codons are selected according to codon frequency.
    codon_str = ''
    for amin_acid in sequence:
        codon_str += most_frequent_codon_for_amino_acid_e_coli[amin_acid]
    return codon_str
