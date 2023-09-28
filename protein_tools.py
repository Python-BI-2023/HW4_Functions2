def compare ():
   pass


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
