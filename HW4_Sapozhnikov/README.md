# HW 4. Functions 2
> *This is the repo for the fourth homework of the BI Python 2023 course*

### Title
'prototool.py' is a special script for working with polyaminoacid sequences

***

### Overview
'prototool.py' includes 7 methods to treatment of polyaminoacid sequences.
'prototool.py' can be used for the next goals:
- recoding 1-letter coded polyaminoacid seqeunces into 3-letter coded and vice versa;
- polyaminoacid sequences aligment with Smith-Waterman algorithm [^1];
- finding possinle RNA sequences for given polyaminoacid sequences;
- determining polyaminoacid isoelectric point;
- calculating polyaminoacid molecular weight;
- finding possinle DNA sequences for given polyaminoacid sequences; 
- determining GC-content of a corresponding DNA sequence to a given polyaminoacid sequence

***

### Usage
This tool can be used both standalone and as module.
- to use 'prototools' standalone you will have to add these lines in the code
  ![image](https://github.com/NSapozhnikov/HW4_Sapozhnikov/assets/81642791/5fa3cf7f-e6f3-4294-9e81-b1ebe17c8514)
  - where *args are sequences you want to process and method is a specified algorithm to use
  - your result will be written in a variable (test on a picture)
- to use 'prototools' as module (recomended) you should import it as any other module (check the path: prototools.py should be in the same directory as your script). Then you can freely use any of its functions (see examples).

***

### Options
Arguments:
- '''*args[str]''' sequences to work with. You can pass several arguments into all functions
- method - a method to use

output: All functions return a dict, where keys are original sequenses, values are results after using a corresponding method.

***

### Examples

def recode allows to translate 1-letter to 3-letters polyaminoacids code
- '''main('AlaValTyr', 'DNT', method = 'recode')'''
- '''recode('AlaValTyr', 'DNT')'''
- ![image](https://github.com/NSapozhnikov/HW4_Sapozhnikov/assets/81642791/117befa5-feaa-433a-9ac9-23cffe9b024f)
***

def local_alignmen perform a local alignment of 2 given sequences. Needs at least two sequences to be passed
- '''main('MetAsnTrp', 'MNT', method='local_alignment')'''
- '''local_alignmen('MetAsnTrp', 'MNT')'''
- Note that local_alignment function has a flag prettify (default = True) that prints out aligned sequences on each another
- ![image](https://github.com/NSapozhnikov/HW4_Sapozhnikov/assets/81642791/4dd36d24-a177-4419-9053-a5e2923a980c)
***

def from_proteins_seqs_to_rna allows to decode polyaminoacid sequences in RNA sequences
- '''main('AlaValTyr', 'DNT', method = 'from_proteins_seqs_to_rna')'''
- '''from_proteins_seqs_to_rna('AlaValTyr', 'DNT')'''
- ![image](https://github.com/NSapozhnikov/HW4_Sapozhnikov/assets/81642791/9ee92d0d-68a4-471b-b65a-2fa6b46ab844)
***

def isoelectric_point_determination allows to determine isoelectric point of polyaminoacid sequences 
- '''main('AlaValTyr', 'DNT', method = 'isoelectric_point_determination')'''
- '''isoelectric_point_determination('AlaValTyr', 'DNT')'''
- ![image](https://github.com/NSapozhnikov/HW4_Sapozhnikov/assets/81642791/24027a07-b20b-42d4-bb10-4ca7189038d4)
***

def back_transcribe allows to decode polyaminoacid sequences in DNA sequences
- '''main('AlaValTyr', 'DNT', method = 'back_transcribe')'''
- '''back_transcribe('AlaValTyr', 'DNT')'''
- ![image](https://github.com/NSapozhnikov/HW4_Sapozhnikov/assets/81642791/71f07616-a37d-48da-9e63-82b81836b9d7)
***

def count_gc_content allows to count the ratio of GC in the entire DNA sequence
- '''main('AlaValTyr', 'DNT', method = 'count_gc_content')'''
- '''count_gc_content('AlaValTyr', 'DNT')'''
- ![image](https://github.com/NSapozhnikov/HW4_Sapozhnikov/assets/81642791/d2705714-a3e8-4054-8998-61d922a4feb6)
***

def count_protein_molecular_weight allows to calculate the molecular weight of the polyaminoacid
- '''main('AlaValTyr', 'DNT', method = 'count_protein_molecular_weight')'''
- '''count_protein_molecular_weight('AlaValTyr', 'DNT')'''
- ![image](https://github.com/NSapozhnikov/HW4_Sapozhnikov/assets/81642791/cc1eff9a-1b39-4232-98e4-80f622101083)

***

### Troubleshooting
If you have '''ValueError("No input defined.")''' it means, that you have an empty input. Please, enter the correct input. 
***
If you have '''ValueError(method, " is not a valid method.")''' it means, that your tool is not correct. Please, enter the right tool.
***
If you have '''ValueError('Non-protein aminoacids in sequence')''' it means, that your sequences contain non-protein aminoacids. Please, check your sequences and enter the correct input. 

***

### References

[^1]: T.F. Smith, M.S. Waterman, (1981). [Identification of common molecular subsequences](https://doi.org/10.1016/0022-2836(81)90087-5). Journal of Molecular Biology.

***

### Contributions and contacts

Feel free to report any bugs and problems encountered.
Email: nikita.sapozhnikov1@gmail.com developed recode(), prettify_alignment(), local_alignmen(), check_input()
***
nekrasovadasha22@mail.ru developed from_proteins_seqs_to_rna(), isoelectric_point_determination()
*** 
alina.potyseva@gmail.com developed back_transcribe(), count_gc_content(), count_protein_molecular_weight()
