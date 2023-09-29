# Protein Info

This project consists of one function "protein" that helps user to predict molecular weight of amino acid (aa) sequences, translate aa sequences from one-letter to three-letter code etc. Sequences are accepted as single-letter code: 20 aa without stop codon (A,R,N,D,C,E,Q,G,H,I,L,K,M,F,P,S,T,W,Y,V). 

## Technology:

python

## How to use:

This function accepts arguments as a list of strings. Last argument in the list should be a procedure that should be applied to the sequences. 

## List of procedures:

- `molecular_weight` — returns list of float values, that indicate predicted molecular weights of given aa sequences (in kDa)
- `one_letter_to_three` — will return list of strings, containing the same sequences written in three-letter code
- 
- 
-
-

## Example of use:

> protein("ACD", "AD", "one_letter_to_three") # ['AlaCysAsp', 'AlaAsp'] \
> protein("ACD", "AD", "molecular_weight") # [0.34, 0.22] \

## Possible erros:
> `ValueError`('Invalid alphabet, please use only single letter amino acid code') # Will occure if character other than A,R,N,D,C,E,Q,G,H,I,L,K,M,F,P,S,T,W,Y,V are used. \
> `ValueError`('Requested procedure is not defined') # Will occure if last argument does not correspond to any listed procedure (see List of procedures). \




