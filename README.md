# protein_tool.py 
> *discription how the protein_tool.py work*
This program contains the function `...`. The `...` function takes as input an arbitrary number of arguments in the form of amino acid (aa)/protein sequences, in the form (*str*), as well as the name of the procedure to be performed. After this, the command performs the specified action on all transmitted sequences. Carefully read the rules of using each options, because this affects the rules for entering arguments, as well as the output and the type of data in the output


**list of options:**

- 'compare' - Compare amino acids between reference sequence and other sequences;
- 'length'- Сounting the length of an amino acid sequence/protein in the number of amino acids;
- 'percentage' - Count percentage of each amino acid in sequence;
- 'pattern' - Find all non-overlaping instances of a given pattern in sequences;
- '3Letter_name'- rename_three_letter_name,
- 'DNA_code' — Transforming of an amino acid sequence/protein to DNA sequence.




# Procedures description
## count_percentage
### Introduction
The **count_percentage** procedure calculates the percentage of all 20 proteinogenic amino acid residues, case-sensitive in the protein sequence.
### Inputs
To start using the count_percentage procedure, enter one or more protein sequences for which you want to get a summary, and at the end add `options = ‘percentage’`. 
### Outputs
The result of the procedure is a list of dictionaries with the percentages of the corresponding amino acids in each sequence. The dictionary contains only amino acid residues whose percentage in the sequence is not equal to 0 (which are contained in the sequence at all). Also, the dictionary is ordered from the largest percentage of content to the smallest. Cases of amino acid residues are taken into account.
> :warning: Attention: We use rounding to 2 decimal places. In some cases, **the sum of percentages** of all amino acid residues for sequence **may not be exactly 100%** due to rounding.
### Usage example
```python
main('LAlLAlwWGPdPA', options = 'percentage') # [{'A': 23.08, 'L': 15.38, 'l': 15.38, 'P': 15.38, 'w': 7.69, 'W': 7.69, 'G': 7.69, 'd': 7.69}]
main('RRRrrrR', 'WGPdPA', 'LAlLAlw', options = 'percentage') # [{'R': 57.14, 'r': 42.86}, {'P': 33.33, 'W': 16.67, 'G': 16.67, 'd': 16.67, 'A': 16.67}, {'L': 28.57, 'A': 28.57, 'l': 28.57, 'w': 14.29}]
```

## rename_three_letter_name
### Introduction
The **rename_three_letter_name** procedure transform one-letter amino acids entry sequences to three-letter with separator. It is case-sensitive procedure.
### Inputs
To start using the rename_three_letter_name procedure, enter one or more protein sequences for which you want to get three-lettered sequences. After the protein sequences put a symbol that will be a separator. And specify the `options = ‘3Letter_name’`. 
### Outputs
The result of the procedure is a list of three-lettered sequences. Each amino acid is separated by the specified separator. The case of the three-letter amino acid coincides with the case of the one-letter designation at the input.
### Usage example
```python
main('wWGPdPA', '', options = '3Letter_name') # ['trpTRPGLYPROaspPROALA']
main('LAlLAlwWGPdPA', '-', options = '3Letter_name') # ['LEU-ALA-leu-LEU-ALA-leu-trp-TRP-GLY-PRO-asp-PRO-ALA']
main('RRRrrrR', 'WGPdPA', 'LAlLAlw', options = 'percentage') # [{'R': 57.14, 'r': 42.86}, {'P': 33.33, 'W': 16.67, 'G': 16.67, 'd': 16.67, 'A': 16.67}, {'L': 28.57, 'A': 28.57, 'l': 28.57, 'w': 14.29}]
main('qwerty', 'G', options = '3Letter_name') # ['glnGtrpGgluGargGthrGtyr']
```
