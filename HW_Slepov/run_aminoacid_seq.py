def count_possible_number_of_disulfide_bonds(sequence: str) -> int:
    """
    takes an amino acid sequence as input and returns the
    number of possible combinations of two different cysteines to form a disulfide bond
    :param sequence: str
    :return: int
    """
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


def count_molecular_weight(sequence: str) -> int:
    """
    takes an amino acid sequence as input and returns the molecular weight of the protein
    :param sequence: str
    :return: int
    """
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


def convert_amino_acid_seq_to_dna(sequence: str) -> str:
    """
    takes an amino acid sequence as input and returns the optimal DNA sequence for E.coli
    :param sequence: str
    :return: str
    """
    most_frequent_codon_for_amino_acid_e_coli = {
        'A': 'GCT', 'R': 'CGT', 'N': 'AAC', 'D': 'GAC', 'C': 'TGC',
        'E': 'GAA', 'Q': 'CAG', 'G': 'GGC', 'H': 'CAC', 'I': 'ATC',
        'L': 'CTG', 'K': 'AAA', 'M': 'ATG', 'F': 'TTC', 'P': 'CCG',
        'S': 'TCT', 'T': 'ACC', 'W': 'TGG', 'Y': 'TAC', 'V': 'GTT',
        'a': 'gct', 'r': 'cgt', 'n': 'aac', 'd': 'gac', 'c': 'tgc',
        'e': 'gaa', 'q': 'cag', 'g': 'ggc', 'h': 'cac', 'i': 'atc',
        'l': 'ctg', 'k': 'aaa', 'm': 'atg', 'f': 'ttc', 'p': 'ccg',
        's': 'tct', 't': 'acc', 'w': 'tgg', 'y': 'tac', 'v': 'gtt'
    }
    # This function selects the optimal DNA sequence with which protein
    # will be produced in the E. coli bacterium. 
    # Codons are selected according to codon frequency.
    codon_str = ''
    for amin_acid in sequence:
        codon_str += most_frequent_codon_for_amino_acid_e_coli[amin_acid]
    return codon_str


def determine_charge(amino_seq: str, percent: bool=False) -> dict:
    
    """
    Takes a string (amino acid sequence),returns the number of positively,
    negatively and neutrally charged amino acids.

    Args:
    - amino_seq - amino acid sequence,
    - percent - optional argument (default False):
    percent = False - output in number of amino acids,
    percent = True - output as a percentage
    """

    dict_charge_acid = {
        'negative_charge': ['E', 'D', 'e', 'd'],
        'positive_charge': ['K', 'R', 'H', 'k', 'r', 'h'],
        'neutral_charge': ['V', 'W', 'P', 'w', 'v', 'p', 'i', 'F', 'f', 'm', 'A',
                           'a', 'L', 'M', 'l', 'I', 'S', 's', 'T', 't', 'N', 'n',
                           'Q', 'q', 'C', 'c', 'Y', 'y', 'G', 'g']}
    charge_amin_acid = []
    for amin_acid in amino_seq:
        for key, values in dict_charge_acid.items():
            if amin_acid in values:
                charge_amin_acid.append(key)
    amount_positive = charge_amin_acid.count('positive_charge')
    amount_neutral = charge_amin_acid.count('neutral_charge')
    amount_negative = charge_amin_acid.count('negative_charge')
    if percent:
        result_dict = {"Процентное содержание положительно заряженных аминокислот":
                           (round((amount_positive * 100) / len(amino_seq))),
                       "Процентное содержание нейтрально заряженных аминокислот":
                           (round((amount_neutral * 100) / len(amino_seq))),
                       "Процентное содержание отрицательно заряженных аминокислот":
                           (round((amount_negative * 100) / len(amino_seq)))}
    else:
        result_dict = {"Количество положительно заряженных аминокислот": amount_positive,
                       "Количество нейтрально заряженных аминокислот": amount_neutral,
                       "Количество отрицательно заряженных аминокислот": amount_negative}

    return result_dict


def determine_polarity(amino_seq: str, percent: bool=False) -> dict:

    """
    Takes a string (amino acid sequence),returns
    a dictionary with the number of hydrophobic and hydrophilic amino acids
    Args:
    - amino_seq - amino acid sequence,
    - percent - optional argument (default False):
    percent = False - output in number of amino acids,
    percent = True - output as a percentage
    """

    dict_class_acid = {
        'hydrophilic': ['t', 'q', 'r', 's', 'y', 'd', 'e', 'g',
                        'c', 'n', 'h', 'k', 'T', 'Q', 'R', 'S',
                        'Y', 'D', 'E', 'G', 'C', 'N', 'H', 'K'],
        'hydrophobic': ['V', 'W', 'P', 'w', 'v', 'p', 'i', 'F',
                        'f', 'm', 'A', 'a', 'L', 'M', 'l', 'I']}
    class_amin_acid = []
    for amin_acid in amino_seq:
        for key, values in dict_class_acid.items():
            if amin_acid in values:
                class_amin_acid.append(key)
    amount_hydrophilic = class_amin_acid.count('hydrophilic')
    amount_hydrophobic = class_amin_acid.count('hydrophobic')
    if percent:
        result_dict = {'Процентное содержание гидрофильных аминокислот':
                           (round((amount_hydrophilic * 100) / len(amino_seq), 2)),
                       'Процентное содержание гидрофобных аминокислот':
                           (round((amount_hydrophobic * 100) / len(amino_seq), 2))}
    else:
        result_dict = {'Количество гидрофильных аминокислот': amount_hydrophilic,
                       'Количество гидрофобных аминокислот': amount_hydrophobic}
    return result_dict


def translate(sequence:str, record_type:int):
    "converts one record type to another"
    aminoacid_dict = {
        'GLY':'G', 'ALA':'A', 'VAL':'V', 'LEU':'L', 'ILE':'I', 'MET':'M',
        'PRO':'P', 'PHE':'F', 'TRP':'W', 'SER':'S', 'THR':'T', 'ASN':'N', 'GLN':'Q',
        'TYR':'Y', 'CYS':'C', 'LYS':'K', 'ARG':'R', 'HIS':'H', 'ASP':'D', 'GLU':'E',
        'gly':'g', 'ala':'a', 'val':'v', 'leu':'l', 'ile':'i', 'met':'m', 
        'pro':'p', 'phe':'f', 'trp':'w', 'ser':'s', 'thr':'t', 'asn':'n', 'gln':'q',
        'tyr':'y', 'cys':'c', 'lys':'k', 'arg':'r', 'his':'h', 'asp':'d', 'glu':'e',       
    }   
    if record_type == 1:
        translate_seq = ''
        for amino_acid in sequence:
            for k, v in aminoacid_dict.items():
                if amino_acid == v:
                    translate_seq += k
        return translate_seq
    else: 
        tuple_sequence = [sequence[i:i + 3] for i in range(0, len(sequence), 3)]
        translate_seq = ''
        for amino_acid in tuple_sequence:
            for k, v in aminoacid_dict.items():
                if amino_acid == k:
                    translate_seq += v
        return translate_seq


def count(sequence:str, record_type:int):
    "counts number of amino acid"
    if record_type == 1:
        return len(sequence)
    elif record_type == 3:
        tuple_sequence = [sequence[i:i + 3] for i in range(0, len(sequence), 3)]
        return len(tuple_sequence)


def summary(sequence:str, record_type:int):
    "returns results of all functions"
    sum = {
        'count': count(sequence, record_type),
        'translate': translate(sequence, record_type),
        'determine_polarity': determine_polarity(translate(sequence, record_type), percent) if record_type == 3 else determine_polarity(sequence, percent),
        'determine_charge': determine_charge(translate(sequence, record_type), percent) if record_type == 3 else determine_charge(sequence, percent),
        'count_molecular_weight':count_molecular_weight(translate(sequence, record_type)) if record_type == 3 else count_molecular_weight(sequence),
        'count_possible_number_of_disulfide_bonds':count_possible_number_of_disulfide_bonds(translate(sequence, record_type)) if record_type == 3 else count_possible_number_of_disulfide_bonds(sequence),
        'convert_amino_acid_seq_to_dna':convert_amino_acid_seq_to_dna(translate(sequence, record_type)) if record_type == 3 else convert_amino_acid_seq_to_dna(sequence),
            
    }
    return sum

    
def run_aminoacid_seq(sequence:str, function:str = 'summary', record_type:int = 1, percent:bool = False):
    """
    Performs the following list of operations:
    count - counts number of amino acid
    translate - converts one record type to another
    determine_charge - counts number or percent of amino acid with different charges
    determine_polarity - counts number or percent of amino acid with different polarity
    convert_amino_acid_seq_to_dna - takes an amino acid sequence as input and returns the optimal DNA sequence for E.coli
    count_possible_number_of_disulfide_bonds - counting the number of possible combinations of two different cysteines to form a disulfide bond
    count_molecular_weight - takes an amino acid sequence as input and returns the molecular weight of the protein
    summary - returns results of all functions (default)

    Arguments:
    - sequence:str - sequence for function
    - function:str - name of the function you need to perform. You can use: 'count', 'translate', 'summary'(default)
    - record_type:int - record type of your sequence. You can use 1(default) for single letter type or 3 for three letter type
    - percent: bool - for determine_charge and determine_polarity shows result in percent (True) or in number (False). Default - False
    
    Return:
    - count - int
    - translate - str
    - determine_charge - dict
    - determine_polarity - dict
    - convert_amino_acid_seq_to_dna - str
    - count_possible_number_of_disulfide_bonds - int
    - count_molecular_weight - int
    - summary - dict
    
    """
    single_letter_alphabet = {'G', 'A', 'V', 'L', 'I', 'M', 'P', 'F', 'W', 'S', 'T', 'N', 'Q', 'Y', 'C', 'K', 'R', 'H', 'D', 'E', 
                              'g', 'a', 'v', 'l', 'i', 'm', 'p', 'f', 'w', 's', 't', 'n', 'q', 'y', 'c', 'k', 'r', 'h', 'd', 'e'}
    three_letter_alphabet = {'GLY', 'ALA', 'VAL', 'LEU', 'ILE', 'MET', 'PRO', 'PHE', 'TRP', 'SER', 'THR', 'ASN', 'GLN', 'TYR', 'CYS', 'LYS', 'ARG', 'HIS', 'ASP', 'GLU', 
                             'gly', 'ala', 'val', 'leu', 'ile', 'met', 'pro', 'phe', 'trp', 'ser', 'thr', 'asn', 'gln', 'tyr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu',
                             }
    sequence = str(sequence)
    if record_type == 1:
        for amino_acid in sequence:
            if amino_acid not in single_letter_alphabet:
                raise ValueError(amino_acid + ' in your sequence is not amino acid')
    elif record_type == 3:
        tuple_sequence = [sequence[i:i + 3] for i in range(0, len(sequence), 3)]
        for amino_acid in tuple_sequence:
            if amino_acid not in three_letter_alphabet:
                raise ValueError(amino_acid + ' is not amino acid')
        sequence = ''.join(tuple_sequence)
    if function == 'count':
        return count(sequence, record_type)
    elif function == 'translate':
        return translate(sequence, record_type)
    elif function == 'summary':
        return summary(sequence, record_type)
    elif function == 'determine_polarity':
        if record_type == 3:
            return determine_polarity(translate(sequence, record_type), percent)
        else: return determine_polarity(sequence)
    elif function == 'determine_charge':
        if record_type == 3:
            return determine_charge(translate(sequence, record_type), percent)
        else: return determine_charge(sequence)
    elif function == 'count_possible_number_of_disulfide_bonds':
        if record_type == 3:
            return count_possible_number_of_disulfide_bonds(translate(sequence, record_type))
        else: return count_possible_number_of_disulfide_bonds(sequence)
    elif function == 'count_molecular_weight':
        if record_type == 3:
            return count_molecular_weight(translate(sequence, record_type))
        else: return count_molecular_weight(sequence)
    elif function == 'convert_amino_acid_seq_to_dna':
        if record_type == 3:
            return convert_amino_acid_seq_to_dna(translate(sequence, record_type))
        else: return convert_amino_acid_seq_to_dna(sequence)
