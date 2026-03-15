# EXERCISE 4
# Write a python program that sends the U5, FRAT1 and ADA genes to the Teacher's server (one at a time)
# It should initially send the message: "Sending the U5 Gene to the server..." and then the gene itself
# Use the class Seq that we have previously developed to load the genes into the program
# Given an object of type Seq, s, you can obtain its sequence as a string just by calling its str(s) method

from Client0 import Client
from Client0 import Seq
from pathlib import Path

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.82"
PORT = 8081

c = Client(IP, PORT)


files = ["../sequences/U5.txt", "../sequences/FRAT1.txt", "../sequences/ADA.txt"]
gene_names = ["U5", "FRAT1", "ADA"]

for i in range(len(gene_names)):
    s = Seq()
    content = Path(files[i]).read_text()
    raw_sequence = s.read_fasta(content)
    seq_obj = Seq(raw_sequence)

    start_message = c.talk(f"Sending the {i} Gene to the server...")
    response = c.talk(str(s))
    print(start_message)
    print(response)
