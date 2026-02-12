# teacher's code
def count_bases(sequence):
    bases = {"A": 0, "C": 0, "T": 0, "G": 0}

    for base in sequence:
        if base in bases:
            bases[base] += 1

    return bases


if __name__ == "__main__":
    dna = input("Enter a DNA sequence:").upper()
    print("The length of the DNA sequence is:", len(dna))

    bases = count_bases(dna)

    print("NUmber of bases of:")
    for base, count in bases.items():
        print(f' {base}: {count}')