# me - this DAT.
#
# dat - the changed DAT
# rows - a list of row indices
# cols - a list of column indices
# cells - the list of cells that have changed content
# prev - the list of previous string contents of the changed cells
#
# Make sure the corresponding toggle is enabled in the DAT Execute DAT.
#
# If rows or columns are deleted, sizeChange will be called instead of row/col/cellChange.


def onTableChange(dat):
    convert_dat = op('convert1')  # Change to your actual Convert DAT name
    dna_sequence = convert_dat.text.strip()  # Extract DNA sequence as a single string

    if not dna_sequence:
        return  # Exit if empty

    # Split into single nucleotides
    nucleotides = list(dna_sequence)

    # Clear both Table DATs before inserting new data
    op('table_nucleotides').clear()
    op('table_codons').clear()

    # Populate Table 1: Single Nucleotides
    for nt in nucleotides:
        op('table_nucleotides').appendRow([nt])

    # Populate Table 2: Codons (Triplets)
    codon_size = 3
    total_full_codons = len(dna_sequence) // codon_size

    for i in range(total_full_codons):
        codon = dna_sequence[i * codon_size : i * codon_size + codon_size]  # Get codon triplet
        op('table_codons').appendRow([codon])  # Add each codon as a row


def onRowChange(dat, rows):
 return

def onColChange(dat, cols):
 return

def onCellChange(dat, cells, prev):
 return

def onSizeChange(dat):
 return
