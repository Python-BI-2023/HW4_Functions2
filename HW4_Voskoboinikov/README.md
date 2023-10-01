# Ultimate Protein Tools

### Overview

This project contains a `ultimate_protein_tools.py` program, which implements the `run_ultimate_protein_tools()` function, the input of which is protein sequences and the action that needs to be applied to them. 

### Installation

```python
import ultimate_protein_tools as upt
```

Make sure the path to the directory with `ultimate_protein_tools.py` is added to the PATH so that Python can find it when importing.

### Usage

You can use next arguments for ***run_ultimate_protein_tools*** function:

0. `run_ultimate_protein_tools` 
    Accepts command and runs it on input data with params

    Arguments:
    - command (str): Valid command from command_dct
    - inp (str): Input in form of path, seq, seq list or seq dct

    Return:
    - output_dct (dict): dict where keys are number or name of seq and values are results of command run

1. `read_seq_from_fasta`: Reads sequences from fasta file and returns dictionary.
    
    Arguments:
    - path_to_seq (str): path to file

    Return:
    - dict: dict of sequences names as keys and sequences themselves as values {'seq_name': 'sequence',}

2. `find_sites`: Finds indexes of given sites.

    Arguments:
    - seq (str): seq to be checked
    - *args (str): sites to be found
    - is_one_based (bool): whether result should be 0- (False) or 1-indexed (True). Default False

    Return:
    - dict: dictionary of sites as keys and lists of indexes for the site where it's been found

3. `get_protein_rnas`: Returns list of all possible RNA's from which can serve as matrix for protein synthesis.

    WARNING: can be computationally intensive on longer sequences, will NOT start unless check_if_user_conscious is True!

    Arguments:
    - seq (str): seq to be checked
    - check_if_user_conscious (bool): checks user's consciousness. Default False

    Return:
    - list: list of possible RNA's as str

4. `get_protein_rnas_number`: Get number of all possible RNA's for a given protein.

    Arguments:
    - seq (str): seq to be checked

    Return:
    - int: number of possible RNA's for seq

5. `get_frameshift_proteins`: Returns list of all possible proteins from all possible frames in peptide.

    WARNING: can be computationally intensive on longer sequences, will NOT start unless check_if_user_conscious is True!
    
    Arguments:
    - seq (str): seq to be checked
    - check_if_user_conscious (bool): checks user's consciousness. Default False
    - is_stop_codon_termination_enabled (bool): terminate translation when reached stop-codon. Default False.

    Return:
    - dict: dict of lists of all possible frames proteins:
    {frame_0: ['protein_seqs'], frame_1: ['protein_seqs'], frame_2: ['protein_seqs']}

6. `get_length_of_protein`: Calculates the length of a protein.

   Argument:
   - seq (str): sequence to calculate the length

   Return:
   - int: sequence length

7. `count_aa`: Counts the number of given or all amino acids in a protein sequence.

   Arguments:
   - seq (str): sequence to count amino acids
   - aminoacids (str): which amino acids to count in sequence. If you want to count all amino acids in the whole sequence, you can provide empty string to this argument or just don't provide this keyword

   Return:
   - dict: a dictionary with amino acids and its count

8. `get_fracture_of_aa`: Calculates the fracture or percentage of amino acids in a protein sequence.

    Arguments:
    - seq (str): sequence in which you need to calculate the fracture of amino acids
    - show_as_percentage (bool): change it to True, if you want to get results with percentages
    - aminoacids (str): the fracture of which amino acids to count in the sequence

    Return:
    - dict: a dictionary with amino acids and its fracture or percentage

9. `calculate_protein_mass`: Calculates the molecular mass of a protein based on its amino acid sequence and a dictionary of amino acid masses.

    Arguments:
    - sequence(str or list): A string or list of characters representing the amino acid sequence.
    - aa_atomic_mass(dict): A dictionary linking amino acids to their masses in atomic mass units.
    
    Return:
    - float: The molecular mass of a protein in atomic mass units, rounded to the third decimal place.

10. `get_atomic_mass`: Calculates the molecular mass of a biological molecule, primarily an amino acid, based on a simple chemical formula.

    Arguments:
    - chem (str): String representing a simple chemical formula, e.g. C2H5OH
    - atomic_mass (dict[str, float], optional): A dictionary linking the chemical elements Carbon, Hydrogen, Oxygen,
    Nitrogen, and Sulfur with their masses in atomic mass units.

    Return:
    - float: Molecular mass of a biological molecule in atomic mass units.

11. `convert_aa_name`: Converts a sequence of one-letter amino acid codes to three-letter designations.

    Arguments:
    - sequence (str): String with one-letter amino acid codes.
    - name_dict (dict[str, str], optional): A dictionary linking one-letter codes to three-letter designations.
    If not provided, the standard AA_NAME_DICT dictionary is used.
    - sep (str, optional): Separator between three-letter amino acid designations. There is no delimiter by default.
    - use_default_register(bool, optional): Determines whether to preserve letter case in three-letter designations.
    If True, the letters will be converted to upper or lower case depending on the case of the depending
    on the case of the one-letter code. The default is False.

    Return:
    - str: A string of three-letter amino acid designations separated by the specified delimiter.

### Input of data

During each run of the main function, the user is required to enter a **protein sequence / sequences / fasta-file** that must be processed using the procedures listed above.

The program involves the analysis of protein sequences consisting of <u>**20 canonical amino acids**</u>.

If the data is entered incorrectly, an appropriate error will be displayed.

```python
run_ultimate_protein_tools('AZAZA', get_length_of_protein)
False
```

### Examples

```python
read_seq_from_fasta('/content/testdata.fasta', use_full_name=True)

{'crab_anapl ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 'MDITIHNPLIRRPLFSWLAPSRIFDQIFGEHLQESELLPASPSLSPFLMRSPIFRMPSWLETGLSEMRLEKDKFSVNLDVKHFSPEELKVKVLGDMVEIHGKHEERQDEHGFIAREFNRKYRIPADVDPLTITSSLSLDGVLTVSAPRKQSDVPERSIPITREEKPAIAGAQRK',
 'crab_bovin ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 'MDIAIHHPWIRRPFFPFHSPSRLFDQFFGEHLLESDLFPASTSLSPFYLRPPSFLRAPSWIDTGLSEMRLEKDRFSVNLDVKHFSPEELKVKVLGDVIEVHGKHEERQDEHGFISREFHRKYRIPADVDPLAITSSLSSDGVLTVNGPRKQASGPERTIPITREEKPAVTAAPKK',
 'crab_chick ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 'MDITIHNPLVRRPLFSWLTPSRIFDQIFGEHLQESELLPTSPSLSPFLMRSPFFRMPSWLETGLSEMRLEKDKFSVNLDVKHFSPEELKVKVLGDMIEIHGKHEERQDEHGFIAREFSRKYRIPADVDPLTITSSLSLDGVLTVSAPRKQSDVPERSIPITREEKPAIAGSQRK',
 'crab_human ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 'MDIAIHHPWIRRPFFPFHSPSRLFDQFFGEHLLESDLFPTSTSLSPFYLRPPSFLRAPSWFDTGLSEMRLEKDRFSVNLDVKHFSPEELKVKVLGDVIEVHGKHEERQDEHGFISREFHRKYRIPADVDPLTITSSLSSDGVLTVNGPRKQVSGPERTIPITREEKPAVTAAPKK',
 'crab_mesau ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 'MDIAIHHPWIRRPFFPFHSPSRLFDQFFGEHLLESDLFSTATSLSPFYLRPPSFLRAPSWIDTGLSEMRMEKDRFSVNLDVKHFSPEELKVKVLGDVVEVHGKHEERQDEHGFISREFHRKYRIPADVDPLTITSSLSSDGVLTVNGPRKQASGPERTIPITREEKPAVTAAPKK',
 'crab_mouse ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN) (P23).': 'MDIAIHHPWIRRPFFPFHSPSRLFDQFFGEHLLESDLFSTATSLSPFYLRPPSFLRAPSWIDTGLSEMRLEKDRFSVNLDVKHFSPEELKVKVLGDVIEVHGKHEERQDEHGFISREFHRKYRIPADVDPLAITSSLSSDGVLTVNGPRKQVSGPERTIPITREEKPAVAAAPKK',
 'crab_rabit ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 'MDIAIHHPWIRRPFFPFHSPSRLFDQFFGEHLLESDLFPTSTSLSPFYLRPPSFLRAPSWIDTGLSEMRLEKDRFSVNLDVKHFSPEELKVKVLGDVIEVHGKHEERQDEHGFISREFHRKYRIPADVDPLTITSSLSSDGVLTVNGPRKQAPGPERTIPITREEKPAVTAAPKK',
 'crab_rat ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 'MDIAIHHPWIRRPFFPFHSPSRLFDQFFGEHLLESDLFSTATSLSPFYLRPPSFLRAPSWIDTGLSEMRMEKDRFSVNLDVKHFSPEELKVKVLGDVIEVHGKHEERQDEHGFISREFHRKYRIPADVDPLTITSSLSSDGVLTVNGPRKQASGPERTIPITREEKPAVTAAPKK',
 'crab_squac ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 'MDIAIQHPWLRRPLFPSSIFPSRIFDQNFGEHFDPDLFPSFSSMLSPFYWRMGAPMARMPSWAQTGLSELRLDKDKFAIHLDVKHFTPEELRVKILGDFIEVQAQHEERQDEHGYVSREFHRKYKVPAGVDPLVITCSLSADGVLTITGPRKVADVPERSVPISRDEKPAVAGPQQK'}

find_sites('FSWLTPSRIFDQIFGEHLQESELLPTSPSLSPFLMRSPFFRMPSWLETGLS', 'M')
{'M': [34, 41]}

run_ultimate_protein_tools('find_sites', '/content/testdata.fasta', 'M')
{'crab_anapl': {'M': [0, 48, 55, 66, 95]},
 'crab_bovin': {'M': [0, 67]},
 'crab_chick': {'M': [0, 48, 55, 66, 95]},
 'crab_human': {'M': [0, 67]},
 'crab_mesau': {'M': [0, 67, 69]},
 'crab_mouse': {'M': [0, 67]},
 'crab_rabit': {'M': [0, 67]},
 'crab_rat': {'M': [0, 67, 69]},
 'crab_squac': {'M': [0, 43, 51, 55, 58]}}

run_ultimate_protein_tools('find_sites', 'FSWLTPSRIFDQIFGEHLQESELLPTSPSLSPFLMRSPFFRMPSWLETGLS', 'M')
{'M': [34, 41]}

run_ultimate_protein_tools('get_protein_rnas', 'NnnN', check_if_user_conscious=True, use_full_name=True)
['AAUaauaauAAU',
 'AACaauaauAAU',
 'AAUaacaauAAU',
 'AACaacaauAAU',
 'AAUaauaacAAU',
 'AACaauaacAAU',
 'AAUaacaacAAU',
 'AACaacaacAAU',
 'AAUaauaauAAC',
 'AACaauaauAAC',
 'AAUaacaauAAC',
 'AACaacaauAAC',
 'AAUaauaacAAC',
 'AACaauaacAAC',
 'AAUaacaacAAC',
 'AACaacaacAAC']

run_ultimate_protein_tools('get_protein_rnas', 'NnnN', use_full_name=True)
'You don't know what you're doing!'

run_ultimate_protein_tools('get_protein_rnas_number', '/content/testdata.fasta', use_full_name=True)
{'crab_anapl ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 306539842376921568815733271183477097188669192775870536614881550927197241900538112709230592,
 'crab_bovin ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 3444683660839151566170764002105685020808749008532141887447338361036488073592878215794262016,
 'crab_chick ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 919619527130764706447199813550431291566007578327611609844644652781591725701614338127691776,
 'crab_human ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 2296455773892767710780509334737123347205832672354761258298225574024325382395252143862841344,
 'crab_mesau ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 765485257964255903593503111579041115735277557451587086099408524674775127465084047954280448,
 'crab_mouse ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN) (P23).': 3444683660839151566170764002105685020808749008532141887447338361036488073592878215794262016,
 'crab_rabit ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 2296455773892767710780509334737123347205832672354761258298225574024325382395252143862841344,
 'crab_rat ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 574113943473191927695127333684280836801458168088690314574556393506081345598813035965710336,
 'crab_squac ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': 9450435283509332143129668044185692786855278487056630692585290428083643548951654913015808}

run_ultimate_protein_tools('get_frameshift_proteins', 'NnnN', check_if_user_conscious=True)
{'frame_0': ['NnnN'],
 'frame_1': ['iit', 'tii', 'tti', 'iti', 'tit', 'itt', 'ttt', 'iii'],
 'frame_2': ['**q', '*qq', '***', '*q*', 'q**', 'qqq', 'qq*', 'q*q']}

run_ultimate_protein_tools('get_frameshift_proteins', 'NnnN', check_if_user_conscious=True, is_stop_codon_termination_enabled=True)
{0: {'frame_0': ['NnnN'],
  'frame_1': ['iit', 'tii', 'tti', 'iti', 'tit', 'itt', 'ttt', 'iii'],
  'frame_2': ['qqq', '*', 'q*', 'qq*']}}

run_ultimate_protein_tools('get_length_of_protein', '/content/testdata.fasta')
{'crab_anapl': 174,
 'crab_bovin': 175,
 'crab_chick': 174,
 'crab_human': 175,
 'crab_mesau': 175,
 'crab_mouse': 175,
 'crab_rabit': 175,
 'crab_rat': 175,
 'crab_squac': 177}

run_ultimate_protein_tools('count_aa', '/content/testdata.fasta', 'MLK', use_full_name=True)
{'crab_anapl ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': {'M': 5,
  'L': 18,
  'K': 10},
 'crab_bovin ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': {'M': 2,
  'L': 15,
  'K': 10},
 'crab_chick ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': {'M': 5,
  'L': 18,
  'K': 10},
 'crab_human ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': {'M': 2,
  'L': 15,
  'K': 10},
 'crab_mesau ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': {'M': 3,
  'L': 14,
  'K': 10},
 'crab_mouse ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN) (P23).': {'M': 2,
  'L': 15,
  'K': 10},
 'crab_rabit ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': {'M': 2,
  'L': 15,
  'K': 10},
 'crab_rat ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': {'M': 3,
  'L': 14,
  'K': 10},
 'crab_squac ALPHA CRYSTALLIN B CHAIN (ALPHA(B)-CRYSTALLIN).': {'M': 5,
  'L': 13,
  'K': 9}}

run_ultimate_protein_tools('count_aa', '/content/testdata.fasta', 'MLK')
{'crab_anapl': {'M': 5, 'L': 18, 'K': 10},
 'crab_bovin': {'M': 2, 'L': 15, 'K': 10},
 'crab_chick': {'M': 5, 'L': 18, 'K': 10},
 'crab_human': {'M': 2, 'L': 15, 'K': 10},
 'crab_mesau': {'M': 3, 'L': 14, 'K': 10},
 'crab_mouse': {'M': 2, 'L': 15, 'K': 10},
 'crab_rabit': {'M': 2, 'L': 15, 'K': 10},
 'crab_rat': {'M': 3, 'L': 14, 'K': 10},
 'crab_squac': {'M': 5, 'L': 13, 'K': 9}}

run_ultimate_protein_tools('get_fracture_of_aa', 'NnnN')
{'n': 0.5, 'N': 0.5}

run_ultimate_protein_tools('calculate_protein_mass', 'NnnN')
474.424

run_ultimate_protein_tools('calculate_protein_mass', '/content/testdata.fasta')
{'crab_anapl': 19936.699,
 'crab_bovin': 20036.552,
 'crab_chick': 20019.741,
 'crab_human': 20158.674,
 'crab_mesau': 20074.577,
 'crab_mouse': 20038.568,
 'crab_rabit': 20106.642,
 'crab_rat': 20088.604,
 'crab_squac': 20253.948}

run_ultimate_protein_tools('get_atomic_mass', 'C2H5OH')
46.06804

run_ultimate_protein_tools('convert_aa_name', 'LTPSRIFDQIFGEHLQESELLP', use_default_register=False, sep='-')
Leu-Thr-Pro-Ser-Arg-Ile-Phe-Asp-Gln-Ile-Phe-Gly-Glu-His-Leu-Gln-Glu-Ser-Glu-Leu-Leu-Pro
```

### Contacts
![Wonderful Team](https://github.com/ArtemVaska/HW4_Functions2/blob/HW4_Vasilev/HW4_Voskoboinikov/Wonderful_team.jpg)

Aleksandr Voskoboinikov – Team Leader (wwoskie@gmail.com)

Artem Vasilev (artem_vasilev_01@list.ru)

Tatiana Lisitsa (ttnlsc@gmail.com)
