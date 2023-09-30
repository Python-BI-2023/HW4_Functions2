# Protein_tools.py
## A tool to work with protein sequences

*Proteins* are under the constant focus of scientists. Currently, there are an enormous amount of tools to operate with nucleotide sequences, however, the same ones for proteins are extremely rare. 


`Protein_tools.py` is an open-source program that facilitates working with protein sequences. 

*В моём представлении здесь должна быть картинка*

## Usage
The programm is based on `run_protein_tools` function that takes the list of **one-letter amino acid sequences**, name of procedure and relevant arguments. If you have three-letter amino acid sequences you could convert them by using `three_one_letter_code` procedure.

To start with the program run the following command:

`run_protein_tools([sequence_1, sequence_2 ..., sequence_n], procedure, ...)`

Where:
- [sequence_1, sequence_2 ..., sequence_n] - a list of protein sequences
- procedure - a type of procedure to use that is inputed in *string* type
- ... - an additional argument that is to be inputed in *string* type

## Options

The program has five types of procedures:

#### `three_one_letter_code`

- The main aim - to convert three-letter amino acid sequences to one-letter ones and vice-versa
- An additional argument: no

#### `define_molecular_weight` 

- The main aim - to determine the exact molecular weight of protein sequences
- An additional argument: no

`check_for_motifs` - to search for the motif of interest in protein sequences

`search_for_alt_frames` - to look for alternative frames that start with methyonine or other non-canonical start amino acids

`convert_to_nucl_acids` - covert protein sequences to DNA and RNA

**Requirments**

Use only sequences that are encoded with one-letter. Если у вас трёхбуквенный код используйте наше функции для конвертации
Трёхбуквенный код также используется для конвертации. Он разделён дефисами 
## Examples

## Troubleshooting

## Contacts
Authors:

Vladimir Grigoriants 

Tulyavko Vlada 

Ekaterina Shitik (EkaterinShitik)


**Список процедур:**

- `transcribe` — напечатать транскрибированную последовательность*
- `reverse` — напечатать перевёрнутую последовательность
- `complement` — напечатать комплементарную последовательность
- `reverse_complement` — напечатать обратную комплементарную последовательность
- `gc_count` — посчитать содержание нуклеотидов *G* и *C* в процентах
  
\* Обратная транскрипция в рамках данной процедуры также учитывается (РНК в ДНК)
