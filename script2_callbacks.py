import math

def cook(scriptOP):
    grid = op('grid1')
    dna_table = op('table_nucleotides')
    dna_codons = op('table_codons')

    scriptOP.clear()
    scriptOP.copy(grid)

    # Get the number of codons
    num_codons = dna_codons.numRows

    # Grid rows = number of condons
    grid.par.rows = num_codons

    time = op('timer_chop')[0]

    cols = grid.par.cols.eval()
    rows = grid.par.rows.eval()

    # Loop through
    for i, point in enumerate(scriptOP.points):
        row = i // cols
        col = i % cols

        flipped_row = rows - 1 - row
        flipped_index = flipped_row * cols + col

        if flipped_index >= dna_table.numRows:
         continue

        nucleotide = dna_table[flipped_index, 0].val  # Get nucleotide

        # Original position from GridSOP
        x, y, z = point.x, point.y, point.z

        # Apply animations based on nucleotide
        x_offset, y_offset, z_offset = 0, 0, 0

        if nucleotide == 'A':
            z_offset = 4 * math.sin((time-0)/2)  # Move back and forth in Z
        elif nucleotide == 'T':
            z_offset = 4 * math.sin((time-3)/2)
        elif nucleotide == 'C':
            z_offset = 4 * math.sin((time-6)/2)
        elif nucleotide == 'G':
            z_offset = 4 * math.sin((time-9)/2)

        # Apply
        point.x = x + x_offset
        point.y = y + y_offset
        point.z = z + z_offset
