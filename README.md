# Protein Info

This project consists of one function "protein" that helps user to predict molecular weight of amino acid (aa) sequences, translate aa sequences from one-letter to three-letter code etc. Sequences are accepted as single-letter code: 20 aa without stop codon (A,R,N,D,C,E,Q,G,H,I,L,K,M,F,P,S,T,W,Y,V). 

## Technology:

python

## How to use:

This function accepts arguments as a list of strings. Last argument in the list should be a procedure that should be applied to the sequences. 

## List of procedures:

- `molecular_weight` — returns list of float values, that indicate predicted molecular weights of given aa sequences (in kDa)
- `one_letter_to_three` — will return list of strings, containing the same sequences written in three-letter code
- `get_amino_acid_sum` — сounts the amount of each amino acid in the injected protein sequences
- `codon_optimization` — makes codon-optimized DNA based on the introduced amino acid sequences for 3 types of cells: Esherichia coli, Pichia pastoris, Mouse
- 
-
-

## Example of use:

> protein("ACD", "AD", "one_letter_to_three") # ['AlaCysAsp', 'AlaAsp'] \
> protein("ACD", "AD", "molecular_weight") # [0.34, 0.22] \


## Possible erros:
> `ValueError`('Invalid alphabet, please use only single letter amino acid code') # Will occure if character other than A,R,N,D,C,E,Q,G,H,I,L,K,M,F,P,S,T,W,Y,V are used. \
> `ValueError`('Requested procedure is not defined') # Will occure if last argument does not correspond to any listed procedure (see List of procedures). \


## Private policy and contacts
This tool can be freely distributed and used.
\
If you have any suggestions for improving the tool or if you find a bug, please contact us by email.
\
This tool was developed by the "workaholics" team:
\
Yulia Volkova volkova.yulia.leonidovna@gmail.com
\
Dasha Sokolova kalabanova_dasha@mail.ru
\
Team leader: Ivan Kozin ivan.d.kozin@gmail.com
\
Team photo:
![Снимок экрана 2023-09-29 210559_2](https://github.com/ivandkoz/HW4_Functions2_Kozin/assets/63678919/ad1302a1-d139-4c82-b7eb-d5b9ac1897e8)





