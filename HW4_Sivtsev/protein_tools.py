aminoacid_alphabet_1to3 = {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp', 'C': 'Cys', 
							'Q': 'Gln', 'E': 'Glu', 'G': 'Gly', 'H': 'His', 'I': 'Ile', 
							'L': 'Leu', 'K': 'Lys', 'M': 'Met', 'F': 'Phe', 'P': 'Pro', 
							'S': 'Ser', 'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val'}

molecular_mass = {'A': 89.094, 'R': 174.203, 'N': 132.119, 'D': 133.104, 'C': 121.154, 
                  'E': 147.131, 'Q': 146.146, 'G': 75.067, 'H': 155.156, 'I': 131.175,
                  'L': 131.175, 'K': 146.189, 'M': 149.208, 'F': 165.192, 'P': 115.132,
                  'S': 105.093, 'T': 119.119, 'W': 204.228, 'Y': 181.191, 'V': 117.148}


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

def calculate_mm(prot: str) -> float:
    """
    Calculates molecular mass of protein.
    Argumets:
        -prot (str) - aminoacid sequence in uppercase 1-symbol format.
    Return:
        -output (float) - molecular mass in float format with 2 digits after dot.
    """
    prot_seq = set(prot)
    output = 0
    if len(prot) == 1:
        output = molecular_mass[prot]
    else:
        for i in prot_seq:
            output += prot.count(i) * molecular_mass[i] - (18.0153*(len(prot)-1))
    return round(output,3)