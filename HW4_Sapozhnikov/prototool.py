from typing import List, Optional, Tuple, Union


def prettify_alignment(aligned_seq_on: str, aligned_seq2: str) -> None:
    """
    Prettifies alignment output by printing out two
    sequences on top of each other

    Finds the start of aligned sequence in the longer of sequences.\\
    Prints the longer sequence as an upper one and aligned sequence
    is bellow separated via vertical lines

    Args:
    - aligned_seq_on, aligned_seq2 - sequences
    from the local_alignment()

    Returns:
    None \\
    Prints out the prettified view in stdout
    """

    print(aligned_seq_on)
    print('|' * len(aligned_seq2))
    print(aligned_seq2)


def local_alignment(seq_on: str,
                    seq2: Union[List[str], str],
                    alignment_dict: dict,
                    seq_id: int,
                    match=2,
                    mismatch=-1,
                    gap=-1,
                    prettify: bool = True) -> dict:
    """
    Perform a local alignment of 2 given sequences

    Args:
    - seq_on - the sequence to align onto
    - seq2 - sequences to align
    - alignment_dict - a dictionary to yield alignment results
    - match, mismatch, gap - alignment scoring and penalty values
    defaulted to 2, -1, -1
    - prettify - if True (default) prints out the prettified version
    of sequences aligned on top of each other
    - seq_id - itterator for a seq list

    Returns:
    - a a dictionary with alignment resluts
    """

    len_seq_on, len_seq2 = len(seq_on), len(seq2)

    # Initialize the score matrix and traceback matrix
    score_matrix = [[0] * (len_seq2 + 1) for _ in range(len_seq_on + 1)]
    traceback_matrix = [[None] * (len_seq2 + 1) for _ in range(len_seq_on + 1)]

    alignment_score = 0  # To keep track of the maximum score in the matrix
    max_i, max_j = 0, 0  # To store the position of the maximum score

    # Fill in the score matrix
    for i in range(1, len_seq_on + 1):
        for j in range(1, len_seq2 + 1):
            if seq_on[i - 1] == seq2[j - 1]:
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
    aligned_seq_on = []
    aligned_seq2 = []

    counter_identity: int = 0
    counter_gaps: int = 0

    i, j = max_i, max_j

    while i > 0 and j > 0:
        if traceback_matrix[i][j] == "match":
            aligned_seq_on.append(seq_on[i - 1])
            aligned_seq2.append(seq2[j - 1])
            counter_identity += 1
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == "delete":
            aligned_seq_on.append(seq_on[i - 1])
            aligned_seq2.append("-")
            counter_gaps += 1
            i -= 1
        elif traceback_matrix[i][j] == "insert":
            aligned_seq_on.append("-")
            aligned_seq2.append(seq2[j - 1])
            counter_gaps += 1
            j -= 1
        else:
            break

    # Reverse the aligned sequences
    aligned_seq_on = "".join(aligned_seq_on[::-1])
    aligned_seq2 = "".join(aligned_seq2[::-1])

    alignment_length = (len(aligned_seq_on)
                        if len(aligned_seq_on) < len(aligned_seq2)
                        else len(aligned_seq2))

    # Form an output dictionary
    alignment_dict['aligned_seq_on'] = aligned_seq_on

    identity = round(counter_identity/alignment_length, 4)

    alignment_dict[f'aligned_seq{seq_id+1}'] = {'seq': aligned_seq2,
                                                'length': alignment_length,
                                                'score': alignment_score,
                                                'identity': identity,
                                                'gaps': counter_gaps}

    # Prettify an alignment output
    if prettify is True:
        prettify_alignment(aligned_seq_on, aligned_seq2)
    else:
        pass

    return alignment_dict


def check_input(*args: List[str]) -> Tuple[List[str],
                                           str,
                                           Optional[str]]:
    """
    Function to check the validity of the input.

    Args:
    *args - are supposed to be all sequences to process and the method to
    process with.
    The method is supposed to be the last argument.

    Returns:
    - seqs_list - list of sequences
    - method - a chosen method to use
    - seq_on (optional) - in case of local_alignment method
    """

    if len(args) < 1:
        # Handle the case where there are no arguments
        raise ValueError("No input defined.")
    else:
        # Check the last element of the input is a valid method
        method = args[-1]
        if method not in ['local_alignment', '', '', '', '']:
            raise ValueError(method, " is not a valid method.")
        else:
            # Form a list with sequences from the input
            seqs_list = list(args[:-1])
            if method == 'local_alignment':
                seq_on = seqs_list.pop(0)
                return seqs_list, method, seq_on
            seq_on = None
            return seqs_list, method, seq_on


def main(*args: Tuple[Union[List[str], str], str]) -> dict:
    """
    This function provides the access to the following methods:
    1. Local Alignment of two sequences - the last argument: 'local_alignment'
       - needs at least 2 protein sequences 1-letter encoded.
       When more than 2 sequences are passed, uses the first
       entered sequence to align the rest on
       - performs an alignment using Smith-Waterman algorithm
    2. ...
    3. ...
    4. ...
    5. ...

    Args:
    *args - are supposed to be all sequences to process and the method
    to process with.
    The method is supposed to be the last argument.

    Returns:
    function_result - result of a chosen function
    """

    seqs_list, method, seq_on = check_input(*args)
    print(seqs_list, method, seq_on)

    match method:

        case 'local_alignment':

            alignment_dict: dict = {}
            for seq_id, seq in enumerate(seqs_list):
                function_result = local_alignment(seq_on=seq_on,
                                                  seq2=seq,
                                                  alignment_dict=alignment_dict,
                                                  seq_id=seq_id,
                                                  prettify=True)

        case '':

            pass

        case _:

            function_result = None

    return function_result


test = main("CGTAGTCGATGCTG", "AGTCGTACAT", "ATGRC", "local_alignment")
print(test)
