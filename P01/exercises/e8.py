# EXERCISE 8
# Write a Python program that creates three sequences: one null, one valid, and one invalid, and then prints their lengths, sequences, the dictionary with the bases, the reverse sequence, and the complement.

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

    def reverse(self):
        if self.strbases is None:
            return "NULL"
        else:
            base = ["A", "C", "G", "T"]
            for i in self.strbases:
                if i in base:
                    self.valid = True
                else:
                    self.valid = False
            if not self.valid:
                return "ERROR"
            else:
                return self.strbases[::-1]

    def complement(self):
        if self.strbases is None:
            return "NULL"
        else:
            base = ["A", "C", "G", "T"]
            for i in self.strbases:
                if i in base:
                    self.valid = True
                else:
                    self.valid = False
            if not self.valid:
                return "ERROR"
            else:
                comp_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
                comp_str = ""
                for base in self.strbases:
                    comp_str += comp_dict[base]
                return comp_str


print("-----| Practice 1, Exercise 8 |------")

# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {len(s1)}) {s1}")
print(f" Bases: {s1.count()}")
print(f" Rev: {s1.reverse()}")
print(f" Comp: {s1.complement()}")
print(f"Sequence 2: (Length: {len(s2)}) {s2}")
print(f" Bases: {s2.count()}")
print(f" Rev: {s2.reverse()}")
print(f" Comp: {s2.complement()}")
print(f"Sequence 3: (Length: {len(s3)}) {s3}")
print(f" Bases: {s3.count()}")
print(f" Rev: {s3.reverse()}")
print(f" Comp: {s3.complement()}")
