def reverse_complement(sequence):
    """
    Returns the reverse complement of a DNA sequence.
    """
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] if base in complement else base for base in reversed(sequence)])


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


# Input FASTA file path
input_file_path = 'Negatativehap.txt'

# Output FASTA file path
output_file_path = 'RevHaplotyp2.txt'

# Read FASTA file
sequences = read_fasta_file(input_file_path)

# Generate reverse complement sequences
reverse_complement_sequences = {}
for name, sequence in sequences.items():
    reverse_complement_sequences[name] = reverse_complement(sequence)

# Write reverse complement sequences to output file
write_fasta_file(output_file_path, reverse_complement_sequences)

print('Reverse complement sequences have been written to:', output_file_path)
