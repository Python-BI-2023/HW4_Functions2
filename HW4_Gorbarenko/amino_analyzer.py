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
    aa_list = str('A, R, N, D, C, E, Q, G, H, I, L, K, M, F, P, S, T, W, Y, V').split(',')
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
