# EXERCISE 9
# Write a Python program that reads a sequence from the U5.txt file.
# Then the program should print the length of the sequence, the sequence itself, the dictionary with the bases, the reverse sequence and the complement.

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

    def read_fasta(self, filename):
        lines = filename.split('\n')
        sequence = ""
        for line in lines:
            if not line.startswith('>'):
                sequence += line.strip()
        return sequence


print("-----| Practice 1, Exercise 9 |------")

from pathlib import Path
U5 = ("../sequences/U5.txt")
u5 = Path(U5).read_text()

# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
seq = s.read_fasta(u5)

sequence = Seq(seq)

print(f"Sequence: (Length: {len(sequence)}) {sequence}")
print(f" Bases: {sequence.count()}")
print(f" Rev: {sequence.reverse()}")
print(f" Comp: {sequence.complement()}")
