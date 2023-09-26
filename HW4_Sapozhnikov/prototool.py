def local_alignment(seq1: str, seq2: str, match=2, mismatch=-1, gap=-1, prettify: bool=True) -> list:
    """
    perform a local alignment of 2 given sequences

    Args:
    - seq1, seq2 (str) - sequences to align
    - match, mismatch, gap (int) - alignment scoring and penalty values
    defaulted to 2, -1, -1

    Returns:
    - a a dictionary of {'aligned_seq1':aligned_seq1,
                        'aligned_seq2':aligned_seq2, 
                        'alignment_score':alignment_score} 
    """

    m, n = len(seq1), len(seq2)
    
    # Initialize the score matrix and traceback matrix
    score_matrix = [[0] * (n + 1) for _ in range(m + 1)]
    traceback_matrix = [[None] * (n + 1) for _ in range(m + 1)]
    
    alignment_score = 0  # To keep track of the maximum score in the matrix
    max_i, max_j = 0, 0  # To store the position of the maximum score

    # Fill in the score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                match_score = score_matrix[i - 1][j - 1] + match
            else:
                match_score = score_matrix[i - 1][j - 1] + mismatch
            
            delete_score = score_matrix[i - 1][j] + gap
            insert_score = score_matrix[i][j - 1] + gap
            
            # Calculate the maximum score for the current cell
            score = max(0, match_score, delete_score, insert_score)
            
            # Update the score matrix and traceback matrix
            score_matrix[i][j] = score
            
            if score > alignment_score:
                alignment_score = score
                max_i, max_j = i, j

            if score == match_score:
                traceback_matrix[i][j] = "match"
            elif score == delete_score:
                traceback_matrix[i][j] = "delete"
            elif score == insert_score:
                traceback_matrix[i][j] = "insert"
            else:
                traceback_matrix[i][j] = "none"
    
    # Traceback to find the aligned sequences
    aligned_seq1 = []
    aligned_seq2 = []
    
    i, j = max_i, max_j
    
    while i > 0 and j > 0:
        if traceback_matrix[i][j] == "match":
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == "delete":
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append("-")
            i -= 1
        elif traceback_matrix[i][j] == "insert":
            aligned_seq1.append("-")
            aligned_seq2.append(seq2[j - 1])
            j -= 1
        else:
            break
    
    # Reverse the aligned sequences
    aligned_seq1 = "".join(aligned_seq1[::-1])
    aligned_seq2 = "".join(aligned_seq2[::-1])

    # Form an output dictionary
    alignment_dict = {'aligned_seq1':aligned_seq1,
                      'aligned_seq2':aligned_seq2,
                      'alignment_score':alignment_score}  

    # Prettify an alignment output
    seq_on = (seq1 if seq1 <= seq2 else seq2)
    if prettify == True:
        prettify_alignment(seq_on, alignment_dict)  
    else: 
        pass

    return alignment_dict


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
    2. ...

    """
    pass