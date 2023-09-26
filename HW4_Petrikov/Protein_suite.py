AMINOACIDS_NAMES = {
    'A': 'Ala',
    'R': 'Arg',
    'N': 'Asn',
    'D': 'Asp',
    'V': 'Val',
    'H': 'His',
    'G': 'Gly',
    'Q': 'Gln',
    'E': 'Glu',
    'I': 'Ile',
    'L': 'Leu',
    'K': 'Lys',
    'M': 'Met',
    'P': 'Pro',
    'S': 'Ser',
    'Y': 'Tyr',
    'T': 'Thr',
    'W': 'Trp',
    'F': 'Phe',
    'C': 'Cys'
}


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
