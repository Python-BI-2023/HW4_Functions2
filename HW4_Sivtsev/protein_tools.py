aminoacid_alphabet_1to3 = {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp', 'C': 'Cys', 
							'Q': 'Gln', 'E': 'Glu', 'G': 'Gly', 'H': 'His', 'I': 'Ile', 
							'L': 'Leu', 'K': 'Lys', 'M': 'Met', 'F': 'Phe', 'P': 'Pro', 
							'S': 'Ser', 'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val'}

def convert_1to3(prot: str) -> str:
    """
    Converts 1-symbol aminoacid sequence into 3-symbol aminoacid sequence.
    Arguments: 
        -prot (str) - aminoacid sequence in uppercase 1-symbol format
    Return: 
        -output (str) - aminoacid sequence in 3-symbol format.
    """
    output = ''
    if len(prot) > 0:
        for i in prot:
            if i in aminoacid_alphabet_1to3:
                output += aminoacid_alphabet_1to3[i]
            else:
                raise ValueError('Input format: aminoacids in uppercase 1-letter symbols')
    return output
