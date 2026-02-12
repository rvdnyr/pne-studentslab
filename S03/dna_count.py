# my code
dna = input("Enter a DNA sequence:").upper()

a = 0
c = 0
t = 0
g = 0

for base in dna:
    if base == "A":
        a += 1
    elif base == "C":
        c += 1
    elif base == "T":
        t += 1
    elif base == "G":
        g += 1

print("The length of the DNA sequence is:", len(dna))
print("NUmber of bases of:")
print("A:", a)
print("C", c)
print("T", t)
print("G", g)



# teacher's code
def count_bases(sequence):
    bases = {"A": 0, "C": 0, "T": 0, "G": 0}  # creamos diccionario

    for base in sequence:
        if base in bases:
            bases[base] += 1

    return bases

dna = input("Enter a DNA sequence:").upper()
bases = count_bases(dna)

print("The length of the DNA sequence is:", len(dna))
print("NUmber of bases of:")
for base, count in bases.items():
    print(f' {base}: {count}')





# solo ejecuta lo que escribas aquí o no se que poias:

def main(): # creas la función con lo que quieras meter
    return

if __name__ == "__main__":
    main() # llamas a la función
