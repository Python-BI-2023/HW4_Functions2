# Amino acid sequences analysis tool
This repository contains an open-source library which makes work with protein sequences clear. It is capable to process multiple proteins and peptides sequences, calculate physical features, find specific sites and easily handle with any protein encodings.

## Installation

To use this toolbox one need to clone repository

```shell
git clone https://github.com/PolinaVaganova/HW4_Functions2
cd HW4_Functions2
```

### System requirements:

Key packages and programs:
- [Python](https://www.python.org/downloads/) (version >= 3.9)

## Usage

```python
# import main function
from protein_analysis_tool import protein_analysis_tool
```      

## Operations

## change_residues_encoding(seq, query='one')

Transfer amino acids from 3-letter to 1-letter code and vice versa. By default, converts all seq into 1-letter format, even those already 1-letter. Case-sensitive.

**Parameters:**- **seq**: *str*

input protein seq in any encoding and case

- **query**: {'one', 'three'}, default: 'one'

specify target encoding

**Returns:**
- **transfered_seq**: *str*

same protein seq in another encoding

**Example**
```python
seq = 'AAA'
change_residues_encoding(seq, query='three')
```

## is_protein(seq)

Check if sequence is protein or not by identify invalid seq elements, which are not presented in dicts above.

**Parameters:**
- **seq**: *str* 

input protein seq in 1-letter encoding and upper case

**Returns:**
- **verification_result**: *bool*

if seq is correct protein seq or not 

**Example**
```python
seq = 'AAA'
is_protein(seq)
```

## get_seq_characteristic(seq)

Count entry of each residue type in your sequence

**Parameters:**
- **seq**: *str* 

input protein seq in 1-letter encoding and upper case

**Returns:**
- **res_count**: *dict*

each residue type in seq in 3-letter code and its amount in current seq

**Example**
```python
seq = 'AAA'
get_seq_characteristic(seq)
```

## find_res(seq, res_of_interest)

Find all positions of certain residue in your seq

**Parameters:**
- **seq**: *str* 

input protein seq in 1-letter encoding and upper case
- **res_of_interest**: *str*

residue of interest in 1-letter encoding and upper case

**Returns:**
- **res_positions**: *str*

positions of specified residue in your seq

**Example**
```python
seq = 'AAA'
res = 'A'
find_res(seq, res)
```

## find_site(seq, site)

Find if seq contains certain site and get positions of its site

**Parameters:**
- **seq**: *str* 

input protein seq in 1-letter encoding and upper case

- **site**: *str*

specify site of interest

**Returns:**
- **site_positions**: *str*

the range of values for amino acid positions of specified site in your seq in which the last number is excluded

**Example**
```python
seq = 'AAADDDF'
site = 'ADF'
find_site(seq, site)
```

## calculate_protein_mass(seq)

Get sum of residues masses in your seq in Da

**Parameters:**
- **seq**: *str* 

input protein seq in 1-letter encoding and upper case

**Returns:**
- **total_mass**: *float*

mass of all residues in seq in Da

**Example**
```python
seq = 'AAA'
calculate_protein_mass(seq)
```

## calculate_average_hydrophobicity(seq)

Get average hydrophobicity index for protein seq as sum of index for each residue in your seq divided by its length

**Parameters:**
- **seq**: *str* 

input protein seq in 1-letter encoding and upper case

**Returns:**
- **average_hydrophobicity_idx**: *float*

average hydrophobicity index for your seq

**Example**
```python
seq = 'AAA'
calculate_average_hydrophobicity(seq)
```

## get_mrna(seq)

Get encoding mRNA nucleotides for your seq

**Parameters:**
- **seq**: *str* 

input protein seq in 1-letter encoding and upper case

**Returns:**
- **mrna_seq**: *str*

potential encoding mRNA sequences with multiple choice for some positions

**Example**
```python
seq = 'AAA'
get_mrna(seq)
```

## calculate_isoelectric_point(seq)

Find isoelectrinc point as sum of known pI for residues in your seq

**Parameters:**
- **seq**: *str* 

input protein seq in 1-letter encoding and upper case

**Returns:**
- **pi**: *float*

isoelectric point for your seq

**Example**
```python
seq = 'AAA'
calculate_isoelectric_point(seq)
```
## analyze_secondary_structure(seq)

Calculates the percentage of amino acids found in the three main types of protein secondary structure: beta-turn, beta-sheet and alpha-helix in your seq

**Parameters:**
- **seq**: *str* 

input protein seq in 1-letter encoding and upper case

**Returns:**
- **result**: *list*

percentage of amino acids belonging to three types of secondary structure for seq

**Example**
```python
seq = 'AAA'
analyze_secondary_structure(seq)
```

## run_protein_analysis(\*args)

Apply one of the operations described above to any number of sequences with any case. 

**Parameters:**
**\*args**:
- **sequences**: *str*

input coma-separated sequences in 1-letter or 3-letter code with any case (as many as you wish)
- **add_arg**: *str*

necessary parameter for certain functions (for example, specify target protein site)
- **procedure** : *str*

specify procedure you want to apply

**Returns**:
- **operation_result**: str or list

result of function work in list or str format (dependent on number of input sequences)

**Note!**
- Operation name always must be the last argument
- Additional argument must be always before operation name

## Troubleshooting
This section lists solutions to problems you might encounter with. 

### Common Problems
Here is a list of common problems:
 * If you run `change_residues_encoding()` function from `run_protein_analysis()` passing only sequences without `query` argument it doesn't work. Always specify `query` argument in this case, despite by default it is `query='one'` 
 * `change_residues_encoding()` function works only with sequences (length >= 2)
 


## Contact

*This is the repo for the 4th homework of the BI Python 2023 course*

Authors:
- *Greenberg Michael*
- *Grishenko Irina*
- *Vaganova Polina*

![Our team](./team.png) 
