from Seq0 import seq_read_fasta
from Seq0 import seq_count_base

from pathlib import Path
U5 = ("../sequences/U5.txt")
u5 = Path(U5).read_text()
ADA = ("../sequences/ADA.txt")
ada = Path(ADA).read_text()
FRAT1 = ("../sequences/FRAT1.txt")
frat1 = Path(FRAT1).read_text()
FXN = ("../sequences/FXN.txt")
fxn = Path(FXN).read_text()

genes = [u5, ada, frat1, fxn]
gene_names = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "T", "G"]

print("-----| Exercise 8 |------")
for i in range(len(gene_names)):
    sequence = seq_read_fasta(genes[i])
    counts = {}
    for base in bases:
        counts[base] = seq_count_base(sequence, base)
    most_frequent = max(counts, key=counts.get)
    print(f"Gene {gene_names[i]}: Most frequent Base: {most_frequent}")
