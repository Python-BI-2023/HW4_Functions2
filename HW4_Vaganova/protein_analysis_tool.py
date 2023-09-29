from typing import Union, List

# three later and corresponding one letter names
RESIDUES_NAMES = {'ALA': 'A',
                  'ARG': 'R',
                  'ASN': 'N',
                  'ASP': 'D',
                  'CYS': 'C',
                  'GLN': 'Q',
                  'GLU': 'E',
                  'GLY': 'G',
                  'HIS': 'H',
                  'ILE': 'I',
                  'LEU': 'L',
                  'LYS': 'K',
                  'MET': 'M',
                  'PHE': 'F',
                  'PRO': 'P',
                  'SER': 'S',
                  'THR': 'T',
                  'TRP': 'W',
                  'TYR': 'Y',
                  'VAL': 'V'
                  }

# first value is hydrophobicity index, second is pKa (pKa1, pKa2, pKa3 respectively), third is molecular mass in Da
RESIDUES_CHARACTERISTICS = {'A': [1.8, [2.34, 9.69, 0], 89],
                            'R': [-4.5, [2.17, 9.04, 12.48], 174],
                            'N': [-3.5, [2.02, 8.80, 0], 132],
                            'D': [-3.5, [1.88, 9.60, 3.65], 133],
                            'C': [2.5, [1.96, 10.28, 8.18], 121],
                            'Q': [-3.5, [2.17, 9.13, 0], 146],
                            'E': [-3.5, [2.19, 9.67, 4.25], 147],
                            'G': [-0.4, [2.34, 9.60, 0], 75],
                            'H': [-3.2, [1.82, 9.17, 6.00], 155],
                            'I': [4.5, [2.36, 9.60, 0], 131],
                            'L': [3.8, [2.36, 9.60, 0], 131],
                            'K': [-3.9, [2.18, 8.95, 10.53], 146],
                            'M': [1.9, [2.28, 9.21, 0], 149],
                            'F': [2.8, [1.83, 9.13, 0], 165],
                            'P': [-1.6, [1.99, 10.60, 0], 115],
                            'S': [-0.8, [2.21, 9.15, 0], 105],
                            'T': [-0.7, [2.09, 9.10, 0], 119],
                            'W': [-0.9, [2.83, 9.39, 0], 204],
                            'Y': [-1.3, [2.20, 9.11, 0], 181],
                            'V': [4.2, [2.32, 9.62, 0], 117]}


def change_residues_encoding(seq: str, query: str = 'one') -> str:
    """
    Transfer amino acids from 3 letter to 1 letter and vice versa
    :param seq:
    :param query:
    :return:
    """
    pass


def get_seq_characteristic(seq: str) -> dict:
    res_count = {}
    for res in seq:
        res_count[[tl_code for tl_code in RESIDUES_NAMES if RESIDUES_NAMES[tl_code] == res][0]] = 0
    for res in seq:
        res_count[[tl_code for tl_code in RESIDUES_NAMES if RESIDUES_NAMES[tl_code] == res][0]] += 1
    return res_count


def find_res_in_seq(seq: str) -> str:
    pass


def find_site(seq: str, site: str) -> str:
    pass


def calculate_protein_mass(seq: str) -> float:
    total_mass = 0
    for res in seq:
        total_mass += RESIDUES_CHARACTERISTICS[res][2]
    return total_mass


def calculate_average_hydrophobicity(seq: str) -> float:
    sum_hydrophobicity_ind = 0
    for res in seq:
        sum_hydrophobicity_ind += RESIDUES_CHARACTERISTICS[res][0]
    return sum_hydrophobicity_ind / len(seq)


def get_mrna(seq: str) -> List[str]:
    pass


def calculate_isoelectric_point(seq: str) -> float:
    sum_pka = 0
    pka_amount = 0
    for ind, res in enumerate(seq, 1):
        if ind == 1:
            sum_pka += RESIDUES_CHARACTERISTICS[res][1][1]
            pka_amount += 1
        elif RESIDUES_CHARACTERISTICS[res][1][2] != 0:
            sum_pka += RESIDUES_CHARACTERISTICS[res][1][2]
            pka_amount += 1
        elif ind == len(seq):
            sum_pka += RESIDUES_CHARACTERISTICS[res][1][0]
            pka_amount += 1
    pi = sum_pka / pka_amount
    return pi
