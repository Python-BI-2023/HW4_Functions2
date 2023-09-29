def check_for_motifs(sequences, motif):
    # new_line = "\n"  # used for user-friendly output
    all_positions = {}
    for sequence in sequences:
        start = 0
        positions = []
        if motif in sequence:
            while True:
                start = sequence.find(motif, start)
                if start == -1:
                    break
                positions.append(start)
                start += 1  # use += len(motif) not to count overlapping matches
            # pos_for_print = ", ".join(str(x) for x in positions)
            # print(f"Sequence: {sequence}")
            # print(f"Motif: {motif}")
            # print(
            #     f"Motif is present in protein sequence starting at positions: {pos_for_print}{new_line}"
            # )
        all_positions[sequence] = positions
        # print(f"Sequence: {sequence}")
        # print(f"Motif: {motif}")
        # print(f"Motif is not present in protein sequence{new_line}")
    return all_positions


def search_for_alt_frames(sequences: str, alt_st_codon: str):
    """
    Search for alternative frames in a protein sequences

    Without an alt_st_codon argument search for frames that start with methionine ('M')
    To search frames with alternative start codon add alt_st_codon argument
    In alt_st_codon argument use one-letter code

    The function ignores the last three amino acids in sequences

    Arguments:
    - sequences (tuple(str) or list(str)): sequences to check
    - alt_st_codon (str): the name of an amino acid that is encoded by alternative start codon (Optional)
    Example: alt_st_codon = 'I'

    Return:
    - dictionary: the number of a sequence and a collection of alternative frames
    """
    # if len(alt_st_codon) > 1:
    #     raise ValueError("Invalid start codon!")
    alternative_frames = {}
    num_position = 0
    for sequence in sequences:
        for amino_acid in sequence[1:-3]:
            num_position += 1
            if amino_acid == alt_st_codon or amino_acid == alt_st_codon.swapcase():
                key = sequences.index(sequence) + 1
                if key in alternative_frames:
                    alternative_frames[key] += sequence[num_position:] + "  "
                else:
                    alternative_frames[key] = sequence[num_position:] + "  "
        num_position = 0
    # for key, value in alternative_frames.items():
    #     print(key, value)
    return alternative_frames


def convert_to_nucl_acids(sequences: str, nucl_acids: str):
    """
    Convert protein sequences to RNA or DNA sequences.

    Use the most frequent codons in human. The source - https://www.genscript.com/tools/codon-frequency-table
    All nucleic acids (DNA and RNA) are showed in 5'-3' direction

    Arguments:
    - sequences (tuple(str) or list(str)): sequences to convert
    - nucl_acids (str): the nucleic acid that is prefered
    Example: nucl_acids = 'RNA' - convert to RNA
             nucl_acids = 'DNA' - convert to DNA
             nucl_acids = 'both' - convert to RNA and DNA
    Return:
    - dictionary: a collection of alternative frames
    If nucl_acids = 'RNA' or nucl_acids = 'DNA' output a collection of frames
    If nucl_acids = 'both' output the name of a nucleic acid and a collection of frames
    """
    # if nucl_acids not in {"DNA", "RNA", "both"}:
    #     raise ValueError("Invalid nucl_acids argument!")
    rule_of_translation = sequences[0].maketrans(alphabet)
    rule_of_transcription = sequences[0].maketrans("AaUuCcGg", "TtAaGgCc")
    nucl_acid_seqs = {"RNA": [], "DNA": []}
    for sequence in sequences:
        rna_seq = sequence.translate(rule_of_translation)
        reverse_dna_seq = rna_seq.translate(rule_of_transcription)[::-1]
        # if "RNA" in nucl_acid_seqs.keys():
        # nucl_acid_seqs["RNA"] += rna_seq + "  "
        # else:
        # nucl_acid_seqs["RNA"] = rna_seq + "  "
        if nucl_acids == "RNA":
            nucl_acid_seqs["RNA"].append(rna_seq)
            if sequence == sequences[-1]:
                del nucl_acid_seqs["DNA"]
        if nucl_acids == "DNA":
            nucl_acid_seqs["DNA"].append(reverse_dna_seq)
            if sequence == sequences[-1]:
                del nucl_acid_seqs["RNA"]
        if nucl_acids == "both":
            nucl_acid_seqs["RNA"].append(rna_seq)
            nucl_acid_seqs["DNA"].append(reverse_dna_seq)
    #     if "DNA" in nucl_acid_seqs.keys():
    #         nucl_acid_seqs["DNA"] += reverse_dna_seq + "  "
    #     else:
    #         nucl_acid_seqs["DNA"] = reverse_dna_seq + "  "
    # if nucl_acids == "RNA":
    #     return nucl_acid_seqs["RNA"]
    # elif nucl_acids == "DNA":
    #     return nucl_acid_seqs["DNA"]
    # elif nucl_acids == "both":
    # for key, value in nucl_acid_seqs.items():
    #     print(key, value)
    return nucl_acid_seqs


procedures_to_functions = {
    "check_for_motifs": check_for_motifs,
    "search_for_alt_frames": search_for_alt_frames,
    "convert_to_nucl_acids": convert_to_nucl_acids,
}

alphabet = {
    "F": "UUU",
    "f": "uuu",
    "L": "CUG",
    "l": "cug",
    "I": "AUU",
    "i": "auu",
    "M": "AUG",
    "m": "aug",
    "V": "GUG",
    "v": "gug",
    "P": "CCG",
    "p": "ccg",
    "T": "ACC",
    "t": "acc",
    "A": "GCG",
    "a": "gcg",
    "Y": "UAU",
    "y": "uau",
    "H": "CAU",
    "h": "cau",
    "Q": "CAG",
    "q": "cag",
    "N": "AAC",
    "n": "aac",
    "K": "AAA",
    "k": "aaa",
    "D": "GAU",
    "d": "gau",
    "E": "GAA",
    "e": "gaa",
    "C": "UGC",
    "c": "ugc",
    "W": "UGG",
    "w": "ugg",
    "R": "CGU",
    "r": "cgu",
    "S": "AGC",
    "s": "agc",
    "G": "GGC",
    "g": "ggc",
}


def check_and_parse_user_input(*args, **kwargs):
    if len(args) == 0:
        raise ValueError("No sequences provided")
    sequences = list(args)
    for sequence in sequences:
        if not all(letters in "".join(alphabet.keys()) for letters in sequence):
            raise ValueError("Invalid sequence given")
    procedure = kwargs["procedure"]
    procedure_arguments = {}
    if procedure not in procedures_to_functions.keys():
        raise ValueError("Wrong procedure")
    if procedure == "check_for_motifs":
        if "motif" not in kwargs.keys():
            raise ValueError("Please provide desired motif")
        procedure_arguments["motif"] = kwargs["motif"]
    elif procedure == "search_for_alt_frames":
        if "alt_st_codon" not in kwargs.keys():
            procedure_arguments["alt_st_codon"] = "M"
        else:
            if len(kwargs["alt_st_codon"]) > 1:
                raise ValueError("Invalid start codon!")
            procedure_arguments["alt_st_codon"] = kwargs["alt_st_codon"]
    elif procedure == "convert_to_nucl_acids":
        if "nucl_acids" not in kwargs.keys():
            raise ValueError("Please provide desired type of nucl_acids")
        if kwargs["nucl_acids"] not in {"DNA", "RNA", "both"}:
            raise ValueError("Invalid nucl_acids argument")
        procedure_arguments["nucl_acids"] = kwargs["nucl_acids"]
    procedure_arguments["sequences"] = sequences
    return procedure_arguments, procedure


def run_protein_tools(*args, **kwargs):
    procedure_arguments, procedure = check_and_parse_user_input(*args, **kwargs)
    return procedures_to_functions[procedure](**procedure_arguments)
