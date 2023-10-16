import csv

compound_list = []

with open("provinces.txt", 'rt') as csvfile:
    
    for row in csvfile:
        clean_file = row.strip()
        compound_list.append(clean_file)
        if clean_file == 'AB':
            INDEX = compound_list.index(clean_file)
            compound_list.pop(INDEX)
            compound_list.insert(INDEX-1, 'Alberta')
            
compound_list.pop(0)
compound_list.pop()
print(compound_list)
print(compound_list.count('AB'))
print(compound_list.count('Alberta'))