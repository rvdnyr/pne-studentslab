from Seq0 import seq_read_fasta
from Seq0 import seq_complement

from pathlib import Path
U5 = ("../sequences/U5.txt")
u5 = Path(U5).read_text()

sequence = seq_read_fasta(u5)
fragment = sequence[:20]
print("-----| Exercise 7 |------")
print("Gene U5")
print("Frag:", fragment)
print("Comp:", seq_complement(fragment))
