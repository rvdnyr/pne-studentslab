# FUNCTIONS | main

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    contents = filename.split("1\n")
    body = contents[1]
    body_joined = body.replace("\n", "")
    return body_joined

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    return {
        'A' : seq.count("A"),
        'T' : seq.count("T"),
        'C': seq.count("C"),
        'G': seq.count("G"),
    }

def seq_reverse(seq, n):
    return seq[n :: -1]

def seq_complement(seq):
    complement_bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement_seq = ""
    for i in seq:
        if i in complement_bases:
            complement_seq += complement_bases[i]
    return complement_seq
