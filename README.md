# Homework 4
## Описание
В файле `protein_tool.py` содержится функция `protein_tool`. Она принимает на вход название процедуры и последовательность аминокислот, или две последовательности, в случае некоторых процедур. Данный тул предназначен для обработки белковых последовательностей. 

Функция возвращает строку, в которой отражен результаты работы с последовательностью. 

### Требования к последовательности

- Последоваетельность должна бысть составлена из однобуквенных названий аминокислот
- Последовательнось может быть передана в верхнем или нижнем регистре
- Последовательность должна содержать протеиногенные аминокислоты, без их модификаций

### Доступные процедуры 

У нас реализованы следующие функции:

- `calculate_amino_acid_percentages` - подсчет относительного аминокислотного состава
- `classify_amino_acid` - подсчет числа аминокислот по классам
- `find_amino_acid_indices` - получить индексы всех вхождений АК в белок
- `counting_point_mutations` - подсчет точечных мутаций и подсчет процента схожеcти (длина последовательности/количество точечных мутаций)
- `counting_molecular_weight` - подсчет молекулярной массы
- `get_occurrences` - найти число вхождений в последовательность другой последовательности, индексы и количество вхождений
- `count_variant_rna` - подсчет вариантов РНК, которые могли бы кодировать заданную последовательность
- `determine_total_protein_charge` - определение суммарного заряда белка
- `calculate_pI` - подсчет примерной изоэлектической точки


**Описание функций и примеры использования**

:computer: Автор: Кабалина Алиса

<img src="https://i.pinimg.com/originals/90/89/ab/9089ab65566a39fa1f9a7ef1f1426ab4.jpg" width="200" height="200">

Функция `count_variant_rna` принимает на вход белковую последовательность (str). После этого функция подсчитывает количество возможных вариантов РНК, которые могут быть матрицей для синтеза заданной аминокислотной последовательности. Возвращается результат, количество возможных РНК (int)
```python
protein_tool('TATAQQQWRVVTDDDA', 'count_variant_rna') # '25165824'
```

Функция `determine_total_protein_charge` принимает на вход белковую последовательность (str). После этого функция определяет является ли заданная аминокислотная последовательнось заряженной положительноб отрицательно или не заряженной. Возвращается результат, строка `negative`, `positive`, `neutral`
```python
protein_tool('TDDDTEQQWRVVTDDDA', 'determine_total_protein_charge') # 'negative'
```

Функция `calculate_pI` принимает на вход белковую последовательность (str). После этого функция подсчитывает приблизительное значение изоэлектрической точки (pI) заданной аминокислотной последовательности. Возвращается результат, изоэлектрическая точка (float)
```python
protein_tool('TKKKKTDDDA', 'calculate_pI') # '7.225555555555555'
```

:computer: Автор: Орлова Виктория.

<img src="https://www.meme-arsenal.com/memes/6e7a90e11e31bbe40c15cdff7e442c92.jpg" width="200" height="200">


Функция counting_point_mutations принимает на вход две белковые последовательности (str). После этого команда подсчитывает количество мутаций - аминокислотных замен, в итоге возвращается результат, а именно число мутаций (int).
```python
run_protein_tools('ASQG', 'AMQR', 'counting_point_mutations') # 2
```

Функция counting_molecular_weight принимает на вход белковую последовательность (str). После этого команда подсчитывает молекулярную массу введенной белковой последовательности, в итоге возвращается результат, а именно число молекулярная масса (int).
```python
run_protein_tools('ASQGAMQR', 'counting_molecular_weight') # 847
```

Функция get_occurrences принимает на вход две белковые последовательности (str) - seq1 и seq2. После этого команда подсчитывает количество вхождений без пересечения второй белковой последовательности в первую, в итоге возвращается результат в виде строки (str) где через пробел идет: количество вхождений второй строки в первую строку, далее через пробел идут индексы вхождения (1 и далее).
```python
run_protein_tools('ASQRGARWQRMQR', 'QR', 'get_occurrences') # 'Number of occurrences: 3; indexes: 3, 9, 12'
```


:computer: Автор: Петухова Анастасия

<img src="https://www.meme-arsenal.com/memes/f07e3014f46a7e8f107c35f3bfc446a6.jpg" width="200" height="200">


Функция calculate_amino_acid_percentages принимает на вход белковую последовательность (str). После этого команда подсчитывает процентное содержание аминокислот в белке, в итоге возвращается результат в виде строки (str), где через двоеточие записана аминокислота и процентное содержание в белке. Функция округляет результат до двух знаков после десятичного разделителя и отсортировывает его в порядке убывания.
```python
run_protein_tools('ADNNDQD', 'calculate_amino_acid_percentages') # 'D: 42.86, N: 28.57, A: 14.29, Q: 14.29'
```

Функция classify_amino_acid принимает на вход белковую последовательность (str). Команда возвращает подсчитанное процентное содержание нейтральных, кислых и основных аминокислот в белке в виде строки (str). Функция округляет полученный результат до двух знаков после десятичного разделителя.
```python
run_protein_tools('ARNDCQ', 'classify_amino_acid') # 'neutral: 66.67, acidic: 16.67, basic: 16.67'
```

Функция find_amino_acid_indices принимает на вход белковую последовательность и аминокислоту (str) - seq и amino_acid. После этого команда ищет индексы вхождения аминокислоты в белке, в итоге возвращается результат в виде строки (str) со всеми индексами. 
```python
run_protein_tools('ARNDCQA', 'A', 'find_amino_acid_indices') # '1, 7'
```
Используя данную функцию вы можете столкнуться с ошибкой **<span style='color: red;'>ValueError</span>: Amino acid not found**.
Данная ошибка возникает, если введенная аминокислота не содержиться в введенной белковой последовательности, либо аминокислота записана в нижнем регистре.
```python
run_protein_tools('ARNDCQA', 'E', 'find_amino_acid_indices') # ValueError: Amino acid not found
```
```python
run_protein_tools('ARNDCQA', 'n', 'find_amino_acid_indices') # ValueError: Amino acid not found
```
