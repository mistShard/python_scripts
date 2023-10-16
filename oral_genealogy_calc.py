# name = list("11123456780000")
# field_dict = {11:"Ordu Samuel Ken", 111:"Mabel Tracy Obinna", 1111:"Williams Precious"}

# name.insert(-4, "_")
# name.insert(-12, "_")
# companyNumber = "ng76_"
# name = "".join(name)

# a = name.split("_")
# print(a)
# b = a[0]
# print(field_dict.get(int(b)))

from oral_genealogy import get_date
import csv        
field_nameCount = 0
dataClerk_nameCount = 0
totalNameCountInFile = 0
agent = "precious"
dataClerk = "progress"
field = set()
data = set()
informants = []
field_NamesNotSent = 0
dataClerk_NamesNotSent = 0
path = "Lasalu field inventory"

with open(f"{path}\Folder Inventory Sat,24,Dec,2022.csv", "rt") as file:
    reader = csv.DictReader(file)
    next(reader)
    for row in reader:
        field.add(row["Field Agent"])
        data.add("Data Entry Clerk")
        totalNameCountInFile += int(row["No. of Entries"])
        if row["Field Agent"] == agent.capitalize():
            informants.append(row["Informant Name"])
            field_nameCount += int(row["No. of Entries"])
        if row["Data Entry Clerk"] == dataClerk.capitalize():
            informants.append(row["Informant Name"])
            dataClerk_nameCount += int(row["No. of Entries"])


print(f"\nAll Field Agents: {field}\n\
All Data Entry Clerks: {data}\n\
Field Agent: {agent.upper()}\n\
Data Entry Clerk: {dataClerk.upper()}\n\n\
Informants Are:" )

for name in set(informants):
    print(name)

print(f"\ntotal {agent.upper()}: {field_nameCount - field_NamesNotSent}\n\
total {dataClerk.upper()}: {dataClerk_nameCount - dataClerk_NamesNotSent}")

# To get the total valid number of names in the file
totalNumberOfNamesNotSent = 0
totalOfNamesSent = totalNameCountInFile - totalNumberOfNamesNotSent
print(f"\nTOTAL OF NAMES IN INVENTORY: {totalOfNamesSent}\n")


