mas = []
with open('FilteredDetections copy.csv') as f:
    mas = f.readlines()

with open('new_file.xlsx', 'w') as ff:
    for i in range(len(mas)):
        ff.write(f'{mas[i][:55]}\n')
