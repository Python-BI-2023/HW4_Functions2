def compare(sequences: list, round_dec=3, percentages=False)->dict:
#"""
#Compare aminoacids between reference sequence and other sequences
#arguments:
#    - sequences (list): reference sequence and other sequences for comparison
#    - round_dec (int): a number of decimals to round the number to
#    - percentages (bool): whether percentages are returned instead of fractions
#return:
#    - comparisons (dict): dictionary with compared sequences as keys and percentages/fractions as their values
#"""
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


def count_length():
   pass


def count_percentage():
   pass 


def compare_pattern(sequence: str, pattern: str)->bool:
#"""
#Compare a given pattern to a fragment of sequence of the same length
#arguments:
#    - sequence (str): sequence fragment to compare with the pattern
#    - pattern (str): pattern for comparison
#return:
#    - (bool): whether pattern and fragment match
#"""
    for i in range(0,len(sequence)):
        if not sequence[i]==pattern[i]:
            return False
            break
    return True
    
def find_pattern(sequences: list, pattern: str)->dict:
#"""
#Find all non-overlaping instances of a given pattern in sequences
#arguments:
#    - sequences (list): sequences to find the pattern in
#    - pattern (str): pattern in question
#return
#    - finds(dict): dictionary with sequences as keys and lists of indexes of patterns and the number of patterns as values
#"""
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


def transform_to_DNA_code():
   pass 


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

    if options == 'compare':
        result = operations[options](proteins[:-2], proteins[-2], proteins[-1])
        return (result)
    elif options == 'pattern':
        result = operations[options](proteins[1:len(proteins)],proteins[0])
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
