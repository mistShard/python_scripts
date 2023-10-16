import tkinter as tk
import number_entry as nent
import csv
from csv import DictWriter
from datetime import datetime

company = "Lasalu Limited"
company_num = "NG76"
subscript = "Copyright 2022, Broadside Technology Inc. All rights reserved."
def get_date():
        """Gets the present date.

        Return:
            The date string in this format: Tues-10-Jan-2022
        """
        date_time = datetime.now()
        date =date_time.strftime("%a-%d-%b-%Y")
        date_str = f"{date}"
        return date_str

date = get_date()
filename = "Folder Inventory " + date

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
    lbl_err = tk.Label(frm_main, text="Errors:", font=("Times New Roman", 12), wraplength=500)
    lbl_subscript = tk.Label(frm_main, text=subscript)

    # Create five string entry boxes where the user will enter the informant, 
    # field agent, field manager, data entry clerk, and data entry manager's names.
    ent_informant = tk.Entry(frm_main, width=50)
    ent_fieldAgent = tk.Entry(frm_main, width=50)
    ent_fieldManager = tk.Entry(frm_main, width=50)
    ent_dataClerk = tk.Entry(frm_main, width=50)
    ent_dataManager = tk.Entry(frm_main, width=50)
    ent_nameCount = nent.IntEntry(frm_main, 10, 10**4, width=25)
    ent_err = tk.Entry(frm_main,)

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear", width=25, height=3)

    # Create the next button
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
    lbl_err.grid(row=4, column=3, padx=(30, 0))
    btn_next.grid( row=5, column=5, padx=3, pady=50, columnspan=5)
    btn_clear.grid(row=5, column=0, padx=(60, 3), pady=50, columnspan=5, sticky="w")
    lbl_subscript.grid( row=5, column=3, padx=3, pady=3)

    def get_input(event):
        """Collect the inputs from the GUI fields
        """
        try:
            # Get the user's input.
            folder = ent_folder.get()
            assert len(folder) >= 15
            informant = ent_informant.get()
            field_agent = ent_fieldAgent.get()
            field_manager = ent_fieldManager.get()
            clerk = ent_dataClerk.get()
            data_manager = ent_dataManager.get()
            name_count = ent_nameCount.get()

        except AssertionError as err:
            # When the program throughs any of the errors excepted,
            # show the error to the user.
            lbl_err.config(text=f"{type(err).__name__}: {err}")

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
    # user presses the "Next" button.
    def next():
        """Save the contents of all the fields in a csv
        file."""
        date = get_date()
        filename = "Folder Inventory " + date 
        try:
            # Get the user's input.
            folder = ent_folder.get()
            informant = ent_informant.get()
            assert len(folder and informant) > 0
            field_agent = ent_fieldAgent.get()
            field_manager = ent_fieldManager.get()
            clerk = ent_dataClerk.get()
            data_manager = ent_dataManager.get()
            name_count = ent_nameCount.get()

            # Stores the column headers for the dictionary in
            # a list.
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
                    with open(filename, "rt") as file:            
                        if isinstance(file.readline(), str):
                            return True
                        else:
                            return False

                except (FileNotFoundError, PermissionError):
                    return False

            check_line_ = check_line()

            create_append_file(check_line_)

            clear()

        except(ValueError, FileNotFoundError, PermissionError, AssertionError) as err:
            print(type(err).__name__, err, sep=": ")

        def create_append_file(check_line_):
            if check_line_ == False:
                with open(filename, "w", newline="") as file:
                # Pass the file object and a list
                # of column names to DictWriter()
                # You will get a object of DictWriter
                    dictwriter_object = DictWriter(file, fieldnames=column_headers)

                    dictwriter_object.writeheader()
                            
                    # Pass the dictionary as an argument to the Writerow()
                    dictwriter_object.writerow(new_dict)

            else:
                with open(filename, "a", newline="") as file:
                # Pass the file object and a list
                # of column names to DictWriter()
                # You will get a object of DictWriter
                    dictwriter_object = DictWriter(file, fieldnames=column_headers)

                    # Pass the dictionary as an argument to the Writerow()
                    dictwriter_object.writerow(new_dict)

    # Bind the get_input function to the age entry box
    # so that the get_input function will be called when
    # the user changes the text in the entry box.
    ent_folder.bind("<KeyRelease>", get_input)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Bind the next function to the next button so
    # that the next function will be called when the
    # user clicks the next button.
    btn_next.config(command=next)

    # Give the keyboard focus to the folder entry box.
    ent_folder.focus()

# If this file is executed like this:
# > python oral_geneology.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.

if __name__ == "__main__":
    main()
