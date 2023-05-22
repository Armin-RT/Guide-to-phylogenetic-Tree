def filter_sequences(fasta_file, output_file):
    sequences_to_exclude = [
        "Fusarium_oxysporum_f._sp._cubense_isolate_VCG0125",
        "Fusarium_oxysporum_f._sp._cubense_isolate_VCG0120",
        "Fusarium_oxysporum_f._sp._cubense_strain_TC1-1",
        "Fusarium_oxysporum_f._sp._cubense_race_1_isolate_VCG01220"
    ]

    excluded_sequences = set(sequences_to_exclude)
    filtered_sequences = []

    with open(fasta_file, "r") as f:
        sequence_name = ""
        sequence_lines = []

        for line in f:
            if line.startswith(">"):
                if sequence_lines:
                    sequence = "".join(sequence_lines)
                    if not any(exclude_seq in sequence_name for exclude_seq in excluded_sequences):
                        filtered_sequences.append(f">{sequence_name}\n{sequence}\n")
                
                sequence_name = line[1:].strip()
                sequence_lines = []
            else:
                sequence_lines.append(line.strip())

        if sequence_lines:
            sequence = "".join(sequence_lines)
            if not any(exclude_seq in sequence_name for exclude_seq in excluded_sequences):
                filtered_sequences.append(f">{sequence_name}\n{sequence}\n")

    with open(output_file, "w") as f:
        f.writelines(filtered_sequences)

# Usage example
filter_sequences("OutputS2_NT.fasta", "OutputS3_NT.fasta")
