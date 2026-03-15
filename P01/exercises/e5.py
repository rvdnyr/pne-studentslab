# EXERCISE 5
# Write a Python program that creates three sequences: one null, one valid, and one invalid, and then prints their lengths, sequences and the number of bases on the console.

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

    def __len__(self):
        if self.strbases is None:
            return 0
        else:
            is_valid = False
            for i in self.strbases:
                if i in ["A", "C", "G", "T"]:
                    is_valid = True
                else:
                    is_valid = False
            if is_valid:
                self.valid = True
                return len(self.strbases)
            else:
                self.valid = False
                return 0

def count_base(self,base):
    if self.strbases is None or not self.valid:
        return 0
    return self.strbases.count(base)


print("-----| Practice 1, Exercise 5 |------")

# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {len(s1)}) {s1}")
print(f" A: {count_base(s1, "A")}, C: {count_base(s1, "C")}, G: {count_base(s1, "G")}, T: {count_base(s1, "T")}")
print(f"Sequence 2: (Length: {len(s2)}) {s2}")
print(f" A: {count_base(s2, "A")}, C: {count_base(s2, "C")}, G: {count_base(s2, "G")}, T: {count_base(s2, "T")}")
print(f"Sequence 3: (Length: {len(s3)}) {s3}")
print(f" A: {count_base(s3, "A")}, C: {count_base(s3, "C")}, G: {count_base(s3, "G")}, T: {count_base(s3, "T")}")
