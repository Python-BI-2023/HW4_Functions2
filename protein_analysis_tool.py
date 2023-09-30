
def get_amino_acid_sum(protein_sequences):
    for protein_sequence in range(len(protein_sequences)):
        dictionary = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
                      'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0,
                      'T': 0, 'V': 0, 'W': 0, 'Y': 0}
        for amino_acid in protein_sequences[protein_sequence]:
            dictionary[amino_acid] += 1
            clone = {
                'Аланин': dictionary['A'],
                'Цистеин': dictionary['C'],
                'Аспарг кислота': dictionary['D'],
                'Глутаминовая кислота': dictionary['E'],
                'Фенилаланин': dictionary['F'],
                'Глицин': dictionary['G'],
                'Гистидин': dictionary['H'],
                'Изолейцин': dictionary['I'],
                'Лизин': dictionary['K'],
                'Лейцин': dictionary['L'],
                'Метионин': dictionary['M'],
                'Аспаргин': dictionary['N'],
                'Пролин': dictionary['P'],
                'Глутамин': dictionary['Q'],
                'Аргинин': dictionary['R'],
                'Серин': dictionary['S'],
                'Трианин': dictionary['T'],
                'Валин': dictionary['V'],
                'Триптофан': dictionary['W'],
                'Тирозин': dictionary['Y']
            }
        print('количество аминокислот в последовательности ', protein_sequence + 1, ':')
        for key, value in clone.items():
            print(key,value)



def beautiful_print(codon_optimization_list):
    for nucleotide_sequence in range(len(codon_optimization_list)):
        print('sequence ', nucleotide_sequence + 1)
        print(codon_optimization_list[nucleotide_sequence])



def codon_optimization(protein_sequences):
    cell_type = input('Введите вид организма для оптимизации кодонов: ')

    if cell_type == 'Esherichia coli' or cell_type == 'E.coli':
        codon_optimization_Ecoli = []
        Ecoli_triplets = {'A': 'GCG', 'C': 'TGC', 'D': 'GAT', 'E': 'GAA', 'F': 'TTT', 'G': 'GGC',
                          'H': 'CAT', 'I': 'ATT', 'K': 'AAA', 'L': 'CTG', 'M': 'ATG', 'N': 'AAC',
                          'P': 'CCG', 'Q': 'CAG', 'R': 'CGT', 'S': 'AGC', 'T': 'ACC', 'V': 'GTG',
                          'W': 'TGG', 'Y': 'TAT'}
        replacer_Ecoli = Ecoli_triplets.get
        for amino_acid in range(len(protein_sequences)):
            codon_optimization_Ecoli += [''.join([replacer_Ecoli(n, n) for n in protein_sequences[amino_acid]])]
        beautiful_print(codon_optimization_Ecoli)

    if cell_type == 'Pichia pastoris' or cell_type == 'P.pastoris':
        codon_optimization_Ppastoris = []
        Ppastoris_triplets = {'A': 'GCT', 'C': 'TGT', 'D': 'GAT', 'E': 'GAA', 'F': 'TTT', 'G': 'GGT',
                              'H': 'CAT', 'I': 'ATT', 'K': 'AAG', 'L': 'TTG', 'M': 'ATG', 'N': 'AAC',
                              'P': 'CCA', 'Q': 'CAA', 'R': 'AGA', 'S': 'TCT', 'T': 'ACT', 'V': 'GTT',
                              'W': 'TGG', 'Y': 'TAC'}
        replacer_Ppastoris = Ppastoris_triplets.get
        for amino_acid in range(len(protein_sequences)):
            codon_optimization_Ppastoris += [''.join([replacer_Ppastoris(n, n) for n in protein_sequences[amino_acid]])]
        beautiful_print(codon_optimization_Ppastoris)

    if cell_type == 'Mouse' or cell_type == 'mouse':
        codon_optimization_Mouse = []
        Mouse_triplets = {'A': 'GCC', 'C': 'TGC', 'D': 'GAC', 'E': 'GAG', 'F': 'TTC', 'G': 'GGC',
                          'H': 'CAC', 'I': 'ATC', 'K': 'AAG', 'L': 'CTG', 'M': 'ATG', 'N': 'AAC',
                          'P': 'CCC', 'Q': 'CAG', 'R': 'CGG', 'S': 'AGC', 'T': 'ACC', 'V': 'GTG',
                          'W': 'TGG', 'Y': 'TAC'}
        replacer_Mouse = Mouse_triplets.get
        for amino_acid in range(len(protein_sequences)):
            codon_optimization_Mouse += [''.join([replacer_Mouse(n, n) for n in protein_sequences[amino_acid]])]
        beautiful_print(codon_optimization_Mouse)
    else:
        print('Для оптимизации кодонов доступны следующие виды организмов: Esherichia coli, Pichia pastoris, Mouse')




b = get_amino_acid_sum(['MSRQEADLKVSIKKACSTEEAAPK','RKHVRACIVFTWDHRSSKAFYNGLRLL'])
#print(b)

#for i in range(len(b)):
 #   print('sequence ', i+1)
  #  print(b[i])
