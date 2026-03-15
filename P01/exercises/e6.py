# EXERCISE 6
# Write a Python program that creates three sequences: one null, one valid, and one that is invalid, and then prints their lengths, sequences and the dictionary returned by the count() method.

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
                return len(self.strbases)
            else:
                return 0

    def count(self):
        base = ["A", "C", "G", "T"]
        if self.strbases is None:
            return {"A": 0, "C": 0, "G": 0, "T": 0}
        else:
            is_valid = False
            for i in self.strbases:
                if i in base:
                    is_valid = True
                else:
                    is_valid = False
            if is_valid:
                a = self.strbases.count("A")
                c = self.strbases.count("C")
                g = self.strbases.count("G")
                t = self.strbases.count("T")
                return {"A": a, "C": c, "G": g, "T": t}
            else:
                return {"A": 0, "C": 0, "G": 0, "T": 0}


print("-----| Practice 1, Exercise 6 |------")

# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {len(s1)}) {s1}")
print(f" Bases: {s1.count()}")
print(f"Sequence 2: (Length: {len(s2)}) {s2}")
print(f" Bases: {s2.count()}")
print(f"Sequence 3: (Length: {len(s3)}) {s3}")
print(f" Bases: {s3.count()}")
