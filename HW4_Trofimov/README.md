<img width="641" alt="Screenshot 2023-09-27 at 17 01 47" src="https://github.com/michtrofimov/HW4_Functions2/assets/92677906/d5c63a17-7f6d-43c7-b88e-a2e994877abb">

# Das biotools.aminoacids
> **The great and terrifying successor of biopython**

Das biotools strikes again! Now it works only with aminoacid sequences! 

## Features

- **get_pI()**: Gives isoelectric point value for each aminoacid individually.

- **build_scoring_matri()**: Auxiliary function for needleman_wunsch. Build a scoring matrix for amino acid pairs, which can be used in sequence alignment algorithms.

- **needleman_wunsch()**: Implement the Needleman-Wunsch algorithm for global sequence alignment of two amino acid sequences.

- **convert_to_3L_code()**: Converts one letter animoacid sequence to three letter aminoacid sequence.

- **protein_mass()**: Calculates molecular weight of the aminoacid sequence using monoisotopic masses.

- **translate_protein_rna()**: Converts aminoacid sequence to RNA sequence. For those aminoacids that are coded with more than one codon, this function randomly chooses one codon from the set.

- **calculate_aa_freq()**: Calculate the frequences of aminoacids in protein sequences.

## Examples

- **get_pI**
  
```python 
calculate_pI('RAHP') -> "Sequence: RAHP. Isoelectric point of each aminoacid: [('R', 10.8), ('A', 6.0), ('H', 7.6), ('P', 6.3)]"
```

- **needleman_wunsch**

```python 
needleman_wunsch('raHP','RAQQHP') -> 'ra--HP, RAQQHP, final score: 2'
```

- **convert_to_3L_code**

```python 
convert_to_3L_code('ACDEF') -> 'Ala-Cys-Asp-Glu-Phe'
```

- **protein_mass**

```python 
protein_mass('ACDEF') -> 565.184
```

- **translate_protein_rna**

```python 
translate_protein_rna('ACDEF') -> 'GCCUGCGACGAGUUC'
```

- **calculate_aa_freq**

```python
calculate_aa_freq('ACDEF') -> {'A': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1}
```

## OUR TEAM
<img width="800" alt="Screenshot 2023-09-30 at 16 34 25" src="https://github.com/michtrofimov/HW4_Functions2/assets/92677906/38fcc288-2d27-445d-b1dc-a3b055099a26">

Up to bottom, left to right:
- Alisa Fedorenko: functions **main**, **calculate_aa_freq**
- Michil Trofimov: functions **get_pI**, **needleman_wunsch** (teamlead)
- Shakir Suleimanov: functions **convert_to_3L_code**, **protein_mass**, **translate_protein_rna**

