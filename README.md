# protein_tools.py
There is a tool, written in Python, for working with protein sequences. It contains several functions, described below in the section "Usage".

## Installation
Download protein_tools.py, adapt it to your code and relax.

## Usage
Provide a tool with the sequence(s) of the protein(s) in 1-letter format (for example, DYKDDDDK) and the function needed. If you
occasionally write down a non-peptide sequence, the programm will return an error.  

Here is the catalogue of actions the user can choose: 

- count_length: gives the length(s) of the protein sequence(s)  
- count_nucleotide_length: counts the length(s) of the coding nucleotide sequence(s) of the protein sequence(s)  
- count_molecular_mass: calculates molecular mass of the input (the algorithm takes into consideration water mass and subtracts it)    
- show_content: shows the aminoacid content of the protein(s)  
- convert_1_to_3: converts 1-letter format into 3-letter one  
- count_extinction_280nm: counts the molar extinction coefficient (this function counts cystine contribution to extinction coefficient as two cysteins give 1 SS-bond) 

## Examples:  
Examples for some of the protein_tools.py functions:  
```
function = 'count_aa_length'
prot1 = 'DYKDDDDK'
prot2 = 'DYKDDdDk'
```
The result would be:
```
[8, 8]
```
Almost same result will be obtained when using 'count_nucl_length'

Count molecular mass:
```
Count molecular mass:
function = 'count_molecular_mass'
prot1 = 'DYKDDDDK'
```
The result of programm work:
```
760.768
```
Converting into 3-letter format
```
function = 'convert_1to3'
prot1 = 'DYKDDDDK'
```
The result:
```
'AspTyrLysAspAspAspAspLys'
```
Showing the content:
```
function = 'show_content'
prot1 = 'DYKDDDDK'
```
The user gets this:
```
{'A': 0, 'C': 0, 'D': 5, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'K': 2, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 1}
```
Count extinction coefficient 280nm:
```
function = 'count_extinction_280nm'
prot1 = 'DYKDDDDK'
prot2 = 'AADDRR'
```
The result:
```
[1490, 0]
```
## Troubleshooting
If the user sees ValueError, the user may inputted a non-protein sequence. The programm works with protein sequences in 1-letter format only. Please, check the sequence.
## Authors' contribution:
- Alexei Sivtsev: calculate_mm, convert_1to3 (team leader)   
- Albina Khairetdinova: count_aa_content, count_extinction_280nm, is_prot (it is the inner function, that appears only when the sequence is non-protein and returns ValueError)  
- Elizaveta Zolotenkova: main function protein_tools, function count_aa_length, function count_nucl_length and Read.me   

## Additional information (a photo of the authors)
![authors](https://github.com/Zoea1/HW4_Functions2/assets/143959084/114d6852-8fb8-4bcc-baf7-873eb3d85a5e)
