# Input file containing protein sequences in FASTA format
input_file = "outputp2.txt"

# Output file to write protein sequences without premature stop codons
output_file = "filprot2.txt"

# Read input protein sequences from file
with open(input_file, "r") as f:
    lines = f.readlines()

# Parse protein sequences from FASTA format
protein_sequences = []
current_header = ""
current_seq = ""
for line in lines:
    if line.startswith(">"):
        if current_seq:
            protein_sequences.append((current_header, current_seq))
            current_seq = ""
        current_header = line.strip()
    else:
        current_seq += line.strip()
if current_seq:
    protein_sequences.append((current_header, current_seq))

# Remove protein sequences with premature stop codons
protein_sequences_no_stop = []
for protein_header, protein_seq in protein_sequences:
    if "*" not in protein_seq:
        protein_sequences_no_stop.append((protein_header, protein_seq))

# Write protein sequences without premature stop codons to output file
with open(output_file, "w") as f:
    for protein_header, protein_seq in protein_sequences_no_stop:
        f.write("{}\n".format(protein_header))
        f.write("{}\n".format(protein_seq))

print("Protein sequences without premature stop codons written to: {}".format(output_file))
