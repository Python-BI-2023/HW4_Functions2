def calculate_pI(
    sequence: str,
    pKa_values: dict = {
        "D": 3.86,  # Aspartic acid (COOH side chain)
        "E": 4.25,  # Glutamic acid (COOH side chain)
        "C": 8.33,  # Cysteine (R-SH)
        "Y": 10.46,  # Tyrosine (phenolic OH)
        "H": 6.0,  # Histidine (imidazole group)
        "K": 10.67,  # Lysine (amino group)
        "R": 12.48,  # Arginine (guanidinium group)
        "N": 3.22,  # Asparagine (amino group)
        "Q": 3.65,  # Glutamine (amino group)
        "T": 2.95,  # Threonine (amino group)
        "S": 2.19,  # Serine (hydroxyl group)
        "W": 11.55,  # Tryptophan (imidazole group)
        "Y": 10.46,  # Tyrosine (phenolic OH)
    },
) -> str:
    """
    Calculates isoelectric point of a whole aminoacid sequence and for each aminoacid individually

    Args:
    - sequence (str): sequence for which to calculate isoelectric point
    - pKa_values (dict): acid dissociation constants for each aminoacid

    Return:
    - str: string, which contains:
            - an original sequence,
            - list of tuple pairs of aminoacid and corresponding isoelectric point,
            - overall isoelectric point of sequence
    """

    aminoacid_pIs = []
    total_charge = 0.0

    # Calculate pI for each amino acid in the sequence while preserving case
    for aa in sequence:
        aa_upper = aa.upper()
        if aa_upper in pKa_values:
            pI = pKa_values[aa_upper]

            if aa.isupper():
                aminoacid_pIs.append((aa_upper, pI))
            else:
                aminoacid_pIs.append((aa, pI))
            total_charge += pI

    # Calculate the overall pI of the sequence
    overall_pI = total_charge / len(sequence)
    overall_pI = round(overall_pI, 2)

    return f"Sequence: {sequence}. Isoelectric point of each aminoacid: {aminoacid_pIs}, Sequence's isoelectric point: {overall_pI}"


def build_scoring_matrix(
    match_score: int,
    mismatch_score: int,
    amino_acid_alphabet: str = "ACDEFGHIKLMNPQRSTVWY",
) -> dict:
    """
    Build a default scoring matrix, if not provided in needleman-wunsch function parameter, as a dictionary of dictionaries

    Args:
    - match_score (int): integer value of a matching score of aminoacids
    - mismatch_score (int): integer value of a mismatching score of aminoacids
    - amino_acid_alphabet (str): upper case amino acid alphabet

    Returns:
    - dictionary of dictionaries of aminoacids scores. In which this dictionary contain aminoacid as a key and its value a dictionary of scores
    """

    scoring_matrix = {}

    for aa1 in amino_acid_alphabet:
        scoring_matrix[aa1] = {}
        for aa2 in amino_acid_alphabet:
            scoring_matrix[aa1][aa2] = (
                match_score if aa1.upper() == aa2.upper() else mismatch_score
            )

    return scoring_matrix
