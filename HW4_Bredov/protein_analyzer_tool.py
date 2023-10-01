from typing import Iterable, Tuple

AA_TR_DICT = {'Ala': 'A', 'Arg': 'R', 'Asn': 'N', 'Asp': 'D',
              'Cys': 'C', 'Gln': 'E', 'Glu': 'Q', 'Gly': 'G',
              'His': 'H', 'Ile': 'I', 'Leu': 'L', 'Lys': 'K',
              'Met': 'M', 'Phe': 'F', 'Pro': 'P', 'Ser': 'S',
              'Thr': 'T', 'Trp': 'W', 'Tyr': 'Y', 'Val': 'V'}
AA_UNIPROT_CONTENT = {
"A": 9.03, "R": 5.84, "N": 3.79, "D": 5.47, "C": 1.29,
"Q": 3.80, "E": 6.24, "G": 7.27, "H": 2.22, "I": 5.53,
"L": 9.85, "K": 4.93, "M": 2.33, "F": 3.88, "P": 4.99,
"S": 6.82, "T": 5.55, "W": 1.30, "Y": 2.88, "V": 6.86
}
AA_CHARGES = {
"A": 0, "R": 1, "N": 0, "D": -1, "C": 0,
"Q": 0, "E": -1, "G": 0, "H": 1, "I": 0,
"L": 0, "K": 1, "M": 0, "F": 0, "P": 0,
"S": 0, "T": 0, "W": 0, "Y": 0, "V": 0
}


def Mann_Whitney_U(seq1: Iterable[int], seq2: Iterable[int]) -> bool:
    """
    Mann-Whitney U-test. Used to compare aminoacids composition in given sequence with average protein composition provided by Uniprot.
    Used as a second step of checkup in `check_and_procees_seq` function if sequence uses 1-letter abbreviation.
    """
    len_seq1, len_seq2 = len(seq1), len(seq2)
    r1, r2 = dict.fromkeys(map(str, seq1), 0), dict.fromkeys(map(str, seq2), 0)

    r = sorted(list(seq1) + list(seq2))
    r_dict = dict.fromkeys(map(str, r), ())
    
    for index, value in enumerate(r):
        value = str(value)
        r_dict[value] = r_dict[value] + (index + 1,)
    for elem in r_dict:
        r_dict[elem] = sum(r_dict[elem]) / len(r_dict[elem])

    for value in seq1:
        value = str(value)
        r1[value] = r1[value] + r_dict[value]
    
    for value in seq2:
        value = str(value)
        r2[value] = r2[value] + r_dict[value]

    u1 = (len_seq1 * len_seq2) + len_seq1 * (len_seq1 + 1) / 2 - sum(r1.values())
    u2 = (len_seq1 * len_seq2) + len_seq2 * (len_seq2 + 1) / 2 - sum(r2.values())

    u_stat = min(u1, u2)

    if u_stat <= 127:
        return False
    
    return True


def decomposition(seq: str) -> list:
    """
    Decomposes 3 letter-sequence into list of single aminoacids.
    Used in `check_and_procees_seq` function if sequence uses 3-letter abbreviation.
    """
    len_seq, dec_seq = len(seq), []
    if len(seq) % 3 == 0:
        for i in range(0, len_seq, 3):
            dec_seq.append(seq[i:i+3].lower().capitalize())
    
    return dec_seq


def seq_transform(seq: list) -> str:
    """
    Transforms aminoacid abbreviation format from 3-letter into 1-letter.
    Used in `check_and_procees_seq` function if sequence uses 3-letter abbreviation.
    """
    seq_tr = ''
    for aa in seq:
        seq_tr += AA_TR_DICT[aa]
    
    return seq_tr
  
  

def aa_content_check(seq: str) -> dict:
    "Returns aminoacids content of the protein"
    seq_content = dict.fromkeys(AA_UNIPROT_CONTENT.keys(), 0)
    for AAcd in seq.upper():
        seq_content[AAcd] = seq_content[AAcd] + 1

    seq_length = len(seq)
    for AAcd, occurence in seq_content.items():
        seq_content[AAcd] = 100 * occurence / seq_length

    return seq_content


def check_and_procees_seq(seq: str, abbreviation: int = 1) -> Tuple[bool, str]:
    "Checks whether the string is valid protein sequence and transforms to 1-letter abbreviation if required"
    exit_code = False
    if isinstance(seq, str):
        if abbreviation == 3:
            seq = decomposition(seq)
            exit_code = bool(seq) and set(seq).issubset(set(AA_TR_DICT.keys()))
            if exit_code:
                seq = seq_transform(seq)
        elif abbreviation == 1:
            seq_set = set(seq.upper())
            exit_code = bool(seq) and seq_set.issubset(set(AA_TR_DICT.values()))
            if exit_code:
                seq_content, uniprot_content = aa_content_check(seq).values(), AA_UNIPROT_CONTENT.values()
                seq_Mann_Whitney_U = Mann_Whitney_U(seq_content, uniprot_content) if len(seq_set) == 20 else True
                exit_code = seq_Mann_Whitney_U
        else:
            raise ValueError("Incorrect abbreviation. Must be 1 or 3, type `int`")
    
    return exit_code, seq


def seq_length(seq: str) -> int:
    return len(seq)


def protein_mass(seq: str):
    "Counts molecular weight of the protein"
    count = 0
    for amino in seq:
        if amino == "A":
            count += 89
        elif amino == "R":
            count += 174
        elif amino == "N":
            count += 132
        elif amino == "V":
            count += 117
        elif amino == "H":
            count += 155
        elif amino == "G":
            count += 75
        elif amino == "Q":
            count += 146
        elif amino == "E":
            count += 147
        elif amino == "I":
            count += 131
        elif amino == "L":
            count += 131
        elif amino == "K":
            count += 146
        elif amino == "M":
            count += 149
        elif amino == "P":
            count += 115
        elif amino == "S":
            count += 105
        elif amino == "Y":
            count += 181
        elif amino == "T":
            count += 119
        elif amino == "W":
            count += 204
        elif amino == "F":
            count += 165
        else:
            count += 133
    return count


def protein_formula(seq: str) -> dict:
    "Returns molecular formula of the protein"
    fС = 0
    fH = 0
    fN = 0
    fO = 0
    fS = 0
    for amino in seq:
        if amino == "A":
            fС += 3
            fH += 7
            fN += 1
            fO += 2
            fS += 0
        elif amino == "R":
            fС += 6
            fH += 14
            fN += 4
            fO += 2
            fS += 0
        elif amino == "N":
            fС += 4
            fH += 8
            fN += 2
            fO += 3
            fS += 0
        elif amino == "V":
            fС += 5
            fH += 11
            fN += 1
            fO += 2
            fS += 0
        elif amino == "H":
            fС += 6
            fH += 9
            fN += 3
            fO += 2
            fS += 0
        elif amino == "G":
            fС += 2
            fH += 5
            fN += 1
            fO += 2
            fS += 0
        elif amino == "Q":
            fС += 5
            fH += 10
            fN += 2
            fO += 3
            fS += 0
        elif amino == "E":
            fС += 5
            fH += 9
            fN += 1
            fO += 4
            fS += 0
        elif amino == "I":
            fС += 6
            fH += 13
            fN += 1
            fO += 2
            fS += 0
        elif amino == "L":
            fС += 6
            fH += 13
            fN += 1
            fO += 2
            fS += 0
        elif amino == "K":
            fС += 6
            fH += 14
            fN += 2
            fO += 2
            fS += 0
        elif amino == "M":
            fС += 5
            fH += 11
            fN += 1
            fO += 2
            fS += 1
        elif amino == "P":
            fС += 5
            fH += 9
            fN += 1
            fO += 2
            fS += 0
        elif amino == "S":
            fС += 3
            fH += 7
            fN += 1
            fO += 3
            fS += 0
        elif amino == "Y":
            fС += 9
            fH += 11
            fN += 1
            fO += 3
            fS += 0
        elif amino == "T":
            fС += 4
            fH += 9
            fN += 1
            fO += 3
            fS += 0
        elif amino == "W":
            fС += 11
            fH += 12
            fN += 2
            fO += 2
            fS += 0
        elif amino == "F":
            fС += 9
            fH += 11
            fN += 1
            fO += 2
            fS += 0
        else:
            fС += 4
            fH += 7
            fN += 1
            fO += 4
            fS += 0
    if fS == 0:
        aa_formula = {"С": fС, "H": fH, "N": fN, "O":fO}
    else:
        aa_formula = {"С": fС, "H": fH, "N": fN, "O":fO, "S": fS}
    return aa_formula


def aa_chain_charge(seq: str, aa_charges: dict = AA_CHARGES) -> int:
    "Returns charge of the protein (pH=7)"
    aa_charge = 0
    for AAcd in seq.upper():
        aa_charge += aa_charges[AAcd]

    return aa_charge
  

def print_result(result: list, corrupt_seqs: list):
    len_seq, len_corr_seq = len(result), len(corrupt_seqs)
    len_seqs = len_seq + len_corr_seq
    success = ["+" for _ in range(len_seqs)]
    if not len_corr_seq:
        print(f"All {len_seqs} sequence(s) processed successfully")
    elif len_corr_seq:
        for i in corrupt_seqs:
            success[i[0]] = "-"
        print(f'Processing result: [{"".join(success)}]\n')
        print(f"{len_seq} sequence(s) out of {len_seq + len_corr_seq} given have been processed successfully.")
        print(f"{len_corr_seq} has been recognized as corrupted, i.e. non-protein")


OPERATIONS = {"content_check": aa_content_check, "seq_length": seq_length, "protein_formula": protein_formula, "protein_mass": protein_mass, "charge": aa_chain_charge}


def run_protein_analyzer_tool(*args, abbreviation: int = 1) -> Tuple[list, list]:
    """
    Provides interface for 5 operations from `OPERATIONS` dictionary. Takes various number of positional arguments and one keyword-only argument:
    
    - First `n` arguments - protein sequences;
    - Latter positional argument - desired operation from list: "content_check", "seq_length", "protein_formula", "protein_mass", "charge";
    - `abbrevition` keyword-only argument. Should be type integer, 1 for 1-letter abbreviation and 3 for 3-letter.
    
    Returns tuple containing two list:

    - `result` - list with operation results for each valid sequence;
    - `corrupt_seqs` - list with non-valid sequences and their indices;
    """
    *seqs, operation = args
    if operation not in OPERATIONS:
        raise ValueError(f'Unknown operation `{operation}`. Please, select from: "content_check", "seq_length", "protein_formula", "protein_mass", "charge"')

    result, corrupt_seqs = [], []
    for seq_index, seq in enumerate(seqs):
        is_seq_valid, seq_alt = check_and_procees_seq(seq, abbreviation)
        if is_seq_valid:
            result.append(OPERATIONS[operation](seq_alt))
        elif not is_seq_valid:
            corrupt_seqs.append((seq_index, seq))

    print_result(result, corrupt_seqs)

    res_len, cor_seq_len = len(result), len(corrupt_seqs)
    result = result[0] if res_len == 1 else result
    corrupt_seqs = corrupt_seqs[0] if cor_seq_len == 1 else corrupt_seqs
    return result, corrupt_seqs
