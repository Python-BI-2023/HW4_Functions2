# AminoAcidTools

## Overview


AminoAcidTools is a mini-program designed to work with amino acid sequences. The program allows the user to perform elementary but necessary procedures in routine scientific work, for example, to calculate various physical and chemical parameters, find certain conservative sequences, etc.

## Usage

To run AminoAcidTools just ... ... ... ... ... ... ...

The program takes as input an arbitrary number of amino acid sequences (`str` type) , as well as the name of the procedure to be executed. Sequences to be analyzed are not case-specific.
:exclamation: The amino acid sequence must be written in single-letter form and in uppercase.

The last argument is necessarily the name of the operation, and is designated as a named argument by "operation=*option*":

>run_amino_acid_tools('ARDeFtt', operation=calculate_percentage)  **# correct**
>run_amino_acid_tools('ARDeFtt', 'deh', operation=calculate_pI)  **# correct**
>
>run_amino_acid_tools('ARDeFtt')  **# incorrect**
>run_amino_acid_tools(ARDeFtt, deh, calculate_pI)  **# incorrect**

:exclamation: When specifying an operation, you must adhere to the established names, which are indicated in the "Options" section.

## Options

The program implements the following operations:

**`calculate_weight`  — calculate the molecular weight of an amino acid sequence**
Calculate the molecular weight of the input amino acid sequences based on the mass of each amino acid residue. Reference values for the masses of amino acid residues are taken from proteomicsresource.washington.edu and rounded to three decimal places. The calculations took into account the presence of *H* and *OH* groups at the termini of the sequences.
The input is a string with amino acid sequences. At the output, the user receives string with the molecular weight of each individual sequence in Daltons (the result is rounded to two decimal places):
>amino_acid_tools('DEHR', operation=calculate_weight)  **# input**
>
>Molecular weight of the sequence DEHR is 555.55 Da **# output**

**`calculate_percentage`  — calculate the percentage of amino acids in a sequence**
Calculate the percentage of each amino acid in the sequence.
The input is a string with amino acid sequences. The output is a string containing the percentage of each amino acid in the sequence (the result is rounded to two decimal places):
>amino_acid_tools('ARG', operation=calculate_percentage) **# input**
>
>Amino acids percentage of the sequence ARG is A: 33.33, R: 33.33, G: 33.33 **# output**

**-   `name3`  — посчитать изоэлектрическую точку**

**-   `name4`  — грубая оценка гидрофильности/гидрофобности аминокислотной последовательности**

**-  `name5`  — поиск распространенных мотивов/сайтов**

## Troubleshooting

The program automatically checks whether the entered amino acid sequence (contains only letters corresponding to one-letter amino acid abbreviations) and the name of the operation are correct. If an error is detected, the program will be interrupted and a corresponding message will be displayed on the screen. Examples:
>
>
>
>

## Contacts:

Kseniia Matveeva (team lead, author * and * functions)
Anastasiya Ivanova (author *weight* and *percentage* functions)
Danila Chernikov (author * and * functions)

![Team photo](https://drive.google.com/file/d/1M3HBfbb2KE1iLe-NhzpUEthPzs3FV3kU/view?usp=drive_link)
