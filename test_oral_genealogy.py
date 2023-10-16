from csv import DictWriter
from oral_genealogy import get_date, check_line
import pytest

def test_get_date():
    # Call the function with the " " seperator
    # and store its results.
    date = get_date(" ")

    # Check the result is a string.
    assert isinstance(date, str)

    # Check that the length of the result is correct.
    assert len(date) == len("sun dec 03 2032")

    # Check that the seperator " " is found in the date.
    assert " " in date

    # Call the function with the "," seperator
    # and store its results.
    date = get_date(",")

    # Check the result is a string.
    assert isinstance(date, str)

    # Check that the length of the result is correct
    assert len(date) == len("sun,dec,03,2032")

    # Check that the seperator " " is found in the date
    assert "," in date

headers = ["Name", "Age", "Country"]
new_dict = {"Name": "Benji", "Age":"22", "Country": "Nigeria"}

def test_check_line():

    # Call the check_line function and store return in a variable
    check = check_line(filename="Benji_test.csv", column_headers=headers)

    # Check the returned value is a boolean.
    assert isinstance(check, bool)

    # Check that the returned value is the boolean "False"
    assert check is False

    with open("Benji_test2.csv", "wt", newline="") as file:
            # Pass the file object and a list
            # of column names to DictWriter()
            # You will get a object of DictWriter
            dictwriter_object = DictWriter(file, fieldnames=headers)

            # Write the column headers to the file
            dictwriter_object.writeheader()
                
            # Pass the dictionary as an argument to the Writerow()
            dictwriter_object.writerow(new_dict)

    # Call the check_line function and store return in a variable
    check = check_line(filename="Benji_test2.csv", column_headers=headers)
 
    # Check the returned value is a boolean.
    assert isinstance(check, bool)

    # Check that the returned value is the boolean "False"
    assert check is True


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])


