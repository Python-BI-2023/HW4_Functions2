from typing import List

def is_aa(seq: str) -> bool:
    """
    Check if a sequence contains only amino acids.

    Args:
        seq (str): The input sequфence to be checked.

    Returns:
        bool: True if the sequence contains only amino acids, False otherwise.
    """
    aa_list = ['V', 'I', 'L', 'E', 'Q', 'D', 'N', 'H', 'W', 'F', 'Y', 'R', 'K', 'S', 'T', 'M', 'A', 'G', 'P', 'C',
               'v', 'i', 'l', 'e', 'q', 'd', 'n', 'h', 'w', 'f', 'y', 'r', 'k', 's', 't', 'm', 'a', 'g', 'p', 'c']
    unique_chars = set(seq)
    amino_acids = set(aa_list)
    return unique_chars <= amino_acids



def choose_weight(weight: str) -> List[float]:
    """
    Choose the weight type of amino acids - average or monoisotopic.

    Args:
        weight (str): The type of weight to choose, either 'average' or 'monoisotopic'.

    Returns:
        List[float]: A list of amino acid weights based on the chosen type.
    """
    if weight == 'average':
        average_weights = [71.0788, 156.1875, 114.1038, 115.0886, 103.1388, 129.1155, 128.1307, 57.0519, 137.1411, 113.1594,
                           113.1594, 128.1741, 131.1926, 147.1766, 97.1167, 87.0782, 101.1051, 186.2132, 163.1760, 99.1326]
        weights_aa = average_weights
    elif weight == 'monoisotopic':
        monoisotopic_weights = [71.03711, 156.10111, 114.04293, 115.02694, 103.00919, 129.04259, 128.05858, 57.02146, 137.05891, 113.08406,
                                113.08406, 128.09496, 131.04049, 147.06841, 97.05276, 87.03203, 101.04768, 186.07931, 163.06333, 99.06841]
        weights_aa = monoisotopic_weights
    else:
        raise ValueError(f"I do not know what '{weight}' is :( \n Read help or just do not write anything except your sequence")

    return weights_aa


def aa_weight(seq: str, weight: str = 'average') -> float:
    """
    Calculate the amino acids weight in a protein sequence.

    Args:
        seq (str): The amino acid sequence to calculate the weight for.
        weight (str, optional): The type of weight to use, either 'average' or 'monoisotopic'. Default is 'average'.

    Returns:
        float: The calculated weight of the amino acid sequence.
    """
    aa_list = str('A, R, N, D, C, E, Q, G, H, I, L, K, M, F, P, S, T, W, Y, V').split(', ')
    weights_aa = choose_weight(weight)
    aa_to_weight = dict(zip(aa_list, weights_aa))
    final_weight = 0
    for i in seq.upper():
        final_weight += aa_to_weight.get(i, 0)
    return round(final_weight, 3)


def count_hydroaffinity(seq: str) -> tuple:
    """
    Count the quantity of hydrophobic and hydrophilic amino acids in a protein sequence.

    Args:
        seq (str): The protein sequence for which to count hydrophobic and hydrophilic amino acids.

    Returns:
        tuple: A tuple containing the count of hydrophobic and hydrophilic amino acids, respectively.
    """
    hydrophobic_aa = ['A', 'V', 'L', 'I', 'P', 'F', 'W', 'M']
    hydrophilic_aa = ['R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'K', 'S', 'T', 'Y']
    
    hydrophobic_count = 0
    hydrophilic_count = 0
    
    seq = seq.upper()
    
    for aa in seq:
        if aa in hydrophobic_aa:
            hydrophobic_count += 1
        elif aa in hydrophilic_aa:
            hydrophilic_count += 1
    
    return hydrophobic_count, hydrophilic_count


def peptide_cutter(sequence: str, enzyme: str = "trypsin") -> str:
    """
    This function identifies cleavage sites in a given peptide sequence using a specified enzyme.
    
    Args:
        sequence (str): The input peptide sequence.
        enzyme (str): The enzyme to be used for cleavage. Choose between "trypsin" and "chymotrypsin". Default is "trypsin".
        
    Returns:
        str: A message indicating the number and positions of cleavage sites, or an error message if an invalid enzyme is provided.
    """
    cleavage_sites = []
    if enzyme not in ("trypsin", "chymotrypsin"):
        return "You have chosen an enzyme that is not provided. Please choose between trypsin and chymotrypsin."
    
    if enzyme == "trypsin":  # Trypsin cuts peptide chains mainly at the carboxyl side of the amino acids lysine or arginine.
        for i in range(len(sequence)-1):
            if sequence[i] in ['K', 'R', 'k', 'r'] and sequence[i+1] not in ['P','p']:
                cleavage_sites.append(i+1)
    
    if enzyme == "chymotrypsin":  # Chymotrypsin preferentially cleaves at Trp, Tyr and Phe in position P1(high specificity) 
        for i in range(len(sequence)-1):
            if sequence[i] in ['W', 'Y', 'F', 'w', 'y', 'f'] and sequence[i+1] not in ['P','p']:
                cleavage_sites.append(i+1)
    
    if cleavage_sites:
        return f"Found {len(cleavage_sites)} {enzyme} cleavage sites at positions {', '.join(map(str, cleavage_sites))}"
    else:
        return f"No {enzyme} cleavage sites were found."
        

def one_to_three_letter_code(sequence: str) -> str:
    """
    This function converts a protein sequence from one-letter amino acid code to three-letter code.
    
    Args:
        sequence (str): The input protein sequence in one-letter code.
        
    Returns:
        str: The converted protein sequence in three-letter code.
    """
    amino_acids = {
        'A': 'Ala', 'C': 'Cys', 'D': 'Asp', 'E': 'Glu', 'F': 'Phe',
        'G': 'Gly', 'H': 'His', 'I': 'Ile', 'K': 'Lys', 'L': 'Leu',
        'M': 'Met', 'N': 'Asn', 'P': 'Pro', 'Q': 'Gln', 'R': 'Arg',
        'S': 'Ser', 'T': 'Thr', 'V': 'Val', 'W': 'Trp', 'Y': 'Tyr'
    }
    
    three_letter_code = [amino_acids.get(aa.upper()) for aa in sequence]
    
    return ''.join(three_letter_code)

def sulphur_containing_aa_counter(sequence):
    """
    This function counts sulphur-containing amino acids in a protein sequence.
    
    Args:
        sequence (str): The input protein sequence in one-letter code.
        
    Returns:
        str: The number of sulphur-containing amino acids in a protein sequence.
    """
    counter = 0
    for i in sequence:
        if i == 'C' or i == 'M':
            counter += 1
    answer = str(counter)
    return 'The number of sulphur-containing amino acids in the sequence is equal to ' + answer

def run_amino_analyzer(sequence, procedure, *, weight_type = 'average'):
    """
    This is the main function to run the amino-analyzer.py tool.
    
    Args:
        sequence (str): The input protein sequence in one-letter code.
        procedure (str): amino-analyzer.py tool has 5 functions at all:
            1. aa_weight - Calculate the amino acids weight in a protein sequence.
            2. count_hydroaffinity - Count the quantity of hydrophobic and hydrophilic amino acids in a protein sequence.
            3. peptide_cutter - This function identifies cleavage sites in a given peptide sequence using a specified enzyme.
            4. one_to_three_letter_code - This function converts a protein sequence from one-letter amino acid code to three-letter code.
            5. sulphur_containing_aa_counter - This function counts sulphur-containing amino acids in a protein sequence.
        weight_type = 'average': default argument for 'aa_weight' function. weight_type = 'monoisotopic' can be used as a second option.
        
    Returns:
        The result of the procedure.
    """

    procedures = ['aa_weight', 'count_hydroaffinity', 'peptide_cutter', 'one_to_three_letter_code', 'sulphur_containing_aa_counter']
    if procedure not in procedures:
        raise ValueError(f"Incorrect procedure. Acceptable procedures: {', '.join(procedures)}")

    for i in sequence:
        if not is_aa(sequence):
            raise ValueError("Incorrect sequence. Only amino acids are allowed (V, I, L, E, Q, D, N, H, W, F, Y, R, K, S, T, M, A, G, P, C, v, i, l, e, q, d, n, h, w, f, y, r, k, s, t, m, a, g, p, c).")

    if procedure == 'aa_weight':
        result = aa_weight(sequence, weight_type)
    elif procedure == 'count_hydroaffinity':
        result = count_hydroaffinity(sequence)
    elif procedure == 'peptide_cutter':
        result = peptide_cutter(sequence)
    elif procedure == 'one_to_three_letter_code':
        result = one_to_three_letter_code(sequence)
    elif procedure == 'sulphur_containing_aa_counter':
        result = sulphur_containing_aa_counter(sequence)
    return result


def peptide_cutter(sequence: str, enzyme: str = "trypsin") -> str:
    """
    This function identifies cleavage sites in a given peptide sequence using a specified enzyme.
    
    Args:
        sequence (str): The input peptide sequence.
        enzyme (str): The enzyme to be used for cleavage. Choose between "trypsin" and "chymotrypsin". Default is "trypsin".
        
    Returns:
        str: A message indicating the number and positions of cleavage sites, or an error message if an invalid enzyme is provided.
    """
    cleavage_sites = []
    if enzyme not in ("trypsin", "chymotrypsin"):
        return "You have chosen an enzyme that is not provided. Please choose between trypsin and chymotrypsin."
    
    if enzyme == "trypsin":  # Trypsin cuts peptide chains mainly at the carboxyl side of the amino acids lysine or arginine.
        for i in range(len(sequence)-1):
            if sequence[i] in ['K', 'R', 'k', 'r'] and sequence[i+1] not in ['P','p']:
                cleavage_sites.append(i+1)
    
    if enzyme == "chymotrypsin":  # Chymotrypsin preferentially cleaves at Trp, Tyr and Phe in position P1(high specificity) 
        for i in range(len(sequence)-1):
            if sequence[i] in ['W', 'Y', 'F', 'w', 'y', 'f'] and sequence[i+1] not in ['P','p']:
                cleavage_sites.append(i+1)
    
    if cleavage_sites:
        return f"Found {len(cleavage_sites)} {enzyme} cleavage sites at positions {', '.join(map(str, cleavage_sites))}"
    else:
        return f"No {enzyme} cleavage sites were found."


def one_to_three_letter_code(sequence: str) -> str:
    """
    This function converts a protein sequence from one-letter amino acid code to three-letter code.
    
    Args:
        sequence (str): The input protein sequence in one-letter code.
        
    Returns:
        str: The converted protein sequence in three-letter code.
    """
    amino_acids = {
        'A': 'Ala', 'C': 'Cys', 'D': 'Asp', 'E': 'Glu', 'F': 'Phe',
        'G': 'Gly', 'H': 'His', 'I': 'Ile', 'K': 'Lys', 'L': 'Leu',
        'M': 'Met', 'N': 'Asn', 'P': 'Pro', 'Q': 'Gln', 'R': 'Arg',
        'S': 'Ser', 'T': 'Thr', 'V': 'Val', 'W': 'Trp', 'Y': 'Tyr'
    }
    
    three_letter_code = [amino_acids.get(aa.upper()) for aa in sequence]
    return ''.join(three_letter_code)

def sulphur_containing_aa_counter(sequence):
    """
    This function counts sulphur-containing amino acids (Cysteine and Methionine) in a protein sequence.
    
    Args:
        sequence (str): The input protein sequence in one-letter code.
        
    Returns:
        str: The number of sulphur-containing amino acids in a protein sequence.
    """
    counter = 0
    for i in sequence:
        if i == 'C' or i == 'M':
            counter += 1
    answer = str(counter)
    return 'The number of sulphur-containing amino acids in the sequence is equal to ' + answer

def run_amino_analyzer(sequence, procedure, *, weight_type = 'average'):
    """
    This is the main function to run the amino-analyzer.py tool.
    
    Args:
        sequence (str): The input protein sequence in one-letter code.
        procedure (str): amino-analyzer.py tool has 5 functions at all:
            1. aa_weight - Calculate the amino acids weight in a protein sequence.
            2. count_hydroaffinity - Count the quantity of hydrophobic and hydrophilic amino acids in a protein sequence.
            3. peptide_cutter - This function identifies cleavage sites in a given peptide sequence using a specified enzyme.
            4. one_to_three_letter_code - This function converts a protein sequence from one-letter amino acid code to three-letter code.
            5. sulphur_containing_aa_counter - This function counts sulphur-containing amino acids in a protein sequence.
        weight_type = 'average': default argument for 'aa_weight' function. weight_type = 'monoisotopic' can be used as a second option.
        
    Returns:
        The result of the procedure.
    """

    procedures = ['aa_weight', 'count_hydroaffinity', 'peptide_cutter', 'one_to_three_letter_code', 'sulphur_containing_aa_counter']
    if procedure not in procedures:
        raise ValueError(f"Incorrect procedure. Acceptable procedures: {', '.join(procedures)}")

    for i in sequence:
        if not is_aa(sequence):
            raise ValueError("Incorrect sequence. Only amino acids are allowed (V, I, L, E, Q, D, N, H, W, F, Y, R, K, S, T, M, A, G, P, C, v, i, l, e, q, d, n, h, w, f, y, r, k, s, t, m, a, g, p, c).")

    if procedure == 'aa_weight':
        result = aa_weight(sequence, weight_type)
    elif procedure == 'count_hydroaffinity':
        result = count_hydroaffinity(sequence)
    elif procedure == 'peptide_cutter':
        result = peptide_cutter(sequence)
    elif procedure == 'one_to_three_letter_code':
        result = one_to_three_letter_code(sequence)
    elif procedure == 'sulphur_containing_aa_counter':
        result = sulphur_containing_aa_counter(sequence)
    return result
