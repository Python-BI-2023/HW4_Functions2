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
    Build a default scoring matrix, if not provided in needleman-wunsch function parameter

    Args:
    - match_score (int): integer value of a matching score of aminoacids
    - mismatch_score (int): integer value of a mismatching score of aminoacids
    - amino_acid_alphabet (str): upper case amino acid alphabet

    Returns:
    - a dictionary of dictionaries representing a scoring matrix for aminoacids paris. Key of a dictionary is an aminoacid and its value is a dictionary of scores
    """

    scoring_matrix = {}

    for aa1 in amino_acid_alphabet:
        scoring_matrix[aa1] = {}
        for aa2 in amino_acid_alphabet:
            scoring_matrix[aa1][aa2] = (
                match_score if aa1.upper() == aa2.upper() else mismatch_score
            )

    return scoring_matrix


def needleman_wunsch(
    seq1: str,
    seq2: str,
    scoring_matrix: dict = None,
    gap_penalty: int = -1,
    match_score: int = 1,
    mismatch_score: int = -1,
) -> str:
    """
    Uses Needleman-Wunsch algorithm to make a global alignment of two sequences.

    Args:
    - seq1 (str): first aminoacid sequence for alignment
    - seq2 (str): second aminoacid sequence for alignment
    - scoring_matrix (dict): A dictionary representing a scoring matrix for amino acid pairs
      If not provided, a default scoring_matrix is generated based on match and mismatch scores
    - gap_penalty (int): integer va;ue of a penalty score for introducing a gap in the alignment
    - match_score (int): integer value of a matching score for matching aminoacids
    - mismatch_score (int): integer value of a mismatching score for mismatched aminoacids

    Returns:
    - string: a string containing the aligned sequences (str), the aligned score (int)
    """
    if scoring_matrix is None:
        # Default scoring matrix if not provided
        scoring_matrix = build_scoring_matrix(match_score, mismatch_score)

    seq1_upper = seq1.upper()  # Convert seq1 to uppercase
    seq2_upper = seq2.upper()  # Convert seq2 to uppercase

    m, n = len(seq1_upper), len(seq2_upper)

    # Initialize matrices
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    traceback = [[""] * (n + 1) for _ in range(m + 1)]

    # Fill in the scoring matrix and traceback matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = dp[i - 1][j - 1] + scoring_matrix.get(seq1_upper[i - 1], {}).get(
                seq2_upper[j - 1], mismatch_score
            )
            delete = dp[i - 1][j] + gap_penalty
            insert = dp[i][j - 1] + gap_penalty

            dp[i][j] = max(match, delete, insert)

            if dp[i][j] == match:
                traceback[i][j] = "D"  # Diagonal (indicates a match/mismatch)
            elif dp[i][j] == delete:
                traceback[i][j] = "U"  # Up (indicates a gap in seq2)
            else:
                traceback[i][j] = "L"  # Left (indicates a gap in seq1)

    # Traceback to find the aligned sequences while preserving case
    aligned_seq1, aligned_seq2 = [], []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and traceback[i][j] == "D":
            # check original case of amionacid in seq1
            if seq1[i - 1].isupper():
                aligned_seq1.append(seq1_upper[i - 1])
            else:
                aligned_seq1.append(seq1[i - 1])

            # check original case of amionacid in seq2
            if seq2[j - 1].isupper():
                aligned_seq2.append(seq2_upper[j - 1])
            else:
                aligned_seq2.append(seq2[j - 1])

            i -= 1
            j -= 1
        elif i > 0 and traceback[i][j] == "U":
            # check original case of amionacid in seq1
            if seq1[i - 1].isupper():
                aligned_seq1.append(seq1_upper[i - 1])
            else:
                aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append("-")

            i -= 1
        else:
            aligned_seq1.append("-")
            # check original case of amionacid in seq2
            if seq2[j - 1].isupper():
                aligned_seq2.append(seq2_upper[j - 1])
            else:
                aligned_seq2.append(seq2[j - 1])

            j -= 1

    aligned_seq1 = "".join(reversed(aligned_seq1))
    aligned_seq2 = "".join(reversed(aligned_seq2))

    return f"{aligned_seq1}, {aligned_seq2}, final score: {dp[m][n]}"
