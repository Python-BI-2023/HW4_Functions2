# ODAAS(Obtaining Data from an Amino Acid Sequence)

## Overview:
The idea of this program is to make life easier for experimenters and bioinformaticians working with amino acid sequences (both long and short). The ODAAS tool will allow you to quickly obtain various characteristics of your amino acid sequence. 

## Instruction: 
The function ‘run_aminoacid_seq’ takes 1 amino acid sequence as input (both in three-letter and one-letter form, str), next you need to specify named arguments: function, record_type.
- The argument **sequence** entirely must be written in capital or lowercase letters without spaces or commas. Output saves register
- The argument **“function “** must be passed a string with the name of the action (see possible actions below) that needs to be performed. 
- The argument **“record_type”** indicates the form in which you present your sequence. If you are using a three-letter sequence, specify **“record_type= 3”**. If you are using a one -letter sequence, specify **“record_type= 1”** (by default). 

### Example:
```run_aminoacid_seq (‘ALAGLNGLU’, function = ‘count_protein_length’, record_type = 1)```
```run_aminoacid_seq (‘glyvalala’, function = ‘count_protein_length’, record_type = 3)```

Also, if necessary specify a named argument **percent=True** (default False) for actions: determine_charge, determine_polarity (Look in the description of actions).

### Example:
```run_aminoacid_seq (‘LLYdD’, function = ‘determine_charge’, record_type = 1, percent=True)```

## Troubleshooting:
The program works with 20 proteinogenic amino acids {'G', 'A', 'V', 'L', 'I', 'M', 'P', 'F', 'W', 'S', 'T', 'N', 'Q', 'Y', 'C', 'K', 'R', 'H', 'D', 'E'}.
If you use a symbol that does not represent an amino acid, or wrong record type, the program will generate an **error** where you can see the first wrong symbol. 
- correct function launch:
```run_aminoacid_seq('ALALEUILE', function = 'count', record_type = 3)```
- incorrect function launch:
```run_aminoacid_seq('ALAmIle', function = 'count', record_type = 3)```

## Possible actions:
1. **translate** - Translation of a one-letter amino acid sequence into a three-letter one (for better visual perception), and the reverse operation. Output: str
2. **count_protein_length** - obtaining the length of the amino acid sequence. Output: int
3. **count_possible_number_of_disulfide_bonds** - counting the number of possible combinations of two different cysteines to form a disulfide bond. Output: int
4. **count_molecular_weight** - calculating the molecular weight of a protein. Output: int
5. **determine_charge** - counting the number of positive, negative and neutral amino acids in a protein. To get the output in percent, specify percent=True. Output: dict
6. **determine_polarity** - counting hybrophobic and hydrophilic amino acids in a protein. To get the output in percent, specify percent=True. Output: dict
7. **convert_amino_acid_seq_to_dna** - convert an amino acid sequence to the most likely DNA sequence. Output: str
8. **summary** - a summary of all information about the sequence (the result of executing all functions). Output: dict

### Example:

```run_aminoacid_seq (‘LLYdD’, function = ‘translate’, record_type = 1)```
```run_aminoacid_seq (‘ALAGLYALA’, function = ‘translate’, record_type = 3)```
```run_aminoacid_seq (‘LLYdD’, function = ‘count_protein_length’, record_type = 1)```
```run_aminoacid_seq (‘ALAGLYALA’, function = ‘count_protein_length’, record_type = 3)```
```run_aminoacid_seq (‘LLYdD’, function = ‘count_molecular_weight’, record_type = 1)```

```run_aminoacid_seq (‘alaglyala’, function = ‘determine_charge', record_type = 3, percent=True)```
```run_aminoacid_seq (‘LLYdD’, function = ‘determine_charge', record_type = 1, percent=True)```

```run_aminoacid_seq (‘alaglyala’, function = ‘determine_charge’, record_type = 3)```
```run_aminoacid_seq (‘LLYdD’, function = ‘determine_charge', record_type = 1)```

## Development team:

**Iurii Slepov** - team leader, author of main, count, translate and summary functions
**Veronika Vadekhina** - author of count_possible_number_of_disulfide_bonds, count_molecular_weight and convert_amino_acid_seq_to_dna functions
**Yulia Nechaeva** - author of determine_charge and determine_polarity functions

