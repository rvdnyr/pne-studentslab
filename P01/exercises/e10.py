# EXERCISE 10
# Write a Python program that automatically calculates the answer to this question:
# Which is the most frequent base in each gene?

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

    def read_fasta(self, filename):
        lines = filename.split('\n')
        sequence = ""
        for line in lines:
            if not line.startswith('>'):
                sequence += line.strip()
        return sequence


from pathlib import Path
files = ["../sequences/U5.txt", "../sequences/ADA.txt", "../sequences/FRAT1.txt", "../sequences/FXN.txt"]
gene_names = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 10 |------")

for i in range(len(gene_names)):
    content = Path(files[i]).read_text() # 1º read the file
    raw_sequence = Seq().read_fasta(content) # 2º read_fasta method
    seq_obj = Seq(raw_sequence) # 3º clean sequence
    counts = seq_obj.count() # 4º count bases
    most_frequent = max(counts, key=counts.get) # 5º most frequent base
    print(f"Gene {gene_names[i]}: Most frequent Base: {most_frequent}")
