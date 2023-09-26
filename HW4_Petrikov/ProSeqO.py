AMINOACIDS_NAMES = {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp', 'V': 'Val', 'H': 'His', 'G': 'Gly', 'Q': 'Gln',
                    'E': 'Glu', 'I': 'Ile', 'L': 'Leu', 'K': 'Lys', 'M': 'Met', 'P': 'Pro', 'S': 'Ser', 'Y': 'Tyr',
                    'T': 'Thr', 'W': 'Trp', 'F': 'Phe', 'C': 'Cys'}

GRAVY_AA_VALUES = {'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6, 'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3,
                   'V': 4.2, 'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5,  'C': 2.5, 'Q': -3.5,  'E': -3.5, 'G': -0.4,
                   'H': -3.2, 'I': 4.5}


def calc_gravy(amino_ac_seq: str) -> float:
    """
    Calculate GRAVY (grand average of hydropathy) value
    for entered amino acids sequence
    """
    gravy_aa_sum = 0
    for amino_ac in amino_ac_seq:
        gravy_aa_sum += GRAVY_AA_VALUES[amino_ac]
    return round(gravy_aa_sum / len(amino_ac_seq), 3)


def transform_to_three_letter(sequence: str) -> str:
    '''
    Transform 1-letter aminoacid symbols in
    sequence to 3-letter symbols separated by
    hyphens.
    '''
    new_protein = ''
    for aminoacid in sequence:
        new_protein += AMINOACIDS_NAMES[aminoacid] + '-'
    return new_protein[:-1]


def sequence_length(sequence: str) -> int:
    '''
    Function counts number of aminoacids in
    inputed sequence
    '''
    return len(sequence)


def longest_sequence(sequences: list) -> str:
    '''
    Function returns longest protein sequence,
    if there is only one sequence, function
    returns it.
    '''
    sequences.sort(key=len, reverse=True)
    return sequences[0]
