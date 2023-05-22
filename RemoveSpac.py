with open('output.fasta', 'r') as infile, open('output2.fasta', 'w') as outfile:
    for line in infile:
        if line.startswith('>'):  # Identify sequence names
            seq_name = line.strip().replace(' ', '_')  # Replace spaces with underscores
            outfile.write(seq_name + '\n')  # Write modified name to output file
        else:
            outfile.write(line)  # Write sequence data to output file
