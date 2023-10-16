import csv
from csv import DictWriter

filename = "Folder Inventory Sat-10-Dec-2022.csv"
folder = "ng76"
informant = "nkizu"
field_agent = "samuel"
field_manager = "ken"
clerk = "amy"
data_manager = "benji"
name_count = 22
column_headers = ["Folder Name", "Informant Name", "Field Agent", "Field Manager"
    , "Data Entry Clerk", "Data Manager", "No. of Entries"]

# Dictionary that we want to add as new row. The column
# headers will be the key and the input gotten from the 
# user will be the value
new_dict = {"Folder Name":folder, "Informant Name": informant, "Field Agent": field_agent,
"Field Manager": field_manager, "Data Entry Clerk": clerk, "Data Manager": data_manager,
"No. of Entries": name_count}

def check_line():
    try:
        with open(filename, "r") as file:  
            reader = csv.reader(file)
            line = next(reader)
            if line == column_headers:
                print("First ran")
                return True
            else:
                print("second ran")
                return False

    except(FileNotFoundError, PermissionError):
        return False
check_line_ = check_line()

if check_line_:
    with open(filename, "a", newline="") as file:
        # Pass the file object and a list
        # of column names to DictWriter()
        # You will get a object of DictWriter
        dictwriter_object = DictWriter(file, fieldnames=column_headers)
    
        # Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(new_dict)

else:
    with open(filename, "w", newline="") as file:
        # Pass the file object and a list
        # of column names to DictWriter()
        # You will get a object of DictWriter
        dictwriter_object = DictWriter(file, fieldnames=column_headers)

        # Write the column headers to the file
        dictwriter_object.writeheader()
    
        # Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(new_dict)
    