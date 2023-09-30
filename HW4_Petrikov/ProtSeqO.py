AMINO_ACIDS_NAMES = {'A': 'Ala',
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
                     'C': 'Cys'}

GRAVY_AA_VALUES = {'L': 3.8,
                   'K': -3.9,
                   'M': 1.9,
                   'F': 2.8,
                   'P': -1.6,
                   'S': -0.8,
                   'T': -0.7,
                   'W': -0.9,
                   'Y': -1.3,
                   'V': 4.2,
                   'A': 1.8,
                   'R': -4.5,
                   'N': -3.5,
                   'D': -3.5,
                   'C': 2.5,
                   'Q': -3.5,
                   'E': -3.5,
                   'G': -0.4,
                   'H': -3.2,
                   'I': 4.5}

VALID_SYMBOLS = set(AMINO_ACIDS_NAMES)


def calc_gravy(seq: str) -> float:
    """
    Calculate GRAVY (grand average of hydropathy) value
    of given amino acids sequence
    """
    gravy_aa_sum = 0
    for amino_ac in seq:
        gravy_aa_sum += GRAVY_AA_VALUES[amino_ac]
    return round(gravy_aa_sum / len(seq), 3)


def calc_total_charge(charged_amino_ac_numbers_list: list,
                      ph_value: float) -> float:
    """
    Calculate the approximate total charge of some amino acid sequence
    for given pH value
    based only on a list of the number of key charged amino acids.
    """
    n_terminal_charge = 1 / (1 + 10 ** (ph_value - 8.2))
    c_terminal_charge = -1 / (1 + 10 ** (3.65 - ph_value))
    cys_charge = -charged_amino_ac_numbers_list[0] / (1 + 10 ** (8.18 - ph_value))
    asp_charge = -charged_amino_ac_numbers_list[1] / (1 + 10 ** (3.9 - ph_value))
    glu_charge = -charged_amino_ac_numbers_list[2] / (1 + 10 ** (4.07 - ph_value))
    tyr_charge = -charged_amino_ac_numbers_list[3] / (1 + 10 ** (10.46 - ph_value))
    his_charge = charged_amino_ac_numbers_list[4] / (1 + 10 ** (ph_value - 6.04))
    lys_charge = charged_amino_ac_numbers_list[5] / (1 + 10 ** (ph_value - 10.54))
    arg_charge = charged_amino_ac_numbers_list[6] / (1 + 10 ** (ph_value - 12.48))
    total_charge = (n_terminal_charge +
                    c_terminal_charge +
                    cys_charge +
                    asp_charge +
                    glu_charge +
                    tyr_charge +
                    his_charge +
                    lys_charge +
                    arg_charge)
    return total_charge


def calc_iso_point(seq: str):
    """
    Calculate approximate isoelectric point of given amino acids sequence
    """
    charged_amino_ac_numbers = []
    for amino_ac in ("C", "D", "E", "Y", "H", "K", "R"):
        charged_amino_ac_numbers.append(seq.count(amino_ac))
    total_charge_tmp = 1
    ph_iso_point = -0.1
    while total_charge_tmp > 0:
        ph_iso_point += 0.1
        total_charge_tmp = calc_total_charge(
            charged_amino_ac_numbers,
            ph_iso_point)
    return round(ph_iso_point, 1)


def transform_to_three_letters(seq: str) -> str:
    """
    Transform 1-letter aminoacid symbols in
    sequence to 3-letter symbols separated by
    hyphens.
    """
    new_name = ''
    for amino_acid in seq:
        new_name += AMINO_ACIDS_NAMES[amino_acid] + '-'
    return new_name[:-1]


def sequence_length(seq: str) -> int:
    """
    Function counts number of aminoacids in
    given sequence
    """
    return len(seq)


def calc_protein_mass(seq: str) -> int:
    """
    Calculate protein molecular weight using the average
    molecular weight of amino acid - 110 Da
    """
    return len(seq) * 110


def find_heaviest_proteins(sequence: list):
    """
    Return the sequence of the heaviest protein from list
    """
    protein_mass = {}
    list_of_protein = sequence
    for i in list_of_protein:
        protein_mass[i] = calc_protein_mass(i)
    return count_uniq_max_mass(protein_mass)


def count_uniq_max_mass(protein_mass):
    """
    Count amount of proteins with the same maximum mass and return them
    """
    max_weight = max(protein_mass.values())
    count_protein = 0
    proteins = []
    for i in protein_mass:
        if protein_mass[i] == max_weight:
            count_protein += 1
            if count_protein >= 1:
                proteins.append(i)

    return f'{proteins} - {max_weight}'


def find_lightest_proteins(sequence: list):
    """
    Return the sequence of the lightest protein from list
    """
    protein_mass = {}
    list_of_protein = sequence
    for i in list_of_protein:
        protein_mass[i] = calc_protein_mass(i)
    return count_uniq_min_mass(protein_mass)


def count_uniq_min_mass(protein_mass):
    """
    Count amount of proteins with the same minimum mass and return them
    """
    min_weight = min(protein_mass.values())
    count_protein = 0
    proteins = []
    for i in protein_mass:
        if protein_mass[i] == min_weight:
            count_protein += 1
            if count_protein >= 1:
                proteins.append(i)
    return f'{proteins} - {min_weight}'


def check_sequences(seqs: list):
    """
    Raise ValueError if at least one sequence
    contains non valid symbols
    """
    if not (isinstance(seqs, list)):
        raise ValueError("Enter valid protein sequence")
    for seq in seqs:
        if (not (isinstance(seq, str))) or (not (set(seq.upper()).issubset(VALID_SYMBOLS))):
            raise ValueError("Enter valid protein sequence")


# Didn't place at the beginning because the functions are defined above
FUNC_STR_INPUT = {
    'gravy': calc_gravy,
    'iso': calc_iso_point,
    'rename': transform_to_three_letters,
    'lengths': sequence_length,
    'molw': calc_protein_mass}

FUNC_LIST_INPUT = {
    'heavy': find_heaviest_proteins,
    'light': find_lightest_proteins}


def process_seqs(option: str, seqs: list):
    """
    Perform some simple operations on amino acids sequences.
    """
    if isinstance(seqs, str):
        seq_tmp = seqs
        seqs = [seq_tmp]
    check_sequences(seqs)
    if option in FUNC_STR_INPUT.keys():
        results = []
        for seq in seqs:
            result_tmp = FUNC_STR_INPUT[option](seq.upper())
            results.append(result_tmp)
        return results
    elif option in FUNC_LIST_INPUT.keys():
        return FUNC_LIST_INPUT[option](seqs)
    else:
        raise ValueError("Enter valid operation")
