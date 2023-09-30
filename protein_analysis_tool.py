amino_short_names_dic = {'A':'Ala', 'R':'Arg', 'N':'Asn',
                         'D':'Asp', 'V':'Val', 'H':'His',
                         'G':'Gly', 'Q':'Gln', 'E':'Glu',
                         'I':'Ile', 'L':'Leu', 'K':'Lys',
                         'M':'Met', 'P':'Pro', 'S':'Ser',
                         'Y':'Tyr', 'T':'Thr', 'W':'Trp',
                         'F':'Phe', 'C':'Cys'}
amino_names_dic = {'ala': 'A', 'arg': 'R', 'asn': 'N',
                    'asp': 'D', 'val': 'V', 'his': 'H',
                    'gly': 'G', 'gln': 'Q', 'glu': 'E',
                    'ile': 'I', 'leu': 'L', 'lys': 'K',
                    'met': 'M', 'pro': 'P', 'ser': 'S',
                    'tyr': 'Y', 'thr': 'T', 'trp': 'W',
                    'phe': 'F', 'cys': 'C'}

amino_names_dic_reverse = {'Ala': 'A', 'Arg': 'R', 'Asn': 'N',
                    'Asp': 'D', 'Val': 'V', 'His': 'H',
                    'Gly': 'G', 'Gln': 'Q', 'Glu': 'E',
                    'Ile': 'I', 'Leu': 'L', 'Lys': 'K',
                    'Met': 'M', 'Pro': 'P', 'Ser': 'S',
                    'Tyr': 'Y', 'Thr': 'T', 'Trp': 'W',
                    'Phe': 'F', 'Cys': 'C'}

def lenght(seqs):
    result = [len(seq) for seq in seqs]
    print(result)
    return result


def reverse(seqs):
    result = [seq[::-1] for seq in seqs]
    return result
def name_transform(seqs, format):
    result = []
    print(seqs)
    if format == 1:
        for seq in seqs: 
            seq = seq.upper()
            for letter in seq:
                if check_amino_acid(letter):
                    pass
            result.append(seq)
        return result
    elif format == 3:
        for seq in seqs:
            seq = seq.lower()
            seq3 = [seq[i:i+3] for i in range(0, len(seq), 3)]
            for triplet in seq3:
                if check_amino_acid(triplet):
                    pass
                else: return False
            seq_transformed = "".join([amino_names_dic.get(seq) for seq in seq3])
            result.append(seq_transformed)
        return result

    else:
        print('Error unsupported format. Only formats 1 and 3 are supported')
        return False
        

def check_amino_acid(input):
    if len(input) == 1:
        letter = input
        if letter not in amino_short_names_dic.keys():
            print(f'Error {letter} is not an amino acid. Correct your input')
            return False
        else: return True
    elif len(input) == 3:
        triplet = input
        if triplet not in amino_names_dic.keys():
            print(f'Error {triplet} is not an amino acid. Correct your input')
            return False
        else: return True
    else:
        print(f'Error {input} is incorrect form of amino acid notation. Correct your input')
        return False
    
    