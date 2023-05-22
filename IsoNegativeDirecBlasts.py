# Open the BLAST result file
with open('results_stitch.txt', 'r') as blast_file:
    with open('negative_direction_results.txt', 'w') as output_file:
        for line in blast_file:
            # Skip comment lines that start with '#'
            if line.startswith('#'):
                continue
            # Split the tab-separated fields in the line
            fields = line.strip().split('\t')
            # Extract start and end positions
            start = int(fields[8])
            end = int(fields[9])
            # Check if direction is negative (end - start < 0)
            if end - start < 0:
                # Write the line to the output file for alignments with negative direction
                output_file.write(line)
