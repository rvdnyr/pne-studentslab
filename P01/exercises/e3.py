# EXERCISE 3
# Write a Python program that creates three sequences: one null, one valid, and one that is invalid, and then prints the objects.

class Seq():
    def __init__(self, strbases=None):
        self.strbases = strbases
        if strbases is not None:
            is_valid = False
            for i in strbases:
                if i in ["A", "C", "G", "T"]:
                    is_valid = True
                else:
                    is_valid = False
            if is_valid:
                print("New sequence created!")
            else:
                print("INVALID sequence")
        else:
            print("NULL sequence created")

    def __str__(self):
        if self.strbases is None:
            return "NULL"
        else:
            is_valid = False
            for i in self.strbases:
                if i in ["A", "C", "G", "T"]:
                    is_valid = True
                else:
                    is_valid = False
            if is_valid:
                return self.strbases
            else:
                return "ERROR"


print("-----| Practice 1, Exercise 3 |------")

# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
print(f"Sequence 3: {s3}")
