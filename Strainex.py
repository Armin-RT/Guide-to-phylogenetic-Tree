import re

# Create a dictionary to store the data
data = {}

# Read the input file
with open("strain3.txt", "r") as f:
    for line in f:
        # Skip empty lines
        if not line.strip():
            continue
        
        # Match the species name and strain data
        match = re.match(r'^(.+):\s*$', line)
        if match:
            species = match.group(1)
            strains = {}
            data[species] = strains
        else:
            match = re.match(r'^\s*([\w\s\.-]+):\s*(\d+)\s+(\d+)$', line)
            if match:
                strain = match.group(1)
                value1 = int(match.group(2))
                value2 = int(match.group(3))
                strains[strain] = (value1, value2)

# Write the output file
with open("Strain3_formatted.tsv", "w") as f:
    # Write the header row
    f.write("Species\tStrain\tValue1\tValue2\n")
    
    # Write the data rows
    for species, strains in data.items():
        for strain, values in strains.items():
            value1, value2 = values
            f.write(f"{species}\t{strain}\t{value1}\t{value2}\n")

