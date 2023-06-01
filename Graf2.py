import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Create a dictionary to store the data
data = {}

# Read the input file
with open("strain3.txt", "r") as f:
    species = None
    strains = {}
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

# Convert the data to a pandas DataFrame
formatted_data = []
for species, strains in data.items():
    for strain, values in strains.items():
        value1, value2 = values
        formatted_data.append([species, strain, value1, value2])

df = pd.DataFrame(formatted_data, columns=["Species", "Strain", "Value1", "Value2"])

# Create a single figure for all species
fig, ax = plt.subplots(figsize=(16, 12))

# Create a color palette for each species
color_palette = cm.get_cmap("tab20c", len(df["Species"].unique()))
color_indices = np.arange(len(df["Species"].unique()))
np.random.shuffle(color_indices)  # Shuffle the color indices

# Set the width of the bars
bar_width = 0.4

# List to store the patches and labels for the legend
legend_patches = []
legend_labels = []

# Iterate over each species and plot their data
for i, species in enumerate(df["Species"].unique()):
    # Get the shuffled color index
    color_index = color_indices[i]

    # Filter the data for the current species
    species_df = df[df["Species"] == species]

    # Assign a unique color to the species
    color = color_palette(color_index)

    # Iterate over the strains and plot the bars
    for index, row in species_df.iterrows():
        strain = row["Strain"]
        fusspoks = row["Value1"]
        pseudogenes = row["Value2"]

        # Plot the bars for each strain
        bar1 = ax.bar(strain, fusspoks, width=bar_width, color=color, alpha=0.8)
        bar2 = ax.bar(strain, pseudogenes, bottom=fusspoks, width=bar_width, color=color, alpha=0.6)

        # Add a black line separating fusspoks and pseudogenes within each bar
        bar_x = bar1[0].get_x()
        bar_height = bar1[0].get_height()
        ax.plot([bar_x, bar_x + bar_width], [fusspoks, fusspoks], color="black")

    # Add the bar patches and species name (without "Fusarium") to the legend
    legend_patches.append(bar1[0])
    legend_labels.append(species.replace("Fusarium ", ""))

# Add a legend on the left side with species names and colors
legend = ax.legend(legend_patches, legend_labels, loc="upper left", bbox_to_anchor=(0.5, 0.95), prop={'size': 8}, title="Species")

# Set the legend title font size
legend.get_title().set_fontsize(10)

# Set the plot title and axis labels
ax.set_title("Strain Data")
ax.set_xlabel("Strain")
ax.set_ylabel("Amount of homologs")

# Adjust the spacing between bars
ax.margins(y=0.1)

# Rotate the x-axis tick labels
plt.xticks(rotation='vertical')

# Save the plot as an image file
plt.savefig("strain_data_plot.png", dpi=300)

# Show the plot
plt.show()

