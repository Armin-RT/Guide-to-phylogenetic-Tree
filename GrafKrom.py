import matplotlib.pyplot as plt

# Read the count file
with open('chromosomecount3.txt', 'r') as file:
    lines = file.readlines()

# Create a dictionary to store the counts
counts_dict = {}
current_strain = ""

# Process the lines in the count file
for line in lines:
    line = line.strip()
    if line.startswith("Strain:"):
        current_strain = line.split(":")[1].strip()
        counts_dict[current_strain] = {}
    elif line.startswith("Chromosome"):
        parts = line.split(":")
        chromosome = parts[0].strip()
        if len(parts) > 1:
            count = parts[1].strip().split()[0]
            unique_chromosome = f"{chromosome}_{current_strain}"
            counts_dict[current_strain][unique_chromosome] = int(count)
        else:
            counts_dict[current_strain][chromosome] = 0

# Create a list of unique strains
strains = list(counts_dict.keys())

# Get all unique chromosomes across all strains
all_chromosomes = set()
for strain_counts in counts_dict.values():
    all_chromosomes.update(strain_counts.keys())

# Assign a unique color to each strain
colors = [plt.cm.tab20(i) for i in range(len(strains))]

# Plot the bar chart with a larger figure size
fig, ax = plt.subplots(figsize=(12, 8))
x = range(len(all_chromosomes))
for i, strain in enumerate(strains):
    counts = counts_dict[strain]
    chromosome_counts = [counts.get(chromosome, 0) for chromosome in all_chromosomes]
    ax.bar(x, chromosome_counts, color=colors[i], label=strain)

ax.set_xlabel("Chromosome")
ax.set_ylabel("Amount of genes")
ax.set_xticks(x)
ax.set_xticklabels(all_chromosomes, rotation=90)
ax.legend()

# Save the figure to an output file
plt.tight_layout()
plt.savefig("chromosome_counts.png")
plt.show()

