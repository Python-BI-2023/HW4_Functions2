# AminoAcidTools

## Overview

AminoAcidTools is a mini-program designed to work with amino acid sequences. The program provides some useful procedures that one can find handy in routine scientific work, for example, calculation of various physical and chemical parameters, to find possible protease cleavage sites etc.

## Usage

To use AminoAcidTools simply import `run_aminoacid_tools` into your `*.py` script as shown below:
```python
from aminoacid_tools import run_aminoacid_tools
```
#### Input
The program has two required input parameters:
* (`str` type) Amino acid sequence(s), variable argument. Sequences to be analyzed are not case-specific;
* (`str` type) Name of the operation to be executed, keyword argument.

:exclamation: The amino acid sequence must be written in single-letter form and in uppercase.

The name of an operation is defined as a keyword argument `operation = 'option'`:

```python
run_aminoacid_tools('ARDF', operation = 'calculate_percentage')  # correct
run_aminoacid_tools('ARDF', 'DEH', operation = 'calculate_pI')  # correct
```
```python
run_aminoacid_tools('ARDF')  # incorrect
run_aminoacid_tools(ARDtt, deh, calculate_pI)   # incorrect
```

:exclamation: You must use one of predefined operation names described in the "Options" section below.

#### Output
A string with details of performed operation.

## Options

The program implements the following operations:

#### `calculate_molecular_weight`  
Calculate the molecular weight of an amino acid sequence.

Calculate the molecular weight of the input amino acid sequences based on the mass of each amino acid residue. Reference values for the masses of amino acid residues are taken from [The University of Washington's Proteomics Resource (UWPR)](https://proteomicsresource.washington.edu/protocols06/masses.php) and rounded to three decimal places. The calculations took into account the presence of *H* and *OH* groups at the termini of the sequences.
The input is a string with amino acid sequence. The output is a string with the molecular weight of sequence in Daltons (the result is rounded to two decimal places):
```python
run_aminoacid_tools('ARG', operation = 'calculate_molecular_weight')  # input

Molecular weight of the sequence ARG: 302.33 Da # output
```

#### `calculate_percentage`
Calculate the percentage of amino acids in a sequence.

Calculate the percentage of each amino acid in the sequence. The input is a string with amino acid sequence. The output is a string containing the percentage of each amino acid in the sequence (the result is rounded to two decimal places):
```python
run_aminoacid_tools('ARG', operation = 'calculate_percentage') # input

Amino acids percentage of the sequence ARG: {A: 33.33, R: 33.33, G: 33.33} # output
```

#### `calculate_pI`
Calculate the isoelectric point of aminoacids sequence.

The function operation is based on the formula for determining the isoelectric point:

$$pI = \dfrac{(pK_1 + pK_2 + ... + pK_n)}{n},$$

where $pK$ - dissociation constant of free $NH_2$ and $COOH$ radicals in amino acids.

The input is a string with amino acid sequences. The output is a string containing the $pI$ (isoelectric point) of sequence:
```python
run_aminoacid_tools('ARG', operation = 'calculate_pI')  # input

Isoelectric point for the sequence ARG: 8.14  # output
```

#### `calculate_hydrophobicity_eisenberg`
Calculate estimation of hydrophilicity/hydrophobicity of amino acid sequence.

The function operation is based on the Einzenberg hydrophilicity/hydrophobicity scale of amino acids. 
The input is a string with amino acid sequences. The output is a string containing the rough estimation of hydrophilicity/hydrophobicity of amino acid sequence:
```python
run_aminoacid_tools('ARG', operation = 'calculate_hydrophobicity_eisenberg')  # input

Sequence ARG: Hydrophilic  # output
```

#### `get_cleavage_sites`
Return amount and coordinates of cleavage sites for motif-specific proteases (casp3, casp6, casp7, enterokinase). 

The function finds traces of motifs in amino acid sequence that can be recognized by next site-specific proteases: caspases 3, 6, 7 and enterokinase, then calculates amount of each protease's site and its coordinates. The coordinate is a position of amino acid in C-end of potentially cleaved peptide. Motifs that can be recognized by these proteases were taken from [PeptideCutter](https://web.expasy.org/peptide_cutter/peptidecutter_enzymes.html) documentation.

Some of the proteases permit more than one possible amino acids at a single position. For example, Caspase 6 protease motif is defined as `V, E, H or I, D`. It means there are two possible sequences `...VEHD...` and `...VEID...`  containing the protease motif. Please note the function implementation supports 'OR' condition only.

The input is 1) a string with amino acid sequence to be analyzed, 2) subsequence to  be found in a sequence. Subsequence is specified as list of lists. Each nested list means more than one possible amino acid at a single position and checked by `or` condition. The output is a string with input amino acid sequence, number and coordinates of cleavage sites for each protease separately:
```python
# input
run_aminoacid_tools('ESDMQDMDSGISLDNDDEEKMQ', operation = 'get_cleavage_sites') 

# output
ESDMQDMDSGISLDNDDEEKMQ
1 protease cleavage site(s) for Caspase 3: [6]
0 protease cleavage site(s) for Caspase 6: []
0 protease cleavage site(s) for Caspase 7: []
1 protease cleavage site(s) for Enterokinase: [20]
```

## Troubleshooting

The program automatically checks whether the input amino acid sequence (contains only letters corresponding to one-letter amino acid abbreviations) and the name of the operation are correct. If an error is detected, the program will be interrupted and a corresponding message will be displayed on the screen. Examples:
```python
# incorrect input sequence
ValueError: Incoming sequence ESDMQDMDSGaISLDNDDEEKMQ is not a peptide

# incorrect operation
ValueError: Incorrect operation value
Supported operations: ['get_cleavage_sites', 'calculate_molecular_weight', 'calculate_percentage', 'calculate_pI', 'calculate_hydrophobicity_eisenberg']
```

## Authors

* Kseniia Matveeva (team lead, author of the `get_cleavage_sites` and `run_aminoacid_tools` functions)
* Anastasiya Ivanova (author of the `calculate_molecular_weight` and `calculate_percentage` functions)
* Danila Chernikov (author of the `calculate_pI` and `calculate_hydrophobicity_eisenberg` functions)

![Team photo](team_photo.png)
