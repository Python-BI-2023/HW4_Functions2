def check_for_motifs(sequences, motif):
    start = 0
    nl = "\n"  # used for user-friendly output
    all_positions = []
    for sequence in sequences:
        if motif in sequence:
            positions = []
            while True:
                start = sequence.find(motif, start)
                if start == -1:
                    break
                positions.append(start)
                start += 1  # use += len(motif) not to count overlapping matches
            all_positions.append(positions)
            pos_for_print = ", ".join(str(x) for x in positions)
            print(f"Sequence: {sequence}")
            print(f"Motif: {motif}")
            print(
                f"Motif is present in protein sequence starting at positions: {pos_for_print}{nl}"
            )
        else:
            all_positions.append([])
            print(f"Sequence: {sequence}")
            print(f"Motif: {motif}")
            print(f"Motif is not present in protein sequence{nl}")
    return all_positions


def search_for_alt_frames(sequences: str, alt_st_codon: str, num_position=0):
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
    if len(alt_st_codon) > 1:
        raise ValueError('Invalid start codon!')
    alternative_frames = {}
    for sequence in sequences:
        for amino_acid in sequence[1:-3]:
            num_position += 1
            if (amino_acid == alt_st_codon or
                    amino_acid == alt_st_codon.swapcase()):
                key = sequences.index(sequence) + 1
                if key in alternative_frames:
                    alternative_frames[key] += sequence[num_position:] + '  '
                else:
                    alternative_frames[key] = sequence[num_position:] + '  '
        num_position = 0
    for key, value in alternative_frames.items():
        print(key, value)


procedures_to_functions = {"check_for_motifs": check_for_motifs}


def run_protein_tools(*args, **kwargs):
    sequences = list(args)
    procedure = kwargs["procedure"]
    if procedure not in procedures_to_functions.keys():
        raise ValueError("Wrong procedure")
    procedure_arguments = {}
    procedure_arguments["sequences"] = sequences
    if procedure == "check_for_motifs":
        procedure_arguments["motif"] = kwargs["motif"]
    return procedures_to_functions[procedure](**procedure_arguments)
