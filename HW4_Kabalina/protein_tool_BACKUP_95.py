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


def counting_point_mutations(seq1: str, seq2: str) -> int:
    """
    Counts the number of mutations - amino acid substitutions in the sequence seq2 relative to seq1

    Arguments:
    - seq1 (str): sequence to compare with
    - seq2 (str): sequence to compare to

    Return:
    - output (int): number of amino acid substitutions
    """
    output = 0
    for number_amino_acid in range(len(seq1)):
        if seq1[number_amino_acid] != seq2[number_amino_acid]:
            output += 1
    return output


def counting_molecular_weight(seq: str) -> int:
    """
    Counts the molecular mass of a protein sequence seq

    Arguments:
    - seq (str): sequence to count the molecular weight

    Return:
    - output (int): molecular weight value
    """
    dict_molecular_mass={
        'G': 75, 'A': 89, 'V': 117, 'L': 131, 'I': 131, 'P': 115,
        'F': 165, 'Y': 181, 'W': 204, 'S': 105, 'T': 119, 'C': 121,
        'M': 149, 'N': 132, 'Q': 146, 'D': 133, 'E': 147, 'K': 146,
        'R': 174, 'H': 155
    }
    output = 0
    for amino_acid in seq:
        output += dict_molecular_mass[amino_acid]
    return output - 18 * (len(seq) - 1)


def get_occurrences(seq1: str, seq2: str) -> str:
    """
   Counting the number of occurrences of string seq2 in string seq1.
   Getting indexes of occurrences of string seq2 in string seq1.

    Arguments:
    - seq1 (str): sequence in which search
    - seq2 (str): sequence to search in

    Return:
    - output (str): str, first element is the number of occurrences (int).
      All subsequent elements are indexes of occurrences of seq2 in seq1.
    """
    output = [seq1.count(seq2)]
    for i in range(len(seq1)):
        if seq1.startswith(seq2, i):
            output.append(i+1)
<<<<<<< HEAD
    return ''.join(output)


def find_amino_acid_indices(seq: str, amino_acid: str) -> str:
    """
    Finds the amino acid indices specified in the input.

    Arguments:
    - seq (str): amino acid sequence. The input must be uppercased and use the single letter amino acid code.
    - amino_acid (str): amino acid for which indices need to be found.

    Returns:
    - output (str): all found indices in the protein for which the entered amino acid corresponds to.
    """
    indices = []
    if amino_acid not in seq:
        raise ValueError('Amino acid not found')
    for index, aa in enumerate(seq):
        if aa == amino_acid:
            indices.append(index+1)
    output = ', '.join(str(i) for i in indices)
    return output
=======
    return ' '.join(str(element) for element in output)
>>>>>>> 0b3071182dabcd72dc36c7b2d8c3c0ec01d0e14e
