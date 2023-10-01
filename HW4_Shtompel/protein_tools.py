"""
Global variables:
- AA_ALPHABET — a dictionary variable that contains a list of proteinogenic aminoacids classes.
- ALL_AMINOACIDS — a set variable that contains a list of all proteinogenic aminoacids.
- FEATURE_FUNCTIONS — a list of available functions of the feature.
- AMINO_ACIDS_MASSES — a dictionary variable that contains masses of all proteinogenic aminoacids.
"""

AA_ALPHABET = {'Nonpolar': ['G', 'A', 'V', 'I', 'L', 'P'],
                'Polar uncharged': ['S', 'T', 'C', 'M', 'N', 'Q'],
                'Aromatic': ['F', 'W', 'Y'],
                'Polar with negative charge': ['D', 'E'],
                'Polar with positive charge': ['K', 'R', 'H']
                }

ALL_AMINOACIDS = set(('G', 'A', 'V', 'I', 'L', 'P', 'S', 'T', 'C', 'M', 'N', 'Q', 'F', 'W', 'Y', 'D', 'E', 'K', 'R', 'H'))

AMINO_ACIDS_MASSES = {
    'G': 57.05, 'A': 71.08, 'S': 87.08, 'P': 97.12, 'V': 99.13,
    'T': 101.1, 'C': 103.1, 'L': 113.2, 'I': 113.2, 'N': 114.1,
    'D': 115.1, 'Q': 128.1, 'K': 128.2, 'E': 129.1, 'M': 131.2,
    'H': 137.1, 'F': 147.2, 'R': 156.2, 'Y': 163.2, 'W': 186.2    
}


def is_protein(seq: str) -> bool:
    """
    Input: a protein sequence (a str type).
    Output: boolean value.
    'is_protein' function check if the sequence contains only letters in the upper case.
    """
    if seq.isalpha() and seq.isupper():
        return True


def count_seq_length(seq: str) -> int:
    """
    Input: a protein sequence (a str type).
    Output: length of protein sequence (an int type).
    'count_seq_length' function counts the length of protein sequence.
    """
    return len(seq)


def classify_aminoacids(seq: str) -> dict:
    """
    Input: a protein sequence (a str type).
    Output: a classification of all aminoacids from the sequence (a dict type — 'all_aminoacids_classes' variable).
    'classify_aminoacids' function classify all aminoacids from the input sequence in accordance with the 'AA_ALPHABET' classification. If aminoacid is not included in this list,
    it should be classified as 'Unusual'.
    """
    all_aminoacids_classes = dict.fromkeys(['Nonpolar', 'Polar uncharged', 'Aromatic', 'Polar with negative charge', 'Polar with positive charge', 'Unusual'], 0)
    for aminoacid in seq:
        aminoacid = aminoacid.upper()
        if aminoacid not in ALL_AMINOACIDS:
            all_aminoacids_classes['Unusual'] += 1
        for aa_key, aa_value in AA_ALPHABET.items():
            if aminoacid in aa_value:
                all_aminoacids_classes[aa_key] += 1
    return all_aminoacids_classes


def check_unusual_aminoacids(seq: str) -> str:
    """
    Input: a protein sequence (a str type).
    Output: an answer whether the sequense contains unusual aminoacids (a str type).
    'check_unusual_aminoacids' function checks the composition of aminoacids and return the list of unusual aminoacids if they present in the sequence. We call the aminoacid
    unusual when it does not belong to the list of proteinogenic aminoacids (see 'ALL_AMINOACIDS' global variable).
    """
    seq_aminoacids = set()
    for aminoacid in seq:
        aminoacid = aminoacid.upper()
        seq_aminoacids.add(aminoacid)
    if seq_aminoacids <= ALL_AMINOACIDS:
        return 'This sequence contains only proteinogenic aminoacids.'
    else:
        unusual_aminoacids = seq_aminoacids - ALL_AMINOACIDS
        unusual_aminoacids_str = ''
        for elem in unusual_aminoacids:
            unusual_aminoacids_str += elem
            unusual_aminoacids_str += ', '
        return f'This protein contains unusual aminoacids: {unusual_aminoacids_str[:-2]}.'


def count_charge(seq: str) -> int:
    """
    Input: a protein sequence (a str type).
    Output: a charge of the sequence (an int type).
    'count_charge' function counts the charge of the protein by the subtraction between the number of positively and negatively charged aminoacids.
    """
    seq_classes = classify_aminoacids(seq)
    positive_charge = seq_classes['Polar with positive charge']
    negative_charge = seq_classes['Polar with negative charge']
    sum_charge = positive_charge - negative_charge
    return sum_charge


def count_protein_mass(seq: str, kda_scale = False) -> float:
    """
    Calculates mass of all aminoacids of input peptide in g/mol or KDa scale.
    Arguments:
    - seq (str): one-letter code peptide sequence, case is not important;
    - kda_scale (bool): if True converts peptide mass into kDa scale (1KDa = 1000g/mol).
    Output:
    Returns mass of peptide (float).
    """
    aa_mass = 0
    for aminoacid in seq.upper():
        if aminoacid in AMINO_ACIDS_MASSES:
            aa_mass += AMINO_ACIDS_MASSES[aminoacid]
    if kda_scale is True:
        kda = round(aa_mass / 1000, 1)
        return kda
    return aa_mass


def count_aliphatic_index(seq: str) -> float:
    """
    Calculates aliphatic index - relative proportion of aliphatic aminoacids in input peptide.
    The higher aliphatic index the higher thermostability of peptide.
    Argument:
    - seq (str): one-letter code peptide sequence, letter case is not important.
    Output:
    Returns alipatic index (float).
    """
    ala_count = seq.count('A') / len(seq)
    val_count = seq.count('V') / len(seq)
    lei_count = seq.count('L') / len(seq)
    izlei_count = seq.count('I') / len(seq)
    aliph_index = ala_count + 2.9 * val_count + 3.9 * lei_count + 3.9 * izlei_count
    return aliph_index


def not_trypsin_cleaved(seq: str) -> int:
    """
    Counts non-cleavable sites of trypsin: Arginine/Proline (RP) and Lysine/Proline (KP) pairs.
    Argument:
    - seq (str): one-letter code peptide sequence, case is not important.
    Output:
    Returns number of exception sites that cannot be cleaved by trypsin (int).
    """
    not_cleavage_count = 0
    not_cleavage_count += seq.upper().count('RP')
    not_cleavage_count += seq.upper().count('KP')
    return not_cleavage_count


def count_trypsin_sites(seq: str) -> int:
    """
    Counts number of valid trypsin cleavable sites:
    Arginine/any aminoacid and Lysine/any aminoacid (except Proline).
    Argument:
    - seq (str): one-letter code peptide sequence, case is not important.
    Output:
    Returns number of valid trypsin cleavable sites (int).
    If peptide has not any trypsin cleavable sites, it will return zero.
    """
    arginine_value = seq.upper().count('R')
    lysine_value = seq.upper().count('K')
    count_cleavage = arginine_value + lysine_value - not_trypsin_cleaved(seq)
    return count_cleavage
  

OPERATIONS = {'count_protein_mass':count_protein_mass,
             'count_aliphatic_index': count_aliphatic_index,
             'count_trypsin_sites': count_trypsin_sites,
             'count_seq_length': count_seq_length,
             'classify_aminoacids': classify_aminoacids,
             'check_unusual_aminoacids': check_unusual_aminoacids,
             'count_charge': count_charge}

def protein_tools(*args):
    """
    Input: a list of protein sequences and one procedure that should be done with these sequences (str type, several values).
    Output: a list of outputs from the chosen procedure (list type).
    'run_protein_tools' function take the protein sequences and the name of the procedure that the user gives and applies this procedure by one of the available functions
    to all the given sequences. Also this function check the availabilaty of the procedure and raise the ValueError when the procedure is not in the list of available
    functions (see 'FEATURE_FUNCTIONS' global variable).
    """
    operation = args[-1]
    parsed_seq_list = []
    for seq in args[0:-1]:
        if not is_protein(seq):
            raise ValueError("One of these sequences is not protein sequence or does not match the rools of input. Please select another sequence.")
        else:
            if operation in OPERATIONS:
                parsed_seq_list.append(OPERATIONS[operation](seq))
            else:
                raise ValueError("This procedure is not available. Please choose another procedure.")
    return parsed_seq_list
