  all_aminoacids = {'A', 'R', 'N', 'D', 'C', 'H', 'G', 'Q', 'E', 'I', 
                     'L', 'K', 'M', 'P', 'S', 'Y', 'T', 'W', 'F', 'V'}
def is_peptide(seq):
    if set(seq).issubset(all_aminoacids): # if set(seq) <= all_aminoacids
        return True
    raise ValueError('Incoming sequence is not a peptide')
    
    
def main(*seqs, operation = None)
    if operation == None:
        raise ValueError('Operation value is not specified')
    
        raise ValueError('Incorrect operation value')
    for seq in seqs:
        is_peptide(seq)
        return operation(seq)
