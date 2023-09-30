# Protein Tool

This Python utility allows you to work with protein sequences. You can perform various operations on protein sequences, such as translating them into RNA, DNA sequences, counting charged, uncharged amino acids and hydrophobic, hydrophilic amino acids in sequence. 

## Table of Contents

- [Installation](#installation)
- [Functions](#functions)
- [Troubleshooting](#troubleshooting)
- [Authors](#authors)

## Installation

You can clone this repository or download the source code. 

##### Requirements:

Python3

## Functions
The program can process one or more amino acid sequences written in a one-letter format and also does not take into account the size of the input and output letters. Tool can work with amino acids which are mentioned in table below.
| One letter amino acid         | Three letter amino acid     |
|-------------------------------|-----------------------------|
| A                             |            Ala              |
| C                             |            Cys              |
| D                             |            Asp              |
| E                             |            Glu              |
| F                             |            Phe              |
| G                             |            Gly              |
| H                             |            His              |
| I                             |            Ile              |
| K                             |            Lys              |
| L                             |            Leu              |
| M                             |            Met              |
| N                             |            Asn              |
| P                             |            Pro              |
| Q                             |            Gln              |
| R                             |            Arg              |
| S                             |            Ser              |
| T                             |            Tre              |
| V                             |            Val              |
| W                             |            Trp              |
| Y                             |            Tyr              |
### change_abbreviation(seq)
Name's operation: "one letter".
Sequences are written in three-letter format, can be converted to one-letter format. Amino acids must be separeted by "-". 

- seq: Amino acid sequence (str).
- Returns: string of one-letter format of sequence or list of sequences.
##### Example:
```python
protein_tool('aLa-CyS', 'one letter') #input ignore letter's size
'AC'
protein_tool('Ala-Cys', 'Ala', 'one letter')
['AC', 'A']
```
### to_dna(seq: str) -> str
Name's operation: "DNA".
Transforms aminoacid sequence to according DNA sequence. 

Arguments:
- sequence: aminoacid sequence to transform into DNA.
Returns:
- String of according DNA sequence
##### Example:
```python
protein_tool('AsDr', 'DNA')
'GCN(TCN or AGY)GAYAGY'
protein_tool('YWNGAS', 'DNA')
'TAY(CGN or AGR)AAYGGNGCN(TCN or AGY)'
```
### to_rna(seq, rna_dict)
Name's operation: "RNA".
Translates an amino acid sequence into an RNA sequence. 

- seq: Amino acid sequence (str).
- rna_dict: Dictionary defining the correspondence of amino acids to RNA triplets (default, standard code).
- Returns: String or list of RNA sequences.
##### Example:
```python
protein_tool('FM', 'RNA')
'UUYAUG'
```
### define_charge(seq, positive_charge, negative_charge)
Name's operation: "charge".
Counts the number of amino acids with positive charge, negative charge, and neutral amino acids in the sequence. 

- seq: Amino acid sequence (string).
- positive_charge: List of amino acids with positive charge (default is ['R', 'K', 'H']).
- negative_charge: List of amino acids with negative charge (default is ['D', 'E']).
- Returns: A dictionary (or list of dictionaries) containing the counts of amino acids and their labels.

##### Example:
```python
protein_tool('ASDRKHDE', 'charge')
{'Positive': 3, 'Negative': 3, 'Neutral': 2}
```
### define_polarity(seq: str) -> dict
Name's operation: "polarity".
Counts polar and nonpolar aminoacids in sequence. 

Arguments:
- sequence: sequence in which we count polar and nonpolar aminoacids.
Returns:
- Dictionary with dictionary with keys 'Polar', 'Nonpolar' and appropriate aminoacid counters as values.
##### Example:
```python
protein_tool('ASDR', 'polarity')
[{'Polar': 3, 'Nonpolar': 1}]
```
## Troubleshooting
Sequences containing characters that do not code for amino acids will be removed from the analysis. The program will write an error and display the sequence with which the problem occurred.
##### Example:
```python
protein_tool('ASDR', 'ala1', 'polarity')
Something wrong with ala1
[{'Polar': 3, 'Nonpolar': 1}]
```
Sequences specified in a three-letter format are accepted only by the function for changing the recording format. In other cases, the program will produce either an error or incorrect calculations.
##### Example:
```python
protein_tool('AGFHGF', 'Ala-ala', 'DNA') # key error "-"
protein_tool('AGFHGF', 'Ala-ala', 'polarity')
[{'Polar': 1, 'Nonpolar': 5}, {'Polar': 0, 'Nonpolar': 7}] # "-" is counted as non-polar
```
## Authors
- Dorzhi Badmadashiev: to_rna, define_charge functions
- Ustin Zolotikov: to_dna, define_polarity functions
- Margarita Beskrovnaia: main, is_correct_seq, change_abbreviation functions
![alt text](/team-HW4.jpg "Команда разработчиков")
