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

## Authors
- Dorzhi Badmadashiev
- 
- 