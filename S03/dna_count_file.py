# para importar funciones de otros archivos:
from dna_count_otra_version import count_bases


lines = ["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]

# option 1
f = open("dna.txt", "r")
lines = f.readlines()
f.close()

# option 2
with open("dna.txt", "r") as f: # esto es lo mismo que las tres líneas anteriores
    lines = f.readlines()

# actual code
total_number = 0
bases = {"A":0, "C":0, "T":0, "G":0}

for sequence in lines:
    sequence = sequence.strip() # this function remove spaces and newline characters at the end of the string (esta la ponemos si abrimos el archivo txt)
    total_number += len(sequence)
    result = count_bases(sequence) # esto es cuando se importa la función del otro archivo
    for key in result:
        bases[key] += result[key]

    #for base in sequence: # esto cuando no se importa la función
        #if base in bases:
            #bases[base] += 1

print("Total number of bases:", total_number)

for base, count in bases.items():
    print(f' {base}: {count}')
