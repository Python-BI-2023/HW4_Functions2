
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








get_amino_acid_sum(['MSRQEADLKVSIKKACSTEEAAPKRKHVRACIVFTWDHRSSKAFYNGLRLLPIQNDEIPLFKSLITIHKVLQEGHPSAIKEGIKNRDWIQSLGHVFPGDGMKRYGRLIREYDRYLIRKIDFHNSHKGFNGTFEYEEYVSLKTVSDPNEGYEAIMDLMVLQDSINDLQRLLFASIDSSSHSELKISALVPLIAESYGIFKF'])
