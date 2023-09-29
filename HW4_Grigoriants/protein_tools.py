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
