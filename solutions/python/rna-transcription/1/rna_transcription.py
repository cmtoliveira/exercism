def to_rna(dna_strand):
    rna = ""
    for nuc in dna_strand:
        if nuc == "A":
            rna += "U"
        if nuc == "C":
            rna += "G"
        if nuc == "G":
            rna += "C"
        if nuc == "T":
            rna += "A"
    return rna
            
