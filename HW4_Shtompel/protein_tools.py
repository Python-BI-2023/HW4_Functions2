def count_protein_mass(seq: str, kda_scale=False) -> float:
    """
    Calculates mass of all aminoacids of input peptide in g/mol or kDa scale.
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
        kda = round(aa_mass/1000, 1)
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
    ala_count = seq.count('A')/len(seq)
    val_count = seq.count('V')/len(seq)
    lei_count = seq.count('L')/len(seq)
    izlei_count = seq.count('I')/len(seq)
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
