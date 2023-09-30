# Protein Tool

This Python utility allows you to work with protein sequences. You can perform various operations on protein sequences, such as translating them into RNA sequences, counting charged and uncharged amino acids, and more...

## Table of Contents

- [Installation](#installation)
- [Functions](#functions)
- [Authors](#Authors)

## Installation

You can clone this repository or download the source code. 

##### Requirements:

Python3

## Functions
### to_rna(seq, rna_dict)
Translates an amino acid sequence into an RNA sequence.

- seq: Amino acid sequence (str).
- rna_dict: Dictionary defining the correspondence of amino acids to RNA triplets (default, standard code).
- Returns: RNA sequence (str).
##### Example:
```python
to_rna('FM')
'UUYAUG'
```
### define_charge(seq, positive_charge, negative_charge)
Counts the number of amino acids with positive charge, negative charge, and neutral amino acids in the sequence.

- seq: Amino acid sequence (string).
- positive_charge: List of amino acids with positive charge (default is ['R', 'K', 'H']).
- negative_charge: List of amino acids with negative charge (default is ['D', 'E']).
- Returns: A dictionary containing the counts of amino acids and their labels.

##### Example:
```python
define_charge('ASDRKHDE')
{'Positive': 3, 'Negative': 3, 'Neutral': 2}
```
### to_dna(seq: str) -> str
Transforms aminoacid sequence to according DNA sequence.

Arguments:
- sequence: aminoacid sequence to transform into DNA.
Returns:
- String of according DNA sequence
##### Example:
```python
to_dna('ASDR') # Returns 'GCN(TCN or AGY)GAYAGY'
to_dna('YWNGAS') # Returns 'TAY(CGN or AGR)AAYGGNGCN(TCN or AGY)' 
```
### define_polarity(seq: str) -> dict
Counts polar and nonpolar aminoacids in sequence.

Arguments:
- sequence: sequence in which we count polar and nonpolar aminoacids.
Returns:
- Dictionary with dictionary with keys 'Polar', 'Nonpolar' and appropriate aminoacid counters as values.
##### Example:
```python
define_polarity('ASDR') # Returns {'Polar': 3, 'Nonpolar': 1}
define_polarity('YWNGAS') # Returns {'Polar': 3, 'Nonpolar': 3}

```
## Authors
- Dorzhi Badmadashiev
- Ustin Zolotikov: to_dna, define_polarity functions
- 
