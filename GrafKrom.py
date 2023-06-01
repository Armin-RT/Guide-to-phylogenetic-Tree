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
    elif line.startswith("Chromosome") or line.startswith("supercont"):
        parts = line.split(":")
        chromosome = parts[0].strip()
        if len(parts) > 1:
            count = parts[1].strip().split()[0]
            if 'Foc' in chromosome:
                unique_chromosome = f"{chromosome}_{current_strain}_Foc"
            else:
                unique_chromosome = f"{chromosome}_{current_strain}"
            counts_dict[current_strain][unique_chromosome] = int(count)

# Create a list of unique strains
strains = list(counts_dict.keys())

# Get all unique chromosomes across all strains
all_chromosomes = set()
for strain_counts in counts_dict.values():
    all_chromosomes.update(strain_counts.keys())

# Sort chromosomes by strain and chromosome name
sorted_chromosomes = sorted(all_chromosomes, key=lambda c: ('_A' in c, 'Foc' in c, 'BC2' in c, c.split('_')[1], c.split('_')[0]))

# Assign a unique color to each strain
colors = [plt.cm.tab20(i) for i in range(len(strains))]

# Plot the bar chart with a larger figure size
fig, ax = plt.subplots(figsize=(12, 8))
x = range(len(sorted_chromosomes))
for i, strain in enumerate(strains):
    counts = counts_dict[strain]
    chromosome_counts = [counts.get(chromosome, 0) for chromosome in sorted_chromosomes]
    full_chromosome_names = [chromosome.replace("Chromosome", "Chrom") if 'Chromosome' in chromosome else chromosome.split('_')[0] for chromosome in sorted_chromosomes]

    ax.bar(x, chromosome_counts, color=colors[i], label=strain)

ax.set_xlabel("Genomic Location")
ax.set_ylabel("Amount of genes")
ax.set_xticks(x)
tick_labels = ax.set_xticklabels(full_chromosome_names, rotation=90, ha='right')  # Get the tick labels

# Define tick colors
tick_colors = ['r' if '_A' in chromosome else 'k' for chromosome in full_chromosome_names]

# Apply colors to x-axis tick labels
for tick_label, color in zip(tick_labels, tick_colors):
    tick_label.set_color(color)

ax.legend(title="Strains")  # Add legend title

# Save the figure to an output file
plt.tight_layout()
plt.savefig("chromosome_counts.png")
plt.show()

