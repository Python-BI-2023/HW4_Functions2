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


def find_pattern(): 
   pass


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
