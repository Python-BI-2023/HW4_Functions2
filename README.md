# run_protein_tool

```run_protein_tool``` includes a set of commands that perform various operations with protein or peptide sequences of any length. The input sequence(s) must be written 
using 1-letter amino acid code and can contain any of the following 20 amino acids:

![aacids](https://github.com/sme229/HW4_Functions2/assets/104040609/825a697f-5562-4829-9771-01e3b519bdee)

The following functions are implemented:

1. ```molecular_weight``` This function takes 1-letter coded protein sequence(s) (string) and calculates molecular weight rounded to integer in g/mol. The function is not case-sensitive.
Usage examples:
```
run_protein_tool('peptide', function='molecular_weight')
799
```
```
run_protein_tool('pEpTiDe', function='molecular_weight')
799
```
2. ```one_to_three_letter``` This function takes 1-letter coded protein sequence(s) (string) and returns a 3-letter coded sequence(s) without spaces (string). Usage examples:
```
run_protein_tool('PEPTIDE', function='one_to_three_letter')
'ProGluProThrIleAspGlu'
```
```
run_protein_tool('p', 'peptide', function='one_to_three_letter')
['Pro', 'ProGluProThrIleAspGlu']
```
3. ```amino_acid_frequency``` This function takes 1-letter coded protein sequence(s) (string), calculates frequency for each unique amino acid and creates a dictionary
with amino acids as keys and corresponding frequencies as values. Usage example:

```
run_protein_tool('MADSEQNQEEAGGGEQREH', function='amino_acid_frequency')
{'M': 5.26,
'A': 10.53,
'D': 5.26,
'S': 5.26,
'E': 26.32,
'Q': 15.79,
'N': 5.26,
'G': 15.79,
'R': 5.26,
'H': 5.26}
```
4. ```find_motifs``` This function takes two string arguments: 1-letter coded protein sequence(s) and a motif of interest, where motif is any sequence which occurence 
will be searched for in the input protein sequence(s). The function returns position(s) of the motif. If a motif was not found, the function will return an empty list.
Please note that this function can only search for one motif at a time. Usage example:

```
find_motifs('MADSEQNQEEAGGGEQREH', function='find_motifs', motif='GG')
[12, 13]
```
# Troubleshooting

Please make sure that your input sequence(s) is written using the **1-letter** amino acid code as shown in the examples. A sequence containing letters that 
do not correspond to one of the 20 amino acids from the table above will result in 'Invalid Input' error. Please note that function ```find_motifs``` also requires the motif
of interest as input after the function name.

# Contributors

Elena Smertina implemented check_protein_seq, molecular_weight, one_to_three_letter and run_protein_tool functions;  
Natalia Erofeeva implemented amino_acid_frequency and find_motifs functions.   











   






         
