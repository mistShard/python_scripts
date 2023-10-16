import csv

def main():
    I_NUMBER = input("What is the student I-Number: ")
    with open("students.csv", "rt") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        student_dict = read_dict(reader, I_NUMBER)

def read_dict(filename, KEY_COLUMN_INDEX):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        KEY_COLUMN_INDEX: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    student_dict = {}
    for key, value in filename:
        student_dict[key] = value

    if KEY_COLUMN_INDEX in student_dict:
        value = student_dict.get(KEY_COLUMN_INDEX)
        print(value)
    else:
        print("No such student")

if __name__ == "__main__":
    main()