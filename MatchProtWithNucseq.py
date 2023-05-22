import re

# Read protein sequences from protein sequence file
protein_seqs = {}
with open('filprot.txt', 'r') as protein_file:
    protein_name = ''
    protein_seq = ''
    for line in protein_file:
        if line.startswith('>'):
            if protein_name != '':
                protein_seqs[protein_name] = protein_seq
            protein_name = line.strip()
            protein_seq = ''
        else:
            protein_seq += line.strip()
    # Add last protein sequence
    if protein_name != '':
        protein_seqs[protein_name] = protein_seq

# Read nucleotide sequences from nucleotide sequence file and match with protein sequences
matching_nucleotide_seqs = {}
with open('CombinedhaplotypesNames.txt', 'r') as nucleotide_file:
    nucleotide_name = ''
    nucleotide_seq = ''
    for line in nucleotide_file:
        if line.startswith('>'):
            nucleotide_name = line.strip()
            # Check if nucleotide sequence name matches with any protein sequence name using regular expression
            for protein_name in protein_seqs.keys():
                pattern = re.escape(protein_name).replace('_1', '(_1)?')
                if re.search(pattern, nucleotide_name):
                    matching_nucleotide_seqs[nucleotide_name] = ''
                    break
        else:
            if nucleotide_name in matching_nucleotide_seqs:
                matching_nucleotide_seqs[nucleotide_name] += line.strip()

# Write matching nucleotide sequences to output file
with open('output.fasta', 'w') as output_file:
    for seq_name, seq in matching_nucleotide_seqs.items():
        output_file.write(seq_name + '\n' + seq + '\n')

print('Matching nucleotide sequences have been written to output.fasta')



