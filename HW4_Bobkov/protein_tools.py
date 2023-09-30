def compare(sequences: list, round_dec=3, percentages=False)->dict:
    """
    Compare aminoacids between reference sequence and other sequences
    arguments:
    - sequences (list): reference sequence and other sequences for comparison
    - round_dec (int): a number of decimals to round the number to
    - percentages (bool): whether percentages are returned instead of fractions
    return:
    - comparisons (dict): dictionary with compared sequences as keys and percentages/fractions as their values
    """
    comparisons={}
    for seq in range(1,len(sequences)):
        comparison=[]
        for j in range(0,len(sequences[seq])):
            comparison.append(sequences[0][j]==sequences[seq][j])
        if percentages:
            comparisons[sequences[seq]]=round(sum(comparison)*100/len(sequences[seq]),round_dec)
        else:
            comparisons[sequences[seq]]=round(sum(comparison)/len(sequences[seq]),round_dec)
    return comparisons


def count_length(protein: str) -> list:
    """
    Сounting the length of an amino acid sequence/protein in the number of amino acids
    :param protein:  sequence of protein
    :return: number of amino acids in an amino acid sequence/protein
    """
    length_p = len(protein)
    return length_p


def count_percentage(seq: str)->dict:
    """
    Count percentage of each amino acid in sequence
    arguments:
        - seq (str): sequence for counting
    return:
        - dict: dictionary with counted percentage    
    """
    l = count_length(seq)
    res = {}
    for aa in seq:
        if aa not in res:
            res[aa] = 1
        else:
            res[aa]+=1
    res.update((key, round(value/l*100, 2)) for key, value in res.items())
    res={key: value for key, value in sorted(res.items(), key=lambda item: item[1], reverse=True)}
    return res


def compare_pattern(sequence: str, pattern: str)->bool:
    """
    Compare a given pattern to a fragment of sequence of the same length
    arguments:
    - sequence (str): sequence fragment to compare with the pattern
    - pattern (str): pattern for comparison
    return:
    - (bool): whether pattern and fragment match
    """
    for i in range(0,len(sequence)):
        if not sequence[i]==pattern[i]:
            return False
            break
    return True
    
def find_pattern(sequences: list, pattern: str)->dict:
    """
    Find all non-overlaping instances of a given pattern in sequences
    arguments:
    - sequences (list): sequences to find the pattern in
    - pattern (str): pattern in question
    return
    - finds(dict): dictionary with sequences as keys and lists of indexes of patterns and the number of patterns as values
    """
    finds={}
    for j in range(0, len(sequences)):
        find=[]
        for i in range(0, len(sequences[j])):
            if compare_pattern(sequences[j][i:i+len(pattern)], pattern):
                find.append(i)
                i+=len(pattern)
            else:
                continue
        finds[sequences[j]]=[len(find)]+find
    return finds


def transform_to_DNA_code(protein):
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


def rename_three_letter_name (seqs: list, sep = '')->list:
    """
    Transform into a three-letter amino acids entry.
    arguments:
        - seqs (list): list of sequences for transforming to three-letter entire
        - sep (str): separator between aminoacids, default = ''
    return:
        - list: transformed sequences with separators
    """
    res=[]
    threel = {'A': 'ALA', 'R': 'ARG', 'N': 'ASN', 'D': "ASP", 'V': 'VAL', 
                 'H': 'HIS', 'G': "GLY", 'Q': "GLN", 'E': 'GLU', 'I': 'ILE', 
                 'L': 'LEU', 'K': 'LYS', 'M': 'MET', 'P': 'PRO', 'S': 'SER', 
                 'Y': 'TYR', 'T': 'THR', 'W': 'TRP', 'F': 'PHE', 'C': 'CYS', 
                 'a': 'ala', 'r': 'arg', 'n': 'asn', 'd': "asp", 'v': 'val', 
                 'h': 'his', 'g': "gly", 'q': "gln", 'e': 'glu', 'i': 'ile', 
                 'l': 'leu', 'k': 'lys', 'm': 'met', 'p': 'pro', 's': 'ser', 
                 'y': 'tyr', 't': 'thr', 'w': 'trp', 'f': 'phe', 'c': 'cys'}
    for seq in seqs:
        threel_form = ''
        for aa in seq:
            threel_form = threel_form + threel[aa] + sep
        if sep:
            threel_form = threel_form[:-1]
        res.append(threel_form)
    return res

def is_protein(seq):
    """
    Checking wheter a sequence is a protein sequence
    """
    aminoacids=['F','f','L','l','S','s','Y','y','C','c','W','w','P','p','H','h','Q','q','R','r','I','i','M','m','T','t','N','n','K','k','V','v','A','a','D','d','E','e','G','g']
    for i in seq:
        if i not in aminoacids:
            raise ValueError('Incorrect input: protein sequences containing 20 common aminoacids in one-letter format were expected. Please try again')

def string_check(sequences):
    """
    Checking whether a sequence is a protein sequence and is of type str 
    """
    for seq in sequences:
        if type(seq) != str:
            raise ValueError('Incorrect input type: protein sequences of type str were expected. Please try again')
        is_protein(seq)

def verify(sequences,options):
    """
    Argument verification for all options
    """
    if options=='length' or options=='percentage' or options=='DNA_code':
        string_check(sequences)
    elif options=='3Letter_name':
        string_check(sequences[:-1])
    elif options=='compare':
        string_check(sequences[:-2])
        for i in range(0,len(sequences[:-2])):
            if len(sequences[i])!=len(sequences[0]):
                raise ValueError('Incorrect input: same length protein sequences were expected. Please try again')
        if type(sequences[-2]) != int or sequences[-2]<0:
            raise ValueError('Incorrect input type: positive integer value was expected as the second-to-last argument. Please try again')
        if type(sequences[-1]) != bool:
            raise ValueError('Incorrect input type: bool value was expected as the last argument. Please try again')
    elif options=='pattern':
        string_check(sequences)
        for i in range(1,len(sequences)):
            if len(sequences[0])>len(sequences[i]):
                raise ValueError('Incorrect input: pattern length shorter or equal to protein sequence length was expected. Please try again')

def protein_tool(*proteins, options = None):
    proteins = list(proteins)
    verify(proteins, options)
    operations = {
        'compare': compare,
        'length': count_length,
        'percentage': count_percentage,
        'pattern': find_pattern,
        '3Letter_name': rename_three_letter_name,
        'DNA_code': transform_to_DNA_code
    }

    if options == 'compare':
        result = operations[options](proteins[:-2], proteins[-2], proteins[-1])
        return (result)
    elif options == 'pattern':
        result = operations[options](proteins[1:len(proteins)],proteins[0])
        return (result)
    elif options == '3Letter_name':
        result = operations[options](proteins[:-1], proteins[-1])
        return (result)
    elif options == 'length' or options =='percentage' or options == 'DNA_code':
        result = []
        for protein in proteins:
            res = operations[options](protein)
            result.append(res)
        return (result)
    else:
        raise ValueError('Incorrect options input, please try again')

protein_tool()
