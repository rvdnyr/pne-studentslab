# EXERCISE 7: DICTIONARIES

# Create a dictionary called student with the following keys and values:

student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

# Write a program that prints:
# The student's name
# The number of subjects they are enrolled in
# Whether "PNE" is in their subjects list
# Their grade in Databases
# Their average grade across all subjects (rounded to 2 decimals)
# All subject-grade pairs, one per line


def get_info(dictionary):
    return dictionary

def subject_enrolled(dictionary):
    return len(dictionary)

def subject_listed(subject, list):
    return subject in list

def average_grade(subjects):
    avg = round((sum(subjects) / len(subjects)), 2)
    return avg

def subject_grade(student):
    for key in student["grades"]:
        grade = student["grades"][key]
        print("  " + key + ": " + str(grade))

    #for subject, grade in student["grades"].items(): # otra forma de hacerlo (más fácil)
        #print("  " + subject + ": " + str(grade))

print("Name:", get_info(student["name"]))
print("Number of subjects:", subject_enrolled(student["subjects"]))
print("Enrolled in PNE:", subject_listed("PNE", student["subjects"]))
print("Databases grade:", get_info(student["grades"]["Databases"]))
print("Average grade:", average_grade(student["grades"].values()))
print("Subject grades:")
subject_grade(student)
