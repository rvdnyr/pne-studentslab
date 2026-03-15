from Seq0 import seq_read_fasta
from Seq0 import seq_reverse

from pathlib import Path
U5 = ("../sequences/U5.txt")
u5 = Path(U5).read_text()

sequence = seq_read_fasta(u5)
print("-----| Exercise 6 |------")
print("Gene U5")
print("Fragment:", sequence[:20])
print("Reverse:", seq_reverse(sequence, 19))
