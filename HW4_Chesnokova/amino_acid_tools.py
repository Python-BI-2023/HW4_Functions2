AMINO_ACIDS = 'ARNDCEQGHILKMFPSTWYVUOarndceqghilkmfpstwyvuo'
SHORT_CODE = list(AMINO_ACIDS)
LONG_CODE = ['Ala', 'Arg', 'Asn', 'Asp', 'Cys', 'Glu', 'Gln', 'Gly', 'His', 'Ile', 'Leu', 'Lys', 'Met', 'Phe', 'Pro',
             'Ser', 'Thr', 'Trp', 'Tyr', 'Val', 'Sec', 'Pyl',
             'Ala', 'Arg', 'Asn', 'Asp', 'Cys', 'Glu', 'Gln', 'Gly', 'His', 'Ile', 'Leu', 'Lys', 'Met', 'Phe', 'Pro',
             'Ser', 'Thr', 'Trp', 'Tyr', 'Val', 'Sec', 'Pyl']
MASSE = [71.08, 156.2, 114.1, 115.1, 103.1, 129.1, 128.1, 57.05, 137.1, 113.2, 113.2, 128.2, 131.2, 147.2, 97.12, 87.08,
         101.1, 186.2, 163.2, 99.13, 168.05, 255.3,
         71.08, 156.2, 114.1, 115.1, 103.1, 129.1, 128.1, 57.05, 137.1, 113.2, 113.2, 128.2, 131.2, 147.2, 97.12, 87.08,
         101.1, 186.2, 163.2, 99.13, 168.05, 255.3]


def molecular_weight(seq: str) -> float:
    """
    Function calculates molecular weight of the amino acid chain
        Parameters:
            seq (str): each letter refers to one-letter coded proteinogenic amino acids
    Returns:
        (float) Molecular weight of tge given amino acid chain in Da
    """
    d_mass = dict(zip(SHORT_CODE, MASSE))
    m = 0
    for acid in seq:
        m = m + d_mass[acid]
    return m


def three_letter_code(seq: str) -> str:
    """
    Function converts single letter translations to three letter translations
        Parameters:
            seq (str): each letter refers to one-letter coded proteinogenic amino acids
        Returns:
            (str) translated in three-letter code
    """
    d_names = dict(zip(SHORT_CODE, LONG_CODE))
    recording = seq.maketrans(d_names)
    return seq.translate(recording)


def show_length(seq: str) -> int:
    """
    Function counts the number of amino acids in the given sequence
        Parameters:
            seq (str): amino acid sequence
        Returns:
            (int): integer number of amino acid residues
    """
    return len(seq)


def folding(seq: str) -> str:
    """
    Counts the number of amino acids characteristic separately for alpha helixes and beta sheets,
    and gives out what will be the structure of the protein more.
    This function has been tested on proteins such as 2M3X, 6DT4 (PDB ID) and MHC, CRP.
    The obtained results corresponded to reality.
        Parameters:
            seq (str): amino acid sequence
        Returns:
            (str): overcoming structure ('alfa_helix', 'beta_sheet', 'equally')
    """
    alfa_helix = ['A', 'E', 'L', 'M', 'G', 'Y', 'S', 'a', 'e', 'l', 'm', 'g', 'y', 's']
    beta_sheet = ['Y', 'F', 'W', 'T', 'V', 'I', 'y', 'f', 'w', 't', 'v', 'i']
    alfa_helix_counts = 0
    beta_sheet_counts = 0
    for amino_acid in seq:
        if amino_acid in alfa_helix:
            alfa_helix_counts += 1
        elif amino_acid in beta_sheet:
            beta_sheet_counts += 1
    if alfa_helix_counts > beta_sheet_counts:
        return 'alfa_helix'
    elif alfa_helix_counts < beta_sheet_counts:
        return 'beta_sheet'
    elif alfa_helix_counts == beta_sheet_counts:
        return 'equally'


def seq_charge(seq: str) -> str:
    """
    Function evaluates the overall charge of the aminoacid chain in neutral aqueous solution (pH = 7)
        Parameters:
            seq (str): amino acid sequence of proteinogenic amino acids
        Returns:
            (str): "positive", "negative" or "neutral"
    Function realized by Anna Chesnokova
    """
    aminoacid_charge = {'R': 1, 'D': -1, 'E': -1, 'K': 1, 'O': 1, 'r': 1, 'd': -1, 'e': -1, 'k': 1, 'o': 1}
    charge = 0
    for aminoacid in seq:
        if aminoacid in 'RDEKOrdeko':
            charge += aminoacid_charge[aminoacid]
    if charge > 0:
        return 'positive'
    elif charge < 0:
        return 'negative'
    else:
        return 'neutral'


def aminoacid_seqs_only(seqs: list) -> list:
    """
    Leaves only the amino acid sequences from the fed into the function.
        Parameters:
            seqs (list): amino acid sequence list
        Returns:
            aminoacid_seqs (list): amino acid sequence list without non amino acid sequence
    """
    aminoacid_seqs = []
    for seq in seqs:
        unique_chars = set(seq)
        amino_acid = set(AMINO_ACIDS)
        if unique_chars <= amino_acid:
            aminoacid_seqs.append(seq)
    return aminoacid_seqs


def amino_acid_tools(*args: str):
    """
    Performs functions for working with protein sequences.

        Parameters:
            The function must accept an unlimited number of protein sequences (str) as input,
            the last  variable must be the function (str) you want to execute.
            The amino acid sequence can consist of both uppercase and lowercase letters.
        Input example:
            amino_acid_tools('PLPKVEL','VDviRIkLQ','PPDFGKT','folding')
        Function:
            molecular_weight: calculates molecular weight of the amino acid chain
            three_letter_code: converts single letter translations to three letter translations
            show_length: counts the number of amino acids in the given sequence
            folding: counts the number of amino acids characteristic separately for alpha helixes and beta sheets,
                    and gives out what will be the structure of the protein more
            seq_charge: evaluates the overall charge of the aminoacid chain in neutral aqueous solution (pH = 7)

        Returns:
            If one sequence is supplied, a string with the result is returned.
            If several are submitted, a list of strings is returned.
            Depending on the function performed, the following returns will occur:
                molecular_weight (int) or (list): amino acid sequence molecular weight number or list of numbers
                three_letter_code (str) or (list): translated sequence from one-letter in three-letter code
                show_length (int) or (list): integer number of amino acid residues
                folding (str) or (list): 'alpha_helix', if there are more alpha helices
                                        'beta_sheet', if there are more beta sheets
                                        'equally', if the probability of alpha spirals and beta sheets are the same
                			seq_charge(str) or (list): "positive", "negative" or "neutral"
    """
    *seqs, function = args
    d_of_functions = {'molecular_weight': molecular_weight,
                      'three_letter_code': three_letter_code,
                      'show_length': show_length,
                      'folding': folding,
                      'seq_charge': seq_charge}
    answer = []
    aminoacid_seqs = aminoacid_seqs_only(seqs)
    for sequence in aminoacid_seqs:
        answer.append(d_of_functions[function](sequence))
    if len(answer) == 1:
        return answer[0]
    else:
        return answer
