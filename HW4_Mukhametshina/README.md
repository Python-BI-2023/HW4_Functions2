[![Будто бы полезная ссылка, но просто попытка вставить ссылку](https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/AminoAcidball_rus.svg/1280px-AminoAcidball_rus.svg.png)](https://ru.wikipedia.org/wiki/%D0%90%D0%BC%D0%B8%D0%BD%D0%BE%D0%BA%D0%B8%D1%81%D0%BB%D0%BE%D1%82%D1%8B)
> *Не смогла уменьшить изображение*

[![Будто бы полезная ссылка, но просто попытка вставить ссылку_2]<a href="url"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/AminoAcidball_rus.svg/1280px-AminoAcidball_rus.svg.png" align="left" height="48" width="48" ></a>](https://ru.wikipedia.org/wiki/%D0%90%D0%BC%D0%B8%D0%BD%D0%BE%D0%BA%D0%B8%D1%81%D0%BB%D0%BE%D1%82%D1%8B)
> *Не смогла вставить ссылку на изображение*

# HW 4. Functions 2
> *This is the repo for the fourth homework of the BI Python 2023 course*

## Table of contents

  * [Project description](#project-description)
  * [Main part](#Main-part)
  * [Running instructions](#project-description) 
  * [Examples](#examples)
  * [Contact](#contact)
  * [License](#Учебный-результат)
  * [See also](#see-also)

## Project description
 This project was supposed to be carried out in a team, but, unfortunately, I was unable to do only part of this project - all the code and the mini-program were written by me independently. As this HW, I refreshed my memory in working through GitHub, as well as the basic concepts of the Python language. 

![alone](https://sun9-40.userapi.com/impf/c636016/v636016166/239f1/p0AWqN3onLw.jpg?size=550x483&quality=96&sign=19b32adae4a5ac6a436a740160fed9c6&type=album)

As a given HW, need to write your own utility for working with amino acid sequences. In addition, it is necessary to issue a file README.md as if this is the last file I wrote in my life 

> *Я очень постараюсь выполнить хороший ридми файл, но не обещаю, что он будет лучшим в моей жизни* 

## Main part
Implemented the program `amino_acid_tools.py `. This program necessarily contains the `amino_acid_tools` function, as well as other functions that are described below. The 'amino_acid_tools` function accepts an arbitrary number of arguments with a sequence of amino acids or several amino acid sequences (*str*), and it is also possible to introduce the word "random", which generates a random chain of amino acids, in addition, you must enter the name of the procedure to be performed (this is always the last argument, *str*, see usage example). After that, the command performs the specified action on all the transmitted sequences. If one sequence is submitted, a string with the result is returned. If several are submitted, a list of strings is returned.

**Список процедур:**
- `long_amino_code (str) or (list)` — translated sequence from one-letter in three-letter code
- `molecular_weight (int) or (list)` — amino acid sequence molecular weight number or list of numbers
- `amino_to_rna (str) or (list)` — possible RNA sequence
- `amino_seq_charge (str) or (list)` — "positive", "negative" or "neutral"

## Examples  
Below is an example of processing an amino acid sequence.

### Using the function for translated sequence from one-letter in three-letter code

```shell  
amino_acid_tools('PLfHnfPdD', 'YsGPFEEt', 'ogknHIPTu', 'long_amino_code')   
```
Input: 'PLfHnfPdD', 'YsGPFEEt', 'ogknHIPTu', 'long_amino_code'  
Output: '['ProLeuPheHisAsnPheProAspAsp', 'TyrSerGlyProPheGluGluThr', 'PylGlyLysAsnHisIleProThrSec']'

### Using the function for molecular weight calculation

```shell  
amino_acid_tools('fHnfPdPL','CpUPQWhmrY','random', 'CpUPQWhmrY','molecular_weight') 
```

Input: 'fHnfPdPL','CpUPQWhmrY','random', 'CpUPQWhmrY','molecular_weight'  
Input: 9
Output:[968.14, 1367.39, ('рандомная последовательнсть', 'FySiDfGym', 1124.43), 1367.39]

### Using the function to convert possible RNA sequence

```shell  
amino_acid_tools('DwhAntMcR', 'cvdrLepaW', 'VurgdOhio', 'amino_to_rna')  
```

Input: 'DwhAntMcR', 'cvdrLepaW', 'VurgdOhio', 'amino_to_rna'  
Output: Unknown amino acid code:  u
Unknown amino acid code:  O
Unknown amino acid code:  o
['GAUuggcauGCGaacacaAUGugcCGU', 'ugugucgaccggCUAgagccggcgUGG', 'GUUcgaggcgaucacauc']


### Using the function to estimate relative charge

```shell  
amino_acid_tools('DwhAntMcR', 'cvdrLepaW', 'VurgdOhio', 'amino_seq_charge')  
```

Input: 'random', 'cvdrLepaW', 'VurgdOhio', 'amino_seq_charge'  
Output: [('рандомная последовательнсть', 'UgMMFsGed', 'negativ'), 'negativ', 'positiv']

**Еще один пример использования**
```python
Using the function for translated sequence from one-letter in three-letter code:
amino_acid_tools('PLfHnfPdD', 'YsGPFEEt', 'ogknHIPTu', 'long_amino_code')  # 'GTA'
amino_acid_tools('fHnfPdPL','CpUPQWhmrY','random', 'CpUPQWhmrY','molecular_weight')  # 'TaC'
amino_acid_tools('DwhAntMcR', 'cvdrLepaW', 'VurgdOhio', 'amino_to_rna')  # 'cAT'
amino_acid_tools('DwhAntMcR', 'cvdrLepaW', 'VurgdOhio', 'amino_seq_charge') # ['GTA', 'Ta']
```


### **Учебный результат**

This task ~~позволило понять, что командная работа сокращает очень много времени и позволяет получить больше баллов за сданный вовремя проект~~ helped to better understand the Git system in practice, also to practice writing your own bioinformatic functions, as well as to better understand such things as "ответственность" "team"

## Смотрите также


## Contact  
- [Mukhametshina Regina] 1709mrd@gmail.com


![это скриншот с командой за которую можно получить допбаллы](https://steamuserimages-a.akamaihd.net/ugc/1997942891875467390/4049C3EF5003271E1F619B28EC4CBD1FBEC1A275/)

> *Поставьте пожалуйста доп балл за будто бы скриншот с командой*

Спасибо! ✨✨
