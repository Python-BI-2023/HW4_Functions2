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
 Данный проект должен был выполняться в команде, но, к сожалению, мне не удалось сделать только часть этого проекта- весь код и мини-программа писалась мной самостоятельно. В качестве данного ДЗ я освежила память в работе через GitHub, а также основые концепции языка Python. 

![alone](https://sun9-40.userapi.com/impf/c636016/v636016166/239f1/p0AWqN3onLw.jpg?size=550x483&quality=96&sign=19b32adae4a5ac6a436a740160fed9c6&type=album)

В качестве данного ДЗ необходимо написать свою собственную утилиту для работы с последовательностями аминокислот. Кроме того, необходимо оформить файл README.md так, будто это последний написанный мной файл в жизни 
> *Я очень постараюсь выполнить хороший ридми файл, но не обещаю, что он будет лучшим в моей жизни* 

## Main part
Реализовала программу `amino_acid_tools.py`. Эта программа обязательно содержит функцию `amino_acid_tools`, а также другие функции которые описаны снизу. Функция `amino_acid_tools` принимает на вход произвольное количество аргументов с последовательностью аминокислот или несколькими аминокислотными последовательностями (*str*), а также возможно введение слова "random", при использовании которого генерируется рандомная цепочка аминокислот, кроме того необходимо ввести название процедуры которую нужно выполнить (это всегда последний аргумент, *str*, см. пример использования). После этого команда делает заданное действие над всеми переданными последовательностями. Если подана одна последовательность - возвращается строка с результатом. Если подано несколько - возвращается список из строк. 

**Список процедур:**
- `long_amino_code (str) or (list)` — translated sequence from one-letter in three-letter code
- `molecular_weight (int) or (list)` — amino acid sequence molecular weight number or list of numbers
- `amino_to_rna (str) or (list)` — possible RNA sequence
- `amino_seq_charge (str) or (list)` — "positive", "negative" or "neutral"

## Examples  
Below is an example of processing an amino acid sequence.


**Еще один пример использования**
```python
Using the function for translated sequence from one-letter in three-letter code:
run_dna_rna_tools('ATG', 'transcribe') # 'AUG'
run_dna_rna_tools('ATG', 'reverse')' # 'GTA'
run_dna_rna_tools('AtG', 'complement') # 'TaC'
run_dna_rna_tools('ATg', 'reverse_complement') # 'cAT'
run_dna_rna_tools('ATG', 'aT', 'reverse') # ['GTA', 'Ta']
```


### **Учебный результат**

Это задание ~~позволило понять, что командная работа сокращает очень много времени и позволяет получить больше баллов за сданный вовремя проект~~ лучше помогло лучше разобраться с системой Git на практике, также потреннироваться в написании собственных биоинформатических функций, а также лучше осознать такие вещи как "ответсвенность" "команда" 


## Смотрите также


## Contact  
- [Mukhametshina Regina] 1709mrd@gmail.com


![это скриншот с командой за которую можно получить допбаллы](https://steamuserimages-a.akamaihd.net/ugc/1997942891875467390/4049C3EF5003271E1F619B28EC4CBD1FBEC1A275/)

> *Поставьте пожалуйста доп балл за будто бы скриншот с командой*

Спасибо! ✨✨
