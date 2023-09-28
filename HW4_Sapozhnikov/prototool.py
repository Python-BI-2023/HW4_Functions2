def main():
    """
    an entry point to the tool

    This tool provides the following functionality:
    - local alignment of two sequences
    - ...

    To get started choose one of the possible programms to run:
    1. Local alignment
    Enter two protein sequences in 1- letter encoding. The code will return alignment scores and 
    sequences aligned on each other. 
    2. ...

    """
    pass


def from_proteins_seqs_to_rna(*seqs):
    PROTEIN_TO_RNA_COMBINATION = {
        'Ala': {'GCU', 'GCC', 'GCA', 'GCG'},
        'Arg': {'CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'},
        'Asn': {'AAU', 'AAC'},
        'Asp': {'GAU', 'GAC'},
        'Cys': {'UGU', 'UGC'},
        'Glu': {'GAA', 'GAG'},
        'Gln': {'CAA', 'CAG'},
        'Gly': {'GGU', 'GGC', 'GGA', 'GGG'},
        'His': {'CAU', 'CAC'},
        'Ile': {'AUU', 'AUC', 'AUA'},
        'Leu': {'CUU', 'CUC', 'CUA', 'CUG'},
        'Lys': {'AAA', 'AAG'},
        'Met': {'AUG'},
        'Phe': {'UUU', 'UUC'},
        'Pro': {'CCU', 'CCC', 'CCA', 'CCG'},
        'Ser': {'UCU', 'UCC', 'UCA', 'UCG'},
        'Thr': {'ACU', 'ACC', 'ACA', 'ACG'},
        'Tyr': {'UAU', 'UAC'},
        'Trp': {'UGG'},
        'Val': {'GUU', 'GUC', 'GUA', 'GUG'},
    }

    for aminoacids in seqs:
        found_sets = []
        divided_acids = [aminoacids[i:i + 3] for i in range(0, len(aminoacids), 3)]
        for divided_acid in divided_acids:
            if divided_acid in PROTEIN_TO_RNA_COMBINATION.keys():
                found_sets.append([])
                for comb in PROTEIN_TO_RNA_COMBINATION[divided_acid]:
                    found_sets[-1].append(comb)

        for i in range(0, len(found_sets)):
            for j in range(0, len(found_sets[i])):
                combination = found_sets[i][j]
                if len(found_sets) > 1:
                    for k in range(0, len(found_sets)):
                        if k != i:
                            for m in range(0, len(found_sets[k])):
                                combination += ' ' + found_sets[k][m]

                    print(combination)

from_proteins_seqs_to_rna('ValTyrMet')