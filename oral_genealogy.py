import tkinter as tk
import number_entry as nent
import csv
from csv import DictWriter
from datetime import datetime

"""
___________________________________PROGRAM DESCRIPTION_____________________________________
Purpose:
    The purpose of this program is to provide a way for oral genealogy contractors to keep
    a digital daily inventory of every folder gotten from the field with all its relevant information.
    oral_genealogy.py presents a GUI (Graphical User interface) for the user to input the requisite data
    Every folder created through this program automatically has the day's date in its folder name,
    making it impossible to have multiple inventory files for the same day. At the same time 
    also preventing inventories entered on different days from having the same folder name.

This week I spent more than 10 hours working on my program and its test file.

List of functions in oral_genealogy.py:
    main()
    populate_main_window(frm_main)
    clear()
    activate_next()
    create_append_file(filename, column_headers, new_dict, checkline)
    check_line(filename, column_headers)
    get_date(date_seperator)

List of test functions in test_oral_genealogy.py:
    test_get_date()
    test_check_line()

In the writing of this program I read the python docs for: csv, dictionaries, tkinter,
    datetime, and open(). I tried to write a function that checks if the first line in a file
    is a header or not. Initially I used a code based around isinstance(cell, str) to make my
    comparison and it seemed to work. Sometime later I am running my code and I discover 
    that that method would always return True because every input in a csv file is
    interpreted as a str, so even if the first line of the file was "99, 99, 99" it would have
    still returned True. To correct this mistake I searched on the internet and found a
    different wy to do it. I used <<reader = csv.reader(file)>> then <<line = next(reader)>>
    and compared "line" to a list of headers, if they do not match, the program overwrites the 
    file with the headers in the list and the user input. I also tried to make error messages
    appear in the GUI by creating a label that changes to show an error when an error occurs.

Finished work:
    - The GUI is populated to show entry boxes to accept user input.
    - Two buttons (Clear and Next) were added to initiate operations that clear the user entry
        fields and store the entered data respectively.
    - User input is stored in a csv file that has the date in its folder name.
    - A column headers are added to the beginning of any file created.
    - If a column header exists, the program simply appends to the end of the file.
_______________________________________________________________________________________________
"""

company = "Lasalu Limited"
subscript = "Copyright 2022, Benji Nwangele Inc. All rights reserved."

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title(company + " Folder Details")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=100)
    
    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Folder Name:"
    lbl_folder = tk.Label(frm_main, text="Folder Name:")

    # Create a string entry box where the user will enter the folder name.
    ent_folder = tk.Entry(frm_main, width=50)

    # Create a label that displays "Informant"
    # "Field Agent Name", "Field Manager", "Data Entry Clerk", "Data Entry manager",
    #  and subscript.
    lbl_informant = tk.Label(frm_main, text="Informant:")
    lbl_fieldAgent = tk.Label(frm_main, text="Field Agent:")
    lbl_fieldManager = tk.Label(frm_main, text="Field Manager:")
    lbl_dataClerk = tk.Label(frm_main, text="Data Entry Clerk:")
    lbl_dataManager = tk.Label(frm_main, text="Data Entry Manager:")
    lbl_nameCount = tk.Label(frm_main, text="Number of Names:")
    lbl_subscript = tk.Label(frm_main, text=subscript)

    # Create five string entry boxes where the user will enter the informant, 
    # field agent, field manager, data entry clerk, and data entry manager's names.
    ent_informant = tk.Entry(frm_main, width=50)
    ent_fieldAgent = tk.Entry(frm_main, width=50)
    ent_fieldManager = tk.Entry(frm_main, width=50)
    ent_dataClerk = tk.Entry(frm_main, width=50)
    ent_dataManager = tk.Entry(frm_main, width=50)
    ent_nameCount = nent.IntEntry(frm_main, 10, 10**4, width=25)

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear", width=25, height=3)

    # Create the activate_next button
    btn_next = tk.Button(frm_main, text="Next", width=25, height=3)

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_folder.grid(  row=0, column=0, padx=3, pady=100)
    ent_folder.grid(  row=0, column=1, padx=3, pady=10)
    lbl_informant.grid(row=0, column=2, padx=(30,3), pady=10)
    ent_informant.grid( row=0, column=3, padx=3, pady=10)
    lbl_fieldAgent.grid( row=0, column=4, padx=(30, 3), pady=10)
    ent_fieldAgent.grid( row=0, column=5, padx=(3, 30), pady=10)
    lbl_fieldManager.grid( row=1, column=0, padx=3, pady=(10, 0))
    ent_fieldManager.grid( row=1, column=1, padx=(3), pady=(10, 0))
    lbl_dataClerk.grid( row=1, column=2, padx=(30, 3), pady=(10, 0))
    ent_dataClerk.grid(row=1, column=3, padx=3, pady=(10, 0))
    lbl_dataManager.grid( row=1, column=4, padx=(30, 3), pady=(10, 0))
    ent_dataManager.grid(row=1, column=5, padx=(3, 30), pady=(10, 0))
    lbl_nameCount.grid(row=4, column=0, padx=3)
    ent_nameCount.grid(row=4, column=1, padx=3, pady=100)
    btn_next.grid( row=5, column=5, padx=3, pady=50, columnspan=5)
    btn_clear.grid(row=5, column=0, padx=(60, 3), pady=50, columnspan=5, sticky="w")
    lbl_subscript.grid( row=5, column=3, padx=3, pady=3)

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_folder.delete(0, tk.END)
        ent_informant.delete(0, tk.END)
        ent_fieldAgent.delete(0, tk.END)
        ent_fieldManager.delete(0, tk.END)
        ent_dataClerk.delete(0, tk.END)
        ent_dataManager.delete(0, tk.END)
        ent_nameCount.delete(0, tk.END)

        ent_folder.focus()
    
    # This function will be called each time the
    # user presses the "activate_Next" button.
    def activate_next():
        """Save the contents of all the fields in a csv
        file."""
        date = get_date(",")
        path = "Lasalu field inventory/"
        filename = f"{path}Folder Inventory " + date +".csv"
        try:
            # Get the user's input.
            folder = ent_folder.get().upper()
            informant = ent_informant.get().title()
            field_agent = ent_fieldAgent.get().title()
            field_manager = ent_fieldManager.get().title()
            clerk = ent_dataClerk.get().title()
            data_manager = ent_dataManager.get().title()
            name_count = ent_nameCount.get()

            # Stores the column headers for the dictionary in
            # a list.
            column_headers = ["Folder Name", "Informant Name", "Field Agent", "Field Manager"
            , "Data Entry Clerk", "Data Manager", "No. of Entries"]

            # Dictionary that we want to add as new row. The column
            # headers will be the key and the input gotten from the 
            # user will be the value.
            new_dict = {"Folder Name":folder, "Informant Name": informant, "Field Agent": field_agent,
            "Field Manager": field_manager, "Data Entry Clerk": clerk, "Data Manager": data_manager,
            "No. of Entries": name_count}

            # Calls the check_line() function and stores the return bool in
            # a variable.
            checkline = check_line(filename=filename, column_headers=column_headers)

            # Call the create_append_file() to create a file and append
            # user input, or just append user input if the file is available.
            create_append_file(filename=filename, column_headers=column_headers,\
                 new_dict=new_dict ,checkline=checkline)

            # Call the clear() function to clear the entry boxes for
            # any other set of user inputs.
            clear()

        # Print error messages.                  
        except(ValueError, FileNotFoundError, PermissionError, TypeError) as err:
            print(type(err).__name__, err, sep=": ")

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Bind the activate_next function to the activate_next button so
    # that the activate_next function will be called when the
    # user clicks the activate_next button.
    btn_next.config(command=activate_next)

    # Give the keyboard focus to the folder entry box.
    ent_folder.focus()

def create_append_file(filename, column_headers, new_dict, checkline):
    """Depending on the return bool from the check_line function,
    this either appends user input to the end of a file or creates
    a new file before appending a header AND then user input

    Parameters:
        filename: the name of the file to create or append to
        column_headers: a list of the headers to append to the file
            if a new file is created.
        new_dict: a dictionary containing column headers as keys and the
            associated user input as the value attached.
        checkline: a boolean that if True means that a new file is not created
            and user input is simply appended to an existing file that has headers.
            if False means that a new file is created in which column headers are
            appended FIRST, and then user input is appended.

    Return:
        nothing
    """
    # If the checkline parameter returns True, do the following:
    if  checkline:

        # Open the file for appending.
        with open(filename, "a", newline="") as file:

            # Pass the file object and a list
            # of column names to DictWriter()
            # You will get a object of DictWriter
            dictwriter_object = DictWriter(file, fieldnames=column_headers)
                
            # Pass the dictionary as an argument to the Writerow()
            dictwriter_object.writerow(new_dict)

    # If the checkline parameter returns False, do the following:
    else:

        # Open a file for appending. It will wipe the file and 
        # write a header in.
        with open(filename, "w", newline="") as file:

            # Pass the file object and a list
            # of column names to DictWriter()
            # You will get a object of DictWriter
            dictwriter_object = DictWriter(file, fieldnames=column_headers)

            # Write the column headers to the file
            dictwriter_object.writeheader()
                
            # Pass the dictionary as an argument to the Writerow()
            dictwriter_object.writerow(new_dict)

def check_line(filename, column_headers):
    """Checks if a file exists. If the file exists, check if
    it has the appropriate column headers.

    Parameters:
        filename: the name of the file you want to check.
        column_headers: a list containing the column headers you
            wish to compare to what is in filename.
    
    Return:
        if file does not exist "False".
        if file header does not compare to column_headers "False"
        if file exists and file header is same as column_headers "True"

    """
    try:
        # Open a file and attempt to read from it.
        with open(filename, "r") as file:  
            reader = csv.reader(file)

            # Store the first line of "reader" as a list in "line".
            line = next (reader)

            # Compares the list in "line" to the list in
            # column_headers.
            if line == column_headers:
                return True
            else:
                return False

    except(FileNotFoundError, PermissionError):
        return False

def get_date(date_seperator):
        """Gets the present date.
        Takes a string.

        Parameters:
            date_seperator: input a sign e.g. "-", "/", ":", ",". Determines what you want 
            the date seperator to be.

        Return:
            the date string in either of these formats: Tues-10-Jan-2022, Tues/10/Jan/2022,
            Tues:10:Jan:2022, Tues,10,Jan,2022 etc.
        """
        # Get current date and time.
        date_time = datetime.now()

        # Get the date parameters you want to use.
        date = date_time.strftime(f"%a{date_seperator}%d{date_seperator}%b{date_seperator}%Y")

        # Convert the date object to a string.
        date_str = f"{date}"

        return date_str    

# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
