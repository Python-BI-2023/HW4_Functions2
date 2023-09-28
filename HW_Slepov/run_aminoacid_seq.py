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
