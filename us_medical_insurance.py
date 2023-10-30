# The goal of this project is to study the data provided in file
# Some of the data needed analysis are
# the average age of the patients
# where are most of the data from
# oldest vs youngest in file, which has the highest cost
# most number of age smokers
# average age of overweight based on bmi
# insurance cost of smoker vs non-smokers
# average insurance cost of overweight
# average age for someone who has atleast one child
import csv
from collections import Counter
# create a dict for the csv file
medical_insurance = {}

# open and read the file

with open("insurance.csv", mode='r') as medical_insurance_data:
    insurance_data = csv.DictReader(medical_insurance_data)
    for rows in insurance_data:
        for key, value in rows.items():
            medical_insurance.setdefault(key, []).append(value)
#print(medical_insurance)

# get the average, youngest, oldest age in the data
def calculate_average_age(medical_insurance):
    # Extracting the ages from the data dictionary
    ages = [int(age) for age in medical_insurance['age']]

    # Calculating the average age
    if len(ages) > 0:
        average_age = sum(ages) / len(ages)
        return average_age
    else:
        return 0
    
def find_youngest_and_oldest(medical_insurance):
    # Extracting the ages from the data dictionary
    ages = [int(age) for age in medical_insurance['age']]

    # Finding the youngest and oldest individuals
    youngest = min(ages)
    oldest = max(ages)

    return youngest, oldest

average_age = calculate_average_age(medical_insurance)
youngest, oldest = find_youngest_and_oldest(medical_insurance)

print(f"The average age on the data is {average_age: .2f} years old, while the youngest registered is {youngest} and the oldest is {oldest}.")

# find out what region is the most number of participants in the data
def get_most_participants(medical_insurance):

    region_counts = Counter(medical_insurance['region'])

    # find the highest ocuurence
    max_region_count = max(region_counts.values())

    # finding the most region counts
    region_with_max_counts = [region for region, count in region_counts.items() if count == max_region_count]
    return region_with_max_counts, max_region_count

region_with_max_counts, max_region_count = get_most_participants(medical_insurance)

print(f"The region with the highest count is {','.join(region_with_max_counts)} with a total of {max_region_count} counts.")

# find the age of most number of smokers
def most_smokers(medical_insurance):
    # get ages os smokers
    smoker_ages = [int(medical_insurance['age'][i]) for i in range(len(medical_insurance['smoker'])) if medical_insurance['smoker'][i] == 'yes']
    age_counts = Counter(smoker_ages)

    age_count = max(age_counts.values())

    # finding the age with highest occurence of smoker 
    most_smoker_age = age_counts.most_common(2)[0][0]

    return age_count, most_smoker_age

age_count, most_smoker_age = most_smokers(medical_insurance)

print(f"The number of the most age of smoker are {age_count} and with the age of {most_smoker_age} years old. ")

# get the average of age overweight people
overweight_age = [int(medical_insurance['age'][i]) for i in range(len(medical_insurance['bmi'])) if float(medical_insurance['bmi'][i]) > 25]
overweight_count = Counter(overweight_age)
overweight_average_age = sum(overweight_age) / len(overweight_age)
overweight_smokers = [medical_insurance['smoker'][i] for i in range(len(medical_insurance['bmi'])) if float(medical_insurance['bmi'][i]) > 25]
#print(overweight_smokers)
print(f"Average of People start to become overweight is {overweight_average_age: .2f} years old.")

# average of someone who has atleast one child
age_with_child = [int(medical_insurance['age'][i]) for i in range(len(medical_insurance['children'])) if int(medical_insurance['children'][i]) >= 1]

average_age_with_child = sum(age_with_child) / len(age_with_child)
print(f"The average age of someone who has atleast one child is {average_age_with_child: .2f} years old.")

# average insurance cost of smokers and non-smokers

# for smokers
insurance_charge_smokers = [float(medical_insurance['charges'][i]) for i in range(len(medical_insurance['smoker'])) if medical_insurance['smoker'][i] == 'yes']

average_charge_smokers = sum(insurance_charge_smokers) / len(insurance_charge_smokers)

# for non-smokers
insurance_charge_non_smokers = [float(medical_insurance['charges'][i]) for i in range(len(medical_insurance['smoker'])) if medical_insurance['smoker'][i] == 'no']
average_charge_non_smokers = sum(insurance_charge_non_smokers) / len(insurance_charge_non_smokers)

if average_charge_smokers > average_charge_non_smokers:

    print(f"Smokers has a hihger charge of insurance cost \nwith an average of {average_charge_smokers: .2f} while non_smokers has only an average charge of {average_charge_non_smokers: .2f}")
else:
    print(f"Non-Smokers has a hihger charge of insurance cost \nwith an average of {average_charge_non_smokers: .2f} while smokers has average charge of {average_charge_smokers: .2f}")

# Charge for overweight and fit people based on bmi
charges_overweight = [float(medical_insurance['charges'][i]) for i in range(len(medical_insurance['bmi'])) if float(medical_insurance['bmi'][i]) > 25]
average_charge_overweight = sum(charges_overweight) / len(charges_overweight)

charges_normal = [float(medical_insurance['age'][i]) for i in range(len(medical_insurance['bmi'])) if float(medical_insurance['bmi'][i]) <= 25]
average_charge_normal = sum(charges_normal) / len(charges_normal)

if average_charge_overweight > average_charge_normal:
    print(f"Overweight people has a higher charges for insurance \nwith an average of {average_charge_overweight: .2f} compare to normal people that has an \naverage {average_charge_normal: .2f} of charge based on the data.")
elif average_charge_overweight < average_charge_normal:
    print(f"Normal people has a higher charges for insurance \nwith an average of {average_charge_normal: .2f} compare to normal overweight people that has an \naverage {average_charge_overweight: .2f} of charge, based on the data.")
else:
    print("They have equal average charge, wether you're obesse or not.")