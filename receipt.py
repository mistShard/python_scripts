import csv
from datetime import datetime

def main():
    PRODUCT_KEY_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    REQUESTED_QUANTITY_INDEX = 1

    filename = "request.csv"
    products_dict = read_dict("products.csv", 0)
    number_of_items = 0
    subtotal = 0
    tax = 0.06

    try:
        print(f"The Real Grocer\n")

        with open(filename, "rt") as request_csv:
            reader = csv.reader(request_csv)
            next(reader)

            for line in reader:
                requested_quantity = int(line[REQUESTED_QUANTITY_INDEX])
                # Gets the key from the first index
                product_key = line[PRODUCT_KEY_INDEX]
                # Uses the key to find the values of the product in the products_dict dictionary
                item = products_dict[product_key]
                # Gets the product name from the values returned in item
                product_name = item[PRODUCT_NAME_INDEX]
                # Computes the number of products multiplied by their cost
                product_price = float(item[PRODUCT_PRICE_INDEX]) * requested_quantity

                print(f"{product_name}: {requested_quantity} @ {product_price}")

                # Adds each products total price to a total_cost variable
                subtotal += product_price
                # Sums the number of items
                number_of_items += requested_quantity
        
        print_statements(number_of_items, subtotal, tax)

    except KeyError as key_err:
        print()
        print(type(key_err).__name__, f"unknown product ID in the {filename}, {key_err}", sep=': ')
    except FileNotFoundError as file_err:
        print()
        print(type(file_err).__name__, "missing file", sep=": ")
        print(file_err)
    except PermissionError as perm_err:
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read {filename}.")
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    product_dict = {}
    
    with open(filename, "rt") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for line in reader:
            product_dict[line[key_column_index]] = line

    return product_dict

def print_statements(number_of_items, subtotal, tax):
    """Print the number of items, Subtotal, Sales Tax, Total,
    date, time, and discount (if applicable).

    Parameters:
        number_of_items: the number of items in the request file.
        subtotal: the total cost of items before tax and discount
            are applied.
        tax: the applicable tax rate.
    """
    print()
    print(f"Number of Items: {number_of_items}")
    print(f"Subtotal: {subtotal:.2f}")

    sales_tax = subtotal * tax

    print(f"Sales Tax: {sales_tax:.2f}")

    total = sales_tax + subtotal

    date_time = datetime.now()
    date = date_time.strftime("%a %b %d %I:%M:%S %Y")
    hour = int(date_time.strftime("%I"))
    format = date_time.strftime("%p")
    
    # Checks if the time is before 11AM.
    # If it is, print the discount amount and apply the discount to the total.
    if  hour < 11 and format == "AM":
        discount = 0.10 * total
        total -= discount
        print(f"Discount: {discount:.2f}")

    print(f"Total: {total:.2f}\n")  
    print("Thank you for shopping at The Real Grocer.")
    print(date)

if __name__ == "__main__":
    main()
