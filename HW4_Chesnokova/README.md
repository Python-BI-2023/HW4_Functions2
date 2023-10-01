 
# Protein sequence utility  
This tool is designed  to work with amino acid sequences consisting of _22 proteinogenic amino acid_ residues (including pyrrolizine and selenocysteine) recorded in a standard one-letter format. It is not intended to process sequences with post-translational and other amino acid modifications

## Usage  
You call the `amino_acid_tools` function, which takes as input an arbitrary number of arguments with amino-acid sequences (str), as well as the name of the procedure to be executed (it is always the last argument, str). After that the command performs the specified action on all the given sequences. If one sequence is submitted, a string with the result is returned. If several sequences are submitted, a list of strings is returned.  
Input sequences can contain both uppercase and lowercase letters, but the last argument with the function name must correspond to the listed functions.

### Remark  
- if the sequences passed by you contain inappropriate characters (not from the single-letter aminoxylot encoding), the result of the function will be a list without them  
- the fewer amino acids a sequence contains, the less reliable the 'folding' function is

## Options  
The following options for aminoacid sequence processing are available at the moment:

- **molecular_weight**: calculate the molecular weight of the amino acid chain in Da, according to the average amino acid residues molecular masses rounded to 1 or 2 decimal places.  
- **three_letter_code**: converts standard single letter translations to three letter translations  
- **show_length**: count the overall number of amino acids in the given  
- **sequence folding**: count the number of amino acids characteristic separately for alpha helixes and beta sheets,and give out what will be the structure of the protein more. This function has been tested on proteins such as 2M3X, 6DT4 (PDB ID) and MHC, CRP. The obtained results corresponded to reality.  
- **seq_charge**: evaluates the overall charge of the aminoacid chain in neutral aqueous solution (pH = 7), according to the pKa of amino acid side chains, lysine, pyrrolizine and arginine contribute +1, while asparagine and glutamic amino acids contribute -1. The total charge of a protein is evaluated as positive, negative, or neutral as the sum of these contributions
  
## Examples  
Below is an example of processing an amino acid sequence.

### Using the function for molecular weight calculation

```shell  
amino_acid_tools('EGVIMSELKLK', 'PLPKvelPPDFVD', 'DVIGISILGKEV', 'molecular_weight')  
```

Input: 'EGVIMSELKLK', 'PLPKvelPPDFVD', 'DVIGISILGKEV', 'molecular_weight'  
Output: '[1228.66, 1447.8400000000001, 1224.6399999999999]'

### Using the function to convert one-letter translations to three-letter translations

```shell  
amino_acid_tools('EGVIMSELKLK', 'PLPKvelPPDFVD', 'DVIGISILGKEV', 'three_letter_code')  
```

Input: 'EGVIMSELKLK', 'PLPKvelPPDFVD', 'DVIGISILGKEV', 'three_letter_code'  
Output: '['GluGlyValIleMetSerGluLeuLysLeuLys', 'ProLeuProLysValGluLeuProProAspPheValAsp', 'AspValIleGlyIleSerIleLeuGlyLysGluVal']'

### Using the function to counts the number of amino acids in the given sequence

```shell  
amino_acid_tools('EGVIMSELKLK', 'PLPKvelPPDFVD', 'DVIGISILGKEV', 'show_length')  
```

Input: 'EGVIMSELKLK', 'PLPKvelPPDFVD', 'DVIGISILGKEV', 'show_length'  
Output: '[11, 13, 12]'

### Using the function to determine the predominant secondary structure

```shell  
amino_acid_tools('EGVIMSELKLK', 'PLPKvelPPDFVD', 'DVIGISILGKEV', 'folding')  
```  
Input: 'EGVIMSELKLK', 'PLPKvelPPDFVD', 'DVIGISILGKEV', 'folding'  
Output: '['alfa_helix', 'equally', 'equally']'

### Using the function to estimate relative charge

```shell  
amino_acid_tools('EGVIMSELKLK', 'PLPKvelPPDFVD', 'DVIGISILGKEV', 'seq_charge')  
```

Input: 'EGVIMSELKLK', 'PLPKvelPPDFVD', 'DVIGISILGKEV', 'seq_charge'  
Output: '['neutral', 'negative', 'negative']'

  

## Contacts  
- [Cesnokova Anna] annachesnokova0303@gmail.com
 - [Lukina Maria] 
 maria.v.luk@gmail.com

![Screenshot](https://github.com/anisssum/HW4_Functions2/blob/HW4_Chesnokova/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-09-30%20223608.png)
