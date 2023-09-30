# Protein_tools.py
## A tool to work with protein sequences

*Proteins* are under the constant focus of scientists. Currently, there are an enormous amount of tools to operate with nucleotide sequences, however, the same ones for proteins are extremely rare. 


`Protein_tools.py` is an open-source program that facilitates working with protein sequences. 

*В моём представлении здесь должна быть картинка*

## Usage
The programm is based on `run_protein_tools` function that takes the list of **one-letter amino acid sequences**, a name of procedure and a relevant argument. If you have three-letter amino acids sequences you could convert them by using `three_one_letter_code` procedure in advance. Before using this procedure, check the *Options*.

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
- In case of three-to-one translation the names of amino acids **must be separated with hyphen**
- An additional argument: no

 `define_molecular_weight` 

- The main aim - to determine the exact molecular weight of protein sequences
- An additional argument: no

 `check_for_motifs` 

- The main aim - to search for the motif of interest in protein sequences
- An additional argument: motif (*str*)

 `search_for_alt_frames` 
 
- The main aim - to look for alternative frames that start with methyonine or other non-canonical start amino acids
- Ignores the last three amino acids due to the insignicance of alternative frames of this length
- An additional argument: alt_start_aa (*str*)
- Use alt_start_aa **only for non-canonical start amino acids**
- Without alt_start_aa the procedure find alternative frames that start with methyonine

`convert_to_nucl_acids` 

- The main aim - to convert protein sequences to DNA, RNA or both nucleic acid sequences
- The program use the most frequent codons in human that could be found [here](https://www.genscript.com/tools/codon-frequency-table)
- An additional argument: nucl_acids (*str*)
- Use as nucl_acids only DNA, RNA or both (for more detailes, check *Examples*)
  

## Examples
```python
# three_one_letter_code
run_protein_tools(['met-Asn-Tyr', 'Ile-Ala-Ala'], procedure='three_one_letter_code')  # ['mNY', 'IAA']
run_protein_tools(['mNY','IAA'], procedure='three_one_letter_code')  # ['met-Asn-Tyr', 'Ile-Ala-Ala']

# define_molecular_weight
run_protein_tools(['MNY','IAA'], procedure='define_molecular_weight')  # [462.52000000000004, 309.35]

# check_for_motifs
run_protein_tools(['mNY','IAA'], procedure='check_for_motifs', motif='NY')
# Sequence: mNY
# Motif: NY
# Motif is present in protein sequence starting at positions: 1
# Sequence: IAA
# Motif: NY
# Motif is not present in protein sequence
# {'mNY': [1], 'IAA': []}

# search_for_alt_frames
run_protein_tools(['mNYQTMSPYYDMId'], procedure='search_for_alt_frames')  # {'mNYQTMSPYYDMId': ['MSPYYDMId']}
run_protein_tools(['mNYTQTSP'], procedure='search_for_alt_frames', alt_start_aa='T')  # {'mNYTQTSP': ['TQTSP']}

# convert_to_nucl_acids
run_protein_tools(['MNY'], procedure='convert_to_nucl_acids', nucl_acids = 'RNA')  # {'RNA': ['AUGAACUAU']}
run_protein_tools(['MNY'], procedure='convert_to_nucl_acids', nucl_acids = 'DNA')  # {'DNA': ['ATGAACTAT']}
run_protein_tools(['MNY'], procedure='convert_to_nucl_acids', nucl_acids = 'both') # {'RNA': ['AUGAACUAU'], 'DNA': ['ATGAACTAT']}

```

## Troubleshooting

|  Type of the problem                                             |  Probable cause
| ------------------------------------------------------------ |--------------------
| Output does not correspond the expected resultes             | The name of procedure is wrong. You see the results of another procedure
| ValueError: No sequences provided                          | A list of sequences are not inputed
| ValueError: Wrong procedure                                | The procedure does not exist in this program
| TypeError: takes from 0 to 1 positional arguments but n were given  | Sequences are not collected into the list type
| ValueError: Invalid sequence given                         | The sequences do not correspond to standard amino acid code
| ValueError: Please provide desired motif                   | There are no an additional argument *motif* in `check_for_motifs`
| ValueError: Invalid start AA!                              | There is more than one letter in an additional argument *alt_start_aa* in `search_for_alt_frames`
| ValueError: Please provide desired type of nucl_acids      | There are no an additional argument *nucl_acids* in `convert_to_nucl_acids`
| ValueError: Invalid nucl_acids argument                    | An additional argument in `convert_to_nucl_acids` is written incorrectly
## Contacts
Authors:

Vladimir Grigoriants (*адрес*)

Tulyavko Vlada (*адрес*)

Ekaterina Shitik (shitik.ekaterina@gmail.com)
