# Welcome to amino_analyzer tool

## Overview
The amino_analyzer is an easy-to-use Python tool designed to facilitate the comprehensive analysis of protein sequences. It provides a broad functionality from basic checks for valid amino acid sequences to more complicated computations like molecular weights, hydrophobicity analysis, and cleavage site identification.

## :green_heart: Key features

### 1. Protein molecular weight calculation
The amino_analyzer offers the capability to calculate the molecular weight of a protein sequence. Users can choose between average and monoisotopic weights.
### 2. Hydrophobicity analysis
This function counts the quantity of hydrophobic and hydrophilic amino acids within a protein sequence.
### 3. Cleavage site identification
Researchers can identify cleavage sites in a given peptide sequence using a specified enzyme. The tool currently supports two commonly used enzymes, trypsin and chymotrypsin.
### 4. One-letter to three-Letter code conversion
The amino_analyzer provides a function to convert a protein sequence from the standard one-letter amino acid code to the three-letter code. 
### 5. Sulphur-containing amino acid counting
The tool allows a quick determine the number of sulphur-containing amino acids, namely Cysteine (C) and Methionine (M), within a protein sequence. 

## Usage

To run amino_analyzer tool you need to use the function ***run_amino_analyzer*** with the following arguments:

```python
from from amino_analyzer import run_amino_analyzer
run_amino_analyzer(sequence, procedure, *, weight_type = 'average', enzyme: str = 'trypsine')`
```

- `sequence (str):` The input protein sequence in one-letter code.
- `procedure (str):` The procedure to perform over your protein sequence.
- `weight_type: str = 'average':` default argument for `aa_weight` function. `weight_type = 'monoisotopic'` can be used as another option.
- `enzyme: str = 'trypsine':` default argument for `peptide_cutter` function. `enzyme = 'chymotrypsin'` can be used as another option
    
    
**Available procedures list**
-   `aa_weight` —  calculates the amino acids weight in a protein sequence.
-   `count_hydroaffinity` — counts the quantity of hydrophobic and hydrophilic amino acids in a protein sequence.
-   `peptide_cutter` — identifies cleavage sites in a given peptide sequence using a specified enzyme (trypsine or chymotripsine).
-   `one_to_three_letter_code` — converts a protein sequence from one-letter amino acid code to three-letter code.
-   `sulphur_containing_aa_counter` - counts sulphur-containing amino acids in a protein sequence.

You can also use each function separately by importing them in advance. Below are the available functions and their respective purposes:

#### 1. **aa_weight** function calculates the weight of amino acids in a protein sequence:
   The type of weight to use, either `average` or `monoisotopic`. Default is `average`.
```python
from amino_analyzer import aa_weight
aa_weight(seq: str, weight: str = `average`) -> float`
```
```python
sequence = "VLDQRKSTMA"
result = aa_weight(sequence, weight='monoisotopic')
print(result)  # Output: 1348.517
```

#### 2. **count_hydroaffinity** сounts the quantity of hydrophobic and hydrophilic amino acids in a protein sequence:
```python
from amino_analyzer import count_hydroaffinity 
count_hydroaffinity(seq: str) -> tuple
```
```python
sequence = "VLDQRKSTMA"
result = count_hydroaffinity(sequence)
print(result)  # Output: (3, 7)
```
#### 3. **peptide_cutter** function identifies cleavage sites in a given peptide sequence using a specified enzyme: trypsine or chymotrypsine:
```python
from amino_analyzer import peptide_cutter
peptide_cutter(sequence: str, enzyme: str = "trypsin") -> str
```
```python
sequence = "VLDQRKSTMA"
result = peptide_cutter(sequence, enzyme="trypsin")
print(result)  # Output: Found 2 trypsin cleavage sites at positions 3, 6
```
#### 4. **one_to_three_letter_code** converts a protein sequence from one-letter amino acid code to three-letter code.
```python
from amino_analyzer import one_to_three_letter_code
one_to_three_letter_code(sequence: str) -> str
```

```python
sequence = "VLDQRKSTMA"
result = one_to_three_letter_code(sequence)
print(result)  # Output: ValLeuAspGlnArgLysSerThrMetAla
```

#### 5. **sulphur_containing_aa_counter** counts sulphur-containing amino acids in a protein sequence
```python
from amino_analyzer import sulphur_containing_aa_counter
sulphur_containing_aa_counter(sequence: str) -> str
```
```python
sequence = "VLDQRKSTMA"
result = sulphur_containing_aa_counter(sequence)
print(result)  # Output: The number of sulphur-containing amino acids in the sequence is equal to 2
```

## Examples
To calculate protein molecular weight:
```python
run_amino_analyzer("VLSPADKTNVKAAW", "aa_weight")  # Output: 1481.715

run_amino_analyzer("VLSPADKTNVKAAW", "aa_weight", weight_type = 'monoisotopic')  # Output: 1480.804
```

To count hydroaffinity:
```python
run_amino_analyzer("VLSPADKTNVKAAW", "count_hydroaffinity")   # Output: (8, 6)
```

To find trypsin/chymotripsine clivage sites:
```python
run_amino_analyzer("VLSPADKTNVKAAW", "peptide_cutter") # Output: 'Found 2 trypsin cleavage sites at positions 7, 11'

run_amino_analyzer("VLSPADKTNVKAAWW", "peptide_cutter", enzyme = 'chymotrypsin') # Output: 'Found 1 chymotrypsin cleavage sites at positions 14'
```

To change to 3-letter code and count sulphur-containing amino acids.
```python
run_amino_analyzer("VLSPADKTNVKAAW", "one_to_three_letter_code") # Output: 'ValLeuSerProAlaAspLysThrAsnValLysAlaAlaTrp'

run_amino_analyzer("VLSPADKTNVKAAWM", "sulphur_containing_aa_counter") # Output: The number of sulphur-containing amino acids in the sequence is equal to 1
```

## Troubleshooting
Here are some common issues you can come ascross while using the amino-analyzer tool and their possible solutions:

1. **ValueError: Incorrect procedure**  
   If you receive this error, it means that you provided an incorrect procedure when calling `run_amino_analyzer`. Make sure you choose one of the following procedures: `aa_weight`, `count_hydroaffinity`, `peptide_cutter`, `one_to_three_letter_code`, or `sulphur_containing_aa_counter`.

   Example:
   ```python
   run_amino_analyzer("VLSPADKTNVKAAW", "incorrect_procedure")
   # Output: ValueError: Incorrect procedure. Acceptable procedures: aa_weight, count_hydroaffinity, peptide_cutter, one_to_three_letter_code, sulphur_containing_aa_counter
   ```

2. **ValueError: Incorrect sequence**
This error occurs if the input sequence provided to run_amino_analyzer contains characters that are not valid amino acids. Make sure your sequence only contains valid amino acid characters (V, I, L, E, Q, D, N, H, W, F, Y, R, K, S, T, M, A, G, P, C, v, i, l, e, q, d, n, h, w, f, y, r, k, s, t, m, a, g, p, c).

    Example:
   ```python
    run_amino_analyzer("VLSPADKTNVKAAW!", "aa_weight")
    # Output: ValueError: Incorrect sequence. Only amino acids are allowed (V, I, L, E, Q, D, N, H, W, F, Y, R, K, S, T, M, A, G, P, C, v, i, l, e, q, d, n, h,   w, f, y, r, k, s, t, m, a, g, p, c).
    ```

3. **ValueError: You have chosen an enzyme that is not provided**
This error occurs if you provide an enzyme other than "trypsin" or "chymotrypsin" when calling peptide_cutter. Make sure to use one of the specified enzymes.

    Example:
    ```python
    peptide_cutter("VLSPADKTNVKAAW", "unknown_enzyme")
    # Output: You have chosen an enzyme that is not provided. Please choose between trypsin and chymotrypsin.
    ```
4. **ValueError: You have chosen an enzyme that is not provided.**
If you encounter this error, it means that you're trying to iterate over a float value. Ensure that you're using the correct function and passing the correct arguments.

    Example:
    ```python
    result = count_hydroaffinity(123)
    # Output: TypeError: 'int' object is not iterable
    ```
## Development team:
![image](https://github.com/CaptnClementine/HW4_Gorbarenko/assets/131146976/ad89e427-5b2a-4b32-b65f-519d284fcaa7)

**Anastasia Gorbarenko** - team leader, author of aa_weight and count_hydroaffinity functions
**Anna Ogurtsova** - author of peptide_cutter and one_to_three_letter_code  functions     
**Ilya Popov** - author of main and sulphur_containing_aa_counter  functions   

## Contacts
If you have any questions, suggestions, or encounter any issues while using the amino-analyzer tool, feel free to reach out:


- **GitHub**: [Cucumberan](https://github.com/YourGitHubUsername), [CaptnClementine](https://github.com/YourGitHubUsername), [iliapopov17](https://github.com/YourGitHubUsername)

