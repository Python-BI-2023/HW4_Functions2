AMINO_ACIDS_NAMES = {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp', 'V': 'Val', 'H': 'His', 'G': 'Gly', 'Q': 'Gln',
                    'E': 'Glu', 'I': 'Ile', 'L': 'Leu', 'K': 'Lys', 'M': 'Met', 'P': 'Pro', 'S': 'Ser', 'Y': 'Tyr',
                    'T': 'Thr', 'W': 'Trp', 'F': 'Phe', 'C': 'Cys'}

GRAVY_AA_VALUES = {'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6, 'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3,
                   'V': 4.2, 'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5, 'Q': -3.5, 'E': -3.5, 'G': -0.4,
                   'H': -3.2, 'I': 4.5}


def calc_gravy(amino_ac_seq: str) -> float:
    """
    Calculate GRAVY (grand average of hydropathy) value
    of given amino acids sequence
    """
    gravy_aa_sum = 0
    for amino_ac in amino_ac_seq:
        gravy_aa_sum += GRAVY_AA_VALUES[amino_ac]
    return round(gravy_aa_sum / len(amino_ac_seq), 3)


def calc_total_charge(charged_amino_ac_numbers_list: list, pH_value: float) -> float:
    """
    Calculate the approximate total charge of some amino acid sequence
    for given pH value
    based only on a list of the number of key charged amino acids.
    """
    N_terminal_charge = 1 / (1 + 10 ** (pH_value - 8.2))
    C_terminal_charge = -1 / (1 + 10 ** (3.65 - pH_value))
    Cys_charge = -charged_amino_ac_numbers_list[0] / (1 + 10 ** (8.18 - pH_value))
    Asp_charge = -charged_amino_ac_numbers_list[1] / (1 + 10 ** (3.9 - pH_value))
    Glu_charge = -charged_amino_ac_numbers_list[2] / (1 + 10 ** (4.07 - pH_value))
    Tyr_charge = -charged_amino_ac_numbers_list[3] / (1 + 10 ** (10.46 - pH_value))
    His_charge = charged_amino_ac_numbers_list[4] / (1 + 10 ** (pH_value - 6.04))
    Lys_charge = charged_amino_ac_numbers_list[5] / (1 + 10 ** (pH_value - 10.54))
    Arg_charge = charged_amino_ac_numbers_list[6] / (1 + 10 ** (pH_value - 12.48))
    total_charge = (N_terminal_charge + C_terminal_charge + Cys_charge + Asp_charge + Glu_charge + Tyr_charge +
                    His_charge + Lys_charge + Arg_charge)
    return total_charge


def calc_iso_point(amino_ac_seq):
    """
    Calculate approximate isoelectric point of given amino acids sequence
    """
    charged_amino_ac_numbers = []
    for amino_ac in ("C", "D", "E", "Y", "H", "K", "R"):
        charged_amino_ac_numbers.append(amino_ac_seq.count(amino_ac))
    print(charged_amino_ac_numbers)
    total_charge_tmp = 1
    pH_iso_point = -0.1
    while total_charge_tmp > 0:
        pH_iso_point += 0.1
        total_charge_tmp = calc_total_charge(charged_amino_ac_numbers, pH_iso_point)
    return round(pH_iso_point, 1)


def transform_to_three_letter(sequence: str) -> str:
    """
    Transform 1-letter aminoacid symbols in
    sequence to 3-letter symbols separated by
    hyphens.
    """
    new_protein = ''
    for aminoacid in sequence:
        new_protein += AMINO_ACIDS_NAMES[aminoacid] + '-'
    return new_protein[:-1]


def sequence_length(sequence: str) -> int:
    """
    Function counts number of aminoacids in
    given sequence
    """
    return len(sequence)


def longest_sequence(sequences: list) -> str:
    """
    Function returns longest protein sequence,
    if there is only one sequence, function
    returns it.
    """
    sequences.sort(key = len, reverse = True)
    return sequences[0]

def calc_protein_mass(sequence: str) -> int: 
    """
    Calculate protein molecular weight using the average 
    molecular weight of amino acid - 110 Da
    """
    return len(sequence) * 110


def heaviest_protein(sequence: list):
    """
    Return the sequence of the heaviest protein from list
    """
    protein_mass = {}
    list_of_protein = sequence
    for i in list_of_protein:
        protein_mass[i] = calc_protein_mass(i)
    return f'{max(protein_mass, key=(lambda k:protein_mass[k]))} - {max(protein_mass.values())}'


def lightest_protein(sequence: list):
    """
    Return the sequence of the lightest protein from list
    """
    protein_mass = {}
    list_of_protein = sequence
    for i in list_of_protein:
        protein_mass[i] = calc_protein_mass(i)
    return f'{min(protein_mass, key=(lambda k:protein_mass[k]))} - {min(protein_mass.values())}'
