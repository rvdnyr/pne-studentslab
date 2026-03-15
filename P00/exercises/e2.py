from Seq0 import seq_read_fasta

from pathlib import Path
FILENAME = ("../sequences/U5.txt")
u5 = Path(FILENAME).read_text()

print("-----| Exercise 2 |------")
body_joined = seq_read_fasta(u5)
FILENAME = input("Enter a filename: ")
print("DNA file:", FILENAME)
print("The first 20 bases are:", body_joined[0:21])
