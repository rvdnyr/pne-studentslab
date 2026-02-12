# EXERCISE 8: COMBINING EVERYTHING

# Write a program that processes a list of students. Each student is represented as a dictionary:

students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]

# Write the following functions:
# average(grades): receives a list of grades and returns the average
# get_status(avg): receives an average and returns "PASS" if >= 5.0 or "FAIL" otherwise
# Then, for each student, print their name, average (rounded to 1 decimal), and status.
# At the end, print how many students passed and how many failed.


def averages(grades):
    total = 0
    for i in grades:
        total += i
    return round((total / len(grades)), 1)

def get_status(avg):
    if avg >= 5:
        return "PASS"
    else:
        return "FAIL"


passed = 0
failed = 0

for student in students:
    print("Name:", student["name"])
    print("Average:", averages(student["grades"]))
    print("Status:", get_status(averages(student["grades"])))
    print(" ")

    if "PASS" in get_status(averages(student["grades"])):
        passed += 1
    else:
        failed += 1

print("Results:", passed, "passed,", failed, "failed.")
