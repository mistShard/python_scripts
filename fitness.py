from datetime import datetime

def main():
    gender = input("Gender (M or F): ")
    birthdate = input("Birthdate (YYYY-MM-DD): ")
    weight = float(input("Weight(US Pounds): "))
    height = float(input("Height (US Inches): "))
    age = compute_age(birthdate)
    weight_kg = lbs_kg(weight)
    height_cm = in_cm(height)
    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(weight_kg, height_cm, gender, age)
    print(f"""Age (years): {age}
Weight (kg): {weight_kg:.2f}
Height (cm): {height_cm:.1f}
Body mass index: {bmi:.1f}
Basal Metabolic rate (kcal/day): {round(bmr)}""")



def lbs_kg(weight_in_lbs):
    kg = weight_in_lbs * 0.453592737
    return kg

def in_cm(height_in_inches):
    cm = height_in_inches * 2.54
    return cm

def body_mass_index(weight_kg, height_cm):
    bmi = 10 ** 4 * weight_kg / height_cm ** 2
    return bmi

def basal_metabolic_rate(weight_kg, height_cm, gender, age):
    if gender.lower() == "male" or gender.lower() == "m":
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) + (4.330 * age)
    elif gender.lower() == "female" or gender.lower() == "f":
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    return bmr

def compute_age(birthdate):
    today = datetime.now()
    birth_year = datetime.strptime(birthdate, "%Y-%m-%d")
    years = today.year - birth_year.year
    if birth_year.month > today.month or (birth_year.month == today.month and \
        birth_year.day > today.day):
        years -= 1
    return years

if __name__ == "__main__":
    main()