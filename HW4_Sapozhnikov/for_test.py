my_input = 'vla', 'ValTrpPhe', 'phe', 'vla', 'ValTrpPhe', 'phe'

for aminoacids in my_input:
    devided = [aminoacids[i:i + 3] for i in range(0, len(aminoacids), 3)]
    print(devided)

