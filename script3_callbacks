import math

def cook(scriptOP):
    dna_table = op('table_nucleotides')  # Reference to DNA Table DAT
    text_holder = op('text_holder')  # Reference to a Text DAT (for passing text)

    scriptOP.clear()  # Clear existing geometry
    text_holder.clear()  # Clear previous text

    # Get the number of codons (each codon consists of 3 nucleotides)
    num_codons = dna_table.numRows // 3

    # Dictionary mapping RNA codons to amino acids
    codon_map = {
        "UUU": "Phe", "UUC": "Phe",
        "UUA": "Leu", "UUG": "Leu",
        "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
        "UAU": "Tyr", "UAC": "Tyr",
        "UGU": "Cys", "UGC": "Cys",
        "UGG": "Trp",
        "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
        "CAU": "His", "CAC": "His",
        "CAA": "Gln", "CAG": "Gln",
        "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
        "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
        "AUG": "Met (Start)",  # Start codon
        "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
        "AAU": "Asn", "AAC": "Asn",
        "AAA": "Lys", "AAG": "Lys",
        "AGU": "Ser", "AGC": "Ser",
        "AGA": "Arg", "AGG": "Arg",
        "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
        "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
        "GAU": "Asp", "GAC": "Asp",
        "GAA": "Glu", "GAG": "Glu",
        "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
        "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"  # Stop codons
    }

# Generate the multi-line text for the Text SOP
text_output = []

for row in range(num_codons):
    codon = ""
    for col in range(3):  # Read three nucleotides at a time
        nucleotide_index = row * 3 + col
        if nucleotide_index < dna_table.numRows:
            dna_nucleotide = dna_table[nucleotide_index, 0].val
            rna_nucleotide = "U" if dna_nucleotide == "T" else dna_nucleotide  # Convert T to U
            codon += rna_nucleotide  # Concatenate codon sequence

    # Get the corresponding amino acid
    amino_acid = codon_map.get(codon, "").strip()  # Strip spaces

    if amino_acid:  # Only add non-empty values
        text_output.append(amino_acid)

# Write the cleaned text to the Text DAT
text_holder.write("\n".join(text_output))
