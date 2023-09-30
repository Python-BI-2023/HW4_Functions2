# ProtSeqO

## Tool for protein sequences operation
This tool can help you find some characteristics of protein sequence such as:
* find length of sequence;
* rewrite 1-letter sequence to 3-letter sequence;
* calculate isoelectric point;
* calculate the approximate total charge of sequence for given pH value;
* etc.

## How use ProtSeqO
Execute script (you should be on directory with script):
```bash
python3
>>> from ProtSeqO import process_seqs
>>>print(process_seqs(_command__, __sequence or list of sequences__))
```

You can input to main function one as string or some as list of strings protein sequences. __Pay attention__ that your sequence(s) should contain only 1-letter symbols of aminoacids.

## ProtSeqO accepts next options
* 'gravy' - this option calculate GRAVY (grand average of hydropathy) value of given amino acids sequence.
* 'iso' -  calculate approximate isoelectric point of given amino acids sequence.
* 'rename' - transform 1-letter aminoacid symbols in sequence to 3-letter symbols separated by hyphens.
* 'lengths' - counts number of aminoacids in given sequence(s).
* 'weights' - calculate protein molecular weight using the average molecular weight of amino acid - 110 Da.
* 'heavy' - return the sequence(s) of the heaviest protein from list
* 'light' - return the sequence(s) of the lightest protein from list

## ProtSeqO using examples
```python
python3
>>> from ProtSeqO import process_seqs
>>> print(process_seqs('iso', ['ACGTWWA', 'ILATTWP']))
### [5.8, 6.0]
```

## In case of problem - contact with us in GitHub
___Developers___:
* Petrikov Kirill
* Muradova Gulgaz
* Yury Popov

![Developers](/images/pic.jpg "We are here")


