def count_disulfide_bonds(sequence):
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


def count_protein_length(sequence):
    return len(sequence)  # Count length of amino acid sequence


def count_molecular_weight(sequence):
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


def convert_amino_acid_seq_to_dna(sequence):
    most_frequent_codon_for_amino_acid_E_coli = {
        'A': 'GCT', 'R': 'CGT', 'N': 'AAC', 'D': 'GAC', 'C': 'TGC',
        'E': 'GAA', 'Q': 'CAG', 'G': 'GGC', 'H': 'CAC', 'I': 'ATC',
        'L': 'CTG', 'K': 'AAA', 'M': 'ATG', 'F': 'TTC', 'P': 'CCG',
        'S': 'TCT', 'T': 'ACC', 'W': 'TGG', 'Y': 'TAC', 'V': 'GTT'
}
    # This function selects the optimal DNA sequence with which protein
    # will be produced in the E. coli bacterium. 
    # Codons are selected according to codon frequency.
    sequence_upper = sequence.upper()
    codon_str = ''
    for amin_acid in sequence_upper:
        codon_str += most_frequent_codon_for_amino_acid_E_coli[amin_acid]
    return codon_str
