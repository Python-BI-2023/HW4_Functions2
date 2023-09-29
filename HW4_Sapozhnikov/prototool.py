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
    2. Call method

    """
    pass


def from_proteins_seqs_to_rna(*seqs: str) -> dict:
    """
    :param seqs: strings with type 'ValTyrAla','AsnAspCys'. seqs is args parameter, so
    you can pass more than one sequences at the time.
    :return: dictionary, where [key] is your input protein sequences
    and values are combinations of RNA codones, which encode this protein
    """
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
    answer_dictionary = {}
    for aminoacids in seqs:
        rna_combination = ''
        divided_acids = [aminoacids[i:i + 3] for i in range(0, len(aminoacids), 3)]
        for divided_acid in divided_acids:
            if divided_acid in PROTEIN_TO_RNA_COMBINATION.keys():
                rna_combination += next(iter(PROTEIN_TO_RNA_COMBINATION[divided_acid]))
        answer_dictionary[aminoacids] = rna_combination
    return answer_dictionary

def isoelectric_point_determination(*seqs: str) -> dict:
    """
    :param seqs: strings with type 'ValTyrAla','AsnAspCys'. seqs is args parameter, so
    you can pass more than one sequences at the time.
    :return: dictionary, when [key] is your input protein sequence and value is an isoelectric point
    of your input proteins
    """
    PKA_AMINOACIDS = {
        'Ala': [2.34, 9.69],
        'Arg': [2.17, 9.04, 12.68],
        'Asn': [1.88, 9.60, 3.65],
        'Asp': [1.88, 9.60, 3.65],
        'Cys': [1.96, 10.28, 8.18],
        'Glu': [2.19, 9.67, 4.25],
        'Gln': [2.17, 9.13],
        'Gly': [2.34, 9.60],
        'His': [1.82, 9.17],
        'Ile': [2.36, 9.68],
        'Leu': [2.36, 9.60],
        'Lys': [2.18, 8.95, 10.53],
        'Met': [2.28, 9.21],
        'Phe': [2.20, 9.13],
        'Pro': [1.99, 10.96],
        'Ser': [2.21, 9.15],
        'Thr': [2.11, 9.62],
        'Tyr': [2.20, 9.11, 10.07],
        'Trp': [2.38, 9.39],
        'Val': [2.32, 9.62],
    }

    answer_dictionary = {}

    for aminoacids in seqs:
        divided_acids = [aminoacids[i:i + 3] for i in range(0, len(aminoacids), 3)]
        for divided_acid in divided_acids:
            if not divided_acid in PKA_AMINOACIDS.keys():
                raise ValueError('Non-protein aminoacids in sequence')

        isoelectric_point_mean = 0
        count_groups = 0
        for acid_index in range(0, len(divided_acids)):
            if acid_index == 0:
                isoelectric_point_mean += PKA_AMINOACIDS[divided_acids[acid_index]][0]
                count_groups += 1
            elif acid_index == len(divided_acids) - 1:
                isoelectric_point_mean = isoelectric_point_mean + PKA_AMINOACIDS[divided_acids[acid_index]][-1]
                count_groups += 1
            else:
                if len(PKA_AMINOACIDS[divided_acids[acid_index]]) > 2:
                    isoelectric_point_mean = isoelectric_point_mean + PKA_AMINOACIDS[divided_acids[acid_index]][1]
                    count_groups += 1
        answer_dictionary[aminoacids] = isoelectric_point_mean / count_groups
    return answer_dictionary
