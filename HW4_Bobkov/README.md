# protein_tools.py 
> *Discription how the protein_tools.py works:*    
This program contains the function `protein_tool`. The `protein_tool` function takes as input an arbitrary number of arguments in the form of amino acid (aa)/protein sequences of type *str*, as well as the name for the procedure to be performed. After this, the function performs the specified action on all provided sequences. Carefully read the rules of usage for each option, because they specify correct ways of entering arguments, as well as the output and the type of data in the output.
### :warning: Attention:
### 1)>  The programm is register-dependent.
### 2)>  Before using some of the options read 'Procedures description' carefully.
### 3)>  If you input sequenses or 'options' incorrectly, the program will provide you with helpful error messages. 

**list of options:**

- 'compare' - Compare amino acids between reference sequence and other sequences;
- 'length'- Сount the number of amino acids in protein sequence(s);
- 'percentage' - Count percentage of each amino acid in sequence;
- 'pattern' - Find all non-overlaping instances of a given pattern in sequences;
- '3Letter_name' - Transform into a three-letter amino acids entry;
- 'DNA_code' - Transform protein sequence(s) to DNA sequence(s).


# Procedures description
## compare
### Introduction
The **compare** procedure compares the first amino acid sequence provided with the following ones.
### Inputs
To start using the length procedure, enter sevreal arguments: 
- _an arbitrary number_ of sequences, where the first sequence is a reference to which the following sequences are compared; each argument should be of type 'str'.
- _second-to-last_ argument is the number of decimals to round the number to; type 'int'
- _last_ argument determines whether percentages are returned instead of fractions; type 'bool'
### Outputs 
It returns a 'dict' object where:
- *keys* are compared-to sequences (type str)
- *values* are either fractions or percentages (type float).
### Usage example
```python
protein_tool('LAlLAlwWGPdPA', 'LAlLAl', 3, False, options = 'compare') # {'LAlLAl': 1.0}
protein_tool('LAlLAlwWGPdPA', 'LAlLAl', 'GPdPA', 3, True, options = 'compare')) # {'LAlLAl': 100.0, 'GPdPA': 20.0}
```

## length
### Introduction
The **length** procedure calculates the length of protein sequence(s) (equal to the number of amino acids).
### Inputs
To start using the length procedure, enter one or more protein sequences for which you want to get a summary, and at the end add `options = ‘length’`. 
### Outputs
The result of the procedure is a list with the numbers of amino acids in each sequence. The list contains only numbers of amico acids in the sequence.
### Usage example
```python
protein_tool('LAlLAlwWGPdPA', options = 'length') # [13]
protein_tool('RRRrrrR', 'WGPdPA', 'LAlLAlw', options = 'length') # [7, 6, 7]
```

## percentage
### Introduction
The **percentage** procedure calculates the percentage of all 20 proteinogenic amino acid residues, case-sensitive in the protein sequence.
### Inputs
To start using the count_percentage procedure, enter one or more protein sequences for which you want to get a summary, and at the end add `options = ‘percentage’`. 
### Outputs
The result of the procedure is a list of dictionaries with the percentages of the corresponding amino acids in each sequence. The dictionary contains only amino acid residues whose percentage in the sequence is not equal to 0 (which are contained in the sequence at all). Also, the dictionary is ordered from the largest percentage of content to the smallest. Cases of amino acid residues are taken into account.
> :warning: Attention: We use rounding to 2 decimal places. In some cases, **the sum of percentages** of all amino acid residues for sequence **may not be exactly 100%** due to rounding.
### Usage example
```python
protein_tool('LAlLAlwWGPdPA', options = 'percentage') # [{'A': 23.08, 'L': 15.38, 'l': 15.38, 'P': 15.38, 'w': 7.69, 'W': 7.69, 'G': 7.69, 'd': 7.69}]
protein_tool('RRRrrrR', 'WGPdPA', 'LAlLAlw', options = 'percentage') # [{'R': 57.14, 'r': 42.86}, {'P': 33.33, 'W': 16.67, 'G': 16.67, 'd': 16.67, 'A': 16.67}, {'L': 28.57, 'A': 28.57, 'l': 28.57, 'w': 14.29}]
```

## pattern
### Introduction
The **pattern** procedure finds all non-overlaping cases of a given pattern in amino acid sequence(s) provided.
### Inputs
To start using the pattern procedure, enter one or more protein sequences for which you want to get a summary,  where the first sequence is a pattern, which is searched for in the following sequences; each argument should be of type 'str' and at the end add `options = ‘pattern’`. 
The *find_pattern()* function goes through a sequence in the following way: it takes a subsequence of amino acids in front of an index equal in length to the pattern and compares it to the pattern. If there is no match, index is moved one amino acid to the end of the sequence. If there is a match, the index is saved, and the function jumps to an aminoacid next to the end of the subsequence, then the algorithm repeats. Comparison is performed by *compare_pattern* subfunction.   
The image explanation of that function.    
![The image explanation of that function **pattern**](https://github.com/GlebBobkov/HW4_Bobkov/raw/HW4_Bobkov/HW4_Bobkov/explanation.jpg)

### Outputs
The result of this procedure is a 'dict' object where:
- *keys* are amino acid sequences (type 'str') 
- _values_ are lists where the first element is a number of pattern instances in a given sequence, and the following elements are indexes of these occurances
### Usage example
```python
protein_tool('LAlLAlwWGPdPA', 'LAlLAl', 'GPdPA', options = 'pattern') # {'LAlLAl': [2, 0, 3], 'GPdPA': [0]}
protein_tool('LAlLAlwWGPdPA', 'AlLAl', options = 'pattern') # {'AlLAl': [1, 2]}
```

## 3Letter_name
### Introduction
The **3Letter_name** procedure transforms one-letter amino acid entry sequences to three-letter amino acid sequences, separated by a specified separator. It is a case-sensitive procedure.
### Inputs
To start using the rename_three_letter_name procedure, enter one or more protein sequences for which you want to get three-letter sequences. After the protein sequences put a symbol (type 'str') that will be a separator. And specify the `options = ‘3Letter_name’`. 
### Outputs
The result of the procedure is a list of three-letter sequences. Each amino acid is separated by the specified separator. The case of the three-letter amino acid coincides with the case of the one-letter designation at the input.
### Usage example
```python
protein_tool('wWGPdPA', '', options = '3Letter_name') # ['trpTRPGLYPROaspPROALA']
protein_tool('LAlLAlwWGPdPA', '-', options = '3Letter_name') # ['LEU-ALA-leu-LEU-ALA-leu-trp-TRP-GLY-PRO-asp-PRO-ALA']
protein_tool('RRRrrrR', 'WGPdPA', 'LAlLAlw', options = 'percentage') # [{'R': 57.14, 'r': 42.86}, {'P': 33.33, 'W': 16.67, 'G': 16.67, 'd': 16.67, 'A': 16.67}, {'L': 28.57, 'A': 28.57, 'l': 28.57, 'w': 14.29}]
protein_tool('qwerty', 'G', options = '3Letter_name') # ['glnGtrpGgluGargGthrGtyr']
```

## DNA_code
### Introduction
The **DNA_code** procedure transforms a protein into a DNA sequence that may encode it (this can be used in genetic ingeneering). 
P.S. codons chosen at the discretion of the tool authors.
### Inputs
To start using the DNA_code procedure, enter one or more protein sequences for which you want to get a summary, and at the end add `options = ‘DNA_code’`. 
### Outputs
The result of the procedure is a list with type 'str' elements - nucleotide sequence that corresponds to the amino acid sequence. 
### Usage example
```python
protein_tool('LAlLAlwWGPdPA', options = 'DNA_code') # ['TTAGCAttaTTAGCAttatggTGGGGGCCCgcaCCCGCA']
protein_tool('RRRrrrR', 'WGPdPA', 'LAlLAlw', options = 'DNA_code') # ['CGACGACGAcgacgacgaCGA', 'TGGGGGCCCgcaCCCGCA', 'TTAGCAttaTTAGCAttatgg']
```

# Contacts
[Gleb Bobkov](https://github.com/GlebBobkov): teamlead, count_length and transform_to_DNA_code functions;     
[Dmitry Matach](https://github.com/zmitserbio): compare, find_pattern functions, is_protein, string_check, verify;   
[Olga Bagrova](https://github.com/Olga-Bagrova): count_percentage and rename_three_letter_name functions.   


![OUR COMMON PHOTO FROM THE GOOGLE MEET ](https://github.com/GlebBobkov/HW4_Bobkov/raw/HW4_Bobkov/HW4_Bobkov/photo_2023-09-28_23-38-46.jpg)

