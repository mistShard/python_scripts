import math
from datetime import datetime

current_date = datetime.now()
date = current_date.strftime("%Y-%m-%d")

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

def tire_volume(w, a, d):
    top = math.pi * w ** 2 * a * (w * a + 2540 * d)
    bottom = 10 ** 10
    v = top / bottom
    print(f"The approximate volume is {v:.2f} liters")

    with open("volume.txt", "at") as volumes_file:
        print(f"{date}, {w}, {a}, {d}, {v:.2f}", file=volumes_file)

    query = input("Would you like to buy a tire with the above dimesions?(yes/no) ")
    if query.lower() == "yes":
        phone_number = input("Please enter your Phone Number: ")
        with open("volume.txt", "at") as volumes_file:
            print(f"Phone number: {phone_number}", file=volumes_file)


tire_volume(w, a, d)


