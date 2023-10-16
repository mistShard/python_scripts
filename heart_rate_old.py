"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

age = int(input("Please enter your age: "))
def heart_rate(age):
    
    max = 220 - age
    ceiling = 85 / 100 * max
    floor = 65 / 100 * max
    print(f"When you exercise to strengthen your heart, you should keep your \
heart rate between {int(floor)} and {int(ceiling)} beats per minute")

heart_rate(age)