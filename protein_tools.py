def compare ():
   pass


def count_length (protein: str) -> list:
    """
    Сounting the length of an amino acid sequence/protein in the number of amino acids
    :param protein:  sequence of protein
    :return: number of amino acids in an amino acid sequence/protein
    """
    length_p = len(protein)
    return length_p


def count_percentage():
   pass 


def find_pattern(): 
   pass


def transform_to_DNA_code():
    """
    Transforming of an amino acid sequence/protein to DNA sequence
    :param protein: amino acid sequence of protein
    :return: sequence of protein in the DNA sequence form 
    """
    retrnaslation_dict = {
        'F': 'TTC', 'f': 'ttc',
        'L': 'TTA', 'l': 'tta',
        'S': 'TCG', 's': 'tcg',
        'Y': 'TAC', 'y': 'tac',
        'C': 'TGC', 'c': 'tgc',
        'W': 'TGG', 'w': 'tgg',
        'P': 'CCC', 'p': 'ccc',
        'H': 'CAT', 'h': 'cat',
        'Q': 'GAA', 'q': 'gaa',
        'R': 'CGA', 'r': 'cga',
        'I': 'ATT', 'i': 'att',
        'M': 'ATG', 'm': 'atg',
        'T': 'ACC', 't': 'acc',
        'N': 'AAT', 'n': 'aat',
        'K': 'AAA', 'k': 'aaa',
        'V': 'GTT', 'v': 'gtt',
        'A': 'GCA', 'a': 'gca',
        'D': 'GAT', 'd': 'gca',
        'E': 'GAG', 'e': 'gag',
        'G': 'GGG', 'g': 'ggg'
    }

    return ''.join([retrnaslation_dict[i] for i in protein])


def rename_three_letter_name():
   pass 


def main(*proteins, options = None):
    proteins = list(proteins)

    operations = {
        'compare': compare,
        'length': count_length,
        'percentage ': count_percentage,
        'pattern': find_pattern,
        '3Letter_name': rename_three_letter_name,
        'plasmid_code': transform_to_DNA_code
    }

    if options == ('compare' or 'pattern' or '3L_name'):
        result = operations[options](proteins[:-2], proteins[-2], proteins[-1])
        return (result)
    elif options == ('3Letter_name'):
        result = operations[options](proteins[:-1], proteins[-1])
        return (result)
    elif options == ('length' or 'percentage' or 'plasmid_code'):
        result = []
        for protein in proteins:
            res = operations[options](protein)
            result.append(res)
        return (result)
    else:
        raise ValueError('Incorrect options input, please try again')

main ()
