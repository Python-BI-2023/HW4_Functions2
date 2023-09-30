# Protein_tools.py
## A tool to work with protein sequences

*Proteins* are under the constant focus of scientists. Currently, there are an enormous amount of tools to operate with nucleotide sequences, however, the same ones for proteins are extremely rare. 


`Protein_tools.py` is an open-source program that facilitates working with protein sequences. 

*В моём представлении здесь должна быть картинка*

## Usage
The programm is based on `run_protein_tools` function that takes the list of **one-letter amino acid sequences**, name of procedure and relevant arguments. If you have three-letter amino acid sequences you could convert them by using `three_one_letter_code` procedure.

To start with the program run the following command:

`run_protein_tools([sequence_1, sequence_2 ..., sequence_n], procedure, ...)`

Where:
- [sequence_1, sequence_2 ..., sequence_n] - a list of protein sequences
- procedure - a type of procedure to use that is inputed in *string* type
- ... - an additional argument that is to be inputed in *string* type

## Options

The program has five types of procedures:

 `three_one_letter_code`

- The main aim - to convert three-letter amino acid sequences to one-letter ones and vice-versa
- An additional argument: no

 `define_molecular_weight` 

- The main aim - to determine the exact molecular weight of protein sequences
- An additional argument: no

 `check_for_motifs` 

- The main aim - to search for the motif of interest in protein sequences
- An additional argument: motif (*str*)

 `search_for_alt_frames` 

- The main aim - to look for alternative frames that start with methyonine or other non-canonical start amino acids
- An additional argument: alt_start_aa (*str*)
- Use alt_start_aa only for non-canonical start amino acids
- Without alt_start_aa the procedure find alternative frames that start with methyonine

`convert_to_nucl_acids` 
- The main aim - to convert protein sequences to DNA, RNA or both nucleic acid sequences
- The program use the most frequent codons in human that could be found [here](https://www.genscript.com/tools/codon-frequency-table)
- An additional argument: nucl_acids (*str*)
  

## Examples
```python
run_protein_tools(['met-Asn-Tyr', 'Ile-Ala-Ala'], procedure = 'three_one_letter_code')  # ['mNY', 'IAA']
run_protein_tools(['mNY','IAA'], procedure = 'three_one_letter_code')  # ['met-Asn-Tyr', 'Ile-Ala-Ala']
run_protein_tools(['MNY','IAA'], procedure = 'define_molecular_weight')  # [462.52000000000004, 309.35]
```
```python
run_protein_tools(['mNY','IAA'], procedure = 'three_one_letter_code') #  ['met-Asn-Tyr', 'Ile-Ala-Ala']
```

## Troubleshooting

## Contacts
Authors:

Vladimir Grigoriants 

Tulyavko Vlada 

Ekaterina Shitik (EkaterinShitik)
