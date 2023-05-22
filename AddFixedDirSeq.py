def read_fasta_file(file_path):
    """
    Reads a FASTA file and returns a dictionary of sequence name and sequence pairs.
    """
    sequences = {}
    with open(file_path, 'r') as file:
        current_sequence = ''
        current_name = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_name != '':
                    sequences[current_name] = current_sequence
                    current_sequence = ''
                current_name = line[1:]
            else:
                current_sequence += line
        if current_name != '':
            sequences[current_name] = current_sequence
    return sequences


def write_fasta_file(output_file_path, sequences):
    """
    Writes sequences in FASTA format to an output file.
    """
    with open(output_file_path, 'w') as file:
        for name, sequence in sequences.items():
            file.write('>' + name + '\n')
            file.write(sequence + '\n')


# Input FASTA file paths
haplotyp1_file_path = 'Haplotyp1.txt'
rev_haplotyp2_file_path = 'RevHaplotyp2.txt'

# Read Haplotyp1.txt and RevHaplotyp2.txt
haplotyp1_sequences = read_fasta_file(haplotyp1_file_path)
rev_haplotyp2_sequences = read_fasta_file(rev_haplotyp2_file_path)

# Replace sequences in haplotyp1_sequences with sequences from rev_haplotyp2_sequences
for name, sequence in haplotyp1_sequences.items():
    if name in rev_haplotyp2_sequences:
        haplotyp1_sequences[name] = rev_haplotyp2_sequences[name]

# Write combined sequences to output file
output_file_path = 'CombinedHaplotyps.txt'
write_fasta_file(output_file_path, haplotyp1_sequences)

print('Combined haplotyp sequences have been written to:', output_file_path)
