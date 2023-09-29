def calculate_amino_acid_percentages(seq: str) -> str:
    """
    Calculating the percentage of amino acids in protein.

    Arguments:
    - seq (str): amino acid sequence. The input must be uppercased and use the single letter amino acid code.

    Returns:
    - output (str): percentage of amino acids in protein in descending order.
    """
    aa_count = {} #counting amino acids in sequence
    for amino_acid in seq:
        if amino_acid in aa_count:
            aa_count[amino_acid] += 1
        else:
            aa_count[amino_acid] = 1
    composition_rates = {}
    for aa in aa_count:
        composition_rates[aa] = aa_count[aa] / len(seq) * 100
    output = ', '.join([ f'{key}: {round(value, 2)}' for key, value in sorted(composition_rates.items(),
                                               key=lambda item: -item[1])])
    return output


def classify_amino_acid(seq: str) -> str:
    """
    Determine the percentage of acidic, basic and neutral amino acids in protein.

    Arguments:
    - seq (str): amino acid sequence. The input must be uppercased and use the single letter amino acid code.

    Returns
    - output (str): percentage of neutral, acidic and basic amino acids in protein.
    """
    amino_acid_counts = {'acidic': 0, 'neutral': 0, 'basic': 0}
    for amino_acid in seq:
        if amino_acid in ['D', 'E']:
            amino_acid_counts['acidic'] += 1
        elif amino_acid in ['A', 'N', 'C', 'Q', 'G', 'I', 'L', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']:
            amino_acid_counts['neutral'] += 1
        elif amino_acid in ['H','R', 'K']:
            amino_acid_counts['basic'] += 1
    acidic_percentage = round(amino_acid_counts['acidic'] / len(seq) * 100, 2)
    neutral_percentage = round(amino_acid_counts['neutral'] / len(seq) * 100, 2)
    basic_percentage = round(amino_acid_counts['basic'] / len(seq) * 100, 2)
    output = f'neutral: {neutral_percentage}, acidic: {acidic_percentage}, basic: {basic_percentage}'
    return output
