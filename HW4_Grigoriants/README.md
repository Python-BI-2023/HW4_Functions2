# Protein_tools.py
## A tool to work with protein sequences

*Proteins* are under the constant focus of scientists. Currently, there are an enormous amount of tools to operate with nucleotide sequences, however, the same ones for proteins are extremely rare. 


`protein_tools.py` is an open-source program that facilitates working with protein sequences. 

## Usage
The programm is based on `run_protein_tools` function that takes the list of **one-letter amino acid sequences**,  a name of procedure and a relevant argument. If you have three-letter amino acids sequences you could convert them by using `three_one_letter_code` procedure in advance. Please convert your three-letter coded sequences with `three_one_letter_code` procedure before using any other procedures on them.

To start with the program run the following command:

`run_protein_tools(sequences, procedure="procedure", ...)`

Where:
- sequences - positional argument, a list of protein sequences
- procedure - keyword argument, a type of procedure to use that is inputed in *string* type
- ... - an additional keyword arguments that are to be inputed in *string* type
- 
Before start, check the *Options* and *Examples*.
## Options

The program has five types of procedures, for more information please see provided docstrings:

 `three_one_letter_code`
 
 ![image](https://drive.google.com/uc?export=view&id=1eACjU_CXFbqeu1iW3ekwcg81n-X3WvTG)

- The main aim - to convert three-letter amino acid sequences to one-letter ones and vice-versa
- In case of three-to-one translation the names of amino acids **must be separated with hyphen**
- An additional argument: no
```
"""
Reverse the protein sequences from one-letter to three-letter format and vice-versa

Case 1: get three-letter sequence\n
Use one-letter amino-acids sequences of any letter case

Case 2: get one-letter sequence\n
Use three-letter amino-acid separated by "-" sequences.
Please note that sequences without "-" are parsed as one-letter code sequences\n
Example: for sequence "Ala" function will return "Ala-leu-ala"

Arguments:
- sequences (tuple[str] or list[str]): protein sequences to convert\n
Example: ["WAG", "MkqRe", "msrlk", "Met-Ala-Gly", "Met-arg-asn-Trp-Ala-Gly", "arg-asn-trp"]

Return:
- list: one-letter/three-letter protein sequences\n
Example: ["Met-Ala-Gly", "Met-arg-asn-Trp-Ala-Gly", "arg-asn-trp", "WAG", "MkqRe", "rlk"]
"""
```

 `define_molecular_weight` 
 
 ![image](https://drive.google.com/uc?export=view&id=1i9_4ys64XsAxnw-08zbgyBQnGzJoGJfr)

- The main aim - to determine the exact molecular weight of protein sequences
- An additional argument: no
```
"""
Define molecular weight of the protein sequences

Use one-letter amino-acids sequences of any letter case
The molecular weight is:
- a sum of masses of each atom constituting a molecule
- expressed in units called daltons (Da)
- rounded to hundredths

Arguments:
- sequences (tuple[str] or list[str]): protein sequences to convert

Return:
- dictionary: protein sequences as keys and molecular masses as values\n
Example: {"WAG": 332.39, "MkqRe": 690.88, "msrlk": 633.86}
"""
```

 `search_for_motifs` 

  ![image](https://drive.google.com/uc?export=view&id=1_bVKRn4RblrfukIxoQc0NZ_FXaJliGAH)

- The main aim - to search for the motif of interest in protein sequences
- An additional arguments: motif (*str*), overlapping (*bool*)
```
"""
Search for motifs - conserved amino acids residues in protein sequence

Search for one motif at a time\n
Search is letter case sensitive\n
Use one-letter aminoacids code for desired sequences and motifs\n
Positions of AA in sequences are counted from 0\n
By default, overlapping matches are counted

Arguments:
- sequences (tuple[str] or list[str]): sequences to check for given motif within\n
Example: sequences = ["AMGAGW", "GAWSGRAGA"]
- motif (str]: desired motif to check presense in every given sequence\n
Example: motif = "GA"
- overlapping (bool): count (True) or skip (False) overlapping matches. (Optional)\n
Example: overlapping = False
Return:
- dictionary: sequences (str] as keys , starting positions for presented motif (list) as values\n
Example: {"AMGAGW": [2], "GAWSGRAGA": [0, 7]}
"""
```
 `search_for_alt_frames` 
 
 ![image](https://drive.google.com/uc?export=view&id=1AdXnkRDIRiC_5yiiI2qiAMSMWbZf1RIm)

- The main aim - to look for alternative frames that start with methyonine or other non-canonical start amino acids
- Ignores the last three amino acids due to the insignicance of alternative frames of this length
- An additional argument: alt_start_aa (*str*)
- Use alt_start_aa **only for non-canonical start amino acids**
- Without alt_start_aa the procedure find alternative frames that start with methyonine
```
"""
Search for alternative frames in a protein sequences

Search is not letter case sensitive\n
Without an alt_start_aa argument search for frames that start with methionine ("M")
To search frames with alternative start codon add alt_start_aa argument\n
In alt_start_aa argument use one-letter code

The function ignores the last three amino acids in sequences

Arguments:
- sequences (tuple[str] or list[str]): sequences to check
- alt_start_aa (str]: the name of an amino acid that is encoded by alternative start AA (Optional)\n
Example: alt_start_aa = "I"

Return:
- dictionary: the number of a sequence and a collection of alternative frames
"""
```
`convert_to_nucl_acids` 
 
 ![image](https://drive.google.com/uc?export=view&id=1_pZJ0Gc-EVcR1zddpDW4Ok3w8t65fW_z)

- The main aim - to convert protein sequences to DNA, RNA or both nucleic acid sequences
- The program use the most frequent codons in human that could be found [here](https://www.genscript.com/tools/codon-frequency-table)
- An additional argument: nucl_acids (*str*)
- Use as nucl_acids only DNA, RNA or both (for more detailes, check *Examples*)
```
"""
Convert protein sequences to RNA or DNA sequences.

Use the most frequent codons in human. The source - https://www.genscript.com/tools/codon-frequency-table\n
All nucleic acids (DNA and RNA) are showed in 5"-3" direction

Arguments:
- sequences (tuple[str] or list[str]): sequences to convert
- nucl_acids (str]: the nucleic acid that is prefered\n
Example: nucl_acids = "RNA" - convert to RNA\n
               nucl_acids = "DNA" - convert to DNA\n
               nucl_acids = "both" - convert to RNA and DNA
Return:
- dictionary: nucleic acids (str) as keys, collection of sequences (list) as values
"""
```

## Examples
```python
# three_one_letter_code
run_protein_tools(['met-Asn-Tyr', 'Ile-Ala-Ala'], procedure='three_one_letter_code')  # ['mNY', 'IAA']
run_protein_tools(['mNY','IAA'], procedure='three_one_letter_code')  # ['met-Asn-Tyr', 'Ile-Ala-Ala']


# define_molecular_weight
run_protein_tools(['MNY','IAA'], procedure='define_molecular_weight')  # {'MNY': 426.52, 'IAA': 273.35}


# check_for_motifs
run_protein_tools(['mNY','IAA'], procedure='search_for_motifs', motif='NY')
#Sequence: mNY
#Motif: NY
#Motif is present in protein sequence starting at positions: 1

#Sequence: IAA
#Motif: NY
#Motif is not present in protein sequence

{'mNY': [1], 'IAA': []}


# search_for_alt_frames
run_protein_tools(['mNYQTMSPYYDMId'], procedure='search_for_alt_frames')  # {'mNYQTMSPYYDMId': ['MSPYYDMId']}
run_protein_tools(['mNYTQTSP'], procedure='search_for_alt_frames', alt_start_aa='T')  # {'mNYTQTSP': ['TQTSP']}


# convert_to_nucl_acids
run_protein_tools(['MNY'], procedure='convert_to_nucl_acids', nucl_acids = 'RNA')  # {'RNA': ['AUGAACUAU']}
run_protein_tools(['MNY'], procedure='convert_to_nucl_acids', nucl_acids = 'DNA')  # {'DNA': ['TACTTGATA']}
run_protein_tools(['MNY'], procedure='convert_to_nucl_acids', nucl_acids = 'both') # {'RNA': ['AUGAACUAU'], 'DNA': ['TACTTGATA']}

```

## Troubleshooting

|  Type of the problem                                             |  Probable cause
| ------------------------------------------------------------ |--------------------
| Output does not correspond the expected resultes             | The name of procedure is wrong. You see the results of another procedure
| ValueError: No sequences provided                            | A list of sequences are not inputed
| ValueError: Wrong procedure                                  | The procedure does not exist in this program
| TypeError: takes from 0 to 1 positional arguments but n were given  | Sequences are not collected into the list type
| ValueError: Invalid sequence given                           | The sequences do not correspond to standard amino acid code
| ValueError: Please provide desired motif                     | There are no an additional argument *motif* in `search_for_motifs`
| ValueError: Invalid start AA                                 | There is more than one letter in an additional argument *alt_start_aa* in `search_for_alt_frames`
| ValueError: Please provide desired type of nucl_acids        | There are no an additional argument *nucl_acids* in `convert_to_nucl_acids`
| ValueError: Invalid nucl_acids argument                      | An additional argument in `convert_to_nucl_acids` is written incorrectly
## Contacts 
Vladimir Grigoriants (vova.grig2002@gmail.com)
Team-leader. Bioinformatician, immunologist, MiLaborary inc. TCR-libraries QC developer 

Ekaterina Shitik (shitik.ekaterina@gmail.com)
Doctor of medicine, molecular biologist with the main interests on gene engineering, AAV vectors and CRISPR/Cas9 technologies

Vlada Tuliavko (vladislavi2742@gmail.com)
MiLaboratory inc. manager&designer, immunologist

## Our team
![image](https://drive.google.com/uc?export=view&id=1tdSGpNl6GorFPZIqweB0PaGxQW5wK5Oo)
