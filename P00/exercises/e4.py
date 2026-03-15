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

print("-----| Exercise 4 |------")
for i in range(len(gene_names)):
    print(f"Gene {gene_names[i]}:")
    sequence = seq_read_fasta(genes[i])
    for i in bases:
        print(f" {i}: {seq_count_base(sequence, i)}")
    print("\n")
