def protein(*args: list, operator: str, cell_type=None) -> list:
    """
    Function protein does:
    -calculate predicted molecular weight of amino acid (aa) sequences in kDa (procedure name: molecular_weight)
    -translate aa sequences from one-letter to three-letter code
    -
    -
    -
    -

    Arguments:
    -
    -

    Return:
    - list, the result of the operation
    """
    aa_seqs = []
    procedure = operator
    procedures = ('molecular_weight', 'one_letter_to_three', 'get_amino_acid_sum', 'codon_optimization')

    for index in range(len(args)):
        aa_seqs.append(args[index])

    for aa_seq in aa_seqs:
        validate(aa_seq)

    if procedure not in procedures:
        raise ValueError('Requested procedure is not defined')

    if procedure == 'molecular_weight':
        return molecular_weight(aa_seqs)

    if procedure == 'one_letter_to_three':
        return one_letter_to_three(aa_seqs)

    if procedure == 'get_amino_acid_sum':
        return get_amino_acid_sum(aa_seqs)

    if procedure == 'codon_optimization':
        return codon_optimization(aa_seqs)

def validate(aa_seq: str) -> None:
    """Validates if aa sequence consists of only amino acid characters"""
    aa_seq_set = set(aa_seq.upper())
    all_aa = {'A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'}
    difference = aa_seq_set.difference(all_aa)
    if len(difference) > 0:
        raise ValueError('Invalid alphabet, please use only single letter amino acid code')


def molecular_weight(aa_seqs: list) -> list:
    """Calculates predicated molecular weight of aa sequences. Returns list of floats"""
    aa_weights = {
            'A': 89.09,
            'R': 174.20,
            'N': 132.12,
            'D': 133.10,
            'C': 121.16,
            'E': 147.13,
            'Q': 146.15,
            'G': 75.07,
            'H': 155.16,
            'I': 131.18,
            'L': 131.18,
            'K': 146.19,
            'M': 149.21,
            'F': 165.19,
            'P': 115.13,
            'S': 105.09,
            'T': 119.12,
            'W': 204.23,
            'Y': 181.19,
            'V': 117.15
        }
    molecular_weights = []
    for seq in aa_seqs:
        total_weight = 0
        for aa in seq:
            aa = aa.upper()
            total_weight += aa_weights[aa]
        molecular_weights.append(round(total_weight/1000, 2))
    return molecular_weights


def one_letter_to_three(aa_seqs: list) -> list:
    """Translates one letter coded aa sequences to three letter coded"""
    three_letter_codes = {
        'A': 'Ala',
        'R': 'Arg',
        'N': 'Asn',
        'D': 'Asp',
        'C': 'Cys',
        'E': 'Glu',
        'Q': 'Gln',
        'G': 'Gly',
        'H': 'His',
        'I': 'Ile',
        'L': 'Leu',
        'K': 'Lys',
        'M': 'Met',
        'F': 'Phe',
        'P': 'Pro',
        'S': 'Ser',
        'T': 'Thr',
        'W': 'Trp',
        'Y': 'Tyr',
        'V': 'Val'
    }
    three_letters_seqs = []
    for seq in aa_seqs:
        three_letters_seq = []
        for aa in seq:
            aa = aa.upper()
            three_letters_seq.append(three_letter_codes[aa])
        three_letters_seqs.append(''.join(three_letters_seq))
    return three_letters_seqs
