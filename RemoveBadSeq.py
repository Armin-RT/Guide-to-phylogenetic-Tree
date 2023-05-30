def filter_sequences(fasta_file, output_file):
    sequences_to_exclude = [
        "Fusarium oxysporum f. sp. cubense isolate VCG0125",
        "Fusarium oxysporum f. sp. cubense isolate VCG0120",
        "Fusarium oxysporum f. sp. cubense strain TC1-1",
        "Fusarium oxysporum f. sp. cubense race 1 isolate VCG01220"
    ]

    excluded_parts = ["TC1-1", "VCG0120", "VCG0125", "race 1 isolate", "Fusarium graminearum genome assembly, chromosome: II_4155879-4157538", "Fusarium graminearum chromosome 2, complete genome_4156656-4158354"]

    filtered_sequences = []

    with open(fasta_file, "r") as f:
        sequence_name = ""
        sequence_lines = []

        for line in f:
            if line.startswith(">"):
                if sequence_lines:
                    sequence = "".join(sequence_lines)
                    if not any(part in sequence_name for part in excluded_parts):
                        filtered_sequences.append(f">{sequence_name}\n{sequence}\n")

                sequence_name = line[1:].strip()
                sequence_lines = []
            else:
                sequence_lines.append(line.strip())

        if sequence_lines:
            sequence = "".join(sequence_lines)
            if not any(part in sequence_name for part in excluded_parts):
                filtered_sequences.append(f">{sequence_name}\n{sequence}\n")

    with open(output_file, "w") as f:
        f.writelines(filtered_sequences)

# Usage example
filter_sequences("CombinedhaplotypesNames.txt", "CombinedhaplotypesNames2.txt")

