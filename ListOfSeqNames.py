# Set the file paths
input_file_path = "Output.fasta"
output_file_path = "sequence_names2.txt"

# Open the input file and output file
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    # Loop over each line in the input file
    for line in input_file:
        # Check if the line starts with ">"
        if line.startswith(">"):
            # Write the sequence name to the output file
            output_file.write(line.strip() + "\n")
