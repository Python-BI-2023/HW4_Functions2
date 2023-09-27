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
):
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

    return aminoacid_pIs, overall_pI


def build_scoring_matrix(match_score, mismatch_score):
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"  # Amino acid alphabet

    # Initialize an empty scoring matrix as a dictionary of dictionaries
    scoring_matrix = {}

    for aa1 in amino_acids:
        scoring_matrix[aa1] = {}
        for aa2 in amino_acids:
            scoring_matrix[aa1][aa2] = (
                match_score if aa1.upper() == aa2.upper() else mismatch_score
            )

    return scoring_matrix


def needleman_wunsch(
    seq1, seq2, scoring_matrix=None, gap_penalty=-1, match_score=1, mismatch_score=-1
):
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
            if seq1[i - 1].isupper():
                aligned_seq1.append(seq1_upper[i - 1])
            else:
                aligned_seq1.append(seq1[i - 1])
            if seq2[j - 1].isupper():
                aligned_seq2.append(seq2_upper[j - 1])
            else:
                aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and traceback[i][j] == "U":
            if seq1[i - 1].isupper():
                aligned_seq1.append(seq1_upper[i - 1])
            else:
                aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append("-")
            i -= 1
        else:
            aligned_seq1.append("-")
            if seq2[j - 1].isupper():
                aligned_seq2.append(seq2_upper[j - 1])
            else:
                aligned_seq2.append(seq2[j - 1])
            j -= 1

    aligned_seq1 = "".join(reversed(aligned_seq1))
    aligned_seq2 = "".join(reversed(aligned_seq2))

    return aligned_seq1, aligned_seq2, dp[m][n]
