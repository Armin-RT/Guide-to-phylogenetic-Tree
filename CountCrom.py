import pandas as pd

# Read the CSV file into a DataFrame with tab delimiter
df = pd.read_csv("fuspok_positions (1).csv", delimiter='\t')

# Remove leading and trailing spaces from column names
df.columns = df.columns.str.strip()

# Group sequences by strain and chromosome, and count the sequences
grouped = df.groupby(["Strain", "Chromosome"]).size().reset_index(name="Count")

# Define the output file path
output_file = "chromosomecount.txt"

# Write the counts for each strain and chromosome to the output file
with open(output_file, "w") as f:
    for strain, group in grouped.groupby("Strain"):
        f.write(f"Strain: {strain}\n")
        for _, row in group.iterrows():
            chromosome = row["Chromosome"]
            count = row["Count"]
            f.write(f"Chromosome {chromosome}: {count} sequences\n")
        f.write("\n")

print(f"Count results saved to {output_file}.")
