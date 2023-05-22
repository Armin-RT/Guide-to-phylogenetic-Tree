import re

# Step 1: extract strain names from data_summary.tsv
strains = {}
with open("data_summary.tsv", "r") as f:
    for line in f:
        fields = re.split(r'\t+', line.rstrip())
        species_name = fields[0].strip()
        for field in fields[1:]:
            strain_match = re.search(r'(?:strain:|isolate:)\s*([^,\t\n\r\f\v]+)', field, re.IGNORECASE)
            if strain_match:
                strain = strain_match.group(1).strip()
                strains[strain] = species_name

# Rest of the code remains the same...


# Step 2: count sequences for each strain in sequence_names2.txt
sequences2 = {}
with open("sequence_names2.txt", "r") as f:
    for line in f:
        for strain, species in strains.items():
            if re.search(r'\b{}\b'.format(re.escape(strain)), line, re.IGNORECASE):
                sequences2.setdefault(species, {}).setdefault(strain, 0)
                sequences2[species][strain] += 1

# Step 3: count sequences for each strain in sequence_names.txt
sequences1 = {}
with open("sequence_names.txt", "r") as f:
    for line in f:
        for strain, species in strains.items():
            if re.search(r'\b{}\b'.format(re.escape(strain)), line, re.IGNORECASE):
                sequences1.setdefault(species, {}).setdefault(strain, 0)
                sequences1[species][strain] += 1

# Step 4: write results to output file
with open("strains2.txt", "w") as f:
    for species, strain_counts2 in sequences2.items():
        f.write(f"{species}:\n")
        for strain, count2 in strain_counts2.items():
            count1 = sequences1.get(species, {}).get(strain, 0)
            difference = count1 - count2
            f.write(f"\t{strain}: {count2} {difference}\n")

    # Handle strains present only in sequence_names.txt
    for species, strain_counts1 in sequences1.items():
        for strain, count1 in strain_counts1.items():
            if strain not in sequences2.get(species, {}):
                f.write(f"\t{strain}: 0 {count1}\n")
