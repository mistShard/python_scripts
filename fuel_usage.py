from tracemalloc import start


def main():
    starting_odometer_value = float(input("Starting odometer value: "))
    ending_odometer_value = float(input("Ending odometer value: "))
    fuel_in_gallons = float(input("Amount of fuel(gallons): "))
    mpg = miles_per_gallon(starting_odometer_value, ending_odometer_value, fuel_in_gallons)
    lp100k = lp100k_from_mpg(mpg)
    print(f"""{mpg:.1f} miles per gallon
{lp100k:.2f} litres per 100 kilometers""")
    

def miles_per_gallon(start_value, end_value, gallons):
    miles_per_gallon = (end_value - start_value) / gallons
    return miles_per_gallon

def lp100k_from_mpg(miles_per_gallon):
    lp100k = 235.215 / miles_per_gallon
    return lp100k

main()
