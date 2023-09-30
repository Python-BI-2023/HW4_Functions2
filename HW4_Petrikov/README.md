# ProtSeqO

## Tool for PROtein SEQuences Operation

*This is the repo for the fourth homework of the BI Python 2023 course*

This tool can perform some simple operations on amino acid sequences:
* help you calculate protein lengths, molecular weights, isoelectric points and GRAVY values
* find and show you heaviest and lightest proteins
* rewrite 1-letter sequence to 3-letter sequence

## How use ProtSeqO
Execute script (you should be on directory with script):
```bash
python3
>>> from ProtSeqO import process_seqs
>>>print(process_seqs(__command__, __sequence or list of sequences__))
```

You can input to `process_seqs()` sequence as string or list with any strings of sequences. __Pay attention__ that your sequence(s) should contain 1-letter symbols (case does not matters) of 20 common amino acids ('U' for selenocysteine and 'O' for pyrrolysine doesn't allowed).

Command must be a string with one of followed options.

## ProtSeqO options
* 'lengths' - return list with numbers of AA in each sequence(s)
* 'molw' - return list of protein molecular weight (use the average molecular weight of AA, 110 Da)
* 'iso' - return list of approximate isoelectric point of given amino acids sequence
* 'gravy' - return list of GRAVY (grand average of hydropathy) values
* 'rename' - return list of sequences in 3-letter AA code (AA separated by hyphens)
* 'heavy' - return the sequence(s) with maximum molecular weight and weigth value
* 'light' - return the sequence(s) with minimum molecular weight and weigth value

## ProtSeqO using examples
```python
python3
>>> from ProtSeqO import process_seqs
>>> print(process_seqs('iso', ['ACGTWWA', 'ILATTWP']))
### [5.8, 6.0]
>>> print(process_seqs('gravy', 'ilattwp'))
### [0.886]
>>> print(process_seqs('rename', ['ACGTwwa']))
### ['Ala-Cys-Gly-Thr-Trp-Trp-Ala']
>>> print(process_seqs('heavy', ['ILATTWP'], ['ACGTwwa']))
### ['ILATTWP', 'ACGTwwa'] - 770
```

## In case of problem - contact with us in GitHub
___Developers___:
* Petrikov Kirill
* Muradova Gulgaz
* Yury Popov

![Developers](https://github.com/KirPetrikov/HW4_Functions2/blob/HW4_Petrikov/HW4_Petrikov/images/pic.jpg "We are here")


