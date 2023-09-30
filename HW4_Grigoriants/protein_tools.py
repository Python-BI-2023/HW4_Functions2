def three_one_letter_code(sequences):
    inversed_sequences = []
    for sequence in sequences:
        inversed_sequence = ""
        if "-" not in sequence:
            for letter in sequence:
                inversed_sequence += amino_acids[letter] + "-"
            inversed_sequence = inversed_sequence[:-1]
            inversed_sequences.append(inversed_sequence)
        else:
            aa_splitted = sequence.split("-")
            for aa in aa_splitted:
                inversed_sequence += list(amino_acids.keys())[
                    list(amino_acids.values()).index(aa)
                ]
            inversed_sequences.append(inversed_sequence)
    return inversed_sequences


def define_molecular_weight(sequences):
    sequences_weights = []
    for sequence in sequences:
        sequence_weight = 0
        for letter in sequence:
            sequence_weight += amino_acid_weights[letter]
        sequences_weights.append(sequence_weight)
    return sequences_weights


def check_for_motifs(sequences, motif):
    new_line = "\n"  # used for user-friendly output
    all_positions = {}
    for sequence in sequences:
        start = 0
        positions = []
        print(f"Sequence: {sequence}")
        print(f"Motif: {motif}")
        if motif in sequence:
            while True:
                start = sequence.find(motif, start)
                if start == -1:
                    break
                positions.append(start)
                # use += len(motif) not to count overlapping matches
                start += 1
            pos_for_print = ", ".join(str(x) for x in positions)
            print(
                f"Motif is present in protein sequence starting at positions: {pos_for_print}{new_line}"
            )
        else:
            print(f"Motif is not present in protein sequence{new_line}")
        all_positions[sequence] = positions
    return all_positions


def search_for_alt_frames(sequences: str, alt_start_aa: str):
    """
    Search for alternative frames in a protein sequences

    Without an alt_start_aa argument search for frames that start with methionine ('M')
    To search frames with alternative start codon add alt_start_aa argument
    In alt_start_aa argument use one-letter code

    The function ignores the last three amino acids in sequences

    Arguments:
    - sequences (tuple(str) or list(str)): sequences to check
    - alt_start_aa (str): the name of an amino acid that is encoded by alternative start codon (Optional)
    Example: alt_start_aa = 'I'

    Return:
    - dictionary: the number of a sequence and a collection of alternative frames
    """
    # if len(alt_start_aa) > 1:
    #     raise ValueError("Invalid start codon!")
    alternative_frames = {}
    num_position = 0
    for sequence in sequences:
        for amino_acid in sequence[1:-3]:
            num_position += 1
            if amino_acid == alt_start_aa or amino_acid == alt_start_aa.swapcase():
                key = sequences.index(sequence) + 1
                if key in alternative_frames:
                    alternative_frames[key] += sequence[num_position:] + "  "
                else:
                    alternative_frames[key] = sequence[num_position:] + "  "
        num_position = 0
    # for key, value in alternative_frames.items():
    #     print(key, value)
    return alternative_frames


def convert_to_nucl_acids(sequences: list, nucl_acids: str):
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
    rule_of_translation = sequences[0].maketrans(translation_rule)
    rule_of_transcription = sequences[0].maketrans("Uu", "Tt")
    nucl_acid_seqs = {"RNA": [], "DNA": []}
    for sequence in sequences:
        rna_seq = sequence.translate(rule_of_translation)
        dna_seq = rna_seq.translate(rule_of_transcription)
        if nucl_acids == "RNA":
            nucl_acid_seqs["RNA"].append(rna_seq)
            if sequence == sequences[-1]:
                del nucl_acid_seqs["DNA"]
        if nucl_acids == "DNA":
            nucl_acid_seqs["DNA"].append(dna_seq)
            if sequence == sequences[-1]:
                del nucl_acid_seqs["RNA"]
        if nucl_acids == "both":
            nucl_acid_seqs["RNA"].append(rna_seq)
            nucl_acid_seqs["DNA"].append(dna_seq)
    return nucl_acid_seqs


procedures_to_functions = {
    "check_for_motifs": check_for_motifs,
    "search_for_alt_frames": search_for_alt_frames,
    "convert_to_nucl_acids": convert_to_nucl_acids,
    "three_one_letter_code": three_one_letter_code,
    "define_molecular_weight": define_molecular_weight,
}
amino_acids = {
    "A": "Ala",
    "C": "Cys",
    "D": "Asp",
    "E": "Glu",
    "F": "Phe",
    "G": "Gly",
    "H": "His",
    "I": "Ile",
    "K": "Lys",
    "L": "Leu",
    "M": "Met",
    "N": "Asn",
    "P": "Pro",
    "Q": "Gln",
    "R": "Arg",
    "S": "Ser",
    "T": "Thr",
    "V": "Val",
    "W": "Trp",
    "Y": "Tyr",
    "a": "ala",
    "c": "cys",
    "d": "asp",
    "e": "glu",
    "f": "phe",
    "g": "gly",
    "h": "his",
    "i": "ile",
    "k": "lys",
    "l": "leu",
    "m": "met",
    "n": "asn",
    "p": "pro",
    "q": "gln",
    "r": "arg",
    "s": "ser",
    "t": "thr",
    "v": "val",
    "w": "trp",
    "y": "tyr",
}

translation_rule = {
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

amino_acid_weights = {
    "A": 89.09,
    "C": 121.16,
    "D": 133.10,
    "E": 147.13,
    "F": 165.19,
    "G": 75.07,
    "H": 155.16,
    "I": 131.17,
    "K": 146.19,
    "L": 131.17,
    "M": 149.21,
    "N": 132.12,
    "P": 115.13,
    "Q": 146.15,
    "R": 174.20,
    "S": 105.09,
    "T": 119.12,
    "V": 117.15,
    "W": 204.23,
    "Y": 181.19,
}


def check_and_parse_user_input(sequences, **kwargs):
    if len(sequences) == 0:
        raise ValueError("No sequences provided")
    procedure = kwargs["procedure"]
    if procedure not in procedures_to_functions.keys():
        raise ValueError("Wrong procedure")
    allowed_inputs = set(amino_acids.keys()).union(
        set(amino_acids.values()).union(set("-"))
    )
    if procedure != "three_one_letter_code":
        allowed_inputs.remove("-")
        allowed_inputs -= set(amino_acids.values())
    for sequence in sequences:
        allowed_inputs_seq = allowed_inputs
        if procedure == "three_one_letter_code" and "-" in sequence:
            allowed_inputs_seq -= set(amino_acids.keys())
            if not all(
                aminoacids in allowed_inputs_seq for aminoacids in sequence.split("-")
            ):
                raise ValueError("Invalid sequence given")
        else:
            if not all(aminoacids in allowed_inputs_seq for aminoacids in sequence):
                raise ValueError("Invalid sequence given")
    procedure_arguments = {}
    if procedure == "check_for_motifs":
        if "motif" not in kwargs.keys():
            raise ValueError("Please provide desired motif")
        procedure_arguments["motif"] = kwargs["motif"]
    elif procedure == "search_for_alt_frames":
        if "alt_start_aa" not in kwargs.keys():
            procedure_arguments["alt_start_aa"] = "M"
        else:
            if len(kwargs["alt_start_aa"]) > 1:
                raise ValueError("Invalid start AA!")
            procedure_arguments["alt_start_aa"] = kwargs["alt_start_aa"]
    elif procedure == "convert_to_nucl_acids":
        if "nucl_acids" not in kwargs.keys():
            raise ValueError("Please provide desired type of nucl_acids")
        if kwargs["nucl_acids"] not in {"DNA", "RNA", "both"}:
            raise ValueError("Invalid nucl_acids argument")
        procedure_arguments["nucl_acids"] = kwargs["nucl_acids"]
    procedure_arguments["sequences"] = sequences
    return procedure_arguments, procedure


def run_protein_tools(sequences=[], **kwargs):
    procedure_arguments, procedure = check_and_parse_user_input(sequences, **kwargs)
    return procedures_to_functions[procedure](**procedure_arguments)
