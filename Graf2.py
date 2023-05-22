import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Load data from the TSV file
df = pd.read_csv("Strain3_formatted.tsv", sep="\t")

# Create a single figure for all species
fig, ax = plt.subplots(figsize=(10, 8))

# Create a color palette for each species
color_palette = cm.get_cmap("tab20c", len(df["Species"].unique()))
color_indices = np.arange(len(df["Species"].unique()))
np.random.shuffle(color_indices)  # Shuffle the color indices

# Iterate over each species and plot their data
for i, species in enumerate(df["Species"].unique()):
    # Get the shuffled color index
    color_index = color_indices[i]
    
    # Filter the data for the current species
    species_df = df[df["Species"] == species]
    
    # Iterate over the strains and plot the bars
    for index, row in species_df.iterrows():
        strain = row["Strain"]
        fusspoks = row["Value1"]
        pseudogenes = row["Value2"]
        
        # Assign a unique color to the species
        color = color_palette(color_index)
        
        # Plot the bars for each strain
        ax.bar(strain, fusspoks, width=0.4, color=color, alpha=0.8)
        ax.bar(strain, pseudogenes, bottom=fusspoks, width=0.4, color=color, alpha=0.6)

# Set the plot title and axis labels
ax.set_title("Strain Data")
ax.set_xlabel("Strain")
ax.set_ylabel("Amount of genes")

# Rotate the x-axis labels
plt.xticks(rotation=90)

# Create a legend with species, pseudogenes, and fusspoks
legend_elements = [
    plt.Rectangle((0, 0), 1, 1, fc=color_palette(color_indices[i]), alpha=0.8, label=species)
    for i, species in enumerate(df["Species"].unique())
]
legend_elements.append(
    plt.Rectangle((0, 0), 1, 1, fc="lightgrey", alpha=0.6, label="Pseudogenes (light shade)")
)
legend_elements.append(
    plt.Rectangle((0, 0), 1, 1, fc="lightgrey", alpha=0.8, label="Non-Pseudogene Fusspoks (Dark shade)")
)
legend = ax.legend(handles=legend_elements, title="Species", loc="upper right")

# Set the legend font size and properties
plt.setp(legend.get_title(), fontsize=8)  # Title font size
plt.setp(legend.get_texts(), fontsize=6)  # Text font size
legend.get_frame().set_linewidth(0.5)  # Legend border linewidth

# Adjust the legend size
legend.set_bbox_to_anchor((1, 1))  # Adjust the position
legend.set_frame_on(True)  # Enable the legend frame

# Adjust the spacing between bars
plt.tight_layout()

# Save the figure
plt.savefig("Strain3_big_graph.png", dpi=300)

# Show the plot
plt.show()





